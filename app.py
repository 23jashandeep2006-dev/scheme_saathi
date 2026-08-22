import streamlit as st
import pandas as pd
schemes = pd.read_csv("schemes.csv")

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="SchemeSaathi",
    page_icon="🇮🇳",
    layout="centered"
)

# -----------------------------
# TITLE
# -----------------------------

st.title("🇮🇳 SchemeSaathi")
st.subheader("Government schemes, made easier.")

st.write(
    "Tell us a little about yourself and we will help you find "
    "possible government schemes."
)

st.divider()

# -----------------------------
# USER DETAILS
# -----------------------------

st.header("👤 Tell us about yourself")
query = st.text_input(
    "💬 Tell us what you need",
    placeholder="Example: I need a scholarship, I'm from Punjab."
)
# Understand simple keywords from the user's message
query_lower = query.lower()

if "scholarship" in query_lower or "education" in query_lower:
    detected_need = "Scholarship / Education"

elif "farmer" in query_lower or "farming" in query_lower:
    detected_need = "Farmer Support"

elif "women" in query_lower or "family" in query_lower:
    detected_need = "Women & Family Support"

else:
    detected_need = None
    # Detect state from the user's message
detected_state = None

if "punjab" in query_lower:
    detected_state = "Punjab"

elif "haryana" in query_lower:
    detected_state = "Haryana"

elif "himachal" in query_lower:
    detected_state = "Himachal Pradesh"

elif "delhi" in query_lower:
    detected_state = "Delhi"

need = st.selectbox(
    "What are you looking for?",
    [
        "Scholarship / Education",
        "Farmer Support",
        "Women & Family Support"
    ]
)
# Use the detected need from the user's message
if detected_need is not None:
    need = detected_need

state = st.selectbox(
    "Which state are you from?",
    [
        "Punjab",
        "Haryana",
        "Himachal Pradesh",
        "Delhi",
        "Other"
    ]
)
if detected_state is not None:
    state = detected_state

age = st.number_input(
    "What is your age?",
    min_value=1,
    max_value=100,
    value=17
)
class12_percentile = st.number_input(
    "Class 12 percentile",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=0.1
)

income = st.selectbox(
    "Approximate annual family income",
    [
        "Below ₹1 lakh",
        "₹1–2.5 lakh",
        "₹2.5–5 lakh",
        "Above ₹5 lakh",
        "I don't know"
    ]
)

# -----------------------------
# FIND SCHEMES BUTTON
# -----------------------------

if st.button("🔎 Find My Schemes", use_container_width=True):

    st.divider()

    st.header("✨ Possible Matches")

    # Student example
    if need == "Scholarship / Education":

        # Find scholarship schemes from our CSV
        scholarship_schemes = schemes[
            schemes["category"] == "Scholarship / Education"
        ]

        if not scholarship_schemes.empty:
            scheme = scholarship_schemes.iloc[0]

            st.subheader(f"🎓 {scheme['scheme_name']}")

            st.write(
                "This scheme was found in our structured government-scheme dataset."
            )

            st.markdown("### 📋 Eligibility")
            st.write(scheme["eligibility"])

            st.markdown("### 🎁 Benefits")
            st.write(scheme["benefits"])

            st.markdown("### 📄 Documents")
            st.write(scheme["documents"])

            st.markdown("### 🔗 Official Source")
            st.write(scheme["official_url"])

    # Simple rule-based matching
    likely_match = True
    reasons = []

    if state == "Other":
        likely_match = False
    else:
        reasons.append(f"State: {state}")

    if age <= 25:
        reasons.append(f"Age: {age}")
    else:
        likely_match = False
    if class12_percentile > 80:
        reasons.append(f"Class 12 percentile: {class12_percentile}%")
    else:
        likely_match = False

    if income in ["Below ₹1 lakh", "₹1–2.5 lakh", "₹2.5–5 lakh"]:
        reasons.append(f"Income: {income}")
    else:
        likely_match = False

    # Result
    if likely_match:

        st.success("🎓 Likely Match")

        st.write(
            "Based on the information provided, "
            "you may fit the basic criteria used by this prototype."
        )

        st.markdown("### ✅ Why you may match")

        for reason in reasons:
            st.write("•", reason)

    else:

        st.warning("⚠️ Needs Further Verification")

        st.write(
            "Some of the information provided does not fit "
            "the basic matching rules used by this prototype."
        )

        st.markdown("### 📄 Documents you may need")

        st.write("""
        - Identity proof
        - Income certificate
        - Previous marksheet
        - Bank account details
        """)

        st.markdown("### ➡️ Next Step")

        st.write(
            "Verify the final eligibility, documents and application "
            "process using the official government scheme information."
        )

        st.info(
            "Prototype note: This is rule-based matching for demonstration. "
            "It does not make an official eligibility decision."
        )
    
    # Farmer example
    if need == "Farmer Support":

        st.success("🌾 We found a possible farmer-support match!")

        st.subheader("Farmer Welfare Scheme")

        st.write(
            "This prototype searches for schemes designed to support "
            "farmers and agricultural households."
        )

        st.markdown("### Information we would check")

        st.write("✅ Farmer status")
        st.write(f"✅ State: {state}")
        st.write(f"✅ Income category: {income}")

        st.markdown("### 📄 Documents you may need")

        st.write("""
        - Identity proof
        - Land / farmer records
        - Bank account details
        """)

    # Women and family example
    else:

        st.success("👩 We found a possible family-support match!")

        st.subheader("Women & Family Support Scheme")

        st.write(
            "This prototype identifies schemes that may support "
            "women and families."
        )

        st.markdown("### Information we would check")

        st.write("✅ Scheme category")
        st.write(f"✅ State: {state}")
        st.write(f"✅ Income category: {income}")

        st.markdown("### 📄 Documents you may need")

        st.write("""
        - Identity proof
        - Income certificate, if required
        - Bank account details
        """)

    st.divider()

    st.caption(
        "SchemeSaathi — AI Government Scheme Assistant | "
        "Bharat Buildathon 2026"
    )