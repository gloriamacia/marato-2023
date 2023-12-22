import streamlit as st
st.title('Calculadora')
num_1 = st.number_input('número 1')
num_2 = st.number_input('número 2')
num_3 = num_1 + num_2
st.write('# La suma és', num_3)