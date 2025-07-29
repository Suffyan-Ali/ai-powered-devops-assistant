import os
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    solution = None
    if request.method == 'POST':
        user_problem = request.form['problem']
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful DevOps assistant."},
                {"role": "user", "content": user_problem}
            ]
        )
        solution = response.choices[0].message.content.strip()

    return render_template('index.html', solution=solution)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
