from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Configure the Gemini API
GEMINI_API_KEY = 'AIzaSyC_Z4P0a4iqwA9Win51W-BQICYCnHdnBqM'
genai.configure(api_key=GEMINI_API_KEY)

# Create a model instance
model = genai.GenerativeModel('gemini-pro')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400

        # Generate response using Gemini
        response = model.generate_content(message)
        
        return jsonify({
            'response': response.text
        })

    except Exception as e:
        print(f"Error: {str(e)}")  # For debugging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) 
