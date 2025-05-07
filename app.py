import streamlit as st
import pandas as pd

st.title("📚 Vocabulary List Viewer")

# Sample vocabulary data
data = {
    "Word": ["analyze", "construct", "define", "evaluate"],
    "Part of Speech": ["verb", "verb", "verb", "verb"],
    "Example": [
        "Please analyze the text.",
        "The students construct a model.",
        "Can you define this term?",
        "We evaluate the results together."
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)


import streamlit as st
import pandas as pd

st.title("📝 English Word Quiz")

question = "What is the synonym of *happy*?"
options = ["angry", "sad", "joyful", "tired", "hungry"]
answer = "joyful"

# ✅ Display the question
st.markdown(question)

user_choice = st.radio("Choose the correct answer:", options)

if st.button("Check Answer"):
    if user_choice == answer:
        st.success("Correct!")
    else:
        st.error("Not quite. Try again.")

import streamlit as st
import pandas as pd
import requests
import io

st.title("📘 English Quiz from CSV")

# --- STEP 1: Load TSV (tab-separated) CSV from GitHub ---
csv_url = "https://raw.githubusercontent.com/yourid/repo/main/quiz_questions.csv"  # use .tsv if applicable

try:
    response = requests.get(csv_url)
    response.raise_for_status()
    
    # ✅ Use sep='\t' for tab-separated files
    df = pd.read_csv(io.StringIO(response.text))

    # ✅ Normalize column names
    df.columns = df.columns.str.strip().str.replace(" ", "").str.capitalize()

except Exception as e:
    st.error(f"❌ Failed to load quiz data: {e}")
    st.stop()

# --- STEP 2: Display Quiz Questions ---
st.header("🧠 Take the Quiz")

if df.empty:
    st.warning("The quiz file is empty or incorrectly formatted.")
else:
    for idx, row in df.iterrows():
        question = row["Question"]
        options = [row[f"Option{i}"] for i in range(1, 6)]
        correct_answer = row["Answer"]

        st.subheader(f"Q{idx+1}: {question}")
        user_choice = st.radio("Choose one:", options, key=f"q_{idx}")

        if st.button("Check Answer", key=f"check_{idx}"):
            if user_choice == correct_answer:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Not quite. The correct answer is **{correct_answer}**")

from gtts import gTTS
from io import BytesIO

st.title("🔊 Pronunciation Practice")

word = st.text_input("Enter a word to hear it:")

if word:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp.getvalue(), format="audio/mp3")
