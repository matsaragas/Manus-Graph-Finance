from typing import Dict, Any
from src.graph.types import State


import logging

from src.llms.llm import get_llm_by_type
from src.prompts.template import OpenManusPromptTemplate
from src.config.agents import AGENT_LLM_MAP

logger = logging.getLogger(__name__)


def coordinator_node(state: State) -> Dict[str, Any]:
    logger.info("Coordinator")
    messages = OpenManusPromptTemplate.apply_prompt_template("coordinator", state)
    response = get_llm_by_type(AGENT_LLM_MAP["coordinator"]).invoke(messages)

