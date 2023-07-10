from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("Add Comment")

class RecipeForm(FlaskForm):
    recipe_categories = [("Breakfast","Breakfast"), ("Lunch","Lunch"), ("Dinner","Dinner")]
    recipe =  StringField("Recipe", validators=[DataRequired()])
    recipe_type = RadioField("Type", choices=recipe_categories)
    description = StringField("Description")
    ingredients = TextAreaField("Ingredients")
    instructions = TextAreaField("Instructions")
    submit = SubmitField("Add Recipe")