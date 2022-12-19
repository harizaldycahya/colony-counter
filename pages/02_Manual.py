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

manual_1 = Image.open('images/manual (1).png')
manual_2 = Image.open('images/manual (2).png')
manual_3 = Image.open('images/manual (3).png')
manual_4 = Image.open('images/manual (4).png')
st.image(manual_1, caption='manual (1)')
st.subheader('1. Browse Files')
st.caption('First step is choosing image that you wanna counting, to do this you need click browse files button, you can find this button in sidebar menu')
st.image(manual_2, caption='manual (2)')
st.subheader('1. Browse Files')
st.caption('First step is choosing image that you wanna counting, to do this you need click browse files button, you can find this button in sidebar menu')
st.image(manual_3, caption='manual (3)')
st.subheader('1. Browse Files')
st.caption('First step is choosing image that you wanna counting, to do this you need click browse files button, you can find this button in sidebar menu')
st.image(manual_4, caption='manual (4)')
st.subheader('1. Browse Files')
st.caption('First step is choosing image that you wanna counting, to do this you need click browse files button, you can find this button in sidebar menu')