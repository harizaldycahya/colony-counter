import streamlit as st
from PIL import Image

hidemenu =  """
<style>
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

st.markdown("# Manual")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

image = Image.open('images/manual (1).png')
st.image(image, caption='manual (1)')