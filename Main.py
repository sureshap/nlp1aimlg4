##############################################
# A simple model/view template for Streamlit #
##############################################
import streamlit as st
################ Model ################
class Model:
    caption = "Hello World"
    Heading1 = "Automatic Ticket Assignment Tool"
    SubHeading1 = "FixITApp - Automatic Ticket Assignment Tool"
    SubHeading2 = "What type of NLP service would you like to use?"
    
###################### View  ################


def assignTicket(shortdesc,desc,caller):
    assignment_group = 'Default'
    info = "Shortdesc :" + shortdesc + "\n" \
           "Description :" + desc + "\n" \
           "Caller :" + caller  
 
    return assignment_group, info

def view(model):   
    #st.title(model.Heading1)
    st.header(model.SubHeading1)
    st.subheader(model.SubHeading2)
 
    def clear_form():
        st.session_state["txt_shortdesc"] = ""
        st.session_state["txa_desc"] = ""
        st.session_state["txt_caller"] = ""        

    #Picking what NLP task you want to do
    #option = st.selectbox('NLP Service',('Ticket Assignment', 'Sentiment Analysis', 'Entity Extraction', 'Text Summarization')) #option is stored in this variable
    
    if st.checkbox("Ticket Assignment"):
        
        #Textbox for text user is entering
        
        st.subheader("Enter the ticket details")
        st.text("Enter the ticket details for the ticket to be assigned to L3 team.")
        
        input_shortdesc = st.text_input('Short Description',value = "", key="txt_shortdesc") #text is stored in this variable
        input_desc = st.text_area('Description',value = "", key="txa_desc") #text is stored in this variable        
        input_caller = st.text_input('Caller',value = "", key="txt_caller") #text is stored in this variable

        col1, col2 = st.columns([.15,1])

        with col1:
            submit_button1 = st.button('Submit', key="submit_button1")
        
        with col2:
            clear_button1 = st.button('Clear', key="clear_button1", on_click=clear_form )
           
    
        if submit_button1:
            assignment_group, info = assignTicket(input_shortdesc,input_desc,input_caller)
            st.success("Assigned group :" +  assignment_group)
            st.success("Ticket Info :" +  info)
            
        if clear_button1:
            pass
            #input_text.clear()
            #st.text_area('Ticket to be assigned',value = "", key="text_area2")
            #with textareacol1:  
                #input_text = st.text_area('Ticket to be assigned',value = "", key="text_area2") #text is stored in this variable
  
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")
            
            
    # Side Menu content
    st.sidebar.subheader("About App")
    st.sidebar.text("NLP Ticket assignment App with Streamlit")
  	
    
    st.sidebar.subheader("By")
    st.sidebar.text("GL NLP1 Group3  ")
    
################ Start  ################
# Start of the program
view(Model())

################ Other methods  ################




   





