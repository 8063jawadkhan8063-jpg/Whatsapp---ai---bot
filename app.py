from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp AI Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Incoming message:", data)
    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run()
