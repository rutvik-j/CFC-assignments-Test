# WAP to sum of two integers. Sum between 15-20 return 20

def sum_calculation(a,b):
    s = a + b
    if s>=15 and s<=20:
        print(20)
    else:
        print(s)


a,b = [int(x) for x in input("Enter two variables:").split()]
sum_calculation(a,b)