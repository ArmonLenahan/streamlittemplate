import streamlit as st
import pandas as pd
import numpy as np

def foo():
	print('bar')


st.set_page_config(layout='wide')
st.title('WELCOME TO THE JUNGLE ')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab2", "Tab3"])

with tab1:
	st.header('WE GOT FUN & GAMES')
	st.subheader('Fact: Bears eat beets. BEARS. BEETS. BATTLESTAR GALATICA.')
	st.button('Josh Allen is the best QB in the NFL (check box below if you agree)')
	st.checkbox('Shit YEAH I agree')

with tab2:
	st.radio('Pick one', ['cats', 'dogs'])
	st.selectbox('Pick one', ['cats', 'dogs'])
	st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

with tab3:
	st.slider('Pick a number', 0, 100,50)
	st.select_slider('Pick a size', ['S', 'M', 'L'])
	st.text_input('First name')