class ShoppingList:
    def __init__(self):
        self.items = []
        
    def add_product(self):
        item= input('Enter item: ')
        quantity = input('Enter # of items: ')
        

        new_product = product(item, quantity)
        self.items.append(new_product)


    def delete_product(self):
        delete_item = input('Enter item to delete: ')

        for i in range(len(self.items)):
            if self.items[i].item.lower() == delete_item.lower():
                self.items.pop(i)
                print('Product Deleted')
                return
            
            print(f'{delete_item} was not found.')
    def print_items(self):
        for item in self.items:
            print(f'{item.item}')
            print(f'quantity: {item.quantity}')
    
    def run(self):
        while True:
            user_choice = input('What would you like to do? (add/delete/show/quit)').lower()

            if user_choice == 'add':
                self.add_product()
            elif user_choice == 'delete':
                self.delete_product()
            elif user_choice == 'show':
                self.print_items()
            elif user_choice == 'quit':
                self.print_items()
                return
            else:
                print('That was not valid input, please try again.')



class product:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

# Erms_book =AddressBook() #instantiate Class
# Erms_book.add_contact()  #Call method
# print(Erms_book.contacts) #Check that method actually worked
# Erms_book.delete_contact()
# print(Erms_book.contacts)


my_list= ShoppingList()
my_list.run()
print()