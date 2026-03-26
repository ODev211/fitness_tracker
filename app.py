import streamlit as st
from main import Workouts

workout_app = Workouts()
st.title("Fitness Tracker")

st.write("Welcome to your fitness tracker!")

option = st.sidebar.radio(
    "Select an option:",
    [
        "Log Workout",
        "View History",
        "Summary",
        "Analytics"
    ]
)

# Log a workout - validates input data too.
if option == "Log Workout":
    st.header("Log a New Workout")

    exercise = st.selectbox(
        "Exercise type",
        ['run', 'swimming', 'walk', 'jog']
    )

    duration = st.number_input("Duration")
    distance = st.number_input("Distance")

    if st.button("Submit Workout"):
        if workout_app.validate_data(duration) and workout_app.validate_data(distance):
            workout_app.log_workout(exercise, duration, distance)
            st.success("Workout submitted!")
        else:
            st.error("Invalid Input")


# View workout History
elif option == "View History":
    st.header("Workout History")

    history = workout_app.history

    if history:
        for item in history:
            st.write(f"{item}")
    else:
        st.info("No workouts logged yet!")


# View summary
elif option == "Summary":
    st.header("Summary")

    summary = workout_app.summary()
    st.write(summary if summary else "No data yet.")


# Analytics
elif option == "Analytics":
    st.header("Analytics")

    analytics = workout_app.analytics()
    st.write(analytics if analytics else "No data yet.")