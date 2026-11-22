from langgraph.graph import START,END,StateGraph

from app.nodes import classify_incident, investigate_incident, recommend_solution
from app.states import IncidentState


#create graph

builder = StateGraph(IncidentState)

#register nodes

builder.add_node("Classification",classify_incident)
builder.add_node("Investigation",investigate_incident)
builder.add_node("Recomandation",recommend_solution)

# add edges

builder.add_edge(START,"Classification")
builder.add_edge("Classification","Investigation")
builder.add_edge("Recomandation",END)

#Complie graph

incident_graph=builder.compile()