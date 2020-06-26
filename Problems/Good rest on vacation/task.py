# put your python code here
duration = int(input())
food = int(input())
flight = int(input())
hotel = int(input())

print(food * duration + flight * 2 + hotel * (duration - 1))