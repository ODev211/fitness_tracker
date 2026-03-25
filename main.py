# This is the main file where the fitness tracker will be run - Waterfall development approach

# Class for exercise
class FitnessTracker:
    def __init__(self):
        self.analytics = []
        self.summary = []
        self.user_interface = []
        self.validate_data = []
        self.log_workout = []
        self.view_history = []

# Class for the main functions
class Workouts:
    def __init__(self):
        self.history = []

    # Log workouts function
    def log_workout(self, exercise, duration, distance):
        pass


    # View workout history function
    def view_history(self):
        pass


    # Weekly / Monthly summary function
    def summary(self):
        pass


    # Basic analytics function
    def analytics(self):
        pass


    # Data validation function
    def validate_data(self):
        pass


    # Main user interface function
    def user_interface(self):
        # Layout of the tui
        print("Welcome to FitnessX Tracker - Specialised in tracking your workouts!")
        print("Please select an option:")
        print("1. Log a new workout")
        print("2. View your workout history")
        print("3. View your weekly/monthly summary")
        print("4. View your basic analytics")
        print("5. Exit")

        # Logic for handling user input and error handling
        user_input = input("Enter your choice: ")

        while user_input != int(user_input):
            print("Invalid input. Please enter a number.")
            user_input = input("Enter your choice: ")

        # User input after validation
        user_choice = int(user_input)
        if user_choice == 1:
            print("Logging a new workout...")
        elif user_choice == 2:
            print("Viewing your workout history...")
        elif user_choice == 3:
            print("Viewing your weekly/monthly summary...")
        elif user_choice == 4:
            print("Viewing your basic analytics...")
        elif user_choice == 5:
            print("Exiting the application...")
        else:
            print("Not a valid option. Please try again.")



# Project startup
if __name__ == "__main__":
    # 1. Create the Manager
    my_app = FitnessTracker()

    # 2. The Manager creates and stores a Workout object
    my_app.log_workout("Swimming", 45, 300)

    # 3. Inside view_history(), the Manager does this:
    for item in my_app.view_history:
        # 'item' is a Workout object. We access its attributes directly:
        print(f"Activity: {item.exercise}")