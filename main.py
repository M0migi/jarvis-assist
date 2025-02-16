from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI APIキー（環境変数から取得する方法）
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "JARVIS is online."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    if not user_input:
        return jsonify({"error": "メッセージを入力してください"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 使いたいモデルを選択
            messages=[{"role": "system", "content": "あなたはJARVISというAIアシスタントです。"}] +
                     [{"role": "user", "content": user_input}]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
