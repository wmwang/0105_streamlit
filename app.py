import streamlit as st
import openai
import opencc

# 設定 OpenAI API 密鑰
openai.api_key = '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'

# Streamlit App 的標題
st.title("OpenAI Chatbot")

# 用於與 OpenAI 進行對話的函數
def chat_with_openai(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150  # 控制生成文本的最大長度
    )
    return response.choices[0].text.strip()

# 與 OpenAI 進行對話的 Streamlit 部分
user_input = st.text_input("你想對 Chatbot 說些什麼?")

converter = opencc.OpenCC('s2t')
if user_input:
    st.text("Chatbot 的回應:")
    chatbot_response = chat_with_openai(user_input)
    st.write(converter.convert(chatbot_response))
