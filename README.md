Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

Q: How to run this Django Project?

Ans:

Step 1: Clone this project using the following command:

git clone https://github.com/akshaylocspd/vendor_management.git

Step 2:

cd vendor_management

Step 3: Create a virtual environment and activate it by using the following commands. Ensure you have Python (3.11.7) installed:

pip install virtualenv
virtualenv venv

# On Windows:
source venv/Scripts/activate

# On macOS/Linux:
source venv/bin/activate

Step 4: Install necessary Python packages by running:

pip install -r requirements.txt

Step 5: Set up the database (if applicable) and run migrations:

python manage.py makemigrations

python manage.py migrate

Step 6: Create a superuser account to access the admin panel (if needed):

python manage.py createsuperuser

Step 7: Finally, run the Django application using the following command:

python manage.py runserver

If you encounter any migration-related problems, ensure your database settings are correct and then rerun the migration commands:

python manage.py makemigrations

python manage.py migrate

Now, you should be able to access the Vendor Management System at http://127.0.0.1:8000/ in your web browser.



/**********************************************************/

# API Documentation: Vendor Management

1.Create Vendor:
URL: http://127.0.0.1:8000/api/vendors/
Method: POST
Request Body:
{
    "email": "newvendor@example.com",
    "password": "password123",
    "name": "newvendor",
    "contact_details": "1234567890",
    "address": "123 Main St, City",
    "on_time_delivery_rate": 95.5,
    "quality_rating_avg": 4.5,
    "average_response_time": 24.5,
    "fulfillment_rate": 98.2
}
Authentication:
Type: Bearer Token
Token: 

2.Update Vendor:
URL: http://127.0.0.1:8000/api/vendors/17/
Method: PUT
Request Body:
{
    "email": "googlemail@example.com",
    "password": "password",
    "name": "updated Name",
    "contact_details": "New Contact Details",
    "address": "New Address",
    "on_time_delivery_rate": 90.5,
    "quality_rating_avg": 4.0,
    "average_response_time": 20.0,
    "fulfillment_rate": 95.0
}
Authentication:
Type: Bearer Token
Token: 

3.Get All Vendors List:
URL: http://127.0.0.1:8000/api/vendors/
Method: GET
Authentication:
Type: Bearer Token
Token: 

4.Get Particular Vendor by ID:
URL: http://127.0.0.1:8000/api/vendors/14/
Method: GET
Authentication:
Type: Bearer Token
Token: 

5.Delete Particular Vendor by ID:
URL: http://127.0.0.1:8000/api/vendors/16/
Method: DELETE
Authentication:
Type: Bearer Token
Token: 

6.Retrieve Performance Metrics for a Vendor with ID:
URL: http://localhost:8000/api/vendors/17/performance/
Method: GET
Authentication:
Type: Bearer Token
Token: 




# API Documentation : Purchase Order
1. Create a Purchase Order:
URL: http://localhost:8000/api/purchase_orders/
Method: POST
Authentication: Bearer Token
Request Body:json
{
    "vendor": 17,
    "order_date": "2024-04-30T12:00:00",
    "delivery_date": "2024-05-30T12:00:00",
    "items": {"item1": "description1", "item2": "description2"},
    "quantity": 10,
    "status": "pending"
}

Response: JSON

2. List all Purchase Orders:
URL: http://localhost:8000/api/purchase_orders/
Method: GET
Authentication: Bearer Token
Response: JSON Array
Authentication:
Type: Bearer Token
Token: 



3. Filtering by Vendor:
URL: http://localhost:8000/api/purchase_orders/?vendor_id=17
Method: GET
Authentication: Bearer Token
Parameters:
vendor_id: ID of the vendor to filter by
Response: JSON Array

4.Retrieve Details of a Specific Purchase Order:
URL: http://localhost:8000/api/purchase_orders/16/
Method: GET
Authentication: Bearer Token
Response: JSON

5.Update a Purchase Order:
URL: http://localhost:8000/api/purchase_orders/16/
Method: PUT
Authentication: Bearer Token
Request Body: json
{
    "vendor": 17,
    "order_date": "2024-04-30T12:00:00",
    "delivery_date": "2024-05-30T12:00:00",
    "items": {"item1": "description1", "item2": "description4"},
    "quantity": 20,
    "status": "completed"
}
Response: JSON

6.Delete a Purchase Order:
URL: http://localhost:8000/api/purchase_orders/7/
Method: DELETE
Authentication: Bearer Token
Response: Success/Failure Message

7.Update Acknowledgment:
URL: http://localhost:8000/api/purchase_orders/12/acknowledge/
Method: PUT
Authentication: Bearer Token
Response: JSON
Authentication:
Type: Bearer Token
Token: 


