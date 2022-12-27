# check if number is even or odd

number = int(input("Enter a number: "))

def even_odd(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

# check if number is even or odd in one line

def even_odd(number): print("Number is even") if number % 2 == 0 else print("Number is odd")

# check if number is even or odd very short way
def even_odd(number): print("Number is even") if not number % 2 else print("Number is odd")


def even_odd(number):
    if number % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"


number = int(input("Enter a number: "))
result = even_odd(number)
print(result)


def even_odd(number):
    return "Number is even" if number % 2 == 0 else "Number is odd"


print(even_odd(int(input("Enter a number: "))))


print((lambda x: "Number is even" if x %
      2 == 0 else "Number is odd")(int(input("Enter a number: "))))

print("Number is even" if int(input("Enter a number: ")) %
      2 == 0 else "Number is odd")


print("Number is even" if int(input("Enter a number: "))
      & 1 == 0 else "Number is odd")
