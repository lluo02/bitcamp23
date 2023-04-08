from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import gptclient as gpt


texts = []

app = Flask(__name__)

@app.route("/texts", methods=['GET'])
def send_data():
    if request.method == 'GET':
        if texts[-1]:
            return str(texts[-1])
        else:
            return ''



@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():


    """Send a dynamic reply to an incoming text message"""
 
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Get the number of the sender
    sender_number = request.values.get('From', None)
    # Start our TwiML response
    resp = MessagingResponse()


    # Determine the right reply for this message
    if request.method == 'POST':
        gpt_response = gpt.generate_response("Write a response to this text message:" + body)

        resp.message(gpt_response)

    texts.append((body, gpt_response))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)