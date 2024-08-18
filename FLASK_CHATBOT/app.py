from flask import Flask, request, render_template
import random
import json

app = Flask(__name__)

# Load responses from JSON file
def load_responses():
    with open('responses.json', 'r') as file:
        return json.load(file)

responses = load_responses()

def get_response(user_input):
    user_input = user_input.lower()
    print(f"User input: {user_input}")  # Debugging line
    for key in responses:
        if key in user_input:
            response = random.choice(responses[key])
            print(f"Matched response: {response}")  # Debugging line
            return response
    default_response = random.choice(responses["default"])
    print(f"Default response: {default_response}")  # Debugging line
    return default_response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["message"]
        bot_response = get_response(user_input)
        return render_template("index.html", user_message=user_input, bot_message=bot_response)
    return render_template("index.html", user_message=None, bot_message=None)

if __name__ == "__main__":
    app.run(debug=True)
