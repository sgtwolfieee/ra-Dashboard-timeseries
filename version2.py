# To run the app, enter this in the Terminal:
#   streamlit run 00_jumpstart/03_streamlit_jumpstart.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set the background color and header styling with Streamlit Markdown and CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp header {
        background-color: #4CAF50;
        color: white;
    }
    .header-text {
        font-size: 24px;
        color: #4CAF50;
        font-weight: bold;
    }
    .sub-header {
        font-size: 20px;
        color: #ff7f50;
    }
    .important-text {
        font-size: 16px;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1.0 Dashboard Title and Introduction
st.markdown("<div class='header-text'>📊 Business Dashboard</div>", unsafe_allow_html=True)
st.write("""
Welcome! This dashboard offers insights into sales, customer demographics, and product performance. 
Upload your data to get started.
""")

# 2.0 Data Upload Section
st.markdown("<div class='sub-header'>📁 Upload Business Data</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Select a CSV file", type="csv")

# 3.0 Dashboard Content - Display Insights if Data is Loaded
if uploaded_file:
    # Load and preview data
    data = pd.read_csv(uploaded_file)
    st.write("### 👀 Data Preview")
    st.dataframe(data.head())

    # 3.1 Sales Insights
    st.markdown("<div class='sub-header'>📈 Sales Insights</div>", unsafe_allow_html=True)
    if 'sales_date' in data.columns and 'sales_amount' in data.columns:
        st.write("#### Sales Over Time")
        fig_sales = px.line(data, x='sales_date', y='sales_amount', title='📅 Sales Over Time')
        st.plotly_chart(fig_sales)
    else:
        st.warning("The data must contain 'sales_date' and 'sales_amount' columns for sales insights.")

    # 3.2 Customer Segmentation
    st.markdown("<div class='sub-header'>🌍 Customer Segmentation</div>", unsafe_allow_html=True)
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.write("#### Customer Distribution by Region")
        fig_region = px.pie(data, names='region', values='sales_amount', title="Customer Segmentation by Region")
        st.plotly_chart(fig_region)
    else:
        st.warning("The data must contain 'region' and 'sales_amount' columns for customer segmentation.")

    # 3.3 Product Analysis
    st.markdown("<div class='sub-header'>📦 Product Analysis</div>", unsafe_allow_html=True)
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.write("#### Top 10 Products by Sales")
        top_products_df = data.groupby('product').sum('sales_amount').nlargest(10, 'sales_amount')
        fig_product = px.bar(top_products_df, x=top_products_df.index, y='sales_amount', title="Top Products by Sales")
        st.plotly_chart(fig_product)
    else:
        st.warning("The data must contain 'product' and 'sales_amount' columns for product analysis.")

    # 3.4 Feedback Section
    st.markdown("<div class='sub-header'>💬 Feedback</div>", unsafe_allow_html=True)
    feedback = st.text_area("Please share your feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# 4.0 Footer
st.write("---")
st.markdown("<div class='important-text'>This dashboard template is adaptable. Feel free to modify it to suit your business needs.</div>", unsafe_allow_html=True)

# Entry Point
if __name__ == "__main__":
    pass
