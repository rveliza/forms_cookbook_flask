from flask import Flask, render_template
from helper import recipes

app = Flask(__name__)

@app.route('/')
def index():
    # print(recipes)
    # {1: 'fried egg', 2: 'buttered toast'}
    return render_template("index.html",
                           template_recipes = recipes)

@app.route('/about')
def about():
    return render_template('about.html')

print(__name__)
if __name__ == '__main__':
    app.run(debug=True)