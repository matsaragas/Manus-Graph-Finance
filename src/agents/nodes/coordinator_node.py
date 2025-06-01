from typing import Dict, Any
from src.graph.types import State
import logging
from src.prompts.template import OpenManusPromptTemplate

logger = logging.getLogger(__name__)

def coordinator_node(state: State) -> Dict[str, Any]:
    logger.info("Coordinator")
    messages = OpenManusPromptTemplate.apply_prompt_template("coordinator", state)

