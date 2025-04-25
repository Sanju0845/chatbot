from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load your OpenAI API key from an environment variable or secret management service
openai.api_key = os.getenv("AIzaSyC_Z4P0a4iqwA9Win51W-BQICYCnHdnBqM")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
