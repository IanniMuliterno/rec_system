import pickle as pk
import streamlit as st
import numpy as np


books = pk.load(open('pkl_store/book_names.pkl','rb'))
book_pivot = pk.load(open('pkl_store/pivot_table.pkl','rb'))
model = pk.load(open('pkl_store/model.pkl','rb'))
url_list = pk.load(open('pkl_store/url_list.pkl','rb'))


def recommendation_system(input_book_title):
    book_index = np.where(book_pivot['title'] == input_book_title)[0]

    if len(book_index) == 0:
        print("this book does not exist on our list.")
        return
    
    book_index = book_index[0]
    _, recomm = model.kneighbors(book_pivot.iloc[book_index,1:].values.reshape(1,-1),n_neighbors=6)
    for i in recomm[0]:
        if i == 0:
            print(f'you selected the book: {input_book_title}')
            print('the recommendations are: ')
            print('')
        else: 
            print(book_pivot.iloc[i]['title'])


st.header("Book recommendation system")
book_selected = st.selectbox('Select a book',books)

if st.button('Recommend 5 books'):

    _, recomm = recommendation_system(book_selected)
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        st.text()
        st.image()