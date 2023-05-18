import requests
from flask import Flask, render_template, request, redirect, session,jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'your_secret_key'
food_intake = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        food = request.form['food']
        quantity = request.form['quantity']
        saturated_fat = get_saturated_fat(food)
        food_item = {'food': food, 'quantity': quantity, 'saturated_fat': saturated_fat}
        food_intake.append(food_item)

    total_saturated_fat = sum(int(item['saturated_fat']) for item in food_intake)

    max_saturated_fat = 20  # Set your desired maximum saturated fat value

    return render_template('index.html', food_intake=food_intake, total_saturated_fat=total_saturated_fat, max_saturated_fat=max_saturated_fat)

@app.route('/suggestions/<food>', methods=['GET'])
def get_suggestions(food):
    # Make a request to Open Food Facts API or any other data source
    # Parse the response and extract the suggestions
    # Return a list of suggestions as JSON

    # Example using Open Food Facts API
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food}&search_simple=1&action=process&json=1"
    response = requests.get(url)
    data = response.json()
    suggestions = [product['product_name'] for product in data['products']]
    return jsonify(suggestions)

@app.route('/remove-item', methods=['POST'])
def remove_item():
    index = int(request.form['index'])
    if 'food_intake' in session and 0 <= index < len(session['food_intake']):
        del session['food_intake'][index]
    return redirect('/')


def get_saturated_fat(food):
    # Make a request to Open Food Facts API or any other data source
    # Parse the response and extract the saturated fat information
    # Return the saturated fat value

    # Example using Open Food Facts API
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food}&search_simple=1&action=process&json=1"
    response = requests.get(url)
    data = response.json()
    if data["products"]:
        saturated_fat = data["products"][0]["nutriments"].get("saturated-fat_100g", "Unknown")
        return saturated_fat

    return "Unknown"

def calculate_total_saturated_fat(food_intake):
    total_saturated_fat = 0
    for food_item in food_intake:
        saturated_fat_per_serving = float(food_item['saturated_fat'])
        quantity_num = float(food_item['quantity'])
        total_saturated_fat += saturated_fat_per_serving * quantity_num
    return round(total_saturated_fat, 2)

if __name__ == '__main__':
    app.run(debug=True)
