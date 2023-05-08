import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# creat a title
st.title("Diamonds EDA and Price Prediction APP")

# create a sidebar
st.sidebar.header("User Input")
# 
uploaded_file = st.sidebar.file_uploader("Upload Diamond Dataset (CSV format)", type=["csv"])


if uploaded_file:
    diamonds_data = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.dataframe(diamonds_data.head(10))

    st.write ("### Summary Statistics")
    summary_stats = diamonds_data.describe().T
    st.table(summary_stats)

    st.sidebar.subheader("Visualization Options")
    columns_to_polt = st.sidebar.multiselect("Select columns to visualize:", diamonds_data.columns)

    if columns_to_polt:
        for column in columns_to_polt:
            fig, ax = plt.subplots()
            sns.histplot(data= diamonds_data, x=column, bins=30, ax=ax)
            ax.set_title(f'Histogram of {column}')
            st.pyplot(fig) 


else:
    st.write("Please upload a dataset")