import  streamlit as st
import  requests
from    streamlit_option_menu import option_menu
from    streamlit_lottie import st_lottie


def load_lottie_url(url):
    request = requests.get(url, timeout=20)
    if request.status_code != 200:
        return None
    return request.json()


st.set_page_config(page_title='Victor Pecine -  Data Scientist',
                   page_icon=':male-technologist:',
                   layout='wide'
                   )

st.subheader('Welcome to my portfolio')

with st.container():
    selected_menu = option_menu(menu_title=None,
                                options=['About', 'Projects', 'Contact'],
                                icons=['person', 'code-slash', 'chat-right-text-fill'],
                                orientation='horizontal'
                                )

if selected_menu == 'About':
    with st.container():
        col1, col2 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col1:
            st.subheader('Electrical engineer with +2 years as data scientist')
        with col2:
            url_img_computer_about = 'https://lottie.host/1fee4682-957a-4ff1-a118-326f22dfeb57/qXCdj2gUYC.json'
            img_computer_about = load_lottie_url(url_img_computer_about)
            st_lottie(img_computer_about)
