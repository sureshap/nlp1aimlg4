##############################################
# A simple model/view template for Streamlit #
##############################################
import streamlit as st
################ Model ################
class Model:
    caption = "Hello World"
    Heading1 = "Automatic Ticket Assignment Tool"
    Heading2 = "FixITApp"
    ################ View  ################
def view(model):   
    st.title(model.Heading1)
    st.subheader("What type of NLP service would you like to use?")
    #Picking what NLP task you want to do
    option = st.selectbox('NLP Service',('Sentiment Analysis', 'Entity Extraction', 'Text Summarization')) #option is stored in this variable

################ Start  ################

   

placeholder = st.container()

# Replace the placeholder with some text:
placeholder.text("Hello")


# Replace the chart with several elements:
with placeholder.container():
    view(Model())

# Clear all those elements:
#placeholder.empty()

