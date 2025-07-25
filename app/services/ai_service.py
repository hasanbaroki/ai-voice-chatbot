"""
Service for AI-related functionality including chat completions.
"""

from app.core.config import openai_client, CHAT_MODEL
from app.core.prompts import build_system_prompt

async def generate_chat_response(user_text: str, personality: str, user_data: dict, plan_active: bool) -> str:
    """
    Generate a chat response using OpenAI's GPT model.
    
    Args:
        user_text: The text input from the user
        personality: The selected personality
        user_data: Dictionary containing user information
        plan_active: Whether the user has an active plan
        
    Returns:
        The generated response text
        
    Raises:
        Exception: If there's an error generating the response
    """
    # Build the system prompt
    system_content = build_system_prompt(personality, user_data, plan_active)
    
    # Prepare the messages
    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_text}
    ]
    
    # Generate the response
    completion = openai_client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.7,  # A bit more creative than default
        max_tokens=150    # Keep responses concise
    )
    
    # Extract and return the response text
    return completion.choices[0].message.content.strip() 