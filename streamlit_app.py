import streamlit
streamlit.title('My Parents Healthy New Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 and Blueberry Muffin')
streamlit.text('🥗Kale.Spinach and Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('fruit')
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

