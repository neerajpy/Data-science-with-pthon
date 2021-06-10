# class laptop:
#     def __init__(self, brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.laptop_name = brand_name + ' ' + model_name
    
#     def final_amount(self,discount):
#         return (f'your final amount is {self.price-(discount/100 * self.price)}')


# l1 = laptop("lenovo","330",630000)

# print(l1.brand_name)
# print(l1.model_name)
# print(l1.price)
# print(l1.laptop_name)
# print(l1.final_amount(40))

class Person:
    count_instance = 0
    def __init__(self, first_name,last_name):
        self.full_name = first_name + ' ' + last_name
        Person.count_instance += 1


p1 = Person('neeraj', 'verma')
p2 = Person('neraj', 'verma')
print(Person.count_instance)



















