two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
a=int(two_digit_number)/10
b=int(two_digit_number)%10
c=int(a)+b
print(c)


                                                                   #METHOD 2

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)
