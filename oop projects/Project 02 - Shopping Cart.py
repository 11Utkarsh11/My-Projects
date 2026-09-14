class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        return f"Name: {self.name}\nPrice: {self.price}"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def all_products(self):
        for product in self.products:
            print(f"Name: {product.name}\nPrice: {product.price}")

    def price_total(self):
        return sum(product.price for product in self.products)

# Create some products

product1 = Product("Keyboard", 2000)
product2 = Product("Mouse", 800)
product3 = Product("Headphones", 1500)


# Create a shopping cart

cart = ShoppingCart()


# Add products to the cart

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

# Display the cart

cart.all_products()


# Calculate total

print(cart.price_total())


# Remove a product

cart.remove_product(product1)


# Display the cart again

cart.all_products()
