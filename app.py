import streamlit as st
import requests

st.title("Recipe Generator")

def generate_recipe(ingredients):
    """Generates a recipe based on given ingredients using a recipe API."""

    api_key = "YOUR_API_KEY"
    base_url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": api_key,
        "ingredients": ",".join(ingredients),
        "number": 1,  
        "addRecipeInformation": True, 
        "fillIngredients": True,  
    }

    response1 = requests.get(base_url, params=params)
    data = response1.json()
    
    if len(data) > 0:
        recipe = data[0]
        
        st.header(recipe["title"])
        st.image(recipe["image"], width=400)

        if recipe.get("missedIngredients"):
                st.subheader("Missing Ingredients:")
                s = ""
                for i in recipe["missedIngredients"]:
                    s = s + i['name'] + ", "
                st.write(s)
        st.subheader("Instructions:")
        id = recipe["id"]
        url = "https://api.spoonacular.com/recipes/{}/analyzedInstructions".format(id)
        response2 = requests.get(url, {"apiKey" : api_key})
        instructions = response2.json()
        instruction = instructions[0]
        for i in instruction['steps']:
            st.write(i['step'])

    else:
        st.write("No recipes found with those ingredients.")

ingredients = st.text_input("Enter ingredients separated by commas:")
if st.button('Show Recipe'):
    if ingredients:
        ingredients_list = ingredients.split(",")
        generate_recipe(ingredients_list)
    else:
        st.write("You have not entered any ingredients!")
    
