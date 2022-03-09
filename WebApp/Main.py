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
   st.write(model.caption)
################ Start  ################
view(Model())



import time


	 
	 
	 
placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

# Clear all those elements:
#placeholder.empty()