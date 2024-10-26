from typing import Annotated
from fastapi import HTTPException, status
from mrs_api.env.settings import get_settings
from mrs_api.services.session import AsyncSession, db_session
from mrs_api.services.odoo import OdooConnection, odoo_conn
from mrs_api.api.router import acl_router, MRS_SECTION
from ..views.patient_view import PatientView, PatientCreateView, PatientUpdateView
from ..models.patient_model import PatientModel

settings = get_settings()


@acl_router.get(
    "/patients/profile", response_model=PatientView, tags=[MRS_SECTION, "Patient"]
)
async def patients(session: Annotated[AsyncSession, db_session()]):
    user_code: str = "PAT00001"
    result = await PatientModel.detail_by_user_code(
        user_code=user_code, session=session
    )
    return PatientView.model_validate(result, from_attributes=True)


@acl_router.post(
    "/patients/profile/create",
    response_model=PatientView,
    tags=[MRS_SECTION, "Patient"],
)
async def create_patient(
    data: PatientCreateView,
    session: Annotated[AsyncSession, db_session()],
    odoo: Annotated[OdooConnection, odoo_conn(settings.odoo_key)],
):
    user_code: str = "PAT00001"
    res = await PatientModel.create(data, odoo)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to created patient."
        )
    result = await PatientModel.detail_by_user_code(
        user_code=user_code, session=session
    )
    return PatientView.model_validate(result, from_attributes=True)


@acl_router.put(
    "/patients/profile/update",
    response_model=PatientView,
    tags=[MRS_SECTION, "Patient"],
)
async def update_patient(
    data: PatientUpdateView,
    session: Annotated[AsyncSession, db_session()],
    odoo: Annotated[OdooConnection, odoo_conn(settings.odoo_key)],
):
    user_code: str = "PAT00001"
    res = await PatientModel.write(user_code, data, session, odoo)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update profile."
        )
    result = await PatientModel.detail_by_user_code(
        user_code=user_code, session=session
    )
    return PatientView.model_validate(result, from_attributes=True)
