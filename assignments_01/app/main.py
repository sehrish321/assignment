

def main():
    # Age Assignments Based on the Riddle
    Anton: int = 21
    Beth: int = 6 
    Chen: int = 20
    Drew: int = Chen + Anton 
    Ethan: int = Chen 
    print("Anton is",Anton) 
    print("Beth is",Beth) 
    print("Chen is",Chen) 
    print("Drew is",Drew) 
    print("Ethan is",Ethan) 
    print('\n')

    # Formatted String Interpolation
    name:str = "Alice"
    age:int = 30
    city:str = "New York"
    print(f"{name} is {age} years old and lives in {city}.")
    print("\n")

    # String Manipulation
    s:str = "hElLo WoRlD"
    print(s.capitalize())
    print(s.upper())
    print(s.lower())
    print("\n")
    # Substring Search
    s:str ="the quick brown fox jumps over the lazy dog"
    word = "fox"
    index_number = s.find(word)
    word2 = "the"
    total_time = s.count(word2)
    print(f"index of {word} is {index_number}")
    print(f"'{word2}' appears {total_time} times")
    print("\n")
    # String Replacement 
    s:str ="I love programming in Python"
    print(s.replace("Python","Java"))
    print("\n")

    # String Splitting and Joining
    s:str ="apple,banana,cherry,dates"
    fruit_list = s.split(',')
    print(fruit_list)
    print(" ".join(fruit_list))
    print("\n")
    # String Stripping and Justifying
    s:str ="   Python is fun!   "
    print(s.strip())
    print(s.strip().ljust(20,"*"))
    print(s.strip().rjust(20,"*"))
    print("\n")
    # Convert an integer to its binary representation
    num:int = 45
    print(f"Binary representation : {bin(num)}")
    print("\n")
    # Calculate Powers of Numbers.
    base:int = 3
    exponent:int = 4
    print(f"Power result: {pow(base,exponent)}")
    print("\n")

    # Round floating-point numbers
    value:float = 12.34567
    print(f"Rounded to nearest integer: {round(value)}")
    print(f"Rounded to two decimal places: {round(value,2)}")








if __name__ == "__main__":
    main()