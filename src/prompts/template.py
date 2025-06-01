import os
import re
from datetime import datetime


from typing import List, Dict
from langchain_core.prompts import PromptTemplate
from langchain.prebuilt.chat_agent_executor import AgentState


class OpenManusPromptTemplate:
    """
    Load and process template manager for handling agentic-specific prompts
    """
    @staticmethod
    def get_prompt_template(prompt_name: str) -> str:
        """Load and process a prompt template from a file"""

        template_path = os.path.join(os.path.dirname(__file__), f"{prompt_name}.md")
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # Escape curly braces for string formatting
        template = template.replace("{", "{{").replace("}", "}}")
        # Convert <<VAR>> to {VAR} format
        template = re.sub(r"<<([^>>]+)>>", r"{1}", template)
        return template


    @staticmethod
    def apply_prompt_template(prompt_name: str, state: AgentState) -> List[Dict[str, str]]:

        current_time = datetime.now().strftime("%a %b %d %Y %H:%M:%S %z")
        system_prompt = PromptTemplate(
            input_variables=["CURRENT_TIME"],
            template=OpenManusPromptTemplate.get_prompt_template(prompt_name),
        ).format(CURRENT_TIME=current_time, **state)





