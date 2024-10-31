import json  # Import JSON module to work with JSON data

# Path to the input file containing the data
input_file_path = "incoming_file/Python-task.json"

# Load data from JSON file
with open(input_file_path, "r") as file:
    data = json.load(file)

# Extract necessary sections from the loaded JSON data
rooms = data['assignment_results'][0]['shown_price']  # Shown prices for each room type
net_prices = data['assignment_results'][0]['net_price']  # Net prices (base price without taxes) for each room
taxes_json = data['assignment_results'][0]['ext_data']['taxes']  # Taxes data as a JSON string

# Parse the tax data and calculate total taxes
taxes = json.loads(taxes_json)  # Convert JSON string to dictionary
total_taxes = sum(float(value) for value in taxes.values())  # Sum all tax values as floats

# Find the cheapest room without using the min function
cheapest_price = float("inf")  # Initialize with an infinitely high price
cheapest_room = None  # To store the room type with the lowest price

for room_type, price in rooms.items():
    room_price = float(price)  # Convert price to float for comparison
    if room_price < cheapest_price:  # Check if this price is the lowest so far
        cheapest_price = room_price  # Update the lowest price
        cheapest_room = room_type  # Update the room type with the lowest price

# Calculate total price (net price + taxes) for each room type
room_totals = {room_type: float(net_price) + total_taxes for room_type, net_price in net_prices.items()}

# Format the result into a dictionary
output = {
    "cheapest_room": cheapest_room,  # Name of the cheapest room type
    "number_of_guests": data['assignment_results'][0]['number_of_guests'],  # Number of guests for the booking
    "cheapest_price": cheapest_price,  # Price of the cheapest room
    "room_totals": room_totals  # Total prices for all rooms with taxes included
}

# Path to the output file in the "outgoing file" folder
output_file_path = "outgoing file/room_prices_output.json"

# Save the output data to a JSON file
with open(output_file_path, "w") as file:
    json.dump(output, file, indent=4)  # Save data with indentation for readability

print(f"Results have been saved to {output_file_path}")  # Print confirmation message
