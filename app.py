import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Athlete Dashboard", layout="wide", page_icon="🏃‍♂️")

# -------------------------------
# Language Dictionary (8 Languages)
# -------------------------------
lang_dict = {
    "English": {
        "dashboard_title": "🏅 Athlete Dashboard",
        "profile_name": "Name",
        "profile_age": "Age",
        "profile_gender": "Gender",
        "profile_state": "State",
        "select_sport": "Your Sports",
        "latest_score": "Latest Score",
        "highest_score": "Highest Score",
        "attempts": "Attempts",
        "last_feedback": "Last Feedback / Problem",
        "record_rules": "Recording Rules",
        "record_upload_video": "Record Video",
        "Sprinting":"Sprinting","Long Jump":"Long Jump","High Jump":"High Jump","Shot Put":"Shot Put",
        "Discus Throw":"Discus Throw","Javelin Throw":"Javelin Throw","Hurdles":"Hurdles","Relay Race":"Relay Race",
        "Pole Vault":"Pole Vault","Marathon":"Marathon"
    },
    "Hindi": {
        "dashboard_title": "🏅 एथलीट डैशबोर्ड",
        "profile_name": "नाम","profile_age": "आयु","profile_gender": "लिंग","profile_state": "राज्य",
        "select_sport": "आपके खेल","latest_score": "नवीनतम स्कोर","highest_score": "उच्चतम स्कोर",
        "attempts": "प्रयास","last_feedback": "पिछली प्रतिक्रिया / समस्या","record_rules": "रिकॉर्डिंग नियम",
        "record_upload_video": "वीडियो रिकॉर्ड करें",
        "Sprinting":"दौड़","Long Jump":"लंबा कूद","High Jump":"ऊंचा कूद","Shot Put":"शॉट पुट",
        "Discus Throw":"डिस्कस थ्रो","Javelin Throw":"भाला फेंक","Hurdles":"हर्डल्स","Relay Race":"रिले दौड़",
        "Pole Vault":"पोल वॉल्ट","Marathon":"मैराथन"
    },
    "Marathi": {
        "dashboard_title": "🏅 अ‍ॅथलीट डॅशबोर्ड",
        "profile_name":"नाव","profile_age":"वय","profile_gender":"लिंग","profile_state":"राज्य",
        "select_sport":"तुमचे खेळ","latest_score":"अंतिम गुण","highest_score":"सर्वोच्च गुण",
        "attempts":"प्रयत्न","last_feedback":"मागील प्रतिक्रिया / समस्या","record_rules":"रेकॉर्डिंग नियम",
        "record_upload_video":"व्हिडिओ रेकॉर्ड करा",
        "Sprinting":"धाव","Long Jump":"लांब उडी","High Jump":"उंच उडी","Shot Put":"शॉट पुट",
        "Discus Throw":"डिस्कस थ्रो","Javelin Throw":"भाला फेक","Hurdles":"हर्डल्स","Relay Race":"रिले रेस",
        "Pole Vault":"पोल व्हॉल्ट","Marathon":"मॅरेथॉन"
    },
    "Telugu": {
        "dashboard_title":"🏅 అథ్లీట్ డాష్‌బోర్డ్","profile_name":"పేరు","profile_age":"వయస్సు","profile_gender":"లింగం",
        "profile_state":"రాష్ట్రం","select_sport":"మీ ఆటలు","latest_score":"చివరి స్కోరు","highest_score":"గరిష్ట స్కోరు",
        "attempts":"ప్రయత్నాలు","last_feedback":"చివరి అభిప్రాయం / సమస్య","record_rules":"రికార్డింగ్ నియమాలు",
        "record_upload_video":"వీడియో రికార్డు చేయండి",
        "Sprinting":"ఒడిస్సు","Long Jump":"పెద్ద జంప్","High Jump":"హై జంప్","Shot Put":"షాట్ పుట్",
        "Discus Throw":"డిస్కస్ దూకుడు","Javelin Throw":"జావెలిన్ త్రో","Hurdles":"హర్డల్స్","Relay Race":"రిలే రేస్",
        "Pole Vault":"పోల్ వాల్ట్","Marathon":"మారథాన్"
    },
    "Tamil": {
        "dashboard_title":"🏅 அணிவகுப்பு வீரர் டாஷ்போர்டு","profile_name":"பெயர்","profile_age":"வயது","profile_gender":"பாலினம்",
        "profile_state":"மாநிலம்","select_sport":"உங்கள் விளையாட்டுகள்","latest_score":"சமீபத்திய மதிப்பெண்",
        "highest_score":"உயர்ந்த மதிப்பெண்","attempts":"முயற்சிகள்","last_feedback":"கடந்த கருத்து / பிரச்சனை",
        "record_rules":"பதிவு விதிகள்","record_upload_video":"வீடியோ பதிவு செய்யவும்",
        "Sprinting":"ஓட்டம்","Long Jump":"நீளம் குதிப்பு","High Jump":"உயர் குதிப்பு","Shot Put":"ஷாட் புட்",
        "Discus Throw":"டிஸ்கஸ் தள்ளல்","Javelin Throw":"ஜாவலின் தள்ளல்","Hurdles":"ஹர்டில்ஸ்","Relay Race":"ரிலே ஓட்டம்",
        "Pole Vault":"போல் வால்ட்","Marathon":"மேரத்தான்"
    },
    "Kannada": {
        "dashboard_title":"🏅 ಅಥ್ಲೀಟ್ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್","profile_name":"ಹೆಸರು","profile_age":"ವಯಸ್ಸು","profile_gender":"ಲಿಂಗ",
        "profile_state":"ರಾಜ್ಯ","select_sport":"ನಿಮ್ಮ ಆಟಗಳು","latest_score":"ಇತ್ತೀಚಿನ ಅಂಕ","highest_score":"ಗರಿಷ್ಟ ಅಂಕ",
        "attempts":"ಪ್ರಯತ್ನಗಳು","last_feedback":"ಕಳೆದ ಪ್ರತಿಕ್ರಿಯೆ / ಸಮಸ್ಯೆ","record_rules":"ರೆಕಾರ್ಡಿಂಗ್ ನಿಯಮಗಳು",
        "record_upload_video":"ವೀಡಿಯೋ ರೆಕಾರ್ಡ್ ಮಾಡಿ",
        "Sprinting":"ಓಟ","Long Jump":"ಉದ್ದ ಜಂಪ್","High Jump":"ಹೈ ಜಂಪ್","Shot Put":"ಶಾಟ್ ಪುಟ್",
        "Discus Throw":"ಡಿಸ್ಕಸ್ ತ್ರೋ","Javelin Throw":"ಜಾವಲಿನ್ ತ್ರೋ","Hurdles":"ಹರ್ಡಲ್ಸ್","Relay Race":"ರಿಲೇ ರೇಸ್",
        "Pole Vault":"ಪೋಲ್ ವಾಲ್ಟ್","Marathon":"ಮ್ಯಾರಥಾನ್"
    },
    "Malayalam": {
        "dashboard_title":"🏅 അഥ്ലറ്റ് ഡാഷ്ബോർഡ്","profile_name":"പേര്","profile_age":"വയസ്","profile_gender":"ലിംഗം",
        "profile_state":"സംസ്ഥാനം","select_sport":"നിങ്ങളുടെ കളികൾ","latest_score":"അവസാന സ്കോര്","highest_score":"മിക്ക സ്കോര്",
        "attempts":"പ്രയത്നങ്ങള്‍","last_feedback":"കഴിഞ്ഞ പ്രതികരണം / പ്രശ്നം","record_rules":"റെക്കോർഡിങ് നിബന്ധനകൾ",
        "record_upload_video":"വീഡിയോ റെക്കോർഡ് ചെയ്യുക",
        "Sprinting":"ഓട്ടം","Long Jump":"വീധികുതിപ്പ്","High Jump":"ഉയര്കുതിപ്പ്","Shot Put":"ഷോട്ട് പുട്",
        "Discus Throw":"ഡിസ്‌കസ് തള്ളി","Javelin Throw":"ജാവലിന്‍ തള്ളി","Hurdles":"ഹർഡിൽസ്","Relay Race":"റിലേ റേസ്",
        "Pole Vault":"പോൾ വാൾട്ട്","Marathon":"മാരത്തോൺ"
    },
    "Tulu": {
        "dashboard_title":"🏅 ಅತ್ಲೀಟ್ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್","profile_name":"ಪೇರ್","profile_age":"ಆಯು","profile_gender":"ಲಿಂಗ","profile_state":"ರಾಜ್ಯ",
        "select_sport":"ನಿಮ್ಮ ಆಟುಗಳು","latest_score":"ಕೊನೆಯ ಅಂಕ","highest_score":"ಅತಿವೈಶಿಷ್ಟ್ಯ ಅಂಕ","attempts":"ಪ್ರಯತ್ನ","last_feedback":"ಕೊನೆಯ ಪ್ರತಿಕ್ರಿಯೆ / ಸಮಸ್ಯೆ",
        "record_rules":"ರೆಕಾರ್ಡಿಂಗ್ ನಿಯಮಗಳು","record_upload_video":"ವೀಡಿಯೋ ರೆಕಾರ್ಡ್ ಮಾಡಿ",
        "Sprinting":"ಓಟ","Long Jump":"ಉದ್ದ ಜಂಪ್","High Jump":"ಹೈ ಜಂಪ್","Shot Put":"ಶಾಟ್ ಪುಟ್",
        "Discus Throw":"ಡಿಸ್ಕಸ್ ತ್ರೋ","Javelin Throw":"ಜಾವಲಿನ್ ತ್ರೋ","Hurdles":"ಹರ್ಡಲ್ಸ್","Relay Race":"ರಿಲೇ ರೇಸ್",
        "Pole Vault":"ಪೋಲ್ ವಾಲ್ಟ್","Marathon":"ಮ್ಯಾರಥಾನ್"
    }
}

