import streamlit as st

st.title("PowerBI 簡報說明")

tab1, tab2,tab3, tab4, tab5 = st.tabs(["肺癌男女分布", "依家族史與吸菸史分布", "依治療方式分布", "依年齡分布", "依病理分布"])

with tab1:
    st.header("肺癌男女分布")
    st.image("images/l2.jpg", caption="肺癌男女分布圖")

with tab2:
    st.header("依家族史與吸菸史分布")
    st.image("images/lung.png", caption="依家族史與吸菸史分布圖")