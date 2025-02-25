import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.header("Bengali Audio Story Dictionary")

st.write(''''বাংলা সাহিত্য হলো বাংলা ভাষায় রচিত সাহিত্য, যা যুগের পর যুগ বিভিন্ন আঙ্গিকে বিকশিত হয়েছে। 
এই সাহিত্যের শেকড় অনেক গভীরে চলে যায়, প্রাচীন কাব্যকাব্যিক রচনা থেকে শুরু করে আধুনিক সময়ের প্রবন্ধ, 
গল্প, কবিতা, নাটক, উপন্যাস ও অন্যান্য নানা ধরনের সাহিত্যের শাখা। বাংলা সাহিত্যের ইতিহাসে অসংখ্য গুণী সাহিত্যিক জন্মেছেন,
 যাদের রচনা বাংলা ভাষা ও সংস্কৃতির অমূল্য রত্ন।''')

st.image('ba1.jpg', caption='This site is created by Somnath Banerjee', use_container_width=True)

# Link to other project
st.write('''My other project link: https://movieexplorationsuggestion-somnath.streamlit.app/''')
st.write('''My Other Projects : Retail Techstore Sales Analysis 
(Please Go through the link) : https://salesanalytics-somnath-techstore.streamlit.app/''')

# First Excel file URL (ssgm.xlsx)
ssgm_url = "https://raw.githubusercontent.com/SomnathBanerjee342000new/MyDatabase/main/ssgm.xlsx"

try:
    # Request the file from GitHub
    response_ssgm = requests.get(ssgm_url)

    if response_ssgm.status_code == 200:
        st.success("File loaded successfully from GitHub")

        # Load the Excel file into a pandas DataFrame
        df_ssgm = pd.read_excel(BytesIO(response_ssgm.content), engine='openpyxl')

        # Create columns for the layout to display filters in the middle
        col1, col2, col3 = st.columns([1, 2, 1])  # 2 is the middle column width

        with col2:
            st.header("🔍Find your story")
            
            # Create filters
            selected_Channel = st.selectbox("Select YouTube Channel Name", ["All"] + df_ssgm["Tou_Tube_Channel"].unique().tolist())
            if selected_Channel != "All":
                df_filtered = df_ssgm[df_ssgm["Tou_Tube_Channel"] == selected_Channel]
            else:
                df_filtered = df_ssgm

            selected_Group = st.selectbox("Select Group", ["All"] + df_filtered["Group"].unique().tolist())
            if selected_Group != "All":
                df_filtered = df_filtered[df_filtered["Group"] == selected_Group]
            
            selected_Series = st.selectbox("Select Series", ["All"] + df_filtered["Series"].unique().tolist())
            if selected_Series != "All":
                df_filtered = df_filtered[df_filtered["Series"] == selected_Series]

            selected_Episode = st.selectbox("Select Episode", ["All"] + df_filtered["Episode"].unique().tolist())
            if selected_Episode != "All":
                df_filtered = df_filtered[df_filtered["Episode"] == selected_Episode]

        # Display the "Link" column as clickable URLs if it exists
        if 'Link' in df_filtered.columns:
            df_filtered['Link'] = df_filtered['Link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

        # Data Overview: Render HTML table with clickable links
        st.subheader("📌 Your Sunday Suspense & Goppo Mir er Thek Dictionary")
        st.markdown(df_filtered.head(12).to_html(escape=False), unsafe_allow_html=True)

    else:
        st.error(f"Failed to retrieve file. HTTP Status code: {response_ssgm.status_code}")

except Exception as e:
    st.error(f"An error occurred while processing the first file: {e}")

st.image('ba2.jpg', caption='Sunday Suspense', use_container_width=True)

# Second Excel file URL (BengaliStory.xlsx)
bengali_story_url = "https://raw.githubusercontent.com/SomnathBanerjee342000new/MyDatabase/main/BengaliStory.xlsx"

try:
    # Request the file from GitHub
    response_bengali_story = requests.get(bengali_story_url)

    if response_bengali_story.status_code == 200:
        st.success("File loaded successfully from GitHub (BengaliStory.xlsx)!")

        # Load the Excel file into a pandas DataFrame
        df_bengali_story = pd.read_excel(BytesIO(response_bengali_story.content), engine='openpyxl')

        # Check if 'Link of playlist' and 'You Tube' columns exist
        if 'Link of playlist' in df_bengali_story.columns and 'You Tube' in df_bengali_story.columns:
            df_bengali_story['Link of playlist'] = df_bengali_story['Link of playlist'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
            df_bengali_story['You Tube'] = df_bengali_story['You Tube'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

        # Display the DataFrame with clickable links
        st.subheader("📌 Bengali Audio Story Channels")

        # Add custom CSS to control the column width and enable text wrapping
        st.markdown("""
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 8px 12px;
                text-align: left;
                word-wrap: break-word; /* Allow text to wrap within the cell */
            }
            th {
                background-color: #f2f2f3;
            }
            td {
                max-width: 250px; /* Adjust the maximum width if necessary */
                overflow: hidden;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(df_bengali_story.to_html(escape=False), unsafe_allow_html=True)

    else:
        st.error(f"Failed to retrieve the file. HTTP Status code: {response_bengali_story.status_code}")

except Exception as e:
    st.error(f"An error occurred while processing the second file: {e}")


st.write(''''আজকের বাংলা সাহিত্যও অনেক বিচিত্র। কবিতা, গল্প, উপন্যাস, নাটক, প্রবন্ধ ইত্যাদির নানা অঙ্গনে বহু 
প্রতিভাবান লেখক কাজ করছেন। ডিজিটাল যুগে বাংলা সাহিত্যে অনলাইন মাধ্যমে লেখালেখি বৃদ্ধি পেয়েছে, 
যেখান থেকে তরুণ প্রজন্ম তাদের সৃষ্টিশীলতা প্রকাশ করছে।
বাংলা সাহিত্যের ঐতিহ্য প্রতিদিন নতুন দিগন্ত উন্মোচন করছে, যেখানে পুরানো এবং নতুন ধারার একসাথে বিকাশ ঘটছে।''')

st.write('''This site is created by Somnath Banerjee. Mail: somnathbanerjee342000@gmail.com''')

st.image('ba3.jpg', caption='Goppo Mir er thek', use_container_width=True)
