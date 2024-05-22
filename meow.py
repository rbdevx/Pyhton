def main():
    number = get_number(print)
    meow(number)

def get_number():
    while True:
        n = int(input("What is the numer? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")
        
        
main()