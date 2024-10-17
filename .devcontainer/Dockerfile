FROM python:3.12.6-bookworm

ARG USER=vscode
ARG UID=1000

RUN apt -y update  && apt -y upgrade

RUN groupadd --gid ${UID} ${USER} \
    && useradd -m --uid ${UID} --gid ${UID} \
    --shell /bin/bash ${USER}

USER $USER

RUN pip install poetry

CMD [ "poetry" "install" ]
