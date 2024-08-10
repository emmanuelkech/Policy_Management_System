# Initialize a new payment with the policyholder's name, product name, and amount
class Payment:
    def __init__(self, policyholder_name, product_name, amount):        
        self.policyholder_name = policyholder_name
        self.product_name = product_name
        self.amount = amount
        self.is_paid = True 
    
    # Method to process the payment
    def process_payment(self):
        try:
            if self.amount <= 0:
                raise ValueError("Payment amount must be positive.")
            print(f"Payment of ${self.amount} for {self.policyholder_name} on {self.product_name} processed successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Method to send a payment reminder if the payment is unpaid
    def send_reminder(self):        
        if not self.is_paid:
            print(f"Reminder: Payment of ${self.amount} is due for {self.policyholder_name} on {self.product_name}.")
    
    # Method to apply a penalty to the payment amount
    def apply_penalty(self, penalty_amount):
        try:
            if penalty_amount <= 0:
                raise ValueError("Penalty amount must be positive.")
            self.amount += penalty_amount
            print(f"Penalty of ${penalty_amount} applied. New amount: ${self.amount}.")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Method to get the current status of the payment
    def get_payment_status(self):        
        status = "Paid" if self.is_paid else "Unpaid"
        return f"Policyholder: {self.policyholder_name}, Product: {self.product_name}, Amount: ${self.amount}, Status: {status}"
