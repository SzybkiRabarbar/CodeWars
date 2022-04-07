'''
https://www.codewars.com/kata/525c65e51bf619685c000059/python
'''

def cakes(recipe:dict, available:dict):
    return min([available.get(ingredient)//recipe.get(ingredient) if ingredient in available else 0 for ingredient in recipe])

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
