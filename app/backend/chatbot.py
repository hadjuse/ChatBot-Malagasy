from dataclasses import dataclass, field
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    HumanMessage, 
    SystemMessage, 
    AIMessage
)
import os
from langchain_core.prompts import ChatPromptTemplate
model=ChatMistralAI(
    api_key=os.environ['API_KEY'], 
    model="mistral-large-latest",
    temperature=0.1
)

def chatting(template: str, model: ChatMistralAI= model):
    """
    Generates a response in Malagasy using the provided template and model.

    Args:
        template (str): The template string to be used for generating the response.
        model (ChatMistralAI, optional): The chat model to be used for generating the response. Defaults to a predefined model.

    Returns:
        str: The generated response content in Malagasy.
    """
    messages = ChatPromptTemplate.from_messages([
        ('system', "Tu Répondras en malgache exclusivement"),
        ('user', "{template}")
    ])
    messages_chat = messages.invoke({
        "template": template
    })
    prompt = messages_chat.to_messages()
    return model.invoke(prompt).content
