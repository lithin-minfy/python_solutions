def calculate_total(*prices,discount=0):
    total = sum(prices)
    return total-total*discount/100
print(calculate_total(10,20,50))
print(calculate_total(25,67,89,discount=20))

def create_multiplier(factor):
    return lambda x:x*factor
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))
print(triple(5))
    