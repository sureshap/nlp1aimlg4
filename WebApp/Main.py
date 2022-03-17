##############################################
# A simple model/view template for Streamlit #
##############################################
import streamlit as st


import pandas as pd

from pathlib import Path

# User defined class for doing input preprocessing
from InputTransformer import InputTransformer

import pickle

#from sklearn.pipeline import Pipeline

################ Model ################
class Model:
    Heading1 = "Automatic Ticket Assignment Tool"
    SubHeading1 = "What type of NLP service would you like to use?"

    # Path for Streamlit cloud implementations    
    app_image_path = Path(__file__).parents[1] / 'WebApp/ProblemSolving.jpg'
    pkl_le_path = Path(__file__).parents[1] / 'WebApp/label_encoder.pkl'
    pkl_pipeline_path = Path(__file__).parents[1] / 'WebApp/saved_pipeline_lr.pkl'    
    
    
###################### View  ################

def assignTicket(input_shortdesc,input_desc,input_caller):

    text = input_shortdesc + input_desc
       
   # Call the model
    pickled_pipleine = pickle.load(open(Model.pkl_pipeline_path, 'rb'))
    print("Pipleline pickled retrieved")
    X_prod = pd.Series(text)
    X_prod = InputTransformer.preprocess_input(X_prod)
    y_pred = pickled_pipleine.predict(X_prod)
    #y_pred = ""
    print("y_pred", y_pred)
    pickled_le = pickle.load(open(Model.pkl_le_path, 'rb'))
    result_lbl_enc = pickled_le.inverse_transform(y_pred)
    assignment_group = result_lbl_enc[0]
    return assignment_group, y_pred


def view(model):   
    #st.title(model.Heading1)
    st.header(model.Heading1)
    st.subheader(model.SubHeading1)
 
    def clear_form():
        st.session_state["txt_shortdesc"] = ""
        st.session_state["txa_desc"] = ""
        st.session_state["txt_caller"] = ""        

    #Picking what NLP task you want to do
    #option = st.selectbox('NLP Service',('Ticket Assignment', 'Sentiment Analysis', 'Entity Extraction', 'Text Summarization')) #option is stored in this variable
    
    if st.checkbox("Ticket Assignment"):
        
        #Textbox for text user is entering
        
        st.subheader("Enter the ticket details")
        st.text("Enter the ticket details for automatic assignment to L3 team.")
        
        input_shortdesc = st.text_input('Short Description',value = "", key="txt_shortdesc") #text is stored in this variable
        input_desc = st.text_area('Description',value = "", key="txa_desc") #text is stored in this variable        
        input_caller = st.text_input('Caller',value = "", key="txt_caller") #text is stored in this variable

        col1, col2 = st.columns([.15,1])

        with col1:
            submit_button1 = st.button('Submit', key="submit_button1")
        
        with col2:
            clear_button1 = st.button('Clear', key="clear_button1", on_click=clear_form )
           
    
        if submit_button1:
            assignment_group, result = assignTicket(input_shortdesc,input_desc,input_caller)       
            st.success("Ticket to be assigned to Group :" +assignment_group)

        if clear_button1:
            pass
            #input_text.clear()
            #st.text_area('Ticket to be assigned',value = "", key="text_area2")
            #with textareacol1:  
                #input_text = st.text_area('Ticket to be assigned',value = "", key="text_area2") #text is stored in this variable
  
    #if st.checkbox("Show Tokens and Lemma"):
        #st.subheader("Tokenize Your Text")
            
            
    # Side Menu content
    try:
        from PIL import Image
        image = Image.open(Model.app_image_path)
    
        st.sidebar.image(image, caption='FixITApp')
    except Exception as e:
        print(e)

    st.sidebar.subheader("About App")
    st.sidebar.text("NLP Ticket assignment App")
  	
    
    st.sidebar.subheader("By")
    st.sidebar.text("GL NLP1 Group3  ")
    
################ Start  ################
# Start of the program
view(Model())

################ Other methods  ################




   





