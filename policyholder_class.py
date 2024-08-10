# Initialize a new policyholder with a name and policy number
class Policyholder:
    def __init__(self, name, policy_number):        
        self.name = name
        self.policy_number = policy_number
        self.is_active = True  

    # Method to register a new policyholder  
    def register_policyholder(self):
        try:
            if not self.name or not self.policy_number:
                raise ValueError("Name and Policy Number are required to register a policyholder.")
            self.active = True
            print(f"Policyholder {self.name} with policy number {self.policy_number} registered successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Method to suspend an existing policyholder
    def suspend_policyholder(self):
        try:
            if not self.active:
                raise Exception("Policyholder is not active and cannot be suspended.")
            self.active = False
            print(f"Policyholder {self.name} with policy number {self.policy_number} has been suspended.")
        except Exception as e:
            print(f"Error: {e}")
    
    # Method to reactivate a suspended policyholder
    def reactivate_policyholder(self):
        try:
            if self.active:
                raise Exception("Policyholder is already active.")
            self.active = True
            print(f"Policyholder {self.name} with policy number {self.policy_number} has been reactivated.")
        except Exception as e:
            print(f"Error: {e}")
    
    # Method to get the details of the policyholder
    def get_details(self):        
        status = "Active" if self.is_active else "Suspended"
        return f"Name: {self.name}, Policy Number: {self.policy_number}, Status: {status}"
    