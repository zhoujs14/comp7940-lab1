def main():
  print("Hello World")

def ex1(arg):
  # Find the all factors of x using a loop and the operator %
  # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
  x = arg or 52633
  for i in range(1,x+1):
    # your code here
    if x%i==0:
      print(i)

def print_factor(x):
  ex1(x)

# Write a program that be able to find all factors of the numbers in the list l
def ex3():
  l = [52633, 8137, 1024, 999]
  for i in l:
    print_factor(i)


if __name__ == '__main__':
  main()
  ex3()
