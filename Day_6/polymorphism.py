class DietPlan:
    pass
#child class keto diet

class KetoDiet(DietPlan):
    def get_breakfast(self):

        return "Eggs,Avocado, and bacon fried"
    #child class 2:vegan Diet

class VeganDiet(DietPlan):
    def get_breakfast(self):
        return "Oatmeal with fruits and nuts"

#Child Class 3:High Protien Diet plan:
class HighProteinDiet(DietPlan):
    def get_breakfast(self):
        return "Protein smoothie with spinach and berries"
    
#Polymorhic function
#this function accept any diet object and calls its get_breakfast method
def print_morning_routine(diet_plan):
    print(f"Today's Breakfast:{diet_plan.get_breakfast()}")    


#create an Instance
my_keto_diet =   KetoDiet()
my_vegan_diet = VeganDiet()
my_protien_diet = HighProteinDiet()

#pass the different diet objects on the polymorphic function 
print_morning_routine(my_keto_diet)
print_morning_routine(my_vegan_diet)
print_morning_routine(my_protien_diet)