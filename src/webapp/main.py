import streamlit as st

st.title("Talent Map")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


from faker import Faker
import pandas as pd

fake = Faker() 

df2 = []

for n in range(20000000):
    df2.append(list(fake.profile().values()))

df2 = pd.DataFrame(df2, columns=fake.profile().keys())
st.dataframe(df2)

