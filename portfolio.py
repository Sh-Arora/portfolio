import streamlit as st
from PIL import Image


def show_about_me():
    st.header(":blue[About Me]")
    st.write("I am a passionate Data Scientist and experienced IT professional with a diverse background rooted in Hyderabad. My love for mathematics led me to pursue engineering, where I discovered a deep interest in Control Systems and Artificial Intelligence. With a rebellious spirit, I pursued my Masters in the USA, becoming the first woman in my family to pursue overseas education and uplifting my family's financial situation. Analytical thinking and Data was at the core of all my professional pursuits. Worked extensively as an IT professional with Multi-Dimensional databases before returning to Hyderabad. I founded an extracurricular activity service industry to restore balance and prioritize holistic development alongside academic pursuits. With a strong track record in organizing impactful events, I am now excited to apply my expertise in Data Science, leveraging my experiences and knowledge to drive innovation and solve complex problems.")
    st.subheader(":blue[What Drives me:]")
    st.write("My journey through education has ignited a deep fascination for artificial intelligence and robotics. Exploring the realms of these cutting-edge technologies during my academic years has sparked a curiosity that continues to drive me forward. In my subsequent work experiences with multi-dimensional databases, I have witnessed firsthand the immense value of harnessing data in multiple ways for making informed and strategic business decisions. Then my entrepreneurial ventures experiences have provided me with valuable insights into the managerial and people skills required to lead and inspire teams. However, the COVID-19 pandemic brought unexpected challenges and a temporary break in my professional pursuits. Yet, amidst the chaos, it reignited the passion for AI that I had nurtured in my younger days, particularly with the current boom in the market. Driven by this renewed enthusiasm, I have worked passionately to relearn and update my knowledge in the field, determined to make a meaningful impact in the world of Artificial Intelligence and DataScience. ")

def show_experience():
    st.header("**:blue[Experience]**")
    "---"
    st.subheader(":green[Data Science Intern:] *Innomatics Research Labs, Nov 2022 - Present*")
    st.write("I am a motivated Data Science Intern with a strong proficiency in Python, data analysis, SQL, Tableau, Advanced Excel, machine learning, and deep learning. Through my studies and hands-on experience, I have gained a solid foundation in these areas and a passion for leveraging data-driven insights to solve complex problems. With a strong command of Python, I can efficiently manipulate and analyze large datasets to extract valuable information. My knowledge of SQL allows me to effectively retrieve, organize, and query data from relational databases. Additionally, my understanding of machine learning and deep learning algorithms equips me to build predictive models and extract meaningful patterns from data. As a Data Science Intern, I am eager to contribute my skills and learn from experienced professionals, driving data-driven decision-making and delivering impactful solutions.")
    "---"
    st.subheader(":green[Operations & Finance Head:] *Self-Employed, Dec 2011 - May 2020*")
    st.write("Gained Experience in following skills: Managerial skills, Negotiation Skills, Crowd Management, Presentation, Funding Management, Procurement, Logistics")
    "---"
    st.subheader(":green[Sr Analyst:] *Oracle India, Apr 2010 - Dec 2010*")
    st.write("Supported and Enhanced American Express systems. With Essbase, Hyperion Planning, OBIEE, Informatica and excellent Communication Skills & Analytical Skills,")
    "---"
    st.subheader(":green[Sr Programming Analyst:] *Limited Brands USA, Feb 2006 - Dec 2009*")
    st.write("Developed, Supported and Enhanced Multi-Dimensional databases. With Essbase, Hyperion Analyzer, Hyperion Interactive Reporting, Microsoft PowerPoint, Teradata, Clarity and excellent Oral & Written Communication Skills")
    "---"
    st.subheader(":green[Sr Hyperion Essbase Consultant:] *RJ Reynolds Tobacco Company, Jan 2005 - Feb 2006*")
    st.write("Mainly dealt in improving performance of multi dimensional databases by Enhancements and Upgrades. With Essbase, Hyperion Analyzer, Hyperion Reports, Hyperion Interactive Reporting, Hyperion Performance Suite, Smartview, Microsoft PowerPoint and excellent Communication Skills")
    "---"
    st.header(":blue[Language Proficiency]")
    st.write("English, Hindi, Telugu")


