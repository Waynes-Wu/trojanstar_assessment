baseurl = window.location.origin
user_id = 1
document.addEventListener('DOMContentLoaded', ()=>{
    
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('value')
    axios.defaults.headers.common['X-CSRFToken'] = csrfToken;

    const addrecipeform = document.querySelector('#add-recipe-form')
    addrecipeform.addEventListener('submit', (e)=>{ e.preventDefault()
    addrecipe()}
)

    const getRecipeButton = document.querySelector('#get-recipe-button')
    getRecipeButton.addEventListener('click', getRecipeById)

    const editRecipeButton = document.querySelector('#edit-recipe-button')
    editRecipeButton.addEventListener('click', (e)=>{ e.preventDefault()
        editRecipeById()})

    const deleteRecipeButton = document.querySelector('#delete-recipe-button')
    deleteRecipeButton.addEventListener('click', deleteRecipe)

    const rateRecipeButton = document.querySelector('#rate-recipe-button')
    rateRecipeButton.addEventListener('click', rateRecipe)

    const getCommentButton = document.querySelector('#get-comment-button')
    getCommentButton.addEventListener('click', getCommentRecipe)
    
    const postCommentButton = document.querySelector('#post-comment-button')
    postCommentButton.addEventListener('click', (e)=>{e.preventDefault();postCommentRecipe()})

});

function fetchRecipes() {
    axios.get(`${baseurl}/recipes/`)
        .then(response => {
            const recipes = JSON.parse(response.data);
            const tableBody = document.querySelector('#recipes-table tbody');

            tableBody.innerHTML = '';
            console.log(recipes)
            recipes.forEach(recipe => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${recipe.recipe_id}</td>
                    <td>${recipe.name}</td>
                    <td>${recipe.ingredients}</td>
                    <td>${recipe.steps}</td>
                    <td>${recipe.preparation_time}</td>
                `;

                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching recipes:', error);
        });
}

function addrecipe(){
    form = document.querySelector('#add-recipe-form')
    const formData = new FormData(form);
    const data = {
        name: formData.get('add-recipe-name'),
        ingredients: formData.get('add-recipe-ingredients'),
        steps: formData.get('add-recipe-steps'),
        preparation_time: parseInt(formData.get('add-recipe-preptime'), 10)
    };
    axios.post(`${baseurl}/recipes/`,data)
    .then(response => {
        console.log(typeof(response.data))
        alert(response.data['message']);
        form.reset();
    })
    .catch(error => {
        alert('Error adding recipe:', error);
    });
}

function getRecipeById(){

    console.log('button clicked')

    let id = document.querySelector('#get-recipe-recipeid').value
    axios.get(`${baseurl}/recipes//`, {
        params: {
            recipe_id: id
        }}
    ).then(response => {
            const recipes = JSON.parse(response.data);
            const tableBody = document.querySelector('#get-recipe-table tbody');

            tableBody.innerHTML = '';
            console.log(recipes)
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${recipes.recipe_id}</td>
                <td>${recipes.name}</td>
                <td>${recipes.ingredients}</td>
                <td>${recipes.steps}</td>
                <td>${recipes.preparation_time}</td>
            `
            tableBody.appendChild(row);
        })
        .catch(error => {
            console.error('Error fetching recipes:', error);
        });
}

function editRecipeById(){
    form = document.querySelector('#edit-recipe-form')
    const formData = new FormData(form);

    const data = {
        id: formData.get('edit-recipe-id'),
        name: formData.get('edit-recipe-name'),
        ingredients: formData.get('edit-recipe-ingredients'),
        steps: formData.get('edit-recipe-steps'),
        preparation_time: parseInt(formData.get('edit-recipe-preptime'), 10)
    };

    axios.put(`${baseurl}/recipes//`, data)
    .then(response => {
        console.log(response.data);
        alert('Recipe updated successfully');
    })
    .catch(error => {
        console.error(error);
        alert('Failed to update recipe');
    });
}

function deleteRecipe(){
    recipe_id = document.querySelector('#delete-recipe-id').value
    // * axios delete does not have data arg
    axios.delete(`${baseurl}/recipes//?recipe_id=${recipe_id}`).then(response => {
        alert('Recipe deleted successfully:', response.data);
    })
    .catch(error => {
        alert('There was an error deleting the recipe:', error);
    });
}

function rateRecipe(){
    recipe_id = document.querySelector('#rate-recipe-id').value
    rating = document.querySelector('#rate-recipe-rating').value

    data = {
        user: user_id,
        recipe_id:recipe_id,
        rating:rating
    }
    axios.post(`${baseurl}/recipes//ratings/`, data).then(response => {
        alert(response.data['message']);
    })
    .catch(error => {
        alert('Error adding recipe:', error);
    });
}

function getCommentRecipe(){
    recipe_id = document.querySelector('#get-comment-id').value

    axios.get(`${baseurl}/recipes//comments/`, {
        params: {
            recipe_id: recipe_id
        }}) .then(response => {
            const comments = JSON.parse(response.data);
            const commentsContainer = document.querySelector('#comments-container');
    
            // Clear any existing comments
            commentsContainer.innerHTML = '';
    
            // Display comments
            comments.forEach(comment => {
                const commentDiv = document.createElement('div');
                commentDiv.innerHTML = `${comment.user_id}: commented "${comment.comment_text}"`;
                commentsContainer.appendChild(commentDiv);
            });
        })
        .catch(error => {
            console.error('There was an error fetching comments:', error);
            // Handle the error, e.g., show an error message to the user
        });
    }
function postCommentRecipe(){
    recipe_id = document.querySelector('#post-comment-id').value
    comment = document.querySelector('#post-comment-text').value

    data = {
        recipe_id: recipe_id,
        comment: comment,
        user_id:user_id
    }
    axios.post(`${baseurl}/recipes//comments/`, data).then(response => {
        alert(response.data['message']);
    })
    .catch(error => {
        alert('Error adding recipe:', error);
    });
    document.querySelector('#post-comment-id').value = ''
    comment = document.querySelector('#post-comment-text').value = ''   
}