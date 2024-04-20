import datetime

class SchedulerConsoleInterface:
    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.available_slots = self.generate_time_slots()
        self.selected_slot = None  # Manage selected slot internally

    def generate_time_slots(self):
        slots = []
        base_time = datetime.datetime.now().replace(hour=9, minute=30, second=0, microsecond=0)
        for i in range(5):  # Generate 5 time slots
            time = base_time + datetime.timedelta(hours=3 * i)
            slots.append(time.strftime("%d/%m/%Y, %a at %I:%M %p"))
        return slots

    def run(self):
        while True:
            self.reset_scheduler()
            response = self.get_valid_response("Welcome to the HealthCare Scheduler. Are you looking to schedule an influenza vaccination? (Yes/No): ")
            if response.lower() == 'no':
                print("Thank you for using the HealthCare Scheduler. Goodbye!")
                break

            self.scheduler.start_conversation(response=response)

            if self.scheduler.state == 'collecting_name':
                self.get_name()

            if self.scheduler.state == 'checking_age':
                age = self.get_valid_age()
                if age < 18:
                    print("Sorry, we can only schedule appointments for individuals 18 and older.")
                    continue  # This restarts the whole process for underage users
                self.scheduler.input_age(age=age)  # Proceed to next state only if age is suitable

            if self.scheduler.state == 'selecting_time':
                if not self.handle_time_slot_selection():
                    continue  # Restart the process if slot selection fails

            if self.scheduler.state == 'confirmation':
                if not self.confirm_appointment():
                    break  # End the loop if no other service is needed

    def reset_scheduler(self):
        self.scheduler.state = 'start'

    def get_name(self):
        while True:
            name = input("Great! Can I have your name, please?: ").strip()
            if not name:  # If name is empty after stripping whitespace
                print("Name can't be blank.")
                continue
            self.scheduler.input_name(name=name)
            break

    def get_valid_response(self, message):
        while True:
            response = input(message)
            if response.lower() in ['yes', 'no']:
                return response
            print("Please enter 'Yes' or 'No'.")

    def get_valid_age(self):
        while True:
            try:
                age = int(input("Thanks! Are you above 18 years old? (Enter age): "))
                return age
            except ValueError:
                print("Invalid age. Please enter a valid number.")

    def handle_time_slot_selection(self):
        print("Here are the available slots:")
        for index, slot in enumerate(self.available_slots, start=1):
            print(f"{index}. {slot}")
        slot_index = self.get_valid_slot_number()
        if slot_index:
            selected_slot = self.available_slots[slot_index - 1]
            self.scheduler.select_time(slot=selected_slot)
            self.selected_slot = selected_slot
            return True
        return False

    def get_valid_slot_number(self):
        for attempt in range(2):
            try:
                slot_index = int(input("Which one do you prefer? (Enter the number): "))
                if 1 <= slot_index <= len(self.available_slots):
                    return slot_index
                print("Invalid option, please select a number from the list.")
            except ValueError:
                print("Please enter a valid number.")
        print("Invalid input received twice. Restarting the process.")
        return None

    def confirm_appointment(self):
        confirm = input(f"Your appointment is scheduled {self.selected_slot}. Do you need another service? (Yes/No): ")
        return confirm.lower() != 'no'
