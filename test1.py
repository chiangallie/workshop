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
        
    docs=db.collection('attendance').get()
    
    if docs.exists:
        print('Attendance: ',docs.to_dict())
    else:
        print('No data found')

    #for doc in docs:
      #  d=doc.to_dict()
      #  print(doc)
      #  print("d : ",d)
        #try:
      #      st.text_area(label=':green[Posted by:]', value=d['drFGifusTIRl6170pwgD'])
      #  except: pass
        