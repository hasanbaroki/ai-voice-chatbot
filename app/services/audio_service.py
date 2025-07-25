"""
Service for handling audio processing including download and transcription.
"""

import os
import uuid
import httpx
import tempfile

from app.core.config import openai_client, WHISPER_MODEL

async def download_mp3(url: str) -> bytes:
    """
    Download an MP3 file from a URL.
    
    Args:
        url: The URL of the MP3 file
        
    Returns:
        The binary content of the MP3 file
        
    Raises:
        httpx.HTTPError: If there's an error downloading the file
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.content


async def transcribe_audio(audio_data: bytes) -> str:
    """
    Transcribe audio data using OpenAI's Whisper API.
    
    Args:
        audio_data: The binary audio data to transcribe
        
    Returns:
        The transcribed text
        
    Raises:
        Exception: If there's an error during transcription
    """
    # Create a temporary file for the audio data
    fd, temp_path = tempfile.mkstemp(suffix=".mp3")
    
    try:
        # Write the audio data to the temporary file
        with os.fdopen(fd, 'wb') as f:
            f.write(audio_data)
        
        # Transcribe the audio
        with open(temp_path, 'rb') as audio_file:
            transcription = openai_client.audio.transcriptions.create(
                model=WHISPER_MODEL,
                file=audio_file
            )
        
        return transcription.text or ""
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path) 