import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

load_dotenv()
st.set_page_config(page_title="Real-World Automated Blogger", page_icon="✍️", layout="centered")
# 1. Model
llm = ChatMistralAI(model="mistral-large-latest", temperature=0.9, max_tokens=1000)
#2. Tool
search_tool = DuckDuckGoSearchRun()
#3. Agent Logic
def web_search_node(inputs: dict) -> dict:
    """Execute a web search based on the user's topic to find real-world events."""
    topic = inputs["topic"]
    print(f"\n🔍 Searching the live web for current events regarding: '{topic}'...")
    search_results = search_tool.invoke(topic)
    return {"topic": topic, "web_context": search_results}

blog_prompt = ChatPromptTemplate.from_messages([
    ("system", (
    """
    You are an expert real-time news blogger. Write a short, high-impact blog post.
    CRITICAL RULES FOR TOKEN MINIMIZATION:
    - Your total output MUST be under 400 words.
    - Focus strictly on summarizing the factual context provided.
    - No filler words, long intros, or unnecessary sign-offs.
    """)),
    ("human", (
        """"
        Topic: {topic}
        Real-world context found:\n{web_context}
        Write the blog post now:
        """
    ))
])


sequential_chain = (RunnableLambda(web_search_node) | blog_prompt | llm)

st.title("✍️ Real-World Automated Blogger")
st.write("Enter a trending topic or news headline below to generate a short, high-impact blog post backed by live web data.")

# User Input
user_topic = st.text_input("Enter the topic/news you want a blog post about:", placeholder="e.g., James Webb Telescope latest discovery")
if st.button("Generate Blog Post", type="primary"):
    if user_topic.strip():
        try:
            # Spinner to let the user know the backend is working
            with st.spinner("Processing your request..."):
                response = sequential_chain.invoke({"topic": user_topic})
            
            # Displaying the Result
            st.success("✨ Blog Post Generated Successfully!")
            st.markdown("---")
            st.markdown(response.content)
            st.markdown("---")
            
            # Subtle footer info
            st.caption("Token Burn Prevention: Output safely capped at 1000 max tokens.")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic before generating.")