def print_menu(ShoppingCart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")
    while 1:
        user_char = input("Choose an option:\n")
        if user_char == "q":
            break
        elif user_char == "a":
            ShoppingCart.add_item(ItemToPurchase(input("Enter name:\n"),float(input("Enter price:\n")),int(input("Enter quantity:\n")),input("Enter description\n")))
        elif user_char == 'r':
            item_name = input("Enter item name\n")
            ShoppingCart.remove_item(item_name)
        elif user_char == "c":
            ShoppingCart.modify_item(ItemToPurchase(input("Enter name:\n"),float(input("Enter price:\n")),int(input("Enter quantity:\n")),input("Enter description\n")))
        elif user_char == "i":
            ShoppingCart.print_descriptions()
        elif user_char == "o":
           ShoppingCart.print_total()
        else:
            print("Please enter a valid character\n")
            print_menu(ShoppingCart)

class ShoppingCart:
    
    def __init__(self,name = "none",date = "January 1, 2020"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []
    
    #Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print(ItemToPurchase.name,"added to shopping cart.\n")
    
    #Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    #If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, ItemName):
        for item in self.cart_items:
            if item.name == ItemName:
                self.cart_items.remove(item)
                print(item.name, "removed from cart\n")
                return
        print("Item not found in cart. Nothing removed.\n")
            
    #Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    #If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
    #If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self,ItemToPurchase):    
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                if ItemToPurchase.price != 0 and ItemToPurchase.quantity != 0 and ItemToPurchase.total != 0:
                    item_index = self.cart_items.index(item)
                    self.cart_items[item_index] = ItemToPurchase
                    print(ItemToPurchase.name, "modified.\n")
                    return
        print("Item not found in cart. Nothing modified.\n")
        
    #Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        total_num = 0
        for item in self.cart_items:
            total_num += item.quantity
        return total_num

    #Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    #Outputs total of objects in cart.
    #If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        if len(self.cart_items) > 0:
            print("\nOUTPUT SHOPPING CART")
            print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
            print("Number of Items:",self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_cost()
            print("Total: ${:.2f}\n".format(self.get_cost_of_cart()))
        else:
            print("SHOPPING CART IS EMPTY\n")
        
    #Outputs each item's description.
    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")
        print()

class ItemToPurchase:
    
    name = "none"
    price = 0
    quantity = 0
    total = 0
    description = "no description"
    
    def __init__ (self,name,price,quantity,description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = self.quantity * self.price
        self.description = description
        
    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.name,self.quantity,self.price,self.total))    

name = input("Enter customer's name:\n")
date = input("Enter today's date:\n")
print("Customer name:", name)
print("Today's date:", date,"\n")


Cart1 = ShoppingCart(name,date)
print_menu(Cart1)

