simport os
from datetime import datetime

class Train:
    def __init__(self, train_name, total_seats=100, fare=500):
        self.train_name = train_name
        self.seats = total_seats
        self.booked_seats = 0
        self.fare = fare
        self.ticket_folder = "tickets"
        self.counter_file = "ticket_counter.txt"

        if not os.path.exists(self.ticket_folder):
            os.makedirs(self.ticket_folder)

    def get_next_ticket_number(self):
        count = 1
        if os.path.exists(self.counter_file):
            with open(self.counter_file, "r") as f:
                try:
                    count = int(f.read().strip()) + 1
                except ValueError:
                    count = 1

        with open(self.counter_file, "w") as f:
            f.write(str(count))

        return f"R-{count:02d}"

    def book_ticket(self):
        available_seats = self.seats - self.booked_seats
        if available_seats <= 0:
            print("No seats available!")
            return

        try:
            n = int(input(f"Enter number of tickets (Max {available_seats}): "))
            if n <= 0:
                print("Number of tickets must be positive.")
                return
            if n > available_seats:
                print(f"Only {available_seats} seats are available.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        try:
            date_input = input("Enter Date of Journey (YYYY-MM-DD): ")
            journey_date = datetime.strptime(date_input, "%Y-%m-%d").date()
            if journey_date < datetime.now().date():
                print("Journey date cannot be in the past.")
                return
        except ValueError:
            print("Invalid date format.")
            return

        passengers = []
        total_fare = 0
        full, half, senior, free = 0, 0, 0, 0

        for i in range(1, n + 1):
            print(f"\nEnter details for Passenger {i}:")
            name = input("Name: ").strip()
            try:
                age = int(input("Age: "))
                if age < 0 or age > 100:
                    print("Invalid age.")
                    return
            except ValueError:
                print("Invalid age input.")
                return

            if age < 5:
                fare = 0
                free += 1
            elif age <= 12:
                fare = self.fare * 0.5
                half += 1
            elif age <= 60:
                fare = self.fare
                full += 1
            else:
                fare = self.fare * 0.25
                senior += 1

            passengers.append((name, age, fare))
            total_fare += fare

        paid = 0
        while paid < total_fare:
            try:
                remaining = total_fare - paid
                amt = int(input(f"Enter amount (₹{remaining:.2f} remaining): ₹"))
                if amt <= 0:
                    print("Enter a valid amount.")
                    continue
                paid += amt
            except ValueError:
                print("Invalid input.")

        self.booked_seats += n
        now = datetime.now()
        ticket_no = self.get_next_ticket_number()
        ticket_file_path = os.path.join(self.ticket_folder, f"{ticket_no}.txt")

        print("\n--------------------------------------------------------------")
        print(f"{'Happy Journey':^62}")
        print("--------------------------------------------------------------")
        print(f"Train Name: {self.train_name:<35} Ticket No: {ticket_no}")
        print(f"Date: {now.date()}                                     Time: {now.strftime('%H:%M:%S')}\n")
        print("--------------------------------------------------------------")
        for idx, (name, age, fare) in enumerate(passengers, 1):
            print(f"Passenger {idx}")
            print(f"   Name: {name:<35} Age: {age}")
        print("--------------------------------------------------------------")
        print(f"\nTotal Paid Amount: ₹{total_fare:.2f}")

        if half > 0 or senior > 0 or free > 0:
            print("\nAge-based discount applied where eligible.")
        print("--------------------------------------------------------------")

        with open(ticket_file_path, "w", encoding="utf-8") as f:
            f.write("--------------------------------------------------------------\n")
            f.write(f"{'Happy Journey':^62}\n")
            f.write("\n--------------------------------------------------------------\n")
            f.write(f"Train Name: {self.train_name:<35} Ticket No: {ticket_no}\n")
            f.write(f"Date: {now.date()}                                     Time: {now.strftime('%H:%M:%S')}\n\n")
            f.write("--------------------------------------------------------------\n")
            for idx, (name, age, fare) in enumerate(passengers, 1):
                f.write(f"Passenger {idx}\n")
                f.write(f"   Name: {name:<35} Age: {age}\n")
            f.write("--------------------------------------------------------------\n")
            f.write(f"\nTotal Paid Amount: ₹{total_fare:.2f}\n")
            if half > 0 or senior > 0 or free > 0:
                f.write("\nAge-based discount applied where eligible.\n")
            f.write("--------------------------------------------------------------\n")

    def get_status(self):
        print(f"Available Seats: {self.seats - self.booked_seats}/{self.seats}")

    def get_fare(self):
        try:
            n = int(input("Enter number of tickets: "))
            if n <= 0:
                print("Tickets must be positive.")
                return
            print(f"Total Fare: ₹{n * self.fare}")
        except ValueError:
            print("Invalid input.")

    def pnr_status(self):
        ticket_no = input("Enter Ticket Number (e.g., R-01): ").strip().upper()
        ticket_file_path = os.path.join(self.ticket_folder, f"{ticket_no}.txt")

        if os.path.exists(ticket_file_path):
            print("\nTicket Found:")
            print("--------------------------------------------------------------")
            with open(ticket_file_path, "r", encoding="utf-8") as f:
                print(f.read())
            print("--------------------------------------------------------------")
        else:
            print("Ticket not found. Please check the ticket number.")

train = Train("Rajdhani Express")

while True:
    print(f"\nWelcome to {train.train_name} Ticketing System")
    print("1. Book Ticket\n2. Get Status\n3. Get Fare Info\n4. PNR Status\n0. Exit")
    ch = input("Enter your choice: ").strip()

    if ch == "1":
        train.book_ticket()
    elif ch == "2":
        train.get_status()
    elif ch == "3":
        train.get_fare()
    elif ch == "4":
        train.pnr_status()
    elif ch == "0":
        print("Thank you for using the Train Booking System. Goodbye!")
        break
    else:
        print("Invalid input.")
