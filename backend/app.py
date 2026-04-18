from flask import Flask, request, jsonify

app = Flask(__name__)

scam_keywords = [
    "win money", "urgent", "click link", "lottery",
    "free prize", "bank alert", "otp", "verify now"
]

def detect_scam(message):
    message = message.lower()
    score = 0

    for word in scam_keywords:
        if word in message:
            score += 1

    if score >= 2:
        return "Scam ❌"
    elif score == 1:
        return "Suspicious ⚠️"
    else:
        return "Safe ✅"

@app.route("/check", methods=["POST"])
def check_message():
    data = request.json
    message = data.get("message")

    result = detect_scam(message)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
