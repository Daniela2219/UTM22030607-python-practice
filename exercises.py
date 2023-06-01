import math

my_list = [1, 2, 3, 4, 5]
my_list[4] = input("Enter the value to be stored in the list: ")
for item in my_list:
    print(item)

nums = (1, 2, 3, 4, 5, 6, 7)
i = 0
while i < len(nums):
    print(nums[i])
    i = i + 1

address = {
    "state": "Aguascalientes",
    "municipality": "Jesús María",
    "street": "Jardín del Rosario"
}

print("Current address:")
print("State:", address["state"])
print("Municipality:", address["municipality"])
print("Street:", address["street"])

# Change the street property
new_street = input("Enter the new street: ")
address["street"] = new_street

print("Updated address:")
print("State:", address["state"])
print("Municipality:", address["municipality"])
print("Street:", address["street"])

def operation(operating, frstnum, secnum):
    operators = {
        "+": frstnum + secnum,
        "-": frstnum - secnum,
        "*": frstnum * secnum,
        "/": frstnum / secnum if secnum != 0 else None
    }

    result = operators.get(operating)

    if result is None:
        print("Error, invalid operator")
    elif operating == "/" and secnum == 0:
        print("You can't divide by zero!")
        return None

    return result

operating = input("Insert the operation (+, -, /, *): ")
frstnum = int(input("Insert your first number: "))
secnum = int(input("Insert your second number: "))

result = operation(operating, frstnum, secnum)
if result is not None:
    print("The result is:", result)
    
