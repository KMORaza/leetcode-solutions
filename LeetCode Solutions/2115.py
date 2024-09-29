from collections import defaultdict
from typing import List
class Solution:
    def findAllRecipes(self, recipe_names: List[str], ingredient_lists: List[List[str]], available_supplies: List[str]) -> List[str]:
        ingredient_to_recipes = defaultdict(list)
        recipe_indegree = {}
        for index in range(len(recipe_names)):
            for ingredient in ingredient_lists[index]:
                ingredient_to_recipes[ingredient].append(recipe_names[index])
            recipe_indegree[recipe_names[index]] = len(ingredient_lists[index])
        supply_stack = list(available_supplies)
        crafted_recipes = []
        available_set = set(available_supplies)
        while supply_stack:
            current_ingredient = supply_stack.pop()
            for recipe in ingredient_to_recipes.get(current_ingredient, []):
                recipe_indegree[recipe] -= 1
                if recipe_indegree[recipe] == 0 and recipe not in available_set:
                    crafted_recipes.append(recipe)
                    supply_stack.append(recipe)
                    available_set.add(recipe)
        return crafted_recipes