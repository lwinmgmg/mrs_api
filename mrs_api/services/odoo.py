# pylint: disable=too-many-instance-attributes, too-many-arguments, too-many-positional-arguments
from typing import AsyncGenerator
from logging import getLogger
import xmlrpc.client
from xmlrpc.client import ServerProxy
from queue import Queue
from fastapi import FastAPI, Request, Depends

_logger = getLogger("#odoo")


class Odoo:
    def __init__(
        self,
        app: FastAPI,
        key: str,
        url: str,
        db: str,
        username: str,
        password: str,
        conn_count: int = 10,
    ):
        self.uid = None
        self.app = app
        self.key = key
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.conn_count = conn_count
        self.queue = Queue(maxsize=conn_count)

    def initialize_conn(self) -> ServerProxy:
        return xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")

    def on_startup(self):
        common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        common.version()
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        for i in range(self.conn_count):
            self.queue.put(self.initialize_conn())
            print(f"Initialized odoo connection #{i + 1}")
            _logger.info("Initialized odoo connection #%s", i + 1)

        setattr(self.app.state, self.key, self)

    def on_shutdown(self):
        # clean all connection
        for i in range(self.conn_count):
            conn = self.queue.get()
            del conn
            print(f"Removed odoo connection #{i + 1}")
            _logger.info("Removed odoo connection #%s", i + 1)


class OdooConnection:
    def __init__(self, conn: ServerProxy, odoo: Odoo):
        self.conn = conn
        self.odoo = odoo


def odoo_conn(key: str) -> AsyncGenerator[OdooConnection, None]:
    async def get_odoo_conn(request: Request):
        odoo: Odoo = getattr(request.app.state, key)
        conn = odoo.queue.get()
        reuseble = True
        try:
            yield OdooConnection(conn, odoo)
        except:
            reuseble = False
            raise
        finally:
            if reuseble:
                odoo.queue.put(conn)
            else:
                odoo.queue.put(odoo.initialize_conn())

    return Depends(get_odoo_conn)
