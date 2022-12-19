import streamlit as st

st.markdown("# Bacteria Colony Counter")
st.write(
    """Web app to counting bacteria colony automatically – easy to use and fast."""
)
link = '[Start Counting Colony](http://harizaldycahya-colony-counter-home-ng37y9.streamlit.app/Counting)'
st.button(link, unsafe_allow_html=True)