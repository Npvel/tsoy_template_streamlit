import pandas as pd
import streamlit as st

import datetime

st.set_page_config(page_title="Импорт Прайсов",  layout="centered")

st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Times'; color: #4d4643;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<h1 class="font">ИМПОРТ ПРАЙС-ЛИСТОВ </h1>', unsafe_allow_html=True)

form = st.form(key="annotation")

now = datetime.datetime.now()

with form:
    cols = st.columns((1, 1, 1))
    suppliers = cols[0].selectbox("Поставщики:", ["MERLION", "3Logic", "ELCO", "NOTIK", "BENEFIT"],
     index=2)
    delivery_type = cols[1].selectbox("Склад и тип доставки", ["MSK", "MSK 501"])
    delivery_date = cols[2].date_input("Дата доставки", now)

    updates = st.radio(
     "Обновление",
     ('Авто - 8:00', 'Ручное',))
        
#     comment = st.text_area("Comment:")
#     cols = st.columns(2)
#     date = cols[0].date_input("Bug date occurrence:")
#     bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
    submitted = st.form_submit_button(label="Применить")

if submitted:
    st.write(suppliers, delivery_type, delivery_date, updates)

with st.container():
    st.write("Структура Каталогов")

    # You can call any Streamlit command, including custom components:
    
    catalogs = st.multiselect(
        'Каталог',
        ['Продукты питания', 'Аудио-видео техника', 'Портативная электроника', 'Усилители', 'Встраиваемая техника', 'Автозапчасти'],
        )

with st.container():
    st.write("Редактирование стоп-листа")

    # You can call any Streamlit command, including custom components:
    
    title_1 = st.text_input('Описание', 'поврежденная')

    title_2 = st.text_input('Описание', 'бракованная')


with st.container():
    st.write("Товары")

    # You can call any Streamlit command, including custom components:
    
    title_1 = st.text_input('Описание', 'поврежденная', key=0)

    title_2 = st.text_input('Описание', 'бракованная', key=1)

vins = ['34810', '235072', '230198', '1230987', '1240987']
goods = ['Ноутбук1', 'Ноутбук2', 'Моноблок', 'Видеоплата', 'SDD']
brand = ['Apple', 'Sony', 'LG', 'Samsung', 'Asus']
artcul = ['fsdadsf', 'adad', 'afddf', 'sdfg', 'rtyu1']
qte = ['10', '20', '3', '55', '3', '23']
price = ['1000', '987', '500', '1200', '1293']

with st.container():
    st.write("Каатлог Товаров")

    df = pd.DataFrame(list(zip(vins, goods, brand, artcul, qte, price)), columns=['VIN', 'Наименование', 'Бренд', 'Артикул', 'Количество', 'Цена'])

    st.dataframe(df)        