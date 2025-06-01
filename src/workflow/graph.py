from langgraph.graph import StateGraph, Start
from src.graph.types import State
from src.agents.nodes import coordinator_node




def build_graph():

    builder = StateGraph(State)
    builder.add_node("coordinator", coordinator_node)
