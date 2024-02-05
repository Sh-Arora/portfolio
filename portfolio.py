import streamlit as st
from PIL import Image


def show_about_me():
    st.header(":blue[About Me]")
    st.write("Hyderabad-native engineer with a passion for mathematics and a specialization in control systems. Pursued Masters in the USA, specializing in control systems. Established a successful career in the analytics field and delivered several projects. Entrepreneurial spirit led to founding extracurricular service company and organizing diversified events. Adaptable leader skilled in crisis management, communication, and analytical thinking. Eager to leverage expertise in artificial intelligence and passion for innovation in next professional endeavor.")
    st.subheader(":blue[What Drives me:]")
    st.write("My journey through education has ignited a deep fascination for artificial intelligence and robotics. Exploring the realms of these cutting-edge technologies during my academic years has sparked a curiosity that continues to drive me forward. In my subsequent work experiences with multi-dimensional databases, I have witnessed firsthand the immense value of harnessing data in multiple ways for making informed and strategic business decisions. Then my entrepreneurial ventures experiences have provided me with valuable insights into the managerial and people skills required to lead and inspire teams. However, the COVID-19 pandemic brought unexpected challenges and a temporary break in my professional pursuits. Yet, amidst the chaos, it reignited the passion for AI that I had nurtured in my younger days, particularly with the current boom in the market. Driven by this renewed enthusiasm, I have worked passionately to relearn and update my knowledge in the field, determined to make a meaningful impact in the world of Artificial Intelligence and DataScience. ")

def show_experience():
    st.header("**:blue[Experience]**")
    "---"
    st.subheader(":green[Jr Data Scientist:] *Innomatics Research Labs, Nov 2022 - Present*")
    st.write("Worked on near real time projects from end to end that include Data collection, Data Cleaning, Data Analysis, Statistical Analysis, SQL querying, Machine Learning model or Deep Learning model building and deployment.")
    "---"
    st.subheader(":green[Director of Operations:] *Spartans Media, Apr 2019 - May 2022*")
    st.write("Handled Operations in organizing several large events like Marathons, Food Festivals, Musical concerts and exhibitions. Involved in presenting sales pitch for securing funds for the events. Created marketing materials and organized marketing campaigns. Worked closely with people in different levels to get the event up and running.")
    "---"
    st.subheader(":green[Director:] *Kidsdale International Pre-school, Feb 2014 - May 2021*")
    st.write("Worked with partners to create a business strategy to setup and run an educational institution. Handled budgeting and finance. Helped in creating marketing materials and campaigns. Involved in design and execution of school curriculum.")
    "---"
    st.subheader(":green[Director Of Operations:] *Arena Events, Oct 2015 - Apr 2019*")
    st.write("Handled Operations in organizing several large events like Marathons, health awareness events. Created marketing materials and organized health awareness campaigns. Worked with people and communities to spread health awareness.")
    "---"
    st.subheader(":green[Director - Operation Head:] *Kids Arena Sports and Activities India Pvt.Ltd, Jan 2013 - Apr 2019*")
    st.write("Created a curriculum from scratch for sports, arts, dance and music. Provided the same as a service to schools that lack infrastructure. Developed a training program for coaches and cross skilled them to train the students. Devised a custom budget for each school based on the requirements.")
    "---"
    st.subheader(":green[Sr Analyst:] *Oracle India, Apr 2010 - Dec 2010*")
    st.write("Involved in support and performance enhancements of Essbase cubes. Learned OBIEE and Informatica as part of cross skilling for supporting the American Express systems. Helped various cross platform resources in understanding Hyperion and its tools and supporting them by conducting training sessions. Worked on team’s communication and reporting skills through training based learning.")
    "---"
    st.subheader(":green[Sr Programming Analyst:] *Limited Brands USA, Feb 2006 - Dec 2009*")
    st.write("Started with an end-to-end support role at Victoria Secret Direct which uses Essbase to analyze the Merchandize planning data. Created a Production schedule to perform builds, loads and calculation of the databases. Also supported UDB (source data), SQL queries and shell scripts pertaining to these processes. Supported a third-party tool called “Clarity”, which was used by a small group of financial people for operational planning. Involved in performance tuning and optimization of Essbase cubes for better performance.")
    "---"
    st.subheader(":green[Sr Hyperion Essbase Consultant:] *RJ Reynolds Tobacco Company, Jan 2005 - Feb 2006*")
    st.write("RJR Hyperion Group uses Essbase to analyze the Sales data. Involved in running the production and resolving issues encountered during the process. Involved in the process of converting applications from BSO to ASO. Converted outline formulae from classic to MDX. Developed new rule files to load data into the cubes. Organized discussions with Business users and analysts to gather requirements and incorporate changes into production. Used Hyperion Analyzer and Excel to check the data availability and accuracy. Created and maintained Users and Groups for Hyperion Essbase and Hyperion Analyzer.")
    "---"
    st.header(":blue[Language Proficiency]")
    st.write("English, Hindi, Telugu")


def show_education():
    st.header(":blue[Education]")
    "---"
    st.subheader(":green[Certified in Data Science:]")
    st.write("*Innomatics Research Labs, Nov 2022 - Aug 2023:* (Grade A)")
    st.write("Python, SQL, Statistics, Tableau, Machine Learning, Aritificial Intelligence, Deep Learning, Flask, MLops")
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
    st.write("*Unlocking Insights: Exploring Client-Server Architecture for Business and Data Science*")
    st.write("https://medium.com/@shubavarma/unlocking-insights-exploring-client-server-architecture-for-business-and-data-science-78d4344b877d")
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
    st.write("Supervised Learning, Unsupervised Learning, Semi Supervised Learning, Reinforcement Learning, Feature Engineering, Model Evaluation and Validation, Hyperparameter tuning, Ensemble Methods, Dimensionality Reduction, Transfer Learning, Deep Learning, Model Deployment, MLOps")
    "---"
    st.subheader(":green[Python:]")
    st.write("Python Programming, Data Manipulation, Data Analysis and Visualization, WebScraping, Numpy, Pandas, PIL, Streamlit, Sklearn, Flask")
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
    "---"
    st.subheader(":green[Pre-School provider for kids]")
    st.write("Started a Pre-school and Day care that concentrated on making learning fun for kids.")
    "---"
    st.subheader(":green[Jewelry Making]")
    st.write("One of my passions, learned making Terracota, Paper Quilling and Bead Jewelry. Sketching out the designs on paper and making them in to Jewelry pieces is artistic satisfaction for me.")




def show_certificates():
    st.header(":blue[Certificates]")
    st.write("Only mentioning relevant Certificates")
    "---"
    st.subheader(":green[DataScience Completion Certificate:]")
    st.write("Innomatics Research Labs")
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
        st.write("[LinkedIn](https://www.linkedin.com/in/subhadrabhupathiraju/)")

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