def show_education():
    st.header(":blue[Education]")
    "---"
    st.subheader(":green[Masters in Electrical Engineering:]")
    st.write("*University of Texas at San Antonio, Jan 2002 - Dec 2003:* (Grade A)")
    st.write("Linear Control, Adaptive Control, Non-Linear Control, Neural Network Control, Intelligent Control and Robotics, Computer Architecture")
    "---"
    st.subheader(":green[Bachelors in Electrical and Electronics Engineering:]")
    st.write("*B.V.Raju Institute of Technology, Nov 1997 - May 2001*: (Grade A)")
    st.write("Control Systems, Power Electronics, Probability and Statistics, Data Structures and C, Computer Engineering, Electronic Devices")


def show_blogs():
    st.header(":blue[Blogs]")
    st.write("*Few Recent Blogs listed below:*")
    "---"
    st.write("*Exploring Decision Trees for Classification and Splitting Strategies: Unraveling the Tom and Jerry Chase*")
    st.write("https://medium.com/@shubavarma/exploring-decision-trees-for-classification-and-splitting-strategies-unraveling-the-tom-and-jerry-604e81080f80")
    "---"
    st.write("*Unleashing the Force of Machine Learning: Understanding Underfitting, Overfitting, Bias, and Variance in Star Wars*")
    st.write("https://medium.com/@shubavarma/unleashing-the-force-of-machine-learning-understanding-underfitting-overfitting-bias-and-9be930d14f64")
    "---"
    st.write("*Understanding the Confusion Matrix with Iron Man….Unleashing the Superhero Within*")
    st.write("https://medium.com/@shubavarma/understanding-the-confusion-matrix-with-iron-man-unleashing-the-superhero-within-a220a2b37e70")
    "---"
    st.write("*Understanding the Confusion Matrix with Iron Man….Unleashing the Superhero Within*")
    st.write("https://medium.com/@shubavarma/understanding-the-confusion-matrix-with-iron-man-unleashing-the-superhero-within-a220a2b37e70")
    "---"
    st.write("*KNN-Lazy Learner…*")
    st.write("https://medium.com/@shubavarma/knn-lazy-learner-d4aa68de9fed")
    "---"
    st.write("*ColumnTransformer and Pipeline …they are here to make our life easy…*")
    st.write("https://medium.com/@shubavarma/columntransformer-and-pipeline-they-are-here-to-make-our-life-easy-b1fd5ecfbe5b")
    "---"
    st.write("*Unlearn Relearn and have fun…*")
    st.write("https://medium.com/@shubavarma/unlearn-relearn-and-have-fun-8ad1b820fe15")


def show_skills():
    st.header(":blue[Skills]")
    "---"
    st.subheader(":green[Machine Learning:]")
    st.write("Supervised Learning, Unsupervised Learning, Semi Supervised Learning, Reinforcement Learning, Feature Engineering, Model Evaluation and Validation, Hyperparameter tuning, Ensemble Methods, Dimensionality Reduction, Transfer Learning, Deep Learning, Model Deployment")
    "---"
    st.subheader(":green[Python:]")
    st.write("Python Programming, Data Manipulation, Data Analysis and Visualization, WebScraping, Numpy, Pandas, PIL, Streamlit, Sklearn")
    "---"
    st.subheader(":green[SQL:]")
    st.write("SQL querying, Data Manipulation, Data Extracting and Joining, Data Modeling, Stored Procedures and Functions, Data Warehousing, Data Validation and Quality")
    "---"
    st.subheader(":green[Visualization:]")
    st.write("Tableau, PowerBI, Matplotlib, Seaborn, Excel")
    "---"
    st.subheader(":green[OLAP Tools:]")
    st.write("Hyperion Essbase 6.x/7.x/9.x/System 9, EAS 7.x, Hyperion Planning 9x, Hyperion Studio, HSS and OBIEE")
    "---"
    st.subheader(":green[ETL Tools:]")
    st.write("Informatica 6.1, Essbase Integration Services 6.5.3/7.0/7.1, IBM Data warehouse Manager")
    "---"
    st.subheader(":green[Reporting tools:]")
    st.write("Hyperion Analyzer 6.5/7.0/7.2/Web-based, Hyperion Smart View Add-in, Excel Addin, Web Analysis Reports and Interactive Reporting.")
    "---"
    st.subheader(":green[Misc:]")
    st.write("Matlab, Simulink, Microsoft Powerpoint, Microsoft Excel, Adobe Photoshop")



