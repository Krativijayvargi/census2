import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings

# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
	warnings.filterwarnings('ignore') 
	st.set_option('deprecation.showPyplotGlobalUse', False)
	# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
	# Store the current value of this widget in a variable 'plot_list'.
	st.title('Visualize Data')
	st.subheader('Visualisation Selector')
	plot_list = st.multiselect('Select plot/charts:',('Count Plot','Pie Chart','Box Plot'))

	# Display count plot using seaborn module and 'st.pyplot()' 
	if 'Count Plot' in plot_list:
	  st.subheader("Count plot")
	  plt.figure(figsize=(15,5))
	  plt.title('Count plot')
	  sns.countplot(x = 'workclass', data = census_df,hue='income')
	  st.pyplot()

	# Display pie plot using matplotlib module and 'st.pyplot()'
	if 'Pie Chart' in plot_list :
		st.subheader('Pie Chart')
		pie_data = census_df['income'].value_counts()
		plt.figure(figsize=(15,5))
		plt.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%', startangle=30,explode = np.linspace(.06, .12, 2))
		plt.title('Distribution of records for the income-group')
		st.pyplot()

		pie_data = census_df['gender'].value_counts()
		plt.figure(figsize=(15,5))
		plt.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%', startangle=30,explode = np.linspace(.06, .12, 2))
		plt.title('Distribution of records for the gender')
		st.pyplot()

	# Display box plot using matplotlib module and 'st.pyplot()'
	if 'Box Plot' in plot_list:
		st.subheader('Box Plot')
		col1 = st.selectbox('Select a column to create box plot:',('income','gender'))
		plt.figure(figsize=(10,5))
		plt.title(f'Box plot for {col1}')
		sns.boxplot(census_df['hours-per-week'],census_df[col1])
		st.pyplot()