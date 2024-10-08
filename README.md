Bank App

Description
The Bank App is a Django-based backend application designed to handle basic banking operations. It allows users to create accounts, perform transactions (deposit and withdrawal), and view their transaction history. The application also tracks user login and logout events.

Features
User Authentication

Signup: Users can register by providing a username, email, and password.
Login: Users can log in using their username and password to obtain JWT tokens.
Logout: Users can log out, which is recorded in the login/logout history.
Bank Account Management

Create Account: Users can create a bank account with an initial balance of 0.
Deposit: Users can deposit money into their bank account, which increases the balance.
Withdraw: Users can withdraw money from their bank account, provided there are sufficient funds.
Transaction History: Users can view a history of their transactions, including deposits and withdrawals.
Transaction Management

Create Transaction: Users can create transactions with details about the type (deposit/withdrawal) and amount.
View Transaction History: Users can view a list of all their transactions.
Login/Logout History

Track User Activity: The application records login and logout events along with timestamps.

Installation

Clone the repository:
git clone https://github.com/afnan006/Bank_App.git

Navigate to the project directory:
cd Bank_App

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Apply migrations to set up the database:
python manage.py migrate

Run the development server:
python manage.py runserver


API Endpoints
Signup:

POST /api/signup/
Request Body: { "username": "user", "email": "email@example.com", "password": "password" }
Login:

POST /api/login/
Request Body: { "username": "user", "password": "password" }
Response: Returns JWT tokens for authentication.
Create Account:

POST /api/create-account/
Requires authentication (JWT token).
Create Transaction:

POST /api/transaction/
Requires authentication (JWT token).
Transaction History:

GET /api/transaction-history/
Requires authentication (JWT token).
Login/Logout History:

GET /api/login-logout-history/
Requires authentication (JWT token).
Testing
Use Postman or any other API testing tool to test the endpoints. Ensure that you include the JWT token in the Authorization header for endpoints requiring authentication.

Troubleshooting
OperationalError (no such table): Run python manage.py migrate to apply any pending migrations.
400 Bad Request: Check that required fields are included in your requests and are formatted correctly.

Contact
For any questions or issues, please contact:
Afnan Ahmed
Phone: 8296635241
Email: afnan006cs@gmail.com