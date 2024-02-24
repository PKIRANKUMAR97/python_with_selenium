try:
    print("enter a value ")
    a = int(input())
    print("enter b value ")
    b = int(input())
    if b == 0:
        raise Exception(" b value is 0")
    print(a / b)

except Exception as e:
    print(e)
    print("in exception block ")
else:
    print("in else block")
finally:
    print("this is always printed ")
