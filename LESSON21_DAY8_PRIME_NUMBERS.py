def prime_checker(number):
  checker = True
  for num in range(2,number):
    if number%num == 0 :
      checker = False
      print(f"It's not a prime number.")
      break
  if checker:
    print(f"It's a prime number.")
    
n = int(input('enter a number to check for prime number'))
prime_checker(number=n)
