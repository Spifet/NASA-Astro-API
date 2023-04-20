import requests
import streamlit as st

api_key = "VYCcR2PMFay10uhCjrZdFWLyec4gPbjJCj3EDMsd"
url = f"https://api.nasa.gov/planetary/apod" \
      f"?api_key={api_key}"

request = requests.get(url)
content = request.json()

st.title(content['title'])
st.image(content['url'])
st.write(content['explanation'])
