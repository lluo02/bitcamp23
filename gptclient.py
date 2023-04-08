import openai,os,sys
from dotenv import load_dotenv
import predict_spam

load_dotenv()
openai.api_key = os.getenv('API_KEY')

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Don't answer questions, but respond to queries like they are text messages."}
        ])

def generate_response(message):
    prompt = f"User: {message}\nChatGPT:"
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )
    message = response.choices[0].text.strip()
    print(predict_spam.predict_spam(message))
    #print(message)
    return message

