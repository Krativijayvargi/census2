# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.
import streamlit as st
import numpy as np
import pandas as pd
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):    
    # Display dataset within beta_expander.
  st.header('View Data')
  with st.beta_expander('View FullDataSet'):
    st.dataframe(census_df)

  if st.checkbox("Show Summary"):
    st.dataframe(census_df.describe())