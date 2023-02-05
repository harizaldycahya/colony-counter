import streamlit as st

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


st.markdown("# Automatic **:blue[Bacteria]** Colony Forming Units Counter")
st.write(
    """Web app to counting bacteria colony forming units automatically – easy to use and fast."""
)
link = '[Start Counting Colony](https://harizaldycahya-colony-counter-home-ng37y9.streamlit.app/Counting)'
st.markdown(link, unsafe_allow_html=True)
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.subheader('Why Colony Counting ?')
st.write(
    """colony counting is important to estimate the number of cells present based on their given ability to continue to grow and expand under certain conditions like temperature and the state of the nutrient medium."""
)
st.markdown('##')
st.markdown('##')
st.subheader('Why Automatic Colony Forming Units Counter ?')
st.write(
    """Manual counting is a thank-less and highly labour-intensive process. As those who do it know it is not uncommon for a total count of a hundred plates to span a full 8-hour working day. Some assays may even require the analysis of thousands of plates which effectively subjects a capable researcher to a menial task for a 1, 2 or even 3-week period. For a researcher to have the necessary skills to count colonies they must be adequately trained which is another expensive and time-consuming process. On top of the time, money and effort invested into manual counts the results may possibly be non-repeatable and are often fraught with errors. Compared to manual counting, automated colony counters provide substantial performance enhancements including faster processing and throughput and improved accuracy – all of which improve research outputs without wasting valuable time or compromising data quality."""
)
st.markdown(
    """
        <style>
            @font-face {
            font-family: 'Poppins';
            src: url(https://fonts.googleapis.com/css2?family=Poppins&display=swap);
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
            }

            html, body, [class*="css"]  {
                font-family: 'Poppins';
            }
        </style>

    """,
        unsafe_allow_html=True,
)
