from crypt import methods
from heapq import merge
from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

#------------------------------
# Add recipe
#------------------------------
@app.route("/new/recipe")
def new_recipe():
    if "user_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect("/")
    data = {
        "user_id" : session['user_id']
    }
    user = User.get_by_id(data)
    return render_template("new_recipe.html", user = user)

@app.route("/new/recipe/create", methods=["POST"])
def add_recipe():
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date" : request.form["date"],
        "time" : request.form["time"],
        "user_id" : session["user_id"]
    }
    if not Recipe.recipe_validate(data):
        return redirect("/new/recipe")
    
    Recipe.add_recipe(data)

    return redirect("/dashboard")

#=======================================
#   Show one Recipe
#=======================================
@app.route("/dashboard/view_recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    data = {
        "recipe_id" : recipe_id
    }
    recipe = Recipe.get_recipe_w_user(data)
    return render_template("show_recipe.html", recipe = recipe)

#=======================================
#   Edit one Recipe
#=======================================
@app.route("/dashboard/edit_recipe/<int:recipe_id>")
def edit_user(recipe_id):
    data = {
        "recipe_id" : recipe_id
    }
    recipe = Recipe.get_recipe_w_user(data)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route("/dashboard/update_recipe/<int:recipe_id>", methods = ["POST"])
def update_recipe(recipe_id):
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date" : request.form["date"],
        "time" : request.form["time"],
        "recipe_id" : recipe_id
    }
    if not Recipe.recipe_validate(data):
        return redirect(f"/dashboard/edit_recipe/{recipe_id}")
    Recipe.update_recipe(data)
    return redirect("/dashboard")

#=======================================
#   Delete one Recipe
#=======================================
@app.route("/dashboard/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    data = {
        "recipe_id" : recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect("/dashboard")