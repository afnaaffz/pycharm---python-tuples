fruits=("apple","mango","orange")
y=list(fruits)
y.append("cherry")
fruits=tuple(y)
print(fruits)



fruits=("apple","mango","orange")
y=("strawberry",)
fruits+=y
print(fruits)