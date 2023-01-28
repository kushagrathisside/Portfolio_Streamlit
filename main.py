import streamlit as st
import yagmail

def sendmail(option,body_recieved):
    try:
        receiver = "kushagrathisside@gmail.com"
        body = body_recieved
        yag = yagmail.SMTP("kushagrathisside.com")
        yag.send(
            to=receiver,
            subject="{option} from your Portfolio",
            contents=body, attachments=None,
        )
        st.write("Mail Sent! :tada:")
    except:
        st.write("Service Unavailable")
st.title("Kushagra Srivastava :wave: ")
st.write("""Hi! My name is ***Kushagra Srivastava*** and I am Computer Science Undergraduate🎓. I am a T-shaped programmer particularly interested in ***Machine Learning and Data Science***, and have good command over languages like Python and C/C++. I like to work on different technologies which are mostly mentioned in my *GitHub* and *LinkedIn* IDs.""") 
st.markdown(f'''<a href='https://www.linkedin.com/in/kushagrathisside/'><button>LinkedIn</button></a>       <a href='https://www.github.com/kushagrathisside/'><button>Github</button></a>       <a href='https://medium.com/@kushagrathisside'><button>Medium</button></a>''',unsafe_allow_html=True)

st.header("Want to Talk?")
Intro = st.text_input("Tell me about you","Hi Kushagra! My name is .... ")
option_selected = st.selectbox('So, What do you want to talk about?',
          ('Technical Queries 🤖', 'Guidance Query 🙋‍♂️', 'Casual Talk ☕'))
explaination = st.text_input("Can you please elaborate about your {option}","So, I want to share that...")
st.write('Let me draft a mail for you...')
st.button("Send your query", on_click=sendmail(option_selected,Intro+'\n'+explaination))
