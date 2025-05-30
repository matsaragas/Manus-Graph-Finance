from typing import AsyncGenerator, Dict, List
from src.workflow.graph import build_graph


async def run_agent_workflow(
        messages: List[Dict[str, str]], debug: bool = False
) -> AsyncGenerator[Dict[str, str], None]:

    workflow = build_graph()

