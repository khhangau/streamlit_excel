import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('world-happiness-report-2021.csv')

st.sidebar.title('World Happiness Index 2021:')

st.image('https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg', caption='World Happiness Dataset')

country_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", "North America and ANZ","Middle East and North Africa", "Latin America and Caribbean","Central and Eastern Europe","Commonwealth of Independent States","Sub-Saharan Africa"]

select = st.sidebar.selectbox('Filter the region here:', country_list, key='1')

if select =="All":
    filtered_df = df
else:
    filtered_df = df[df['Regional indicator']==select]

score = st.sidebar.slider('Select min Ladder Score', min_value=5, max_value=10, value = 10)
df = df[df['Ladder score'] <= score]

st.write(filtered_df)

fig = px.scatter(filtered_df,
x="Logged GDP per capita",
y="Healthy life expectancy",
size="Ladder score",
color="Regional indicator",
hover_name="Country name",
size_max=10)

st.write(fig)

st.write(px.bar(filtered_df, y='Ladder score', x='Country name'))

corr = filtered_df.corr()

plt.figure(figsize=(8, 8))

fig1 = plt.figure()

ax = sns.heatmap(corr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(20, 220, n=200),
square=True
)

ax.set_xticklabels(
ax.get_xticklabels(),
rotation=45,
horizontalalignment='right'
);

st.pyplot(fig1)
