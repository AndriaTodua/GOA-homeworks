start = int(input("Enter the start of the range: "))
end = int (input("Enter the end of the range: "))

my_range = range(start + (start % 2), end + 1, 2)

for num in my_range:
    print(num)