import streamlit
import pandas as pd
import requests

streamlit.title('*************My Parents New Healthy Diner*************')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 HArd-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Please select some fruits:', list(my_fruit_list.index), ['Banana','Honeydew'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#to display
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit advice .... ulala..')

fruit_picked = streamlit.text_input('Enter a fruit to pick from fruityvice:', value = "")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_picked)

#streamlit.text(fruityvice_response.json()) This will be replaced with below formatter code

fruityvice_normailzed_json = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normailzed_json)


