from typing import TypedDict, Literal, List, Dict, Any
from langchain_core.messages import BaseMessage


class State(TypedDict):
    messages: List[BaseMessage]
    full_plan: str
    deep_thinking_mode: bool
    search_before_planning: bool

