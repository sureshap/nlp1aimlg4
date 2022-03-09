##############################################
# A simple model/view template for Streamlit #
##############################################
import streamlit as st
################ Model ################
class Model:
   caption = "Hello World"
################ View  ################
def view(model):
   st.write(model.caption)
################ Start  ################
view(Model())