# -------------------------------
# Sidebar Options
# -------------------------------
selected_lang = st.sidebar.selectbox("Select preferred Language", list(lang_dict.keys()))
t = lang_dict[selected_lang]

dark_mode = st.sidebar.checkbox("Dark Mode", value=True)
bg_color = "#111111" if dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if dark_mode else "#000000"

st.markdown(f'''
<style>
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}
.sport-banner {{
    border-radius: 20px;
    padding: 20px;
    margin: 15px 0;
    display: flex;
    align-items: center;
    color: white;
    font-size: 20px;
    height: 150px;
}}
.sport-image {{
    height: 130px;
    width: 130px;
    object-fit: cover;
    border-radius: 15px;
    margin-right: 15px;
}}
</style>
''', unsafe_allow_html=True)

# -------------------------------
# Sample Athlete Data with GitHub Images
# -------------------------------
sports_data = [
    {"sport": s, "score": 80+i*2, "highest": 90+i, "attempts": i+3,
     "last_feedback":"Some issue detected", 
     "color": f"#FF{hex(20+i*20)[2:]}33",
     "image": f"https://raw.githubusercontent.com/sportsprojectapp/athlete_version/main/{s.replace(' ','').lower()}.jpg",
     "rules":["Follow camera rules","Wear proper attire","Full body visible"]}
    for i,s in enumerate(["Sprinting","Long Jump","High Jump","Shot Put","Discus Throw","Javelin Throw","Hurdles","Relay Race","Pole Vault","Marathon"])
]

