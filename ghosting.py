from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import gptclient as gpt


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
 
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()


    # Determine the right reply for this message
    if request.method == 'POST':
        gpt_response = gpt.generate_response("Write a response to this text message:" + body)

        resp.message(gpt_response)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)