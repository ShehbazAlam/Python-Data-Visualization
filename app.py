import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Survey Data Visualization: Screen Time and Effects")
# Load the survey data
file_path = 'Data/survey.csv'  # Adjust the path as necessary
survey_data = pd.read_csv(file_path)

# Drop unnecessary columns
survey_data = survey_data.drop(columns=[col for col in survey_data.columns if "Unnamed" in col])

# Streamlit app
def main():
    st.title("Survey Data Visualization: Screen Time and Effects")

    # Display raw data
    st.header("Raw Survey Data")
    st.dataframe(survey_data)

    # Gender distribution
    st.subheader("Gender Distribution")
    gender_counts = survey_data["What is your gender?"].value_counts()
    gender_fig = px.pie(
        values=gender_counts.values,
        names=gender_counts.index,
        title="Gender Distribution",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(gender_fig)

    # Age distribution
    st.subheader("Age Distribution")
    age_fig = px.histogram(
        survey_data,
        x="What is your age?",
        nbins=10,
        title="Age Distribution",
        color_discrete_sequence=["#636EFA"]
    )
    st.plotly_chart(age_fig)

    # Level of study
    st.subheader("Level of Study")
    level_counts = survey_data["What is your current level of study?"].value_counts()
    level_fig = px.bar(
        level_counts,
        x=level_counts.index,
        y=level_counts.values,
        title="Level of Study",
        labels={"x": "Level of Study", "y": "Count"},
        color_discrete_sequence=["#FFA15A"]
    )
    st.plotly_chart(level_fig)

    # Field of study
    st.subheader("Field of Study")
    field_counts = survey_data["What is your field of study?"].value_counts()
    field_fig = px.bar(
        field_counts,
        x=field_counts.index,
        y=field_counts.values,
        title="Field of Study",
        labels={"x": "Field of Study", "y": "Count"},
        color_discrete_sequence=["#19D3F3"]
    )
    st.plotly_chart(field_fig)

    # Screen time
    st.subheader("Screen Time Per Day")
    screen_time_counts = survey_data["How many hours do you spend on screens (phones, tablets, laptops, TVs) per day?"].value_counts()
    screen_time_fig = px.bar(
        screen_time_counts,
        x=screen_time_counts.index,
        y=screen_time_counts.values,
        title="Screen Time Per Day",
        labels={"x": "Hours", "y": "Count"},
        color_discrete_sequence=["#EF553B"]
    )
    st.plotly_chart(screen_time_fig)

    # Activities on screens
    st.subheader("Activities on Screens")
    activities = survey_data["What activities do you usually do on screens? (Select all that apply)"].dropna()
    activities_split = activities.str.split(',').explode()
    activities_counts = activities_split.value_counts()
    activities_fig = px.bar(
        activities_counts,
        x=activities_counts.index,
        y=activities_counts.values,
        title="Activities on Screens",
        labels={"x": "Activity", "y": "Count"},
        color_discrete_sequence=["#00CC96"]
    )
    st.plotly_chart(activities_fig)

    # Effects on academic performance
    st.subheader("Effects on Academic Performance")
    effects_counts = survey_data["Do you think your screen time affects your academic performance?"].value_counts()
    effects_fig = px.pie(
        values=effects_counts.values,
        names=effects_counts.index,
        title="Effects on Academic Performance",
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    st.plotly_chart(effects_fig)

    # Distraction frequency
    st.subheader("Frequency of Distractions")
    distraction_counts = survey_data["How often do you get distracted by screens while studying?"].value_counts()
    distraction_fig = px.bar(
        distraction_counts,
        x=distraction_counts.index,
        y=distraction_counts.values,
        title="Frequency of Distractions",
        labels={"x": "Frequency", "y": "Count"},
        color_discrete_sequence=["#AB63FA"]
    )
    st.plotly_chart(distraction_fig)

if __name__ == "__main__":
    main()
