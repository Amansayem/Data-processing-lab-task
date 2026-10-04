name = input("Enter passenger name: ")
destination = input("Enter flight destination (Dubai/Malaysia/Singapore/London/Thailand): ")
email = input("Enter email address: ")
ptype = input("Enter passenger type (Adult/Child/Student/Senior): ")
tickets = int(input("Enter number of tickets: "))

# Convert input into lowercase for comparison
dest = destination.strip().lower()
pt = ptype.strip().lower()

# Destination fares
if dest == "dubai":
    fare = 45000
    dest_name = "Dubai"
elif dest == "malaysia":
    fare = 32000
    dest_name = "Malaysia"
elif dest == "singapore":
    fare = 38000
    dest_name = "Singapore"
elif dest == "london":
    fare = 85000
    dest_name = "London"
elif dest == "thailand":
    fare = 28000
    dest_name = "Thailand"
else:
    fare = 0
    dest_name = destination
    print("Invalid destination entered.")

# Passenger type discounts
if pt == "adult":
    discount = 0
    type_name = "Adult"
elif pt == "child":
    discount = 50
    type_name = "Child"
elif pt == "student":
    discount = 40
    type_name = "Student"
elif pt == "senior":
    discount = 30
    type_name = "Senior"
else:
    discount = 0
    type_name = ptype
    print("Invalid passenger type entered.")

# Calculate total fare
total_fare = fare * tickets
total_fare = total_fare - (total_fare * discount) / 100

# Print ticket info
print("\nAIRLINE FLIGHT TICKET")
print("Passenger Name:", name)
print("Email Address:", email)
print("Destination:", dest_name)
print("Passenger Type:", type_name)
print("Tickets:", tickets)
print("Discount:", discount, "%")
print("Total Fare:", total_fare)
