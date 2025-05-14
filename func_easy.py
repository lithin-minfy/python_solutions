def calculate_average(numbers):
   return sum(numbers)/len(numbers) if numbers else 0
print(calculate_average([12,34,23,56,78])) 
print(calculate_average([]))

def greet_user(name,greet = "Hello"):
   return f"{greet},{name}!"
print(greet_user("sam"))
print(greet_user('Alice','Hi'))
