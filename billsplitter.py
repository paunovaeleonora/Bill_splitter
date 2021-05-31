import random


def is_it_integer(n):
    if not n.is_integer():
        return round(n, 2)
    return int(n)


def split_the_bill(bill, n):
    split = bill / n
    return is_it_integer(split)


people_going_to_party = []
people_and_bill = {}
number_of_people_joining_the_party = int(input('Enter the number of friends joining(including you):\n'))

if number_of_people_joining_the_party <= 0:
    print('\nNo one is joining for the party')

else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    people_going_to_party=[input() for _ in range(number_of_people_joining_the_party)]
    total_bill = int(input('\nEnter the total bill value:\n'))

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == 'Yes':
        number_of_people_joining_the_party -= 1
        split_bill = split_the_bill(total_bill, number_of_people_joining_the_party)
        lucky_one = random.choice(people_going_to_party)
        for name in people_going_to_party:
            if name == lucky_one:
                people_and_bill[name] = 0
            else:
                people_and_bill[name] = split_bill

        print(f'\n{lucky_one} is the lucky one!\n')
        print(people_and_bill)

    else:
        split_bill = split_the_bill(total_bill, number_of_people_joining_the_party)
        print('\nNo one is going to be lucky')
        people_and_bill = {friend: split_bill for friend in people_going_to_party}
        print(f'\n{people_and_bill}')
