from typing import List
from sqlalchemy import select
from mrs_api.services.session import async_session
from mrs_api.api.router import router, MRS_SECTION
from ..views.visit_view import VisitView
from ..models.visit_model import VisitModel

@router.get("/visits", response_model=List[VisitView], tags=[MRS_SECTION, "Medical History"])
async def visits():
    output: List[VisitView] = []
    stmt = select(VisitModel)
    async with async_session() as session:
        results = await session.execute(stmt)
        for res in results.scalars():
            output.append(VisitView.model_validate(res, from_attributes=True))
    return output