def show_interests():
    st.header(":blue[Interests]")
    st.write("*Below includes my Intersts and Non-IT Experience of 10 Years*")
    "---"
    st.subheader(":green[Marathon Organizer, Concert Organizer, Event Organizer]")
    st.write("Handling of huge teams and crowd. Project presentations, Funding exploration, Designing marketing material.")
    "---"
    st.subheader(":green[Extracurricular service provider for kids]")
    st.write("Handling school management and parents. Research and Documentation of various activities and lesson plans. Procurement of goods.")

def show_certificates():
    st.header(":blue[Certificates]")
    st.write("Only mentioning relevant Certificates")
    "---"
    st.subheader(":green[SQL (Intermediate) Certificate:]")
    st.write("https://www.hackerrank.com/certificates/9c68030c3f05")
    "---"
    st.subheader(":green[Python (Basic) Certificate:]")
    st.write("https://www.hackerrank.com/certificates/bba8c0d9b177")
    "---"
    st.subheader(":green[EDA project using Python:]")
    st.write("Innomatics Research Labs")
    "---"
    st.subheader(":green[Masterclass Certificate - Become a Data Ninja: Master the art of Exploratory Data Analysis in Python]")
    st.write("https://certificates.almabetter.com/en/verify/71287955462256")
    "---"
    st.subheader(":green[Data Analysis with Excel:]")
    st.write("Great Learning")
    "---"
    st.subheader(":green[Mathematics in DataScience:]")
    st.write("Great Learning")







Image1 = Image.open(r"photo 1.JPG")

st.set_page_config(layout="wide")  # Use the full screen width


col1, col2 = st.columns([1, 3])

with col1:
    st.image(Image1, width=200)

with col2:
    st.title(":blue[Portfolio]")

    st.markdown(":green[**Name:**] Subhadra Bhupathiraju")
    st.markdown(":green[**Email:**] shubavarma@gmail.com")
    st.markdown(":green[**Phone:**] 9160054949")
    st.write("")  # Add a line break

    link_column = st.columns(3)

    with link_column[0]:
        st.write("[LinkedIn](https://www.linkedin.com/in/shuba-bhupathiraju-25646489/)")

    with link_column[1]:
        st.write("[Medium](https://medium.com/@shubavarma)")

    with link_column[2]:
        st.write("[GitHub](https://github.com/shubavarma)")

st.write("")  # Add a line break

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.columns(7)

about_me_clicked = tab1.button(":green[About Me]")
experience_clicked = tab2.button(":green[Experience]")
education_clicked = tab3.button(":green[Education]")
skills_clicked = tab4.button(":green[Skills]")
certificates_clicked = tab5.button(":green[Certificates]")
blogs_clicked = tab6.button(":green[Blogs]")
interests_clicked = tab7.button(":green[Interests]")

if about_me_clicked or (not about_me_clicked and not experience_clicked and not education_clicked and not skills_clicked and not certificates_clicked and not blogs_clicked and not interests_clicked):
    show_about_me()

if experience_clicked:
    show_experience()

if education_clicked:
    show_education()

if skills_clicked:
    show_skills()

if certificates_clicked:
    show_certificates()

if blogs_clicked:
    show_blogs()

if interests_clicked:
    show_interests()