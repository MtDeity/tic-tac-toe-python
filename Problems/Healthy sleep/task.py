under = int(input())
over = int(input())
ann = int(input())

if ann > over:
    print("Excess")
elif ann < under:
    print("Deficiency")
else:
    print("Normal")
