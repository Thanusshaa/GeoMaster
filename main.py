import streamlit as st
from openai import OpenAI
import google.generativeai as genai


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def interactive_qa(question, sysprompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": question}
        ],
        max_tokens=300
    )
    answer = response.choices[0].message.content
    return answer

def dynamic_answer(location, category):
        question = f"What is the {category} of {location}?"
        answer = interactive_qa(question, sysprompt)
        return answer

def real_time_data(event_type):
        if event_type == "Natural Disasters":
            data = "Latest natural disaster updates: Hurricane season is approaching in the Atlantic region."
        elif event_type == "Climate Change":
            data = "Latest climate change updates: Global temperatures have risen by 1.1°C since 1880."
        elif event_type == "Weather Patterns":
            data = "Latest weather pattern updates: A high-pressure system is moving across the Midwest region."
        elif event_type == "Seismic Activities":
            data = "Latest seismic activity updates: A magnitude 6.5 earthquake struck off the coast of Japan."
        elif event_type == "Ocean Currents":
            data = "Latest ocean current updates: The Gulf Stream is experiencing a unusual slowdown."
        else:
            data = "No data available for this event type."
        return data

st.title("GeoMaster AI")

st.sidebar.title("Features")
feature = st.sidebar.selectbox(
    "Select a feature",
    ["Interactive Q&A", "Dynamic Answer", "Real-Time Data"]
)

sysprompt = "You are a geography expert. Provide detailed and accurate answers. You are require only to answer geography related. You are allowed to use the internet for information. You are allowed to generate images related to geography."

if feature == "Interactive Q&A":
    st.header("Interactive Q&A")
    question = st.text_input("Ask a geography question:")
    if st.button("Get Answer"):
        answer = interactive_qa(question, sysprompt)
        st.write(answer)

elif feature == "Dynamic Answer":
        st.header("Dynamic Answer")
        location = st.text_input("Enter a location:")
        category = st.selectbox("Select category", ["Climate Zones", "Population Density", "Topography", "Political Boundaries"])
        if st.button("Show Answer"):
            answer = dynamic_answer(location, category)
            st.write(answer)
        
elif feature == "Real-Time Data":
            st.header("Real-Time Data")
            event_type = st.selectbox("Select event type", ["Natural Disasters", "Climate Change", "Weather Patterns", "Seismic Activities", "Ocean Currents"])
            if st.button("Get Data"):
                data = real_time_data(event_type)
                st.write(data)

