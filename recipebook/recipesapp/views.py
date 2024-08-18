from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.
import json

def index(request):
    return redirect(reverse('homepage'))

def homePage(request):
    # return HttpResponse("Hello, world. You're at the polls index.") 
    return render(request, 'index.html')

def recipeList(request):
    if request.method == 'GET':
        # GET /recipes/: Retrieve a list of all recipes, sorted by most recent.
        query = """
        SELECT * FROM recipe
        ORDER BY recipe_id DESC;
        """
        recipes = sqlExecute(query, 'read')
        
        recipes_list = [dict(zip(COLUMN_RECIPE, recipe)) for recipe in recipes]
        
        return JsonResponse(json.dumps(recipes_list), safe=False)
    
    if request.method == 'POST':
        # POST /recipes/: Add a new recipe. Accepts recipe name, ingredients, steps, and preparation time.
        data = json.loads(request.body)
        print(data)
        name = data.get('name')
        ingredients = data.get('ingredients')
        steps = data.get('steps')
        preparation_time = int(data.get('preparation_time'))
        
        query = f"""
        INSERT INTO recipe (name, ingredients, steps, preparation_time)
        VALUES ('{name}', '{ingredients}', '{steps}', {preparation_time})
        """
        sqlExecute(query, 'write')
        return JsonResponse({'message': 'Recipe added successfully!'})
    
def recipeModification(request):
    if request.method == 'GET':
        # GET /recipes//: Retrieve details of a specific recipe by its ID.
        recipeid = int(request.GET.get('recipe_id'))
        query = f"""
        select * from recipe
        where recipe.recipe_id = {recipeid};
        """
        recipe_info = sqlExecute(query, 'read')
        
        return JsonResponse(json.dumps(dict(zip(COLUMN_RECIPE, recipe_info[0]))), safe=False)
        
    if request.method == 'PUT':
        # PUT /recipes//: Update a specific recipe by its ID.
        data = json.loads(request.body.decode('utf-8'))
        query = f"""
        UPDATE recipe
        SET 
            name = '{data.get('name')}',
            ingredients = '{data.get('ingredients')}',
            steps = '{data.get('steps')}',
            preparation_time = {int(data.get('preparation_time'))}
        WHERE recipe_id = {int(data.get('id'))}
        """
        sqlExecute(query, 'write')
        return JsonResponse({'message': 'Recipe edited successfully!'})
    
    if request.method == 'DELETE':
        # DELETE /recipes//: Delete a specific recipe by its ID.
        recipe_id = request.GET.get('recipe_id')
        query = f"""
        DELETE FROM recipe
        WHERE recipe_id = {recipe_id}
        """
        sqlExecute(query, 'write')
        return JsonResponse({'message': 'Recipe deleted successfully!'})
    

def recipeRating(request):
    if request.method == 'POST':
        # POST /recipes//ratings/: Rate a specific recipe. Accepts a rating (1-5).
        data = json.loads(request.body)
        user_id = int(data.get('user'))
        recipe_id = int(data.get('recipe_id'))
        rating = int(data.get('rating'))
        
        query = f"""
        INSERT INTO rating (recipe_id, rating, user_id) 
        VALUES ({recipe_id}, {rating}, {user_id})
        """
        sqlExecute(query, 'write')
        return JsonResponse({'message': 'rating successfully added!'})

def recipeComments(request):
    if request.method == 'GET':
        # GET /recipes//comments/: Retrieve all comments for a specific recipe.
        recipe_id = request.GET.get('recipe_id')
        query = f"""
        select * from comments
        where recipe_id = {recipe_id};
        """
        result = sqlExecute(query, 'read')
        
        comments = [dict(zip(COLUMN_COMMENT, comment)) for comment in result]
        
        return JsonResponse(json.dumps(comments), safe=False)
    
    if request.method == 'POST':
        # POST /recipes//comments/: Comment on a specific recipe. Accepts a comment text.
        data = json.loads(request.body)        
        
        recipe_id  = int(data.get('recipe_id'))
        comment_text = data.get('comment')
        user_id = int(data.get('user_id'))
        
        query = f"""
        INSERT INTO comments (recipe_id, comment_text, user_id) VALUES 
        ({recipe_id}, '{comment_text}', {user_id})"""
        sqlExecute(query, 'write')        
        return JsonResponse({'message': 'comment successfully added!'})
