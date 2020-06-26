score = int(input())
maximum = int(input())
percentage = score / maximum

if percentage >= 0.9:
    print("A")
elif percentage >= 0.8:
    print("B")
elif percentage >= 0.7:
    print("C")
elif percentage >= 0.6:
    print("D")
else:
    print("F")
