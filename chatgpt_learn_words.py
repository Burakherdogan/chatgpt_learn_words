import openai
import gradio

openai.api_key = "your_APIs"

messages = [{"role": "system", "content": "You are a 4 grade child and you will definite word which is input."}]

def get_definiton(word):
    messages.append({"role": "user", "content": word})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=get_definiton, inputs = "text", outputs = "text", title = "4 grade child as a teacher :)")

demo.launch()