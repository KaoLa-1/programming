from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Set up OpenAI client with timeout
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    timeout=60.0  # Increase timeout to 60 seconds
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'response': 'Please enter a message'})
    
    max_retries = 2  # Maximum number of retries
    retry_count = 0
    
    while retry_count <= max_retries:
        try:
            # Use OpenAI's ChatGPT API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            
            bot_response = response.choices[0].message.content
            return jsonify({'response': bot_response})
        except Exception as e:
            error_message = str(e)
            retry_count += 1
            
            if "Request timed out" in error_message:
                if retry_count > max_retries:
                    return jsonify({'response': 'Error: 请求超时，请检查网络连接或稍后重试。您可以尝试：1. 检查网络连接 2. 简化问题 3. 稍后再试'})
                else:
                    # Wait before retrying
                    time.sleep(2)
                    continue
            elif "API key" in error_message:
                return jsonify({'response': 'Error: API密钥无效或未设置，请在.env文件中设置正确的API密钥'})
            else:
                return jsonify({'response': f'Error: {error_message}'})

if __name__ == '__main__':
    app.run(debug=True)
