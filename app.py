from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from llm import ask_llm

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    # Get what the user said from Twilio
    user_input = request.form.get("SpeechResult", "")

    # Send it to the LLM
    ai_reply = ask_llm(user_input)

    # Respond with Twilio's built-in voice (simpler for demo)
    vr = VoiceResponse()
    vr.say(ai_reply, voice="alice")

    # For demo: log transcript to console
    print(f"User: {user_input}")
    print(f"AI: {ai_reply}")

    return str(vr)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
