tickets = []
ticket_id = 1

while True:
    print("\n=== IT Help Desk ===")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        user = input("User name: ")
        issue = input("Issue description: ")
        priority = input("Priority (Low/Medium/High): ")

        ticket = {
    "id": ticket_id,
    "user": user,
    "issue": issue,
    "priority": priority,
    "status": "Open"
}

        tickets.append(ticket)
        ticket_id += 1

        print("Ticket created successfully!")

    elif choice == "2":
        print("\n--- Tickets ---")

        if len(tickets) == 0:
            print("No tickets found.")

        for ticket in tickets:
            print(
    f"ID: {ticket['id']} | "
    f"User: {ticket['user']} | "
    f"Priority: {ticket['priority']} | "
    f"Status: {ticket['status']}"
)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")