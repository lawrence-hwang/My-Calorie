## USE

import classes



def build_meal():
    meal_name = input("Enter name or identifier for meal: ")
    meal_time = input("Meal time:   ")
    meal_numb = input("Meal number: ")
    print("Enter ingredients as follows\n"+"-"*28)
    ingredients = _collect_ingredients()
    return classes.meal(meal_name, ingredients, meal_time, meal_numb)
        
def _collect_ingredients():
    building = True

    ingredients = []
    while building:
        print("Current Ingredients:",_current_ingredients(ingredients))

        name = input("Name:     ")
        cals = input("Calories: ")
        proteins = input("Proteins: ")
        carbs = input("Carbs:    ")
        fats = input("Fats:     ")

        ingredients.append(classes.ingredient(name,cals,proteins,carbs,fats))
        cont = input("Enter another ingredient? (y/n): ")
        if cont == "n":
            building = False
            
    return ingredients
        
def display_meals(meals):
    total = 0
    for meal in meals:
        print(str(meal.get_meal_no())+": " + str(meal.get_name()) + " - calories: "+
              str(meal.cals()))
        total += meal.cals()
    print("Daily total:",total)
    

def _current_ingredients(ingredient_list):
    names = [x.get_name() for x in ingredient_list]
    result = ""
    for name in names:
        result = result+name+", "
    return result
        
def driver():
    _intro()
    meals = []
    
    running = True
    while running:
        _show_commands()
        command = input("Enter command: ")
        print("-"*50)
        c = command.lower().strip()
        if c == "q":
            running = False
        if c == "b":
            meals.append(build_meal())
        if c == "v":
            if not meals:
                print("No meals currently added")
            display_meals(meals)
        else:
            print("Error: No legal command entered. Check input")
        print("-"*50)
            
    return meals

def _intro():
    print("*"*5,"Welcome to Calorie Counter","*"*5,"\n", " "*4,"Written by: Lawrence Hwang")
    print("Please enter key based on desired operation:")


def _show_commands():
    print("     b: Build meal")
    print("     v: View daily intake")
    print("     q: Quit")

def main():
    daily = []
    daily.append(build_meal())
    print(daily[0].get_name())

if __name__ == "__main__":
    driver()
        
