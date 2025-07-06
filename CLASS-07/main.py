import datetime

class Habit:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty  # "easy", "medium", "hard"
        self.is_completed_today = False

    def mark_complete(self):
        self.is_completed_today = True

    def reset_daily(self):
        self.is_completed_today = False


class User:
    def __init__(self, username):
        self.username = username
        self.level = 1
        self.exp_points = 0
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def complete_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name and not habit.is_completed_today:
                habit.mark_complete()
                points = self.get_exp_points(habit.difficulty)
                self.exp_points += points
                print(f"You gained {points} experience points 🎉!")
                self.check_level_up()
                return
        print("Habit already completed or not found.")

    def get_exp_points(self, difficulty):
        return {"easy": 5, "medium": 10, "hard": 15}.get(difficulty, 5)

    def check_level_up(self):
        if self.exp_points >= self.level * 50:
            self.level += 1
            self.exp_points = 0
            print(f"🎉 Level Up! You are now Level {self.level}!")

    def show_status(self):
        print(f"\nUser: {self.username}")
        print(f"Level: {self.level}")
        print(f"XP: {self.exp_points}")
        print("Today's Habits:")
        for habit in self.habits:
            status = "✔️" if habit.is_completed_today else "❌"
            print(f"- {habit.name} ({habit.difficulty}) {status}")
        print()


def daily_reset(user):
    for habit in user.habits:
        habit.reset_daily()


# ---- MAIN APP ----
def main():
    print("🌟 Welcome to Habit Hero 🌟")
    username = input("Enter your username: ")
    user = User(username)

    while True:
        print("\n--- Menu ---")
        print("1. Add Habit")
        print("2. Complete Habit")
        print("3. Show Status")
        print("4. Reset Day (new day)")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter habit name: ")
            difficulty = input("Difficulty (easy/medium/hard): ").lower()
            habit = Habit(name, difficulty)
            user.add_habit(habit)
            print("Habit added.")

        elif choice == '2':
            name = input("Enter habit to complete: ")
            user.complete_habit(name)

        elif choice == '3':
            user.show_status()

        elif choice == '4':
            daily_reset(user)
            print("Habits reset for a new day!")

        elif choice == '5':
            print("Goodbye! Keep leveling up! 🚀")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
