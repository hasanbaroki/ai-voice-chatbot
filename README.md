# AI Voice Chatbot

A powerful, personality-based voice chatbot API built with Python and FastAPI. This service transcribes voice messages and responds with text in different personality styles.

## Features

- **Voice Transcription**: Converts speech to text using OpenAI's Whisper model
- **Multiple Personalities**: Choose from three distinct personalities:
  - **Girlfriend**: Warm, playful, and affectionate with casual language
  - **Buddy**: Energetic, fun-loving friend with upbeat casual tone
  - **Psychologist**: Thoughtful, insightful professional with formal empathetic style
- **User Data Integration**: Personalizes responses based on user information
- **Premium Plan Support**: Adapts behavior based on user's subscription status
- **Modular Design**: Clean, maintainable code structure

## Technology Stack

- **Python 3.7+**
- **FastAPI**: Modern, high-performance web framework
- **OpenAI API**: For AI-powered transcription and chat responses
- **Pydantic**: Data validation and settings management
- **HTTPX**: Asynchronous HTTP client

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-voice-chatbot.git
   cd ai-voice-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Start the server:
   ```bash
   python main.py
   ```

2. The API will be available at `http://localhost:8001`

## API Documentation

### GET /
Returns basic API information:
```json
{
  "app": "Voice Chatbot API",
  "version": "1.0.0",
  "status": "running"
}
```

### POST /chat-voice
Process voice input and generate an AI response with the selected personality.

#### Request Body

```json
{
  "mp3_url": "https://example.com/audio.mp3",
  "chat_room_id": "room-123",
  "personality": "buddy",
  "plan_active": true,
  "userdata": {
    "name": "John",
    "gender": "male",
    "age": 30
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| mp3_url | string (URL) | Public URL to an MP3 file containing speech |
| chat_room_id | string | Unique identifier for the chat session |
| personality | string | Personality to use ("girlfriend", "buddy", or "psychologist") |
| plan_active | boolean | Whether the user has a premium plan |
| userdata | object | User information for personalization |

#### Response

```json
{
  "message": "Hey there! How's it going?",
  "chat_room_id": "room-123",
  "timestamp": "2023-07-25T19:21:43.187915",
  "transcription": "Hello, can you hear me?"
}
```

| Field | Type | Description |
|-------|------|-------------|
| message | string | AI-generated response text |
| chat_room_id | string | The chat room identifier (same as request) |
| timestamp | string (ISO 8601) | When the response was generated |
| transcription | string | The transcribed text from the audio file |

## Project Structure

```
ai-voice-chatbot/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py       # Configuration and environment settings
│   │   └── prompts.py      # Personality prompts and templates
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py       # Pydantic data models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_service.py   # AI generation service
│   │   └── audio_service.py # Audio processing service
│   └── __init__.py
├── main.py                 # FastAPI app and endpoints
├── requirements.txt        # Project dependencies
└── README.md
```

## Personality Styles

### Girlfriend

A warm, playful, and affectionate companion who speaks in a casual, intimate style. Uses endearing terms and shows emotional support.

```
Input: "Hello, hello, can you hear me?"
Response: "Hey there, Alex! Loud and clear, babe. What's on your mind today?"
```

### Buddy

An energetic, fun-loving friend who's always ready with a joke or playful comment. Uses casual language and slang.

```
Input: "Hello, hello, can you hear me?"
Response: "Hey there, I hear ya loud and clear! What's up, buddy?"
```

### Psychologist

A thoughtful, insightful professional with expertise in human behavior and emotions. Formal yet warm, using professional language.

```
Input: "Hello, hello, can you hear me?"
Response: "Hello, Sir. I can hear you. How are you feeling today?"
```

## Error Handling

The API provides descriptive error messages with appropriate HTTP status codes:

- **400**: Bad request (e.g., invalid MP3 URL)
- **422**: Unprocessable entity (e.g., couldn't transcribe audio)
- **500**: Internal server error

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[MIT License](LICENSE) 
