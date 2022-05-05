# Kai Geller
# GitHub Username: KaiGeller
# 5/4/2022
# This funtion is tring to find the standard deviation of peoples ages
class Person:
    def __init__(self,name,age):
        """This will initialize the class of the person"""
        self.name=name
        self.age=age
    def get_age(self):
        return(self.age)
def std_dev(Person):
    """This will find the standard deviation of the people"""
    total_age = 0
    for p in Person:
        total_age += p.get_age()
    total_age = total_age/len(Person)
    total_variance = 0
    for p in Person:
        total_variance += (p.get_age()-total_age)**2
    mean_variance = (total_variance/len(Person))**0.5
    return mean_variance

