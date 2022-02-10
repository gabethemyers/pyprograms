import random

dice_sum = 0
dice_list = []
dice_roll = int(input('Enter number of sides on each die: '))
dice_count = int(input('Enter number of dice to roll: '))
listorsum = int(input('Enter 0 if you would like to see a list of what each die rolled or \nEnter 1 if you would like '
                      'to see the sum of the dice rolled also: '))
for i in range(dice_count):
    dice_list.append(random.randint(1, dice_roll))

if listorsum == 0:
    print(dice_list)

elif listorsum == 1:
    for i in dice_list:
        dice_sum += i
    print(dice_list)
    print(dice_sum)
