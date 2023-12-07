import openai
from API_KEY import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

chat_log = []

while True:
    assistant_response = ""
    prompt = input("\n\n- Enter your prompt: ")
    chat_log.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=chat_log,
        stream=True,
    )

    for chunk in response:
        temp_chunk = chunk.choices[0].delta.content
        if temp_chunk is not None:
            assistant_response += temp_chunk
            print(temp_chunk, end="")

    chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip(" ")})
