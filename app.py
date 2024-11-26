import  requests
import  streamlit as st
from    streamlit_option_menu    import option_menu
from    streamlit_lottie         import st_lottie
from    datetime                 import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def load_lottie_url(url):
    request = requests.get(url, timeout=20)
    if request.status_code != 200:
        return None
    return request.json()

# Page config
st.set_page_config(page_title='Victor Pecine -  Data Scientist',
                   page_icon=':👨‍💻:',
                   layout='wide',
                   initial_sidebar_state="collapsed"
                   )

selected = option_menu(menu_title=None,
                        options=['About', 'Projects', 'Contact'],
                        icons=['person', 'file-code', 'envelope'],
                        orientation='horizontal'
                        )

# About infos
if selected == 'About':
    my_birthdate = datetime(1991, 12, 31)
    my_age = calculate_age(my_birthdate)
    st.markdown('# Welcome to my portfolio')
    st.markdown(f"""### My name is Victor, I'm {my_age} and my goal as Data Scientist is to help companies \
                            become data-driven and use data to make strategic decisions, increase \
                                profits and optimize processes.""")
    st.write('---')
    # About
    with st.container():
        col1, col2 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
    with col1:
        st.markdown("""
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

                    Furthermore, the modeling process includes the use of hyperparameters, analysis of \
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
                  quality='high'
                  )
    # Education
    with st.container():
        st.markdown('---')
        st.subheader('Education')
        st.markdown('- MBA in Data Science and Analytics - USP (2024)')
        st.markdown('- Postgraduate in Renewable Energies and Energy Efficiency - UFPR (2020)')
        st.markdown('- Bachelor of Electrical Engineering - UTFPR (2017)')

    # Skills
    with st.container():
        st.markdown('---')
        col3, col4 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col3:
            st.subheader('Hard skills')
            st.markdown('- Python')
            st.markdown('- Machine learning')
            st.markdown('- Statistical analysis')
            st.markdown('- Data visualization')
            st.markdown('- Code versioning')
            st.markdown('- SQL')
        with col4:
            st.subheader('Soft skills')
            st.markdown('- Analytical capability')
            st.markdown('- Planning')
            st.markdown('- Organization')
            st.markdown('- Adaptability')
            st.markdown('- Assertiveness')
            st.markdown('- Communication')

# Projects infos
if selected == 'Projects':
    st.markdown('# +2 years as Data Scientist')
    st.markdown('### Here you can find many ways to use machine learning')
    st.markdown('---')
    # APS failure truck
    st.markdown('## 1)   36% savings on truck maintenance')
    st.markdown('### [Github repo](https://github.com/victorpecine/aps_failure_truck_prediction)')
    st.markdown("""
                ### What
                
                The project aims to reduce maintenance costs for truck air pressure systems.
                
                Costs incurred include \$10 for inspections without defects, \$25 for preventive repairs, \
                and \$500 for corrective maintenance when defects are not preemptively addressed.
                
                ### Why
                
                Despite maintaining a consistent fleet size, the company has observed increasing \
                expenses on air system maintenance over the past three years. The project's primary goal \
                is to estimate and reduce next year's maintenance costs.
                
                ### How
                
                The technical team provided historical data with classifications:
                
                - "pos" for trucks with air system defects
                
                - "neg" for defects in other systems.
                
                Supervised machine learning techniques (Random Forest, XGBoost, Multi-layer \
                Perceptron, AdaBoost) were applied.
                
                The final model used was the **Random Forest Classifier** with hyper parameters, \
                with a maintenance cost of $13,555, which represents a 36% reduction in costs
                """
                )
    st.markdown('---')

# Contact infos
if selected == 'Contact':
    st.markdown("# Let's chat!")
    # To use bootstrap icons
    st.markdown("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.9.1/font/bootstrap-icons.min.css"> """,
            unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns(spec=[0.33, 0.33, 0.33],
                                      gap='small',
                                      vertical_alignment='center',
                                      )
        with col1:
            st.markdown('# [<i class="bi bi-envelope"></i>](mailto:victorpecine@gmail.com)',
                        unsafe_allow_html=True
                        )
        with col2:
            st.markdown('# [<i class="bi bi-linkedin"></i>](https://www.linkedin.com/in/victorpecine/)',
                        unsafe_allow_html=True
                        )
        with col3:
            st.markdown('# [<i class="bi bi-github"></i>](https://github.com/victorpecine?tab=repositories)',
                        unsafe_allow_html=True
                        )
