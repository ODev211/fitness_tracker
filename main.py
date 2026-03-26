class WorkoutSession:
    def __init__(self, exercise, duration, distance):
        self.exercise = exercise
        self.duration = duration
        self.distance = distance


class FitnessManager:
    def __init__(self):
        self.history = []

    @staticmethod
    def validate_data(duration, distance):
        try:
            return float(duration) > 0 and float(distance) >= 0
        except ValueError:
            return False

    def log_workout(self, exercise, duration, distance):
        if self.validate_data(duration, distance):
            new_session = WorkoutSession(exercise, float(duration), float(distance))
            self.history.append(new_session)
            return True
        return False

    def view_history(self):
        if not self.history:
            print("\nNo workouts logged yet!")
            return

        print("\n--- Workout History ---")
        for i, workout in enumerate(self.history, 1):
            print(f"{i}. {workout.exercise}: {workout.duration} mins, {workout.distance} meters")

    def get_summary(self):
        total_dist = sum(item.distance for item in self.history)
        total_time = sum(item.duration for item in self.history)
        return f"\nSummary: {len(self.history)} workouts, {total_time} mins total, {total_dist}m total."

    def analytics(self):
        if not self.history:
            return "No data for analytics."
        avg_dist = sum(item.distance for item in self.history) / len(self.history)
        return f"Average distance per workout: {avg_dist:.2f}m"


class TUI:
    def __init__(self, admin):
        self.manager = admin

    @staticmethod
    def get_valid_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            print("Invalid input. Please enter a number.")

    def run(self):
        while True:  # Keep the app running until exit
            print("\n--- FitnessX Tracker ---")
            print("1. Log a new workout")
            print("2. View your workout history")
            print("3. View summary")
            print("4. View analytics")
            print("5. Exit")

            user_choice = self.get_valid_input("Enter choice: ")

            if user_choice == 1:
                ex = input("Exercise name: ")
                dur = input("Duration (mins): ")
                dist = input("Distance (m): ")
                if self.manager.log_workout(ex, dur, dist):
                    print("Workout logged successfully!")
                else:
                    print("Error: Invalid duration or distance.")

            elif user_choice == 2:
                self.manager.view_history()

            elif user_choice == 3:
                print(self.manager.get_summary())

            elif user_choice == 4:
                print(self.manager.analytics())

            elif user_choice == 5:
                print("Exiting... Stay active!")
                break
            else:
                print("Not a valid option.")


if __name__ == "__main__":
    # In Waterfall, we instantiate our 'Units' here
    manager = FitnessManager()
    app = TUI(manager)
    app.run()