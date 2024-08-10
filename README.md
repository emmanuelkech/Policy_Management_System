# Policy Management System for an Insurance Company
*BAN6420 Module 3 Milestone Assignment*

## Overview
This project is a Policy Management System designed for an insurance company to manage policyholders, products, and payments. The system allows policy managers to perform various tasks, such as registering new members, managing policy products, updating and suspending policyholders.

## Features
The project is organized into four main components:
1. **Policyholder Class:** Handles operations related to policyholders. These operations includes registering, suspending, and reactivating policyholders.
2. **Product Class:** Manages insurance products, which includes creating, updating, and suspending products.
3. **Payment Class:** Processes payments, send reminders, and apply penalties.
4. **Demo:** Demonstrates how to use the classes and their methods to manage policyholders, products, and payments.

## Usage
### Policyholder Management
The Policyholder class includes methods to manage policyholders, with error handling for invalid input and actions: </br>
***register_policyholder():*** Register a new policyholder. Raises a ValueError if required fields are missing. </br>
***suspend_policyholder():*** Suspend an existing policyholder. Raises an Exception if the policyholder is not active. </br>
***reactivate_policyholder():*** Reactivate a suspended policyholder. Raises an Exception if the policyholder is already active.

### Product Management
The Product class includes methods to manage products, with error handling for invalid input and actions: </br>
***create_product():*** Create a new product. Raises a ValueError if required fields are missing or if the price is not positive. </br>
***update_product():*** Update the details of an existing product. Raises an Exception if the product is inactive or a ValueError for invalid price updates. </br>
***suspend_product():*** Suspend an existing product. Raises an Exception if the product is already suspended.

### Payment Management
The Payment class includes methods to manage payments, with error handling for invalid input: </br>
***process_payment():*** Process a payment for a policyholder. Raises a ValueError if the payment amount is not positive. </br>
***send_reminder():*** Send a payment reminder to a policyholder. Catches any general exceptions. </br>
***apply_penalty():*** Apply a penalty to a policyholder's payment. Raises a ValueError if the penalty amount is not positive.

### Running the Demo
The demo.py script demonstrates how to utilize the classes and methods provided in this project. Running this script will:
- Create and register an insurance product.
- Create two policyholders.
- Register these policyholders.
- Process payments for the policyholders.
- Display payment status and policyholder details.

## Handling Exceptions
The error handling mechanisms that have been put in place ensure that common mistakes are caught early, while providing informative feedback that guides in resolving the issue.

A *try-except* block has been used to address that might cause an error. If an error happens, the program will print a message that explains what went wrong instead of crashing.

Sometimes, we know that certain things should never happen. For instance, like having a negative price. We can *"raise"* an error to stop the program and print a message, helping us find and fix mistakes.

## Conclusion
This Policy Management System is a practical example of how Python can be used to manage core operations in an insurance company. This includes handling policyholders, products, and payments. 
By following the usage instructions, you can easily run the system on your local machine. 
