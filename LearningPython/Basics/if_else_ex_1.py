num = int(input())
if (num % 2) != 0:
    print("Weird")
elif (num % 2) == 0 and range(2, 6):
    print("Not Weird")
elif (num % 2) == 0 and range(6, 21):
    print("Weird")
elif (num % 2) == 0 and ((num > 20) and (num <= 100)):
    print("Not Weird")
