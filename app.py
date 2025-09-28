import streamlit as st
import pandas as pd
from datetime import datetime
import random

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="Athlete Dashboard", layout="wide", page_icon="🏃‍♂️")

# -------------------------------
# Sidebar: Language & Theme
# -------------------------------
languages = {
    "English": "en",
    "Malayalam": "ml",
    "Tamil": "ta",
    "Telugu": "te",
    "Hindi": "hi",
    "Kannada": "kn"
}

selected_lang = st.sidebar.selectbox("Select Language / ഭാഷ / மொழி", options=list(languages.keys()))
dark_mode = st.sidebar.checkbox("Dark Mode", value=True)

# -------------------------------
# Theme CSS
# -------------------------------
bg_color = "#111111" if dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if dark_mode else "#000000"

st.markdown(f"""
<style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .stButton>button {{
        color: {text_color};
    }}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Athlete Data
# -------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("sample_athlete.csv", parse_dates=["date"])
    except:
        df = pd.DataFrame(columns=["sport","score","date","video_url"])
    return df

df = load_data()

# -------------------------------
# Athlete Profile
# -------------------------------
st.markdown(f"<h1 style='color:{text_color}'>🏅 Athlete Dashboard</h1>", unsafe_allow_html=True)

profile_col1, profile_col2 = st.columns([1,3])
with profile_col1:
    st.image("https://randomuser.me/api/portraits/men/1.jpg", width=120)
with profile_col2:
    st.markdown(f"<h3 style='color:{text_color}'>Name: Athlete 1</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:{text_color}'>Age: 20</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:{text_color}'>Gender: Male</h4>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# Sport Options
# -------------------------------
st.subheader("Select Your Sport / നിങ്ങളുടെ സ്പോർട്ട് / உங்கள் விளையாட்டு")

sports = df["sport"].unique()
selected_sport = st.radio("", options=sports)

sport_data = df[df["sport"]==selected_sport]

if not sport_data.empty:
    latest_score = sport_data.sort_values("date", ascending=False).iloc[0]["score"]
    highest_score = sport_data["score"].max()
    attempts = len(sport_data)

    st.markdown(f"**Latest Score:** {latest_score}")
    st.markdown(f"**Highest Score:** {highest_score}")
    st.markdown(f"**Attempts:** {attempts}")

    # Video Record / Upload
    st.markdown("### Record or Upload Video")
    video_file = st.file_uploader("Upload Video", type=["mp4"])
    camera_input = st.camera_input("Record Video")

    if video_file:
        st.video(video_file)
    elif camera_input:
        st.video(camera_input)
else:
    st.info("No data for this sport yet.")

st.markdown("---")

# -------------------------------
# Motivation Test
# -------------------------------
st.subheader("Motivation Test / പ്രചോദന പരീക്ഷ / உந்துதலை பரிசோதனை")

questions = [
    "Do you feel motivated today?",
    "Are you confident in your sport?",
    "Do you enjoy training?"
]

responses = []
for q in questions:
    col1, col2, col3 = st.columns(3)
    col1.button("😃 Yes", key=f"{q}-yes", on_click=lambda: responses.append(1))
    col2.button("😐 Maybe", key=f"{q}-maybe", on_click=lambda: responses.append(0))
    col3.button("😞 No", key=f"{q}-no", on_click=lambda: responses.append(-1))
    st.markdown(f"**{q}**")

if st.button("Show Motivation Score"):
    if responses:
        score = sum(responses)
        if score > 0:
            st.success("💪 You are motivated!")
        else:
            st.info("Keep pushing! You can do it 💪")
    else:
        st.warning("Answer the questions first!")
