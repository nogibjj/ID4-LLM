from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_activity', methods=['POST'])
def get_activity():
    # Get the user's mood from the form
    user_mood = request.form['mood']

    # Use OpenAI API to get an activity suggestion
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"I am feeling {user_mood}. What activity should I do?",
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )

    activity_suggestion = response.choices[0].text.strip()

    return render_template('result.html', mood=user_mood, activity=activity_suggestion)

if __name__ == '__main__':
    app.run(port=8000)
