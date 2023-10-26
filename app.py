import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import webbrowser

st.set_page_config(
    page_title='Scholarspot',
    page_icon="None",
    layout='centered',
    initial_sidebar_state='auto',
)

st.title("Welcome To Scholar's Spot ")

data = pd.read_csv('schs.csv')

EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Scholarships", "Study Center", "Profile", "About"],  # required
                icons=["house", "book", "envelope", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Scholarships", "Study Center", "Profile", "About"],  # required
            icons=["house", "book", "envelope", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Scholarships", "Study Center", "Profile", "About"],  # required
            icons=["house", "book", "envelope", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

# Your existing UI code goes here...

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
 
background-image: url("https://i.pinimg.com/564x/68/42/95/684295d68a6bcb557e06d7b32636a32c.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
background-color: transparent;
}

[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}

div[role="combobox"] {
background-color: transparent;
}

div[role="listbox"] {
background-color: transparent;
}

div[role="option"] {
background-color: transparent;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Rest of your Streamlit app code
caste = st.multiselect(
    'Select Your Category:',
    options=data['Category'].unique(),
    default=None
)
qualify = st.multiselect(
    'Select your Qualification:',
    options=data["Qualification"].unique(),
    default=None
)
income = st.multiselect(
    'Select Your Income:',
    options=data["Income"].unique(),
    default=None
)
type = st.multiselect(
    'Select Your type: ',
    options=data["Type"].unique(),
    default=None 
)
state = st.multiselect(
    'Select Your State: ',
    options=data["State"].unique(),
    default=None 
)
# data_selection = data.query("Category == @caste & Qualification == @qualify  & Income == @income & Type==@type & State==@state")
data_selection = data[
    data['Category'].isin(caste) &
    data['Qualification'].isin(qualify) &
    data['Income'].isin(income) &
    data['Type'].isin(type) &
    data['State'].isin(state)
]


if st.button("Recommend"):
    for _, row in data_selection.iterrows():
        scholarship_html = f"""
        <div style="border: 4px solid #ccc; padding: 10px; margin: 10px; background-color: #000000;">
            <h3>{row['Name']}</h3>
            <p><strong>Description:</strong> {row['Description']}</p>
            <p><strong>Category:</strong> {row['Category']}</p>
            <p><strong>Qualification:</strong> {row['Qualification']}</p>
            <p><strong>Income:</strong> {row['Income']}</p>
            <p><strong>Type:</strong> {row['Type']}</p>
            <p><strong>State:</strong> {row['State']}</p>
            <a href="{row['LINKS']}" target="_blank">Apply Here</a>
        </div>
        """
        st.markdown(scholarship_html, unsafe_allow_html=True)


url = 'http://192.168.182.83:5500/index%20(1).html'
if st.button("Back to Home Page"):
    webbrowser.open_new_tab(url)

st.title("Feedback Section")

# Get scholarship ID for feedback
selected_scholarship_id = st.text_input("Enter Scholarship ID for Feedback:")

# Get user's query related to the scholarship
feedback_query = st.text_area("Enter Your Query/Feedback:")

# Get user's star rating for the scholarship (1 to 5 stars)
feedback_rating = st.slider("Rate the Scholarship (1 to 5 stars)", 1, 5, 3)

if st.button("Submit Feedback"):
    # Process the feedback (you can store it in a database or file)
    feedback_data = {
        "Scholarship ID": selected_scholarship_id,
        "Query/Feedback": feedback_query,
        "Rating": feedback_rating
    }

    st.success("Feedback submitted successfully!")
    # Reset input fields
    selected_scholarship_id = ""
    feedback_query = ""
    feedback_rating = 3 

st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.markdown("© 2023 Scholarspot. All rights reserved. Powered by Scholarspot.")
st.markdown('</div>', unsafe_allow_html=True)
