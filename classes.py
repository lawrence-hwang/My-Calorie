## S W O L E Calorie Counter
## Written by Lawrence Hwang

class ingredient:
    def __init__(self, name, cals=None, proteins=None, carbs=None, fats=None):
        self.name = name
        self.cals = cals
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    ## If values for ingredient changes or was not specified at init
    def set_name(self,val):
        self.name = val
    def set_cals(self, val):
        self.cals = val
    def set_proteins(self, val):
        self.proteins = val
    def set_carbs(self,val):
        self.carbs = val
    def set_fats(self,val):
        self.fats = val

    ## Getter methods for collecting info stored in ingredient class
    def get_info(self):
        return {"name":self.name, "cals":self.cals, "proteins":self.proteins,
                "carbs":self.carbs, "fats":self.fats}
    def get_name(self):
        return self.name
    def get_cals(self):
        return self.cals
    def get_proteins(self):
        return self.proteins
    def get_carbs(self):
        return self.carbs
    def get_fats(self):
        return self.fats

class meal:
    def __init__(self, name, ingredients=[], time=None, meal_no=None):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.meal_no = meal_no

    def set_name(self,val):
        self.name = val
    def set_ingredients(self,val):
        self.ingredients = val
    def set_time(self,val):
        self.time = val
    def set_meal_no(self,val):
        self.meal_no = val

    def get_name(self):
        return self.name
    def get_ingredients(self):
        return self.ingredients
    def get_time(self):
        return self.time
    def get_meal_no(self):
        return self.meal_no

    def cals(self):
        result = 0
        for i in self.ingredients:
            result+=int(i.get_cals())
        return result
            

    
    
    
