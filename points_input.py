input_coordinates = input("Please enter points: ")

points = input_coordinates.split(";")
result = []

for i in points:
    x, y = i.split(",")
    x = float(x)
    y = float(y)
    x = x ** 2
    y = y ** 2

    result_dict = {'x': x, 'y': y}
    result.append(result_dict)

print(result)