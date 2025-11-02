import traceback
import streamlit as st

st.set_page_config(page_title="End-to-End Chatbot", page_icon="🤖")
st.title("End-to-End Chatbot")
st.write("Type a message and press Send:")

# ---------- Load bot safely (so the page never goes blank) ----------
@st.cache_resource(show_spinner=False)
def load_bot():
    try:
        from bot import get_response  # bot.py loads vectorizer/classifier from models/
        return get_response, None
    except Exception as e:
        return None, f"{e}\n\n{traceback.format_exc()}"

get_response, load_err = load_bot()

# ---------- Diagnostics panel if loading failed ----------
with st.expander("Diagnostics", expanded=bool(load_err)):
    if load_err:
        st.error("Model failed to load. See details below:")
        st.code(load_err, language="text")
        st.markdown(
            """
**Quick fixes:**
1) Ensure `models/vectorizer.pkl` and `models/classifier.pkl` exist (run `python ml.py` if missing).
2) Confirm `bot.py`, `intents.py`, and `app.py` are in the same folder.
3) Restart: `streamlit run app.py`
"""
        )
    else:
        st.success("Model loaded successfully.")

# ---------- Sidebar: confidence slider ----------
threshold = st.sidebar.slider(
    "Confidence threshold",
    min_value=0.0, max_value=1.0, value=0.5, step=0.05,
    help="Higher = bot answers only when more confident; otherwise says 'I'm not sure I understand.'"
)

# ---------- Session state ----------
if "chat" not in st.session_state:
    st.session_state.chat = []            # list of (speaker, text)
if "ended" not in st.session_state:
    st.session_state.ended = False        # disable input after goodbye

# ---------- Input form (prevents duplicates on rerun) ----------
disabled = st.session_state.ended
with st.form("chat_form", clear_on_submit=True):
    user = st.text_input("You", value="", placeholder="Type a message", disabled=disabled)
    submitted = st.form_submit_button("Send", disabled=disabled)

# ---------- Handle a submitted message ----------
if submitted and user:
    st.session_state.chat.append(("You", user))
    lower = user.strip().lower()

    if get_response is None:
        bot_reply = "The model isn't loaded yet. Open the Diagnostics panel for details."
    else:
        try:
            bot_reply = get_response(user, threshold=threshold)
        except Exception as e:
            bot_reply = f"(Error calling bot) {e}"

    st.session_state.chat.append(("Bot", bot_reply))

    # End session on common exit phrases
    if lower in {"bye", "goodbye", "exit", "quit"}:
        st.session_state.ended = True

# ---------- Render transcript ----------
for speaker, msg in st.session_state.chat:
    st.write(f"**{speaker}:** {msg}")

# ---------- Footer hint ----------
if st.session_state.ended:
    st.info("Session ended. Refresh the page to start a new chat.")
