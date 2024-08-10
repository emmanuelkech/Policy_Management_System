# We Import the classes for policyholder, product, and payment
from policyholder_class import Policyholder
from product_class import Product
from payment_class import Payment

# Create product
product1 = Product("Car Insurance", "PRD001", 5000)

# Register product
product1.create_product()

# Create two policyholders
policyholder1 = Policyholder("Kevin Hart", "P001")
policyholder2 = Policyholder("Dwayne Johnson", "P002")

# Register policyholders
policyholder1.register_policyholder()
policyholder2.register_policyholder()

# Process payment for both policyholders
payment1 = Payment("Kevin Hart", "Car Insurance", 5000)
payment1.process_payment()
payment2 = Payment("Dwayne Johnson", "Car Insurance", 5000)
payment2.process_payment()

# Display payment status
print(payment1.get_payment_status())
print(payment2.get_payment_status())

# Display policyholders' details
print(policyholder1.get_details())
print(policyholder2.get_details())
