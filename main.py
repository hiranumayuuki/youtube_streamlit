
from pandas.io.pytables import Table
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title("streamlit 超入門")
st.write("プログレスバーの表示")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ１の回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ２の回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ３の回答")



#text = st.text_input("あなたが好きな数字を教えてください")
#condition = st.slider("あなたの今の調子は?",0,100,50)

#"あなたの趣味:", text

#"コンディション:", condition
#if st.checkbox("Show Imag"):
#    img = Image.open("旅に1000万.jpeg")
#st.image(img,caption="tabi",use_column_width=True)




