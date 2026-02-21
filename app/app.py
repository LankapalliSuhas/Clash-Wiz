import streamlit as st

st.set_page_config(page_title="ClashWiz", layout="wide")

st.title("ClashWiz")
st.subheader("Smarter Decks. Better Crowns.")

st.divider()

st.header("Deck vs Deck Prediction")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Deck A")
    deckA = []
    for i in range(8):
        card = st.text_input(f"Deck A - Card {i+1}", key=f"a{i}")
        deckA.append(card)

with col2:
    st.subheader("Deck B")
    deckB = []
    for i in range(8):
        card = st.text_input(f"Deck B - Card {i+1}", key=f"b{i}")
        deckB.append(card)

if st.button("Predict Winner"):
    st.success("Prediction will appear here")
