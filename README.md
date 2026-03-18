# ChatBot Application

This is a simple ChatBot application built using Flask and OpenAI's ChatGPT API.

## Features
- Web-based interface for interacting with the ChatBot
- Uses OpenAI's ChatGPT API for natural language processing
- Simple and intuitive user interface

## Requirements
- Python 3.7+
- Flask
- OpenAI Python SDK

## Installation
1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:5000`
3. Type your message in the input field and press Enter to chat with the bot

## Project Structure
- `app.py`: Main application file
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript)
- `requirements.txt`: Dependencies
- `.env`: Environment variables
