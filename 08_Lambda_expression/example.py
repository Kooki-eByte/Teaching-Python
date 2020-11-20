# Lambda expressions

# ----- Original way -------
def addTen(x):
    return x + 10


print(f"Original way : {addTen(5)}")

# ----- Lambda way -------


x= lambda x: x + 10


print(f"lambda way: {x(5)}")
