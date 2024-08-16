from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request):
    return HttpResponse("Hello, world. You're at the polls index.") 

def recipeList(request):
    
    if request.method == 'GET':
        # GET /recipes/: Retrieve a list of all recipes, sorted by most recent.
        pass
    
    if request.method == 'POST':
        # POST /recipes/: Add a new recipe. Accepts recipe name, ingredients, steps, and preparation time.
        pass
    pass
    
def recipeModification(request):
    if request.method == 'GET':
        # GET /recipes//: Retrieve details of a specific recipe by its ID.
        pass
    
    if request.method == 'PUT':
        # PUT /recipes//: Update a specific recipe by its ID.
        pass
    
    if request.method == 'DELETE':
        # DELETE /recipes//: Delete a specific recipe by its ID.
        pass
    pass

def recipeRating(request):
    if request.method == 'POST':
        # POST /recipes//ratings/: Rate a specific recipe. Accepts a rating (1-5).
        pass
    pass


def recipeComments(request):
    if request.method == 'GET':
        # GET /recipes//comments/: Retrieve all comments for a specific recipe.
        pass
    
    if request.method == 'POST':
        # POST /recipes//comments/: Comment on a specific recipe. Accepts a comment text.
        pass
    pass
