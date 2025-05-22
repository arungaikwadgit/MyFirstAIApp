from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_cohere import ChatCohere
from langchain import PromptTemplate

import streamlit as st
import os

# LLM Options and API Key Mapping
LLM_OPTIONS = {
    "Google Gemini": {"model": "gemini-1.5-flash-latest", "api_key_name": "GOOGLE_API_KEY", "class": ChatGoogleGenerativeAI},
    "OpenAI GPT-3.5": {"model": "gpt-3.5-turbo", "api_key_name": "OPENAI_API_KEY", "class": ChatOpenAI},
    "OpenAI GPT-4": {"model": "gpt-4", "api_key_name": "OPENAI_API_KEY", "class": ChatOpenAI},
    "Anthropic Claude 3 Sonnet": {"model": "claude-3-sonnet-20240229", "api_key_name": "ANTHROPIC_API_KEY", "class": ChatAnthropic},
    "Anthropic Claude 3 Haiku": {"model": "claude-3-haiku-20240307", "api_key_name": "ANTHROPIC_API_KEY", "class": ChatAnthropic},
    "Cohere Command R": {"model": "command-r", "api_key_name": "COHERE_API_KEY", "class": ChatCohere},
}

st.header("Tweet Generator - Arun Gaikwad")
st.subheader("Generate tweets using Generative AI")

selected_llm_name = st.selectbox("Choose your LLM:", options=list(LLM_OPTIONS.keys()))

llm = None  # Initialize llm to None

if selected_llm_name:
    selected_option = LLM_OPTIONS[selected_llm_name]
    api_key_name = selected_option["api_key_name"]
    api_key = st.secrets.get(api_key_name)

    if api_key:
        llm_class = selected_option["class"]
        model_name = selected_option["model"]
        
        if selected_llm_name == "Google Gemini":
            # For Google Gemini, pass the API key directly to the constructor
            llm = llm_class(model=model_name, google_api_key=api_key)
        else:
            llm = llm_class(model=model_name, api_key=api_key)
    else:
        st.error(f"API key for {selected_llm_name} ({api_key_name}) not found in st.secrets. Please add it to continue.")

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template=tweet_template, input_variables=['number', 'topic'])

# Create LLM chain using the prompt template and model
# This is now dynamic based on the selected LLM
if llm:
    tweet_chain = tweet_prompt | llm
else:
    tweet_chain = None # Or some default behavior if no LLM is selected/API key missing

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate") and llm:
    if tweet_chain:
        tweets = tweet_chain.invoke({"number": number, "topic": topic})
        st.write(tweets.content)
    else:
        # This case should ideally be prevented by the button condition 'and llm'
        st.error("LLM not initialized. Please select an LLM and ensure the API key is available.")
elif st.button("Generate") and not llm:
    st.error("LLM not initialized. Please select an LLM and ensure the API key is available.")
    
