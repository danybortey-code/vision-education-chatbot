import streamlit as st
from datetime import datetime
from llm_utils import analyze_vision_symptoms

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Vision Chatbot",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(71, 163, 255, 0.16), transparent 28%),
            radial-gradient(circle at top right, rgba(116, 123, 255, 0.14), transparent 25%),
            linear-gradient(180deg, #f4f8fc 0%, #eef4f9 100%);
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .topbar {
        background: rgba(255,255,255,0.82);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(214, 226, 239, 0.95);
        border-radius: 24px;
        padding: 1.2rem 1.4rem;
        box-shadow: 0 18px 40px rgba(28, 60, 92, 0.08);
        margin-bottom: 1rem;
    }

    .brand-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .brand-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .brand-icon {
        width: 62px;
        height: 62px;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        background: linear-gradient(135deg, #1f6feb 0%, #5f8dff 100%);
        color: white;
        box-shadow: 0 10px 22px rgba(31,111,235,0.22);
    }

    .brand-title {
        font-size: 2.05rem;
        font-weight: 800;
        color: #16324d;
        line-height: 1.1;
        margin: 0;
    }

    .brand-subtitle {
        color: #587188;
        font-size: 1rem;
        margin-top: 0.25rem;
    }

    .top-badge {
        display: inline-block;
        padding: 0.55rem 0.9rem;
        border-radius: 999px;
        background: #edf5ff;
        color: #215580;
        border: 1px solid #d4e4f6;
        font-size: 0.86rem;
        font-weight: 700;
    }

    .panel {
        background: rgba(255,255,255,0.88);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(217, 228, 240, 0.95);
        border-radius: 24px;
        padding: 1rem;
        box-shadow: 0 16px 34px rgba(25, 59, 92, 0.08);
    }

    .panel-title {
        font-size: 0.92rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 800;
        color: #2d648f;
        margin-bottom: 0.7rem;
    }

    .metric-card {
        background: linear-gradient(180deg, #ffffff 0%, #f8fbfe 100%);
        border: 1px solid #dce8f3;
        border-radius: 18px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.8rem;
    }

    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        font-weight: 700;
        color: #6c8195;
        letter-spacing: 0.05em;
        margin-bottom: 0.25rem;
    }

    .metric-value {
        font-size: 1rem;
        font-weight: 700;
        color: #17324d;
    }

    .mini-note {
        color: #5f7487;
        font-size: 0.94rem;
        line-height: 1.55;
    }

    .safety-banner {
        border-radius: 18px;
        padding: 0.95rem 1rem;
        background: linear-gradient(180deg, #fff8e9 0%, #fffdf7 100%);
        border: 1px solid #f1dfaa;
        color: #735814;
        font-size: 0.94rem;
        line-height: 1.5;
        margin-top: 0.7rem;
    }

    .chat-header {
        background: linear-gradient(135deg, #173b65 0%, #204d7d 45%, #3668a4 100%);
        color: white;
        border-radius: 22px;
        padding: 1rem 1.1rem;
        margin-bottom: 1rem;
        box-shadow: 0 14px 28px rgba(26, 56, 92, 0.18);
    }

    .chat-header-title {
        font-size: 1.2rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }

    .chat-header-sub {
        font-size: 0.94rem;
        color: rgba(255,255,255,0.88);
    }

    .quick-chip-label {
        font-size: 0.92rem;
        font-weight: 700;
        color: #2f628e;
        margin-bottom: 0.55rem;
    }

    .result-box {
        border-radius: 22px;
        padding: 1rem 1.05rem;
        margin: 0.8rem 0 0.4rem 0;
        border: 1px solid #d8e7f3;
        box-shadow: 0 12px 26px rgba(17, 44, 73, 0.06);
        background: white;
    }

    .result-title {
        font-size: 1.1rem;
        font-weight: 800;
        color: #183450;
        margin-bottom: 0.55rem;
    }

    .tag {
        display: inline-block;
        padding: 0.35rem 0.72rem;
        border-radius: 999px;
        font-size: 0.79rem;
        font-weight: 800;
        margin-right: 0.4rem;
        margin-bottom: 0.45rem;
        border: 1px solid transparent;
    }

    .tag-red {
        background: #fff0f0;
        color: #a52a2a;
        border-color: #f1c6c6;
    }

    .tag-yellow {
        background: #fff8e8;
        color: #8b6508;
        border-color: #eed9a0;
    }

    .tag-green {
        background: #effcf4;
        color: #1d7540;
        border-color: #cdecd8;
    }

    .urgent {
        background: linear-gradient(180deg, #fff5f5 0%, #fffafa 100%);
        border-left: 8px solid #d64545;
    }

    .routine {
        background: linear-gradient(180deg, #fffdf4 0%, #fffefb 100%);
        border-left: 8px solid #d9a91d;
    }

    .low {
        background: linear-gradient(180deg, #f4fff8 0%, #fbfffd 100%);
        border-left: 8px solid #2b965e;
    }

    .summary-card {
        background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
        border: 1px solid #dce8f5;
        border-radius: 18px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.8rem;
    }

    .summary-title {
        font-size: 0.9rem;
        font-weight: 800;
        color: #2c648f;
        margin-bottom: 0.45rem;
    }

    .summary-line {
        color: #29475e;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }

    .footer-note {
        text-align: center;
        color: #778da1;
        font-size: 0.87rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "consent_given" not in st.session_state:
    st.session_state.consent_given = False

if "conversation_closed" not in st.session_state:
    st.session_state.conversation_closed = False

def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

def reset_chat():
    st.session_state.messages = []
    st.session_state.conversation_closed = False

def result_card(title, urgency, guidance, action, style="low"):
    tag_class = {
        "Urgent": "tag-red",
        "Prompt": "tag-yellow",
        "Routine": "tag-green"
    }.get(urgency, "tag-green")

    return f"""
    <div class="result-box {style}">
        <div class="result-title">{title}</div>
        <div><span class="tag {tag_class}">{urgency}</span></div>
        <div style="margin-top:0.35rem; color:#29475e; line-height:1.6;">
            <b>Educational guidance:</b> {guidance}
        </div>
        <div style="margin-top:0.45rem; color:#29475e; line-height:1.6;">
            <b>Recommended action:</b> {action}
        </div>
    </div>
    """

def render_llm_summary(analysis):
    blur_type = analysis.get("blur_type", "unknown")
    eye = analysis.get("eye", "unknown")
    onset = analysis.get("onset", "unknown")
    red_flags = analysis.get("red_flags", [])
    urgency = analysis.get("urgency", "unknown")

    return f"""
    <div class="summary-card">
        <div class="summary-title">LLM symptom extraction</div>
        <div class="summary-line"><b>Blur type:</b> {blur_type}</div>
        <div class="summary-line"><b>Eye involvement:</b> {eye}</div>
        <div class="summary-line"><b>Onset:</b> {onset}</div>
        <div class="summary-line"><b>Red flags:</b> {red_flags}</div>
        <div class="summary-line"><b>Urgency:</b> {urgency}</div>
    </div>
    """

# =========================================================
# TOP HEADER
# =========================================================
st.markdown("""
<div class="topbar">
    <div class="brand-row">
        <div class="brand-left">
            <div class="brand-icon">👁️</div>
            <div>
                <div class="brand-title">Vision Chatbot</div>
                <div class="brand-subtitle">
                    LLM-powered symptom intake with safety guardrails
                </div>
            </div>
        </div>
        <div class="top-badge">LLM symptom extraction · Educational use only</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LAYOUT
# =========================================================
left_col, right_col = st.columns([1, 2.2], gap="large")

# =========================================================
# LEFT PANEL
# =========================================================
with left_col:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown('<div class="panel-title">System Type</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Architecture</div>
        <div class="metric-value">LLM + Safety Rules</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">LLM Module</div>
        <div class="metric-value">llm_utils.py</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="panel-title">What the LLM extracts</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="mini-note">
        • Near vs distance blur<br>
        • One eye vs both eyes<br>
        • Sudden vs gradual onset<br>
        • Pain, flashes, and floaters<br>
        • Urgency level
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="safety-banner">
        <b>Safety guardrails:</b> pain, flashes, floaters, or sudden onset still trigger urgent-care guidance.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("###")
    if st.button("🔄 Start New Chat", use_container_width=True):
        reset_chat()
        st.rerun()

    st.markdown(f"""
    <div class="footer-note">
        Daniel Bortey · {datetime.now().strftime("%b %d, %Y")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# RIGHT PANEL
# =========================================================
with right_col:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("""
    <div class="chat-header">
        <div class="chat-header-title">Describe your vision concern naturally</div>
        <div class="chat-header-sub">
            The LLM extracts structured intake information from your message.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.session_state.consent_given = st.checkbox(
        "I understand this tool is for educational guidance only and is not a diagnosis.",
        value=st.session_state.consent_given
    )

    if not st.session_state.consent_given:
        st.info("Check the consent box above to begin.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.stop()

    if len(st.session_state.messages) == 0:
        st.markdown("""
        <div class="summary-card">
            <div class="summary-title">How to use</div>
            <div class="summary-line">Type your symptoms in natural language.</div>
            <div class="summary-line">Example: “My distance vision is blurry and I see flashes.”</div>
        </div>
        """, unsafe_allow_html=True)

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"], unsafe_allow_html=True)

    user_text = None
    if not st.session_state.conversation_closed:
        user_text = st.chat_input("Describe your vision problem...")
    else:
        st.success("Conversation completed. Click 'Start New Chat' to begin again.")

    if user_text:
        add_message("user", user_text)
        msg = user_text.lower().strip()

        greetings = ["hi", "hello", "hey"]
        thanks = ["thank you", "thanks", "thx"]

        if any(g == msg for g in greetings):
            response = (
                "Hi — describe your vision concern in a sentence. "
                "For example: **My near vision is blurry**."
            )
            add_message("assistant", response)
            st.rerun()

        if any(t in msg for t in thanks):
            response = "You’re welcome. This conversation is now complete."
            add_message("assistant", response)
            st.session_state.conversation_closed = True
            st.rerun()

        with st.chat_message("assistant"):
            with st.spinner("Using LLM to analyze symptoms..."):
                try:
                    analysis = analyze_vision_symptoms(user_text)

                    summary_html = render_llm_summary(analysis)
                    st.markdown(summary_html, unsafe_allow_html=True)
                    add_message("assistant", summary_html)

                    blur_type = analysis.get("blur_type", "unknown")
                    onset = analysis.get("onset", "unknown")
                    red_flags = analysis.get("red_flags", [])
                    urgency = analysis.get("urgency", "routine")
                    explanation = analysis.get("explanation", "This symptom should be reviewed by an eye care professional.")

                    has_red_flag = (
                        urgency == "urgent"
                        or onset == "suddenly"
                        or len(red_flags) > 0
                    )

                    if has_red_flag:
                        response = result_card(
                            "⚠️ Urgent warning signs detected",
                            "Urgent",
                            explanation,
                            "Seek urgent in-person eye care as soon as possible.",
                            style="urgent"
                        )
                    else:
                        response = result_card(
                            "✅ Educational guidance summary",
                            "Routine",
                            explanation,
                            "Schedule a routine eye exam/refraction. Seek urgent care if pain, flashes, floaters, or sudden worsening develops.",
                            style="low"
                        )

                    st.markdown(response, unsafe_allow_html=True)
                    add_message("assistant", response)

                    st.session_state.conversation_closed = True
                    st.rerun()

                except Exception as e:
                    fallback = (
                        "I could not complete the LLM analysis. "
                        "Please check that your OpenAI API key is valid and billing is enabled.\n\n"
                        f"Error: `{e}`"
                    )
                    st.error(fallback)
                    add_message("assistant", fallback)
                    st.session_state.conversation_closed = True
                    st.rerun()

    st.markdown("""
    <div class="footer-note">
        Built with Streamlit, OpenAI API, and deterministic safety guardrails
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)