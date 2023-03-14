from io import StringIO
from pathlib import Path
import streamlit as st
import time
# import detect
from detect import main
import os
import sys
import argparse
from PIL import Image
import cv2


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


def get_subdirs(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    return result


def get_detection_folder():
    '''
        Returns the latest folder in a runs\detect
    '''
    return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)


if __name__ == '__main__':

    st.markdown(hidemenu,unsafe_allow_html=True)
    st.title('Automatic Bacteria Colony Forming Units Counter')
    st.write('Note : **:blue[The image resolution should be above 800px to get the best results]**')

    uploaded_file = st.sidebar.file_uploader(
        "Image", type=['png', 'jpeg', 'jpg'])
    if uploaded_file is not None:
        is_valid = True
        with st.spinner(text='Loading...'):
            st.sidebar.image(uploaded_file)
            picture = Image.open(uploaded_file)
    else:
        is_valid = False


    if is_valid:
        print('valid')
        if st.button('Counting'):
            
            # Edited
            gray = cv2.cvrColor(picture, cv2.COLOR_GGR2GRAY)
            img = cv2.medianBlur(gray, 5)

            cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1,120, param1=100, param2=30, minRadius=0, maxRadius=0)
            circles = np.uint16(np.around(circles))

            for i in circles[0, :]:
            # Outer Circle
            cv2.circle(picture, (i[0], i[1]), i[2], (0,255,0), 2)

            # center circle
            cv2.circle(picture, (i[0], i[1]), 2, (0,255,0), 3)
            # End Edited

            # detect(opt)
            #main(opt)
            Image.open(picture)
