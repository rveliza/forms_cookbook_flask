from flask import Flask, render_template
from helper import recipes, types, descriptions, ingredients, instructions, comments

app = Flask(__name__)

@app.route('/')
def index():
    # print(recipes)
    # {1: 'fried egg', 2: 'buttered toast'}
    return render_template("index.html",
                           template_recipes = recipes)

@app.route('/recipe/<int:id>')
def recipe(id):
    # print(recipes[id])
    # "buttered toast"
    # return "Hello" + str(id)
    return render_template("recipe.html",
                           template_recipes = recipes[id],
                           template_type = types[id],
                           template_description = descriptions[id],
                           template_ingredients = ingredients[id],
                           template_instructions = instructions[id],
                           template_comments = comments[id])

@app.route('/about')
def about():
    return render_template('about.html')

print(__name__)
if __name__ == '__main__':
    app.run(debug=True)