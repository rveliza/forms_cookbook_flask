from flask import Flask, render_template
from helper import recipes, types, descriptions, ingredients, instructions, comments
from forms import CommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route('/')
def index():
    # print(recipes)
    # {1: 'fried egg', 2: 'buttered toast'}
    return render_template("index.html",
                           template_recipes = recipes)

@app.route('/recipe/<int:id>', methods=["GET", "POST"])
def recipe(id):
    # print(recipes[id])
    # "buttered toast"
    # return "Hello" + str(id)
    comment_form = CommentForm(csrf_enabled=False)
    # print(comment_form)
    # <forms.CommentForm object at 0x000001D0C7E3FFA0>
    # print(comment_form.comment)
    # <input id="comment" name="comment" type="text" value="">
    # print(comment_form.submit)
    # <input id="submit" name="submit" type="submit" value="Add Comment">
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
    return render_template("recipe.html",
                           template_recipes = recipes[id],
                           template_type = types[id],
                           template_description = descriptions[id],
                           template_ingredients = ingredients[id],
                           template_instructions = instructions[id],
                           template_comments = comments[id],
                           template_form = comment_form)

@app.route('/about')
def about():
    return render_template('about.html')

print(__name__)
if __name__ == '__main__':
    app.run(debug=True)