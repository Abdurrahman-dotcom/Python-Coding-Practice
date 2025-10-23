print('Bill Split Calculator')

bill_amount = float(input())
tip_percentage = float(input())
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
total_amount = bill_amount + tip_amount
print(f'Total (including tip): ${total_amount}')
people = int(input())
per_person = total_amount / people
print(f'Each person pays: ${per_person}')