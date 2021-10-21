import random


friends = []
final_data = {}
participants = int(input('Enter the number of friends joining(including you):\n'))
if participants <= 0:
    print('\nNo one is joining for the party')

else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(participants):
        name = input()
        friends.append(name)
    print('\nEnter the total bill value:')
    final_bill = int(input())
    # split_bill = final_bill / participants
    # if not split_bill.is_integer():
    #     split_bill = round(split_bill, 2)
    # else:
    #     split_bill = int(split_bill)
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == 'Yes':
        print(f'\n{random.choice(friends)} is the lucky one!')
    else:
        print('\nNo one is going to be lucky')

    # for friend in friends:
    #     final_data[friend] = split_bill
    # print()
    # print(final_data)
