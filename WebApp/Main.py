##############################################
# A simple model/view template for Streamlit #
##############################################
import streamlit as st

import unicodedata  # Replace accented encoding characters 
from googletrans import Translator # translate given text to English text
import re # Text pre-processing


# Import stop words list from NLTK
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords # Import stop words


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
#from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#import sklearn
import pickle

#import joblib

################ Model ################
class Model:
    caption = "Hello World"
    Heading1 = "Automatic Ticket Assignment Tool"
    SubHeading1 = "Automatic Ticket Assignment Tool"
    SubHeading2 = "What type of NLP service would you like to use?"
    
###################### View  ################

def remove_whitespace_CR(input_text):
    # Replace white space characters with space
    process_text = input_text.replace(r'\n',' '). replace(r'_x000D_',' ')
    return process_text

# Replace accented encoding characters
# Using normalize function returns the conventional form for the Unicode string unistr. 
# The valid values for form are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.
def remove_accents(input_text):
  try:
      process_text = unicode(input_text, 'utf-8')
  except (TypeError, NameError): # unicode is a default on python 3 
      process_text = input_text
  process_text = unicodedata.normalize('NFC', process_text)
  process_text = process_text.encode('ascii', 'ignore')
  process_text = process_text.decode("utf-8")
  return str(process_text)

def Translate_text(input_text):
  translator = Translator()
  try:
    trans_text = translator.translate(input_text).text
  except Exception as e:
    print(e)
    trans_text = input_text
  return trans_text

def preprocess_text(input_text):
  # convert column to string
  process_text=str(input_text)
  # Select only alphabets
  process_text = (re.sub('[^A-Za-z]+', ' ', process_text))
  # Convert text to lowercase
  process_text = process_text.lower()
  # Strip unwanted spaces
  process_text = process_text.strip()
  return process_text

def preprocess_vocab(input_text):
    stop_words=set(stopwords.words('english'))
    #stem=PorterStemmer()
    lem=WordNetLemmatizer()

    words=[w for w in word_tokenize(input_text) if (w not in stop_words)]
    words=[lem.lemmatize(w) for w in words if len(w)>2]


    process_text = ''
    for i, val in enumerate(words):
        process_text = process_text + ' ' + val

    process_text = [process_text]
    
    return  process_text


def getInfo(shortdesc,desc,caller):

    info = "Shortdesc :" + shortdesc + "\n" \
           "Description :" + desc + "\n"  \
           "Caller :" + caller  
 
    return info

def process_input(input_text):
    #print("##########################Inside process input##########################")
    process_text = remove_whitespace_CR(input_text)
    #print("Inside process input -after remove_whitespace_CR",process_text )
    process_text = remove_accents(process_text)
    #print("Inside process input -after remove_accents",process_text )    
    process_text = Translate_text(process_text)
    #print("Inside process input -after Translate_text",process_text )
    process_text = preprocess_text(process_text)
    #print("Inside process input -after Preprocessing",process_text )   
    process_text = preprocess_vocab(process_text)
    #print("Inside process input -after Vocab Preprocessing",process_text )   
    #print("##########################nside process input completed##########################")
    return process_text


def assignTicket(input_shortdesc,input_desc,input_caller):
    assignment_group = "Model under construction"
    text = input_shortdesc + input_desc
    
    process_text = process_input(text)
    
    info = process_text
    
   
   # Call the model
    pickled_model = pickle.load(open("saved_model3_lr.pkl", 'rb'))
    print("Model pickled retrieved")
    pickled_vectorizer = pickle.load(open("count_vectorizer.pkl", 'rb'))
    print("Vector pickled retrieved")
    print(process_text)
    X_prod_bow = pickled_vectorizer.transform(process_text)
    print("Bow data", X_prod_bow)
    y_pred = pickled_model.predict(X_prod_bow)
    print("y_pred", y_pred)
    pickled_le = pickle.load(open("label_encoder.pkl", 'rb'))
    result_lbl_enc = pickled_le.inverse_transform(y_pred)
    assignment_group = result_lbl_enc[0]
    return assignment_group, info, result_lbl_enc


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
            info = getInfo(input_shortdesc,input_desc,input_caller)
            assignment_group, message, result = assignTicket(input_shortdesc,input_desc,input_caller)
            st.success("Ticket Info :" +  info)    
            st.success(message)
            st.success(result)            
            st.success("Assignment group :" +assignment_group)

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
        image = Image.open('ProblemSolving.jpg')
    
        st.sidebar.image(image, caption='FixITApp')
    except Exception as e:
        print(e)

    st.sidebar.subheader("About App")
    st.sidebar.text("NLP Ticket assignment App with Streamlit")
  	
    
    st.sidebar.subheader("By")
    st.sidebar.text("GL NLP1 Group3  ")
    
################ Start  ################
# Start of the program
view(Model())

################ Other methods  ################




   





