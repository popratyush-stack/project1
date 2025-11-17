print('='*40)
invoice_no=7
customer_name= 'john doe'
amount= 199.99
snap='invoice'
result=snap.upper().center(40)
print(result)
print (f'Invoice No:INV-{str(invoice_no).rjust(5,'0')}'.center(35))
print(f'Costumer:{customer_name.title()}'.center(35))
print(f'Amount:${amount:3f}'.center(35))
print('='*40)