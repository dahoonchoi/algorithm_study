# 002.
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to 2, 5 print Not Weird
# If  is even and in the inclusive range of  to 6, 20 print Weird
# If  is even and greater than 20,  print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

def Calculation(value1):

    n = value1

    if __name__ == "__main__":
        try:
            if n%2 != 0:
                print("Weird")
            elif n%2 == 0 and 2 <= n and 5 > n:
                print("Not Weird")
            elif n%2 == 0 and 6 <= n and 20 >= n: 
                print("Weird")
            elif n > 20 :
                print("Not Weird")
        except ValueError as e:
            print(e)

Calculation(20)

# 기존의 else if 와 다르게 Python 에서는 elif 를 사용하는 것을 알게되었습니다.

