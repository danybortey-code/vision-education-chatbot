import streamlit as st

st.title("👁️ Vision Chatbot")
st.info("Educational only — not a medical diagnosis.")

# ----------------------------
# Consent gate
# ----------------------------
consent = st.checkbox("I understand and want to continue.")

# ----------------------------
# Session state initialization
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "idle"

if "case" not in st.session_state:
    st.session_state.case = {
        "blur_type": None,
        "eye": None,
        "onset": None
    }

def add_message(role, content):
    st.session_state.messages.append({
        "role": role,
        "content": content
    })

# ----------------------------
# Show chat history
# ----------------------------
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ----------------------------
# Block chat until consent
# ----------------------------
if not consent:
    st.write("✅ Check the box above to start chatting.")
    st.write("Hello — how can I help you today?")
    st.stop()

# ----------------------------
# Chat input
# ----------------------------
user_text = st.chat_input("Describe your vision problem...")

if user_text:

    add_message("user", user_text)
    msg = user_text.lower().strip()

    # ----------------------------
    # Small talk / greetings
    # ----------------------------
    greetings = ["hi", "hello", "hey"]
    thanks = ["thank you", "thanks", "thx"]
    casual = ["ok", "okay", "cool", "great"]

    if any(g in msg for g in greetings):
        add_message(
            "assistant",
            "Hello 🙂 How can I help you with your vision today? "
            "Is the blur worse for **near (reading/close)** or **distance (far)**?"
        )
        st.rerun()

    if any(t in msg for t in thanks):
        add_message(
            "assistant",
            "You are welcome. Come back any day, any time for eye care education."
        )
        st.rerun()

    if any(c == msg for c in casual):
        add_message(
            "assistant",
            "Tell me about your vision — is the blur worse for **near** or **distance**?"
        )
        st.rerun()

    # ----------------------------
    # Immediate safety red flags
    # ----------------------------
    if any(w in msg for w in ["pain", "flash", "flashes", "floater", "floaters"]):
        add_message(
            "assistant",
            "\n- ⚠️ **Possible warning signs detected**\n"
            "- Flashes, floaters, or eye pain can indicate a serious issue.\n"
            "- **Recommended action:** seek urgent eye care."
        )
        st.session_state.stage = "idle"
        st.session_state.case = {"blur_type": None, "eye": None, "onset": None}
        st.rerun()

    # ----------------------------
    # Intake flow logic
    # ----------------------------
    if st.session_state.stage == "idle":

        if "distance" in msg or "far" in msg:
            st.session_state.case["blur_type"] = "distance"
            st.session_state.stage = "ask_eye"
            add_message(
                "assistant",
                "To guide you better — is the blur affecting **one eye or both eyes**?"
            )
            st.rerun()

        elif "near" in msg or "reading" in msg or "close" in msg:
            st.session_state.case["blur_type"] = "near"
            st.session_state.stage = "ask_eye"
            add_message(
                "assistant",
                "To guide you better — is the blur affecting **one eye or both eyes**?"
            )
            st.rerun()

        else:
            add_message(
                "assistant",
                "I can help with blur that is worse for **near (reading/close)** or **distance (far)**. Which one fits your case?"
            )
            st.rerun()

    elif st.session_state.stage == "ask_eye":

        if "both" in msg:
            st.session_state.case["eye"] = "both"
        elif "one" in msg or "left" in msg or "right" in msg:
            st.session_state.case["eye"] = "one eye"
        else:
            st.session_state.case["eye"] = "not sure"

        st.session_state.stage = "ask_onset"
        add_message(
            "assistant",
            "Did this start **suddenly** or **gradually**?"
        )
        st.rerun()

    elif st.session_state.stage == "ask_onset":

        if "grad" in msg:
            st.session_state.case["onset"] = "gradually"
        elif "sud" in msg:
            st.session_state.case["onset"] = "suddenly"
        else:
            st.session_state.case["onset"] = "not sure"

        blur_type = st.session_state.case["blur_type"]
        onset = st.session_state.case["onset"]

        # ✅ Sudden onset = urgent pivot
        if onset == "suddenly":
            add_message(
                "assistant",
                "\n- ⚠️ **Sudden vision change can be serious**\n"
                "- Because this started suddenly, prompt in-person evaluation is recommended.\n"
                "- **Recommended action:** seek urgent eye care."
            )
        else:
            if blur_type == "distance":
                explanation = "This pattern is often associated with needing an updated distance prescription."
            else:
                explanation = "This pattern is often related to focusing changes or visual strain."

            add_message(
                "assistant",
                "\n**Educational guidance**\n"
                f"- {explanation}\n\n"
                "**Next step**\n"
                "- Consider scheduling a **routine eye exam/refraction**.\n"
                "- Seek urgent care if pain, sudden worsening, or flashes/floaters develop."
            )

        # reset flow
        st.session_state.stage = "idle"
        st.session_state.case = {"blur_type": None, "eye": None, "onset": None}
        st.rerun()