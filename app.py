# @Email:  awais.dev2serve@gmail.com
# @Group:  Tri Oxy Genz
# Hack Fest 2.0 Remote Base 

from multiprocessing.sharedctypes import Value
from turtle import color, left
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import altair as alt

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Project", page_icon=":bar_chart:", layout="wide")

# read csv file 
@st.cache
def get_data_from_csv():
    df = pd.read_csv("Employee-data.csv", index_col=False)
    df.reset_index(drop=True, inplace=True)
    df.set_index("Age" , inplace=True)
    return df

df = get_data_from_csv()

st.title(":chart_with_upwards_trend: Employee Evaluation Dashboard")

name = st.multiselect(
    "Select the Employee's Name:",
    options=df["Name"].unique()
)

# selected data to be stored 
df_selection = df.query(
    "Name == @name "
)

# only filter data shows 
if(name):
    st.dataframe(df_selection)

# employee evaluation report
st.header(":chart_with_upwards_trend: Employee Performance Evaluation Dashboard")

left_column, middle_column, right_column= st.columns(3)

with left_column:
    st.write("""
    ### :bar_chart: Performance
    """)
    bar_chart = alt.Chart(df_selection[["Month","performance"]]).mark_bar().encode(
        y = "performance",
        x = "Month",
        color = alt.Color("performance" ,type="ordinal")
    )
    st.altair_chart(bar_chart , use_container_width=True )

with middle_column:
    st.write("""
    ### :bar_chart:  Analytical Ability
    """)
    bar_chart = alt.Chart(df_selection[["Month", "analytical ability"]]).mark_bar().encode(
        y = "analytical ability",
        x = "Month",
        color = alt.Color("analytical ability", type="nominal")
    )
    st.altair_chart(bar_chart , use_container_width=True )

with right_column:
    st.write("""
    ### :bar_chart: Social Life Balance
    """)
    bar_chart = alt.Chart(df_selection[["Month", "social life balance"]]).mark_bar().encode(
        y = "social life balance",
        x = "Month",
        color = alt.Color("social life balance")

    )
    st.altair_chart(bar_chart , use_container_width=True )


# psychological test evaluation report
st.header(":chart_with_downwards_trend: Employee Psychological Activity Evaluation Dashboard")


l_column, m_column, r_column= st.columns(3)

with l_column:
    st.write("""
    ### :bar_chart: Building Trust
    """)
    bar_chart = alt.Chart(df_selection[["Month","Building Trust"]]).mark_bar().encode(
        y = "Building Trust",
        x = "Month",
        color = alt.Color("Building Trust" ,type="ordinal")
    )
    st.altair_chart(bar_chart , use_container_width=True )

with m_column:
    st.write("""
    ### :bar_chart: Teamwork
    """)
    bar_chart = alt.Chart(df_selection[["Month", "Teamwork"]]).mark_bar().encode(
        y = "Teamwork",
        x = "Month",
        color = alt.Color("Teamwork", type="nominal")
    )
    st.altair_chart(bar_chart , use_container_width=True )

with r_column:
    st.write("""
    ### :bar_chart: Confidence
    """)
    bar_chart = alt.Chart(df_selection[["Month", "Confidence"]]).mark_bar().encode(
        y = "Confidence",
        x = "Month",
        color = alt.Color("Confidence")

    )
    st.altair_chart(bar_chart , use_container_width=True )


