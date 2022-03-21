import streamlit as st

st.set_page_config("CGPA Calculator")

def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade

def calc(sem):
    subjects = {}
    labs = {}
    CGPA = 0
    flag = 0  #for the warning message when marks haven't entered
    credits = 0
    col7, col8 = st.columns(2)  #for columns: one for theory sub, and another for lab sub

    if sem == 1 :
        subjects = { 'App. Maths-I' : 4, 'App. Physics-I' : 3, 'Manufacturing Processes' : 4, 'Electrical Science' : 3, 'Communication Skills' : 3, 'App. Chemistry' : 3 }
        labs = { 'App. Physics Lab-I' : 1, 'Elecrical Science Lab' : 1, 'Engg. Graphics Lab' : 2, 'App. Chemistry Lab' : 1 }
        credits = 25

    elif sem == 2:
        subjects = { 'App. Maths-II' : 4, 'App. Physics-II' : 3, 'Programming in C' : 3,'Indian Constitution' :2, 'Human Values and Ethics': 1, 'Engineering Mechanics' : 3, 'Environmental Studies' : 3 }
        labs = {  'Programming in C' : 1, 'App. Physics Lab-II' : 1, 'Workshop Practice' : 2, 'Engineering Graphics Lab' : 1, 'Environmental Studies Lab' : 1 }
        credits = 25

    elif sem == 3:
        subjects = { 'Computational Methods':4, 'Programme Core Theory Papers':16, 'Elements of Indian History for Engineers': 2 }
        labs = { 'Computational Methodos Lab' : 1, 'Programme Core Lab Papers':3}
        credits = 26

    elif sem == 4:
        subjects = { 'Probability, Statistics and Linear Programming' : 4, 'Programme Core Theory Papers':16,'Technical Writing': 2 }
        labs = { 'Probability, Statistics and Linear Programming Lab': 1 , 'Programme Core Lab Papers' : 3 }
        credits = 26

    elif sem == 5:
        subjects = { 'Programm Core Theory Paper' : 20, 'Econimics for Engineers' : 2}
        labs = { 'Programm Core Lab Paper' : 3, 'Summer Training Report ':1}
        credits = 26

    elif sem == 6:
        subjects = { 'Programm Core Elective Paper ':12,'Emerging Area / OpenArea Elective Papers ':8, 'Principles of Management For Engineers':4 }
        labs = { 'NSS / NCC /Cultural Clubs / Technical Society':2 }
        credits = 26

    elif sem == 7:
        subjects = { 'Programm Core Elective Paper ':8,'Emerging Area / OpenArea Elective Papers ':12, 'Principles Entrepreneurship Mindset':2 }
        labs = { 'Minor Project':3, 'Summer Training Report':1 }
        credits = 26    

    elif sem == 8:
        subjects = {  }
        labs = { 'Internship / Major Project -Disseration':14, 'Internship / Major project Viva Vioce':4, 'Internship / Project Progress Evaluation':2 }
        credits = 20

    with col7:
        with st.expander("Theory Subjects"):
            for subject in subjects:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                CGPA += num * subjects[subject]

    with col8:
        with st.expander("Practical Subjects"):
            for lab in labs:
                marks = st.number_input("{}: ".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                CGPA += num * labs[lab]

    if flag:
        st.warning("Please Enter Marks of All Subjects to get Correct CGPA")

    CGPA = CGPA / credits
    return CGPA



st.markdown(" <h1 style='text-align: center; font-size : 40px'><u> GGSIPU CGPA Calculator For CSE Branch </u></h1>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semesterwise CGPA Calculator of B.Tech(CSE)</h3> <br><br>", unsafe_allow_html=True)

st.text("Fields marked with * are required to be filled")
st.markdown("<hr>",unsafe_allow_html=True)  
st.subheader("Enter Personal Delails :")
my_bar = st.progress(0)
st.markdown("<hr>",unsafe_allow_html=True)

t=0
col1,col2 = st.columns(2)
with col1:
    n1=st.text_input("ENTER FIRST NAME : *")
if n1:
    my_bar.progress(20)
with col2:
    n2=st.text_input("ENTER LAST NAME : *")
if n2:
    my_bar.progress(40)
col5,col6 = st.columns(2)
with col5:
    roll=st.number_input("ENTER UNIVERSITY ROLL NO. : *",1 )
if roll > 1:
    my_bar.progress(60)
with col6:
    d=st.date_input("ENTER DATE OF BIRTH :")
cname=st.text_input("ENTER COLLEGE NAME : *")
if cname:
    my_bar.progress(80)
col3,col4 = st.columns(2)
with col3:
    sem = st.number_input("ENTER YOUR SEMESTER : *",0,8)
if sem > 0:
    my_bar.progress(100)
    t=1
with col4:
    st.date_input("ENTER SESSION YEAR :")

if t == 1:    

    st.markdown("<br><hr>",unsafe_allow_html=True)  
    st.subheader("Enter Academic Delails :") 
    st.markdown("<hr>",unsafe_allow_html=True)
    
    if sem:
        CGPA_final= calc(sem)

    st.write("")
    st.write("")

    cola,cola1,cola2,cola3,colb,colc3,colc2,colc1,colc = st.columns(9) 
    with colb:
        ans = st.button("Submit")

    if ans:
        result = "Your GPA: {}".format(str(round(CGPA_final,2)))
        st.markdown(f"<h2 style='text-align: center; '>{result}</h2>", unsafe_allow_html=True)
        if CGPA_final >= 8.0 :
            st.subheader("CONGRATS!! You Rocks...")
            st.balloons()