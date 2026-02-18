# number_analyzer.py
# Function to check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main function
def number_analyzer():
    try:
        num = int(input("Enter a number: "))
        
        # Even or Odd
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
        
        # Positive or Negative
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")
        
        # Prime check
        if is_prime(num):
            print("Prime")
        else:
            print("Not Prime")
    
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Run program
if __name__ == "__main__":
    number_analyzer()
