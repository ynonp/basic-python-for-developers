# Read an input number from the user,
# print BOOM if:
# the number is divisible by 7
# OR the number contains 7

number : int = int(input("Please select a number"))
is_divisible_by_7 : bool = number % 7 == 0
contains_7 : bool        = "7" in str(number)

if is_divisible_by_7 or contains_7:
    print("BOOM")


