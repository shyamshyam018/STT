import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def main():
    st.title("Hello, World! EDA Streamlit App")

    # Sidebar navigation
    st.sidebar.header("Navigation")
    navigation_options = ["Upload CSV", "Data Overview"]
    selected_navigation = st.sidebar.selectbox("Select an option", navigation_options)

    if selected_navigation == "Upload CSV":
        st.header("Upload CSV Data")
        data_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

        if data_file is not None:
            data = pd.read_csv(data_file)
            st.sidebar.success("File uploaded successfully!")

    elif selected_navigation == "Data Overview":
        st.header("Data Overview")
        data = None
        st.write("Please upload a CSV file.")

    # Chatbot interface
    st.header("Chatbot Interface")
    user_input = st.text_input("You: ")

    if user_input.lower() in ['hi', 'hello']:
        st.write("Chatbot: Welcome!")

    if selected_navigation == "Data Overview" and data is not None:
        st.write("Chatbot: Here is the data overview:")
        st.write(data.head())

    # Visualization selection
    st.write("Chatbot: Now, let's select a type of visualization.")

    # Ask for the type of visualization
    st.write("Chatbot: Which type of visualization would you like? (Options: Bar plot, Scatter plot, Histogram, Box plot, Pie chart)")
    selected_plot = st.text_input("You: ")

    if selected_plot.lower() in ["bar plot", "scatter plot", "histogram", "box plot", "pie chart"]:
        st.write(f"Chatbot: You chose {selected_plot.capitalize()}.")

    if selected_plot.lower() == "bar plot":
        # Ask for x-axis column
        st.write("Chatbot: Please enter the x-axis column:")
        x_axis = st.text_input("You: ")

        # Ask for y-axis column
        st.write("Chatbot: Please enter the y-axis column:")
        y_axis = st.text_input("You: ")

        st.write("Chatbot: Bar plot will be generated.")

    elif selected_plot.lower() == "scatter plot":
        # Ask for x-axis column
        st.write("Chatbot: Please enter the x-axis column:")
        x_axis = st.text_input("You: ")

        # Ask for y-axis column
        st.write("Chatbot: Please enter the y-axis column:")
        y_axis = st.text_input("You: ")

        st.write("Chatbot: Scatter plot will be generated.")

    elif selected_plot.lower() == "histogram":
        # Ask for column for the histogram
        st.write("Chatbot: Please enter the column for the histogram:")
        column = st.text_input("You: ")

        st.write("Chatbot: Histogram will be generated.")

    elif selected_plot.lower() == "box plot":
        # Ask for column for the box plot
        st.write("Chatbot: Please enter the column for the box plot:")
        column = st.text_input("You: ")

        st.write("Chatbot: Box plot will be generated.")

    elif selected_plot.lower() == "pie chart":
        # Ask for column for the pie chart
        st.write("Chatbot: Please enter the column for the pie chart:")
        column = st.text_input("You: ")

        st.write("Chatbot: Pie chart will be generated.")

    # Generate Visualization button
    generate_button = st.button("Generate Visualization")

    if generate_button:
        if selected_plot.lower() == "bar plot":
            fig, ax = plt.subplots()
            sns.barplot(x=data[x_axis], y=data[y_axis], ax=ax)
            ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=10))
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

        elif selected_plot.lower() == "scatter plot":
            fig, ax = plt.subplots()
            sns.scatterplot(x=data[x_axis], y=data[y_axis], ax=ax)
