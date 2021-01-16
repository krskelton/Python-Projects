numbers = ["1", "2", "3"]
for num in numbers:
    print(num)
numbers.append("4")
print(numbers)
newNumbers = list(numbers)
print(newNumbers)
print(numbers + newNumbers)
numbers.reverse()
print(numbers)
