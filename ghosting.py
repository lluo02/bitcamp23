from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from predict_spam import predict_spam

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
 
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()
    
    print(predict_spam(body))
    # Determine the right reply for this message
    if request.method == 'POST':
        if body == 'hello':
            resp.message("Hi!")
        elif body == 'bye':
            resp.message("Goodbye")
        else:
            resp.message("Testing")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)