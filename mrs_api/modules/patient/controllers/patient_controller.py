from typing import Annotated
from mrs_api.services.session import AsyncSession, db_session
from mrs_api.api.router import acl_router, MRS_SECTION
from ..views.patient_view import PatientView
from ..models.patient_model import PatientModel


@acl_router.get(
    "/patients/profile", response_model=PatientView, tags=[MRS_SECTION, "Patient"]
)
async def patients(session: Annotated[AsyncSession, db_session()]):
    user_code: str = "PAT00001"
    result = await PatientModel.detail_by_user_code(
        user_code=user_code, session=session
    )
    return PatientView.model_validate(result, from_attributes=True)
