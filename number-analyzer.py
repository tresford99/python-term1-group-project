def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def number_analyzer():
    try:
        num = int(input("Enter a number: "))
        
        print("Even" if num % 2 == 0 else "Odd")
        
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")
        
        print("Prime" if is_prime(num) else "Not Prime")
        
    except ValueError:
        print("Invalid input! Please enter an integer.")
if __name__ == "__main__":
    number_analyzer()
