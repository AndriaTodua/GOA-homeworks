def calculate_average(numbers):
    if not numbers:  
        return 0  

    total = sum(numbers)  
    count = len(numbers)  
    average = total / count  

    return average  

numbers_list = [34, 50, 82, 12, 20]
average = calculate_average(numbers_list)

print("საშუალო რიცხვი:", average)