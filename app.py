import pickle as pk
import streamlit as st
import numpy as np


books = pk.load(open('pkl_store/book_names.pkl','rb'))
book_pivot = pk.load(open('pkl_store/pivot_table.pkl','rb'))
model = pk.load(open('pkl_store/model.pkl','rb'))
url_list = pk.load(open('pkl_store/url_list.pkl','rb'))

def fetch_img(title):
    return url_list[url_list['title'] == title].head(1)['img_urll']

def recommendation_system(input_book_title):
    book_index = np.where(book_pivot['title'] == input_book_title)[0]
    #print(book_pivot.iloc[964]['title'])
    if len(book_index) == 0:
        print("this book does not exist on our list.")
        return
    
    book_index = book_index[0]
    _, recomm = model.kneighbors(book_pivot.iloc[book_index,1:].values.reshape(1,-1),n_neighbors=6)

    book_output = []
    book_url = []
    j = 0
    for i in recomm[0]:
        if i > 0:
            book_output[j] = book_pivot.iloc[i]['title']
            book_url[j] = fetch_img(book_output[j])
            j += 1
    return book_url, book_output


st.header("Book recommendation system")
book_selected = st.selectbox('Select a book',books)

if st.button('Recommend 5 books'):

    url_recomm, recomm = recommendation_system(book_selected)
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        st.text(recomm[0])
        st.image(url_recomm[0])