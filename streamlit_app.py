
import streamlit
streamlit.title('My Mom s New Healthy Diner')


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omegea 3 & Blueberry Oatmeal')

streamlit.text(' 🥗  Kale , Spinash & Rocket Smoothie')

streamlit.text(' 🐔  Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
