import streamlit as st
from groq import Groq

# Function to simulate SQL query result using Groq API
def get_sql_query_output(api_key, sql_query):
    try:
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Model for processing the query
            messages=[
                {
                    "role": "user",
                    "content": f"give sample output for given sql query? {sql_query}"
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        result = ""
        for chunk in completion:
            result += chunk.choices[0].delta.content or ""
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit App UI
st.set_page_config(page_title="SQL Query Viewer", layout="centered")
st.title("🔍 SQL Query Viewer")

# Introduction Section
st.markdown(
    """
    ### Welcome to the SQL Query Viewer! 👨‍💻
    This app allows you to input a SQL query and view the simulated output based on the query.
    Provide the required details below, and we'll show the expected output from the query.
    """
)

# Input Section for API Key and SQL Query
st.markdown("#### 🔑 Enter Your Details:")
api_key = "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"
sql_query = st.text_area("Enter SQL Query:", placeholder="Type your SQL query here...")

# Processing and Displaying Results
if st.button("🚀 Get Query Output"):
    if not api_key or not sql_query:
        st.error("⚠️ Please provide both the API key and the SQL query.")
    else:
        st.markdown("### ⏳ Processing your SQL query... Please wait!")
        solution = get_sql_query_output(api_key, sql_query)
        
        st.markdown(f"### Simulated Output:\n{solution}")
