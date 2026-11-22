
from typing import TypedDict


class IncidentState(TypedDict):

    incident_id: str
    title: str
    description: str
    application: str
    environment: str
    affected_users: int
    business_impact: str

    category: str
    severity: str
    possible_root_cause: str

    recommended_actions: list[str]
    assigned_team: str

    escalation_required: bool
    status: str
