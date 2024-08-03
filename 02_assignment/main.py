def get_last_element(lst):
    print(lst[-1])




def main()->None:
    # Quention 1
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}.\n")
    
    # Quention 2
    animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {animal}! \n")
    
    # Quention 3
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C\n")
    
    # Quention 4
    
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}.")
    print('')
    # Quention 5
    number = float(input("Type a number to see its square: "))
    square = number ** 2
    print(f"{number} squared is {square}.")
    print('')

    # Quention 6
    numbers = [1, 2, 3, 4, 5]
    numbers.remove(3)
    print(numbers)
    print('')

    # Quention 8
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)
    print('')
    # Quention 9
    # Define the list
    items = [10, 20, 30, 40]
    removed_item = items.pop()
    print("Updated list:", items)
    print("Removed item:", removed_item)
    print(" ")

    # Quention 10
    colors = ['red', 'blue', 'green', 'yellow']
    index = colors.index('green')
    print("The index of 'green' is:", index)

    # challenge 1
    get_last_element([1,3,False,True,"Fiza"])
    print('')
    # challenge 2 
    user_list = []
    while True:

        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)

    print("Here's the list:", user_list)





















if __name__ == "__main__":
    main()    
