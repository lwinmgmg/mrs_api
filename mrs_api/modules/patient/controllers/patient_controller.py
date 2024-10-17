from typing import List
from sqlalchemy import select
from mrs_api.services.session import async_session
from mrs_api.api.router import router, MRS_SECTION
from ..views.patient_view import PatientView
from ..models.patient import PatientModel


@router.get(
    "/patients", response_model=List[PatientView], tags=[MRS_SECTION, "Patient"]
)
async def patients():
    output: List[PatientView] = []
    stmt = select(PatientModel).order_by(PatientModel.id)
    async with async_session() as session:
        results = await session.execute(stmt)
        for res in results.scalars():
            output.append(PatientView.model_validate(res, from_attributes=True))
    return output
