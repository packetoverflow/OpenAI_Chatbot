import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_KEY")

chatbot = OpenAI(api_key=openai_api_key)

while True:
    question = input('What is your question (type "quit" to exit): ')

    if question.lower() == 'quit':
        break

    response = chatbot.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": f"{question}"},
            ]
        )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(f"Question: {question} - Answer:")
    print("-----------------------------------------------------------------")
    print(result)