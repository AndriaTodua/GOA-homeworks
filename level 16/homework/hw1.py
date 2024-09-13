start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
step = int(input("Enter the step of the range: "))

my_range = range(start, end, step)

for num in my_range:
    print(num)