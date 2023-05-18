# LDL Monitor

LDL Monitor is a Python Flask application that helps you monitor your daily saturated fat intake. It allows you to track the foods you consume and calculates the total saturated fat based on the information retrieved from Open Food Facts.

## Features

- Add food items with quantity to track your daily intake
- Retrieve saturated fat information using Open Food Facts API
- Calculate and display the total saturated fat consumed
- Set a maximum saturated fat limit to track your goals


## Prerequisites

- Python 3.6 or higher
- Flask web framework

## Usage

1. Start the Flask application:
2. Open your web browser and navigate to `http://localhost:5000`.
3. Enter the food item name and quantity in the provided form and click "Add".
4. The table will display the daily food intake along with the saturated fat information for each item.
5. To remove an item, click the "Remove" button next to the item in the table.

## Configuration

- You can modify the maximum saturated fat limit by updating the `max_saturated_fat` variable in the `app.py` file.


