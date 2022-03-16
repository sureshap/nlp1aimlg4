from sklearn.base import BaseEstimator, TransformerMixin

import unicodedata  # Replace accented encoding characters 
from googletrans import Translator # translate given text to English text
import re # Text pre-processing

import time

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords # Import stop words
stop_words = set(stopwords.words('english'))

nltk.download('punkt')

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class ExperimentalTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>init() called.\n')
    
    def remove_whitespace_CR(input_text):
        #print(input_text)
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
          time.sleep(1)
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
        
        #print('Step 1', words)
        #print(type(words))
        
        process_text = ''
        for i, val in enumerate(words):
            process_text = process_text + ' ' + val
        
        #print('Step 2', process_text)
        #print(type(process_text))
        #process_text = [process_text]
        
        #print('Step 3', process_text)
        #print(type(process_text))    
        return  process_text

    def preprocess_input(input_text):
        print("##########################Inside process input##########################")
        #print(type(input_text))
        process_text = input_text.apply(ExperimentalTransformer.remove_whitespace_CR)
        #print(type(process_text))
        print("Inside process input -after remove_whitespace_CR",process_text )
        process_text = process_text.apply(ExperimentalTransformer.remove_accents)
        print("Inside process input -after remove_accents",process_text )    
        process_text = process_text.apply(ExperimentalTransformer.Translate_text)
        print("Inside process input -after Translate_text",process_text )
        process_text = process_text.apply(ExperimentalTransformer.preprocess_text)
        print("Inside process input -after Preprocessing",process_text )   
        process_text = process_text.apply(ExperimentalTransformer.preprocess_vocab)
        print("Inside process input -after Vocab Preprocessing",process_text )   
        print("##########################nside process input completed##########################")
        return process_text

    def fit(self, X, y = None):
        print('\n>>>>>>>fit() called.\n')
        return self

    def transform(self, X, y = None):
        print('\n>>>>>>>transform() called.\n')
        #X_ = X.copy() # creating a copy to avoid changes to original dataset
        X = ExperimentalTransformer.preprocess_input(X)
        return X

def test():
    print("Import test success")
