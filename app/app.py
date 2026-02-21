import streamlit as st
import numpy as np
import joblib
import json
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ClashWiz",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# THEME (Clash-Inspired Clean Modern)
# --------------------------------------------------

st.markdown("""
<style>
    .stApp {
        background-color: #0F1E3D;
        color: white;
    }

    h1, h2, h3 {
        color: #FFD700;
    }

    .stButton>button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }

    .stMetric {
        background-color: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL + CARD MAPPING
# --------------------------------------------------

MODEL_PATH = "models/model.pkl"
MAPPING_PATH = "models/card_mapping.json"

if not os.path.exists(MODEL_PATH) or not os.path.exists(MAPPING_PATH):
    st.error("Model or card mapping not found. Ensure models/ folder is correct.")
    st.stop()

model = joblib.load(MODEL_PATH)

with open(MAPPING_PATH, "r") as f:
    card_mapping = json.load(f)

all_cards = sorted(list(card_mapping.keys()))
feature_size = len(card_mapping)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("ClashWiz")
st.caption("Meta-Aware Deck Evaluation Engine")
st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    ["Deck Prediction", "Card Explorer", "Counter Engine"]
)

# ==================================================
# TAB 1 — DECK PREDICTION
# ==================================================

with tab1:
    st.subheader("Deck vs Deck Prediction")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Deck A")
        deckA = []
        for i in range(8):
            card = st.selectbox(
                f"Deck A - Card {i+1}",
                all_cards,
                key=f"a{i}"
            )
            deckA.append(card)

    with col2:
        st.markdown("### Deck B")
        deckB = []
        for i in range(8):
            card = st.selectbox(
                f"Deck B - Card {i+1}",
                all_cards,
                key=f"b{i}"
            )
            deckB.append(card)

    st.divider()

    if st.button("Predict Winner"):

        if len(set(deckA)) != 8 or len(set(deckB)) != 8:
            st.error("Each deck must contain 8 unique cards.")
        else:
            vecA = np.zeros(feature_size)
            vecB = np.zeros(feature_size)

            for card in deckA:
                vecA[card_mapping[card]] = 1

            for card in deckB:
                vecB[card_mapping[card]] = 1

            feature = vecA - vecB

            prob = model.predict_proba([feature])[0][1]
            percent = round(prob * 100, 2)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Deck A Win Probability", f"{percent}%")

            with col2:
                st.metric("Deck B Win Probability", f"{round(100-percent,2)}%")

# ==================================================
# TAB 2 — CARD EXPLORER
# ==================================================

with tab2:
    st.subheader("Card Explorer")

    search = st.text_input("Search Card")
    category = st.selectbox("Category", ["All", "Troops", "Spells", "Buildings"])

    # Basic filtering (extend later with real metadata)
    filtered_cards = [
        c for c in all_cards
        if search.lower() in c.lower()
    ]

    cols = st.columns(4)

    for i, card in enumerate(filtered_cards):
        with cols[i % 4]:
            if st.button(card, key=f"card_{card}"):
                st.session_state.selected_card = card

    if "selected_card" in st.session_state:
        st.divider()
        st.markdown(f"### {st.session_state.selected_card}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Win Rate", "Data Needed")

        with col2:
            st.metric("Usage Rate", "Data Needed")

        with col3:
            st.metric("Elixir Cost", "Data Needed")

        st.markdown("### Hard Counters")
        st.write("Counter data will appear here.")

# ==================================================
# TAB 3 — COUNTER ENGINE
# ==================================================

with tab3:
    st.subheader("Counter Engine")

    st.write("Select a deck to find potential hard counter decks.")

    deck_input = []
    for i in range(8):
        card = st.selectbox(
            f"Deck Card {i+1}",
            all_cards,
            key=f"counter_{i}"
        )
        deck_input.append(card)

    if st.button("Find Counters"):

        if len(set(deck_input)) != 8:
            st.error("Deck must contain 8 unique cards.")
        else:
            st.success("Counter recommendation logic to be added by ML.")
