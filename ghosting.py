from flask import Flask, request, redirect, render_template
from twilio.twiml.messaging_response import MessagingResponse
import gptclient as gpt
from predict_spam import predict_spam
from flask_cors import CORS

texts = []

parent_numbers = []

friend_numbers = []

app = Flask(__name__)
CORS(app)

@app.route("/texts", methods=['GET'])
def send_data():
    if request.method == 'GET':
        if len(texts) > 0:
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
    
    #Predict if it is spam with accuracy > 0.8
    if predict_spam([body])[0][0] > 0.8:
        resp.message('STOP UNSUBSCRIBE OPT OUT')
        return str(resp)
    


    # Determine the right reply for this message
    if request.method == 'POST':

        #Check if number is a friend of parent
        if sender_number in parent_numbers:
            gpt_response = gpt.generate_parent_response('Write a response to this text message:' + body)

        elif sender_number in friend_numbers:
            gpt_response = gpt.generate_friend_response('Write a response to this text message:' + body)

        else:
            gpt_response = gpt.generate_response('Write a response to this text message:' + body)
            

        resp.message(gpt_response)

    texts.append((body, gpt_response))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)