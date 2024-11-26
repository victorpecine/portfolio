import  requests
import  streamlit as st
from    streamlit_option_menu import option_menu
from    streamlit_lottie      import st_lottie
from    datetime              import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

my_birthdate = datetime(1991, 12, 31)  # Year, Month, Day
my_age = calculate_age(my_birthdate)

def load_lottie_url(url):
    request = requests.get(url, timeout=20)
    if request.status_code != 200:
        return None
    return request.json()

# Page config
st.set_page_config(page_title='Victor Pecine -  Data Scientist',
                   page_icon=':👨‍💻:',
                   layout='wide'
                   )

st.header('Welcome to my portfolio')
st.subheader("""My goal is to help companies become data-driven and use data to make \
                strategic decisions, increase profits and optimize processes.""")
st.write('---')

with st.container():
    selected_menu = option_menu(menu_title=None,
                                options=['About', 'Projects', 'Contact'],
                                icons=['person', 'code-slash', 'chat-right-text-fill'],
                                orientation='horizontal'
                                )

# About menu
if selected_menu == 'About':
    st.header('+2 years as Data Scientist')

    with st.container():
        col1, col2 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col1:
            st.write(f"""
                     I'm {my_age}
                     Using data science, I have identified compressed air leaks of around 70%, \
                         significantly contributing to cost reduction. Additionally, I have analyzed \
                             data from oil quality, humidity, and vibration sensors in machines and engines.

                     I was also part of a team that developed a machine learning model to identify \
                         the chemical composition of scrap metal for steel production. This resulted \
                             in the client reducing their consumption of more expensive scrap, thereby \
                                 cutting costs both in material purchase and steel production.

                     My daily work and study routine involve using Python and libraries such as Pandas, \
                         Numpy, Scikit-learn, SciPy, Matplotlib, and Plotly.

                     I have developed models using supervised bagging techniques with Random Forest and \
                         gradient boosting with XGBoost, CatBoost, LightGBM, and AdaBoost for both classification\
                             and regression problems.

                     Furthermore, my modeling process includes the use of hyperparameters, analysis of \
                         overfitting and underfitting, cross-validation, and metrics evaluation.
                     """)
        with col2:
            url_img_computer_about = 'https://lottie.host/29bc0eee-b34a-43ac-b6b1-1b862e565d30/To7aVTzMzF.json'
            img_computer_about = load_lottie_url(url_img_computer_about)
            st_lottie(img_computer_about,
                      speed=5,
                      height=0,
                      width=0,
                      loop=True,
                      quality='high')

    with st.container():
        st.write('---')
        st.subheader('Education')
        st.write('- MBA in Data Science and Analytics - USP (2024)')
        st.write('- Postgraduate in Renewable Energies and Energy Efficiency - UFPR (2020)')
        st.write('- Bachelor of Electrical Engineering - UTFPR (2017)')

    with st.container():
        st.write('---')
        col3, col4 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col3:
            st.subheader('Hard skills')
            st.write('- Python')
            st.write('- Machine learning')
            st.write('- Statistical analysis')
            st.write('- Data visualization')
            st.write('- Code versioning')
            st.write('- SQL')
        with col4:
            st.subheader('Soft skills')
            st.write('- Analytical capability')
            st.write('- Planning')
            st.write('- Organization')
            st.write('- Adaptability')
            st.write('- Assertiveness')
            st.write('- Communication')

# Projects menu
if selected_menu == 'Projects':
    st.header('Many ways to use machine learning')
    with st.container():
        col1, col2 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col1:
            st.write('---')
            url_img_maintenance_cost = 'https://lottie.host/8d95105a-b152-4cf2-b1e1-48aa15716c49/8bsx2bSodG.json'
            img_maintenance_cost = load_lottie_url(url_img_maintenance_cost)
            st_lottie(img_maintenance_cost,
                      speed=5,
                      height=200,
                      width=400,
                      loop=True,
                      quality='high'
                      )
        with col2:
            st.write('---')
            st.subheader('36% savings on truck maintenance')
            st.write('- Model with Random Forest classifier')
            st.write('- Use of hyper parameters to improve results')
            st.write('- [Github repo](https://github.com/victorpecine/aps_failure_truck_prediction)')

# footer = """<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: white;
# color: black;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Developed by Victor Pecine <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Heflin Stephen Raj S</a></p>
# </div>
# """
# st.markdown(footer,unsafe_allow_html=True)