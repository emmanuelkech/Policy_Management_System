# Initialize a new product with a product name, product ID, and premium amount
class Product:
    def __init__(self, product_name, product_id, premium):        
        self.product_name = product_name
        self.product_id = product_id
        self.premium = premium
        self.is_available = True  
    
    # Method to create a new product
    def create_product(self):
        try:
            if not self.product_name or not self.product_id or self.premium <= 0:
                raise ValueError("Product name, product ID, and a positive premium amount are required to create a product.")
            self.active = True
            print(f"Product: {self.product_name} with ID {self.product_id} created successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Method to update the product's name and premium amount
    def update_product(self, new_name=None, new_premium=None):
        try:
            if not self.active:
                raise Exception("Cannot update an inactive product.")
            if new_name:
                self.product_name = new_name
            if new_premium is not None:
                if new_premium <= 0:
                    raise ValueError("Price must be positive.")
                self.premium = new_premium
            print(f"Product: {self.product_name} with ID {self.product_id} has been successfully updated.")
        except (Exception, ValueError) as e:
            print(f"Error: {e}")
    
    # Method to suspend a product. This makes it unavailable
    def suspend_product(self):
        try:
            if not self.is_available:
                raise Exception("Product is already suspended.")
            self.is_available = False
            print(f"Product {self.product_name} with ID {self.product_id} has been suspended.")
        except Exception as e:
            print(f"Error: {e}")
    
    # Method to get the details of the product
    def get_details(self):        
        status = "Available" if self.is_available else "Suspended"
        return f"Product Name: {self.product_name}, Product ID: {self.product_id}, Premium: ${self.premium}, Status: {status}"

