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
st.subheader('2. Select file')
st.caption('Second step is select the file, file that you can upload must be beloow 200MB with file format PNG, JPEG OR, JPG')
st.image(manual_3, caption='manual (3)')
st.subheader('3. Upload file')
st.caption('Third step is make sure that your file is uploaded correctly, your uploaded file is showing in sidebar, if your image is already showing, that mean you can go to the next steps')
st.image(manual_4, caption='manual (4)')
st.subheader('4. Counting')
st.caption('Four step is click the counting button and wait, system gonna run the code and counting your colony')
st.image(manual_5, caption='manual (5)')
st.subheader('5. Result')
st.caption('Five step is checking the results, after counting you gonna see the result showing how much colony in is detected')
