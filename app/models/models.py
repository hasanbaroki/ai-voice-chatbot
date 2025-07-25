from datetime import datetime
from pydantic import BaseModel, HttpUrl

class UserData(BaseModel):
    """User data model containing personal information."""
    name: str = "User"
    gender: str = "unspecified"
    age: int = 0

class VoiceChatRequest(BaseModel):
    """Request model for the voice chat endpoint."""
    mp3_url: HttpUrl
    chat_room_id: str
    personality: str
    plan_active: bool = False
    userdata: UserData

class VoiceChatResponse(BaseModel):
    """Response model for the voice chat endpoint."""
    message: str
    chat_room_id: str
    timestamp: datetime
    transcription: str = ""  # Added to return what was transcribed 