# -------------------------------
# Profile Section
# -------------------------------
st.markdown(f"<h1 style='color:{text_color}'>{t['dashboard_title']}</h1>", unsafe_allow_html=True)
profile_col1, profile_col2 = st.columns([1,3])
with profile_col1:
    st.image(f"https://raw.githubusercontent.com/sportsprojectapp/athlete_version/main/athlete.jpg", width=120)
with profile_col2:
    st.markdown(f"**{t['profile_name']}:** Athlete 1")
    st.markdown(f"**{t['profile_age']}:** 20")
    st.markdown(f"**{t['profile_gender']}:** Male")
    st.markdown(f"**{t['profile_state']}:** Kerala")

st.markdown("---")

# -------------------------------
# Sport Banners
# -------------------------------
st.subheader(t['select_sport'])
for sport in sports_data:
    sport_name_lang = t.get(sport["sport"], sport["sport"])
    with st.expander(f"{sport_name_lang}"):
        banner_html = f'''
        <div class="sport-banner" style="background-color:{sport['color']};">
            <img src="{sport['image']}" class="sport-image">
            <div>
                <b>{sport_name_lang}</b><br>
                {t['latest_score']}: {sport['score']} | {t['highest_score']}: {sport['highest']} | {t['attempts']}: {sport['attempts']}<br>
                {t['last_feedback']}: {sport['last_feedback']}
            </div>
        </div>
        '''
        st.markdown(banner_html, unsafe_allow_html=True)
        st.markdown(f"**{t['record_rules']}:**")
        for rule in sport['rules']:
            st.markdown(f"- {rule}")
        recorded_video = st.camera_input(t['record_upload_video'], key=sport['sport'])
        if recorded_video:
            st.video(recorded_video)

