from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meal_suggestions', methods=['POST'])
def get_meal_suggestions():
    # Get the ingredients and cuisine from the form
    ingredients = request.form['ingredients']
    cuisine = request.form['cuisine']

    # Call OpenAI API to generate meal ideas
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate meal ideas using these ingredients: {ingredients}, in the style of {cuisine} cuisine.",
        max_tokens=150
    )
    meal_ideas = response.choices[0].text.strip()

    return render_template('result.html', ingredients=ingredients, cuisine=cuisine, meal_ideas=meal_ideas)

if __name__ == '__main__':
    app.run(debug=True)
