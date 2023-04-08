import openai,os,sys
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('GPT_API_KEY')

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a very kind helpdesk agent."}
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
    return message
