from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meal_suggestions', methods=['POST'])
def get_meal_suggestions():
    # Get the ingredients and cuisine from the form
    ingredients = request.form['ingredients']
    cuisine = request.form['cuisine']

    # Call OpenAI API to generate meal ideas
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "We have ingredients: " + ingredients + " I want cusisine: " + cuisine},
    ])
    meal_ideas = response.choices[0]["message"]["content"]

    return render_template('result.html', ingredients=ingredients, cuisine=cuisine, meal_ideas=meal_ideas)

if __name__ == '__main__':
    app.run(debug=True)
