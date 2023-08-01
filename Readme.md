Project for Bitcamp 2023, an annual UMD hosted hackathon

This project connects a flask front end to a python script that interacts with the Twilio API to route text messages to a pre-registered phone number, from which it then generates an automated response depending on the incoming text by running the text on a text generation model optimized from GPT3.5 via OpenAI's API with the goal of expressing that the message will be returned at a later date. 

Before sending them to the API, incoming texts are first run against a locally trained LSTM based classifier to identify if they are spam messages. If the model suspects spam with a 90% confidence, then the sender will be ghosted. Moreover, if it suspects the message to be an advertisement, then it will attempt to opt out of the messages by sending keywords such as "STOP" and "UNSUSCRIBE".
