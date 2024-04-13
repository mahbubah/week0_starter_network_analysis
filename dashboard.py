import streamlit as st
import pandas as pd

# Load data from CSV file
@st.cache
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Main function to create the dashboard
def main():
    st.title("Article Dashboard")

    # Load data
    data_file = "data/rating.csv"
    data = load_data(data_file)

    # Display data
    st.write("## Displaying Data")
    st.write(data)

    # Sidebar filters
    st.sidebar.title("Filters")
    category_filter = st.sidebar.selectbox('Filter by Category', data['category'].unique())
    sentiment_filter = st.sidebar.selectbox('Filter by Sentiment', ['All', 'Positive', 'Neutral', 'Negative'])

    # Apply filters
    filtered_data = data[data['category'] == category_filter]
    if sentiment_filter != 'All':
        filtered_data = filtered_data[filtered_data['title_sentiment'] == sentiment_filter]

    # Display filtered data
    st.write("## Filtered Data")
    st.write(filtered_data)

if __name__ == "__main__":
    main()
