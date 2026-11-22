
from fastapi import FastAPI
from uuid import uuid4

from app.schemas import IncidentRequest, IncidentResponse
from app.states import IncidentState
from app.graph import incident_graph


app = FastAPI(
    title="AI Incident Management API",
    version="1.0"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post(
    "/incidents",
    response_model=IncidentResponse
)
def create_incident(request: IncidentRequest):

    incident_id = f"INC-{uuid4().hex[:8].upper()}"

    initial_state: IncidentState = {
        "incident_id": incident_id,
        "title": request.title,
        "description": request.description,
        "application": request.application,
        "environment": request.environment,
        "affected_users": request.affected_users,
        "business_impact": request.business_impact,

        "category": "",
        "severity": "",
        "possible_root_cause": "",

        "recommended_actions": [],
        "assigned_team": "",

        "escalation_required": False,
        "status": "NEW"
    }

    result = incident_graph.invoke(initial_state)

    return result
