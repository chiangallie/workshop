import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:/Users/Allie Chiang/workshop/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def app():
    if 'db' not in st.session_state:
        st.session_state.db = db
        print("Connection successful")