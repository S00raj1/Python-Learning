from typing import List
def print_item_row(sn, item: "Item"):
    print(f'|  {sn: 2d}  {item.name.ljust(22)}  {item.rate: 8.1f}  {item.quantity: 8.1f}  {item.total(): 8.1f}  |')

class Item:
    name:str
    rate:float
    quantity:float
    def __init__(self,name,rate,quantity):
        self.name = name
        self.rate = rate
        self.quantity = quantity

    def total(self):
        return self.rate*self.quantity


class Bill:
    customer_name:str= input('Enter your name:')
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.items:List[Item] = []

    def grand_total(self):
        return sum([i.total() for i in self.items])
    def add_items(self,item:Item):
        self.items.append(item)
    def print_invoice(self):
        print('+','-'*60,'+',sep='')
        print('|', 'Suraj Mart'.center(60),'|',sep='')

        print('|','.'*60,'|',sep='')
        print('|',f' Order Invoice For: {self.customer_name}'.ljust(60),'|',sep='')
        print('|','.'*60,'|',sep='')

        print(f'| SN {"name".ljust(22)}  {"rate".rjust(8)} {"Quantity".rjust(15)} {"total".rjust(6)} |')
        print('|', '.' * 60, '|', sep='')
        for i,j in enumerate(self.items):
            print_item_row(i,j)
        print('|', '.' * 60, '|', sep='')
        print('|'.ljust(41),f'Grand Total:   {self.grand_total()} '.rjust(0),'|',sep='')
        print('|', '.' * 60, '|', sep='')
        print('|', 'Thank You for visiting Suraj Mart'.center(50), '|'.rjust(9))
        print('+', '.' * 60, '+', sep='')



bill = Bill(customer_name=Bill.customer_name)
bill.add_items(Item('Rice',2.4,5))
bill.add_items(Item('Apple',1,1))
bill.add_items(Item('Notebook',3,1.5))
bill.print_invoice()


