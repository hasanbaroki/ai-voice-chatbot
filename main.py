"""
Voice Chatbot API main entry point.

This module initializes the FastAPI app and defines the API endpoints.
"""

from datetime import datetime
from fastapi import FastAPI, HTTPException

from app.core.config import APP_TITLE, APP_DESCRIPTION, APP_VERSION, HOST, PORT, RELOAD
from app.models.models import VoiceChatRequest, VoiceChatResponse
from app.services.audio_service import download_mp3, transcribe_audio
from app.services.ai_service import generate_chat_response

# Create FastAPI app
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

@app.get("/")
async def root():
    """Root endpoint that returns API information."""
    return {
        "app": APP_TITLE,
        "version": APP_VERSION,
        "status": "running"
    }

@app.post("/chat-voice", response_model=VoiceChatResponse)
async def chat_voice(req: VoiceChatRequest):
    """
    Process voice input and generate AI response with selected personality.
    
    Args:
        req: The voice chat request containing MP3 URL and user data
        
    Returns:
        A response containing the AI-generated message
    """
    try:
        # Download the audio file
        audio_bytes = await download_mp3(str(req.mp3_url))
        
        # Transcribe the audio to text
        user_text = await transcribe_audio(audio_bytes)
        
        # If no transcription was obtained, raise an error
        if not user_text:
            raise HTTPException(status_code=422, detail="Could not transcribe audio input")
        
        # Generate AI response
        ai_response = await generate_chat_response(
            user_text=user_text,
            personality=req.personality,
            user_data=req.userdata.dict(),
            plan_active=req.plan_active
        )
        
        # Return the response
        return VoiceChatResponse(
            message=ai_response,
            chat_room_id=req.chat_room_id,
            timestamp=datetime.utcnow(),
            transcription=user_text  # Include transcription in response
        )
        
    except Exception as e:
        # Handle errors
        error_detail = str(e)
        status_code = 500
        
        if "download" in error_detail.lower() or "url" in error_detail.lower():
            status_code = 400
            error_detail = f"Failed to fetch MP3: {error_detail}"
        elif "transcribe" in error_detail.lower() or "audio" in error_detail.lower():
            status_code = 422
            error_detail = f"Audio processing error: {error_detail}"
        else:
            error_detail = f"Internal server error: {error_detail}"
            
        raise HTTPException(status_code=status_code, detail=error_detail)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)
