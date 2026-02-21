import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("OPENROUTER_API_KEY")

client= OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key

)
st.title("AI Career Assistant")
st.write("Ask career-related questions and get AI-powered advice.")


user_input= st.text_input("Enter your skills or career related query: ")

if(st.button("Get Advice")):
    if not user_input:
        st.write("Write something!")
    else:
        st.spinner("Generating response...")
        response= client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            max_tokens=300,
            messages=[
                {"role":"system","content":"You are a helpful career assistant and give best career related advices. Dont give very detaile answers. THe answers should be kept brief"},
                {"role":"user", "content":user_input}
            ]
        )
        st.subheader("AI Carrer Advice:")
        st.write(response.choices[0].message.content)