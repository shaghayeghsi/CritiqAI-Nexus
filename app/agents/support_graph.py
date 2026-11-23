from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.agents.provider import get_provider
class SupportState(TypedDict):
    message:str
    tenant_id:str
    category:str
    priority:str
    escalate:bool
    answer:str
def classify(state):
    p=get_provider().classify(state["message"])
    return {"category":p["category"],"priority":p["priority"]}
def route(state):
    t=state["message"].lower()
    return {"escalate":state["priority"]=="high" or any(x in t for x in ["urgent","still cannot","still can't","complaint","refund"])}
def respond(state):
    answer=get_provider().respond(state["message"])
    if state["escalate"]: answer+=" Your request has been flagged for human review."
    return {"answer":answer}
def build_graph():
    g=StateGraph(SupportState)
    g.add_node("classify",classify); g.add_node("route",route); g.add_node("respond",respond)
    g.set_entry_point("classify"); g.add_edge("classify","route"); g.add_edge("route","respond"); g.add_edge("respond",END)
    return g.compile()
_graph=build_graph()
def run_support_workflow(message,tenant_id):
    return _graph.invoke({"message":message,"tenant_id":tenant_id,"category":"general","priority":"normal","escalate":False,"answer":""})
