from login import login_class
from prettytable import PrettyTable
from  discount import discount
x=input('enter name : ')
y=input('enter password: ')
L1=login_class(x,y)
L1.Login()


products=[ {'name':'water','price':80.0,'quantity':1200},
            {'name':'soda','price':120.0,'quantity':1200},
           {'name':'chips','price':75.0,'quantity':1200},
           {'name':'bread','price':45.0,'quantity':1200},
           {'name':'eggs','price':65.0,'quantity':1200} 
]
table=PrettyTable()
table.field_names=['name','price','quantity']
for product in products:
    table.add_row([product['name'],product['price'],product['quantity']])
print(table)
discount(products)
