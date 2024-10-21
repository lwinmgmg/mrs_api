from typing import List, Annotated
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from mrs_api.services.session import db_session, AsyncSession
from mrs_api.api.router import router, MRS_SECTION
from ..views.visit_view import VisitView
from ..models.visit_model import VisitModel


@router.get(
    "/visits", response_model=List[VisitView], tags=[MRS_SECTION, "Medical History"]
)
async def visits(session: Annotated[AsyncSession, db_session()]):
    output: List[VisitView] = []
    stmt = select(VisitModel).options(joinedload(VisitModel.patient))
    results = await session.execute(stmt)
    for res in results.scalars():
        output.append(VisitView.model_validate(res, from_attributes=True))
    return output
