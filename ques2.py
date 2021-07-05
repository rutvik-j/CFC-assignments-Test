# WAP to find the count of 'a' in a list

def count_a(arr):
    count_letter = 0
    for i in arr:
        if i == 'a':
            count_letter+=1
    print(count_letter)

count_a(input("Enter the string:"))