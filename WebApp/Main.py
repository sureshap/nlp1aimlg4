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



st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")