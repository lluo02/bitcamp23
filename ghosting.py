from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from predict_spam import predict_spam, tokenize
from gptclient import generate_response

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
 
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()
    
    print(predict_spam(tokenize(body)))
    # Determine the right reply for this message
    if request.method == 'POST':
        if body == 'hello':
            resp.message(generate_response(body))
        elif body == 'bye':
            resp.message("Goodbye")
        else:
            resp.message("Testing")

    return str(resp)

@app.route("/contacts", methods=['GET', 'POST'])
def update_contacts():
    contacts = ['Mom', 'Roommate', 'Boss', 'Group Project', 'Ex', 'Kevin']
    return ""

if __name__ == "__main__":
    app.run(debug=True)