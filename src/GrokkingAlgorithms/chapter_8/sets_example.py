fruits = {"avocado", "tomato", "banana"}
vegetables = {"beets", "carrots", "tomato"}

print(f"Объединение (|): {fruits | vegetables}")  # Union
print(f"Пересечение (&): {fruits & vegetables}")  # Intersection
print(f"Разность (-):    {fruits - vegetables}")  # Difference
print("By using sets' functions")
print(f"Объеденение (union function):         {fruits.union(vegetables)}")
print(f"Пересечение (intersection function):  {fruits.intersection(vegetables)}")
print(f"Разность    (difference function):    {fruits.difference(vegetables)}")
