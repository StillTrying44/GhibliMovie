#%pip install numpy
import numpy as np
import streamlit as st

movies = [  "The Castle of Cagliostro", 
            "Nausicaä of the Valley of the Wind", 
            "Castle in the Sky",	
            "My Neighbor Totoro",	
            "Kiki's Delivery Service",	
            "Porco Rosso",	
            "Whisper of the Heart",	
            "Princess Mononoke",
            "Spirited Away",
            "Howl's Moving Castle",	
            "Ponyo",		
            "Arrietty",	
            "From Up on Poppy Hill",
            "The Wind Rises",	
            "The Boy and the Heron" ]
x = np.random.choice(movies)

st.title("Ghibli Movie:")

gen = st.button('generate')
if gen:
    st.success(x)

