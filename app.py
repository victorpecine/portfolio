import  requests
import  streamlit as st
from    streamlit_option_menu import option_menu
from    streamlit_lottie      import st_lottie
from    datetime              import datetime


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
                        options=['About', 'Projects', 'Contact', 'Letter of recommendation'],
                        icons=['person', 'file-code', 'envelope', 'card-text'],
                        orientation='horizontal'
                        )

# About
if selected == 'About':
    my_birthdate = datetime(1991, 12, 31)
    my_age = calculate_age(my_birthdate)
    st.markdown('# Welcome to my portfolio')
    st.markdown(f"""### My name is Victor, I'm {my_age} and my goal as Data Scientist is to help companies \
                            become data-driven and use data to make strategic decisions, increase \
                                profits and optimize processes.""")
    st.markdown('######')
    # Download resume button
    resume_url = 'https://drive.google.com/uc?export=download&id=1DlOpk-SpFRC5hWI9mF-qao636usLncMT'
    response = requests.get(resume_url, timeout=20)
    resume_content = response.content
    st.download_button(label='Download resume',
                       data=resume_content,
                       file_name='Victor_Pecine_Payan_resume.pdf',
                       type='primary'
                       )
    # Download letter of recommendation button
    resume_url = 'https://drive.google.com/uc?export=download&id=1Dmw2Z9SuCvFnnyyDwIIHa18Yvr51-86m'
    response = requests.get(resume_url, timeout=20)
    resume_content = response.content
    st.download_button(label='Download letter of recommendation',
                       data=resume_content,
                       file_name='Victor_Pecine_Payan_letter_recommendation.pdf',
                       type='primary'
                       )
    st.write('---')
    # About
    with st.container():
        col1, col2 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col1:
            st.markdown("""
                        Using data science, I identified compressed air leaks of around 70%, \
                            significantly contributing to cost reduction. Additionally, I have analyzed \
                                data from oil quality, humidity, and vibration sensors in machines and engines.

                        I was also part of a team that developed a machine learning model to identify \
                            the chemical composition of scrap metal for steel production. This resulted \
                                in the client reducing their consumption of more expensive scrap, thereby \
                                    cutting costs both in material purchase and steel production.

                        My daily work and study routine involve using :green[***Python***] and libraries such as \
                            :green[***Pandas, Numpy, Scikit-learn, SciPy, Matplotlib, and Plotly***].

                        I have developed models using supervised bagging techniques with Random Forest and \
                            gradient boosting with :green[***Decision Trees, Random Forest, XGBoost, CatBoost, \
                                LightGBM, and AdaBoost***] for both classification and regression problems.

                        Furthermore, the modeling process includes the use of hyperparameters, analysis of \
                            overfitting and underfitting, cross-validation, and metrics evaluation.
                        """)
        with col2:
            url_img_computer_about = 'https://lottie.host/29bc0eee-b34a-43ac-b6b1-1b862e565d30/To7aVTzMzF.json'
            img_computer_about = load_lottie_url(url_img_computer_about)
            st_lottie(img_computer_about,
                    speed=5,
                    height=500,
                    width=500,
                    loop=True,
                    quality='high'
                    )
    st.write('---')

    # Education
    with st.container():
        st.markdown('## Education')
        st.markdown('- MBA in Data Science and Analytics - USP (2024)')
        st.markdown('- Postgraduate in Renewable Energies and Energy Efficiency - UFPR (2020)')
        st.markdown('- Bachelor of Electrical Engineering - UTFPR (2017)')
    st.markdown('---')

    # Past experiences
    with st.container():
        st.markdown('## Past experiences')
        st.markdown('### +2 years as Data Scientist')

        st.markdown('#### Data Scientist at Ubiratã')
        st.markdown('- From Jan. 2024 to Aug. 2024')
        st.markdown('- I took part in a project where we developed a supervised machine learning \
                        model with non-negative least squares regression to estimate the percentage \
                            amount of chemical elements in the scrap used to produce steel. Using the \
                                model generated monthly savings of thousands of dollars.')
        st.markdown('- The routine involved statistical analysis, drawing up graphs to present to \
                        costumers, searching and manipulating data in :green[***PostgreSQL***], meetings in English \
                            with costumers, using :green[***Scipy, Scikit-learn, Numpy, Pandas, Matplotlib and \
                                Plotly***] libraries.')
        st.markdown('######')
        st.markdown('#### Data Scientist at PredData')
        st.markdown('- From Oct. 2022 to Jan. 2024')
        st.markdown("- I was responsible for starting the company's data science department. \
                        I developed unsupervised machine learning algorithms for :green[***clustering and \
                            supervised algorithms for classification***] to identify compressed air leaks. \
                                With this, we identified leaks of more than 60% for a multinational \
                                vehicle manufacturer.")
        st.markdown('- I also created dashboards for costumers to view compressed air \
                            consumption and analyze estimated losses in real time.')
    st.markdown('---')

    # Skills
    with st.container():
        col3, col4 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='top'
                                )
        with col3:
            st.markdown('## Hard skills')
            st.markdown('- Python')
            st.markdown('- Machine learning')
            st.markdown('- Statistical analysis')
            st.markdown('- Data visualization')
            st.markdown('- Code versioning')
            st.markdown('- SQL')
        with col4:
            st.markdown('## Soft skills')
            st.markdown('- Analytical capability')
            st.markdown('- Planning')
            st.markdown('- Organization')
            st.markdown('- Adaptability')
            st.markdown('- Assertiveness')
            st.markdown('- Communication')
    st.markdown('---')

