import streamlit as st

hidemenu =  """
<style>

    @import url('https://fonts.googleapis.com/css2?family=Rubik+Gemstones&display=swap');
    html, body, [class*=“css”]{
        font-family: 'Rubik Gemstones', cursive !important;
    }
    #MainMenu{
        visibility:hidden;
    }
    footer{
        visibility:visible;
    }
    footer:after{
        content:'Copyright © 2022 Universitas Bengkulu';
        display:block;
        position:relative;
        color:tomato;
    }
</style>
"""


st.markdown("# Bacteria Colony Counter")
st.write(
    """Web app to counting bacteria colony automatically – easy to use and fast."""
)
link = '[Start Counting Colony](https://harizaldycahya-colony-counter-home-ng37y9.streamlit.app/Counting)'
st.markdown(link, unsafe_allow_html=True)