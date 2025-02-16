from flask import Flask, request, jsonify
import random
import textblob

app = Flask(__name__)

@app.route("/")
def home():
    return "JARVIS is online."

@app.route("/decision", methods=["GET"])
def decision_assist():
    options = request.args.get("options", "").split(",")
    if not options or options == [""]:
        return "選択肢がありません。"

    choice = random.choice(options)
    return f"おすすめは「{choice}」です。"

@app.route("/emotion", methods=["POST"])
def emotion_analysis():
    data = request.json
    text = data.get("text", "")

    analysis = textblob.TextBlob(text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        return jsonify({"emotion": "ポジティブ", "message": "いいですね！"})
    elif sentiment < 0:
        return jsonify({"emotion": "ネガティブ", "message": "大丈夫ですか？"})
    else:
        return jsonify({"emotion": "ニュートラル", "message": "特に問題なさそうです。"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
