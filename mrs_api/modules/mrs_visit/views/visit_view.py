# pylint: disable=unsubscriptable-object
from pydantic import BaseModel
from mrs_api.modules.patient.views.patient_view import PatientInfoView


class VisitView(BaseModel):
    id: int
    name: str
    state: str
    patient: PatientInfoView
