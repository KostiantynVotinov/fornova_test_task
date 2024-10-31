# Test Task: Hotel Room Price Analysis

### Overview

This script was developed as a test task to analyze and process hotel room pricing data. The primary objective was to load a JSON file with room price information, identify the cheapest room, calculate total prices (net price + taxes) for each room type, and display the results in a clear format. Additionally, the results are saved to a separate JSON file for further use.

### Task Execution Details

1. **Data Loading**: The script reads data from the input file `Python-task.json`, which includes information on room types, their prices, the number of guests, and applicable taxes.
2. **Data Analysis and Processing**:
   - The script identifies the cheapest room by iterating through the dictionary of prices without using the `min` function.
   - Taxes are summed, and the total price for each room (net price + taxes) is calculated accordingly.
3. **Results Display and Saving**:
   - The results are output in a readable format and also saved to `outgoing file/room_prices_output.json` for potential reuse.

### Sample Output

Upon running the script, the following output is displayed:

=== Cheapest Room Information ===

Room Type: King Studio Suite - Non Smoking
Number of Guests: 4
Cheapest Price: $90.00

=== Total Prices for All Room Types (Net + Taxes) ===

Room Type: King Studio Suite - Hearing Accessible/Non-Smoking - Total Price: $131.76
Room Type: King Studio Suite - Non Smoking - Total Price: $108.71
Room Type: King Room - Mobility/Hearing Accessible - Non-Smoking - Total Price: $133.76
Room Type: Queen Suite with Two Queen Beds - Non-Smoking - Total Price: $130.76

Results have also been saved to 'outgoing file/room_prices_output.json'

