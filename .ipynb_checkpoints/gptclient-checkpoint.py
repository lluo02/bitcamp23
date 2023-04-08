import openai,os,sys
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('API_KEY')



def generate_response(message):
    prompt = f"User: {message}\nChatGPT:"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message