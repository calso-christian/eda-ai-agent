import streamlit as st
import pandas as pd
from agent import agent_start

# Initialize Streamlit
st.set_page_config(page_title="EDA Agent", layout="wide")
st.title("📊 EDA Agent Assistant")

# Initialize session state for history if not already present
if "history" not in st.session_state:
    st.session_state.history = []

# Get user query
user_query = st.text_input("💬 Ask a question about your data:")

# Only invoke agent when user submits a query
if user_query:
    with st.spinner("🤖 Thinking..."):
        agent = agent_start()
        response = agent.invoke({"input": user_query})

        # Store to history
        st.session_state.history.append({
            "query": user_query,
            "response": response
        })

# Show query history (most recent first)
if st.session_state.history:
    st.markdown("## 📜 Query History")
    for i, entry in enumerate(reversed(st.session_state.history)):
        st.markdown(f"**Q{i+1}:** {entry['query']}")
        
        # Extract output safely
        output = entry["response"].get("output", "")
        st.markdown(f"**🧠 Answer:** {output}")

        # Attempt to extract and display SQL preview
        intermediate_steps = entry["response"].get("intermediate_steps", [])
        sql_query = None
        for step in intermediate_steps:
            if isinstance(step, tuple) and "SELECT" in step[0]:
                sql_query = step[0]
                break
        
        if sql_query:
            with st.expander("📝 SQL Preview"):
                st.code(sql_query, language="sql")

        # Try to detect if output is table-like
        if isinstance(output, str) and output.strip().startswith("[["):
            try:
                df = pd.DataFrame(eval(output))
                st.dataframe(df)
            except:
                pass
