
from pydantic import BaseModel, Field
from typing import Literal, Optional

class IncidentRequest(BaseModel):

    title: str = Field(
        min_length=5,
        description="Short incident title"
    )

    description: str = Field(
        min_length=10,
        description="Detailed description of the issue"
    )

    application: str

    environment: Literal[
        "DEV", "QA", "UAT", "PROD"
    ]

    affected_users: int = Field(gt=0)

    business_impact: Literal[
        "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

    reported_by: Optional[str] = None

class IncidentResponse(BaseModel):

    incident_id: str
    category: str
    severity: str
    possible_root_cause: str
    recommended_actions: list[str]
    assigned_team: str
    escalation_required: bool
    status: str