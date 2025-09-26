import streamlit as st
import  pandas as pd
st.set_page_config(layout="wide")
df = pd.read_csv('us_student.csv')
df = df[['Student ID', 'Name', 'mother_name', 'Gender', 'Age', 'State', 'Degree',
       'Field of Study', 'University', 'Graduation Year', 'Visa Status',
       'Employment Status']]
st.dataframe(df   , height=800 , width="stretch")

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(df)

st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="my_dataframe.csv",
    mime="text/csv",
    key="primary"
)
st.markdown("""
    <style>
    .stDownloadButton > button {
        background-color: #FF5733; /* Custom background color (e.g., orange-red) */
        color: white; /* Text color */
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stDownloadButton > button:hover {
        background-color: #C70039; /* Darker color on hover */
    }
    </style>
    """, unsafe_allow_html=True)