# Projects
if selected == 'Projects':
    st.markdown('# +2 years as Data Scientist')
    st.markdown('### developing machine learning models for clustering, classification and \
                        regression to contribute to the modernization of Brazilian industries \
                            and help teams and leaders make decisions')
    st.markdown('---')
    # APS failure truck
    with st.container():
        col1, col2 = st.columns(spec=2,
                                gap='small',
                                vertical_alignment='center'
                                )
    with col1:
        st.markdown("""
                    ### What
                    
                    The project aims to reduce maintenance costs for truck air pressure systems.
                    
                    Costs incurred include \$10 for inspections without defects, \$25 for preventive repairs, \
                    and \$500 for corrective maintenance.
                    
                    ### Why
                    
                    Despite maintaining a consistent fleet size, the company has observed increasing \
                    expenses on air system maintenance over the past three years. The project's primary goal \
                    is to estimate and reduce next year's maintenance costs.
                    
                    ### How
                    
                    The technical team provided historical data with classifications:
                    
                    - "pos" for trucks with air system defects
                    
                    - "neg" for defects in other systems
                    
                    Supervised machine learning techniques (Random Forest, XGBoost, Multi-layer \
                    Perceptron, AdaBoost) were applied.
                    
                    The final model used was the :green[***Random Forest Classifier***] with hyper parameters, \
                    :green[***saving $13,555, which represents a 36% reduction in costs***].
                    """
                    )
        with col2:
            st.image('https://i.ibb.co/WnH12w9/historical-cost.png')
            st.image('https://i.ibb.co/PZXKbxt/pct-cost-variation.png')
    st.markdown('---')

# Contact
if selected == 'Contact':
    st.markdown("# Just click and let's chat!")
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

# Letter of recommendation
if selected == 'Letter of recommendation':
    # Download letter of recommendation button
    resume_url = 'https://drive.google.com/uc?export=download&id=1Dmw2Z9SuCvFnnyyDwIIHa18Yvr51-86m'
    response = requests.get(resume_url, timeout=20)
    resume_content = response.content
    st.download_button(label='Download letter of recommendation',
                       data=resume_content,
                       file_name='Victor_Pecine_Payan_letter_recommendation.pdf',
                       type='primary'
                       )
    letter_url = 'https://drive.google.com/file/d/1Dmw2Z9SuCvFnnyyDwIIHa18Yvr51-86m/preview'
    st.components.v1.html(f'<iframe src="{letter_url}" width="700" height="900"></iframe>',
                          height=900)
