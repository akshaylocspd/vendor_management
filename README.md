# Vendor Management System using Django and Django REST Framework
<!-- ```markdown -->

This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## How to Run This Django Project

### Step 1: Clone the Project

Clone this project using the following command:

```bash
git clone https://github.com/akshaylocspd/vendor_management.git
```

### Step 2: Navigate to the Project Directory

```bash
cd vendor_management
```

### Step 3: Set Up Virtual Environment

Create a virtual environment and activate it by using the following commands. Ensure you have Python (3.11.7) installed:

```bash
pip install virtualenv
virtualenv venv

# On Windows:
source venv/Scripts/activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Necessary Python Packages

Install necessary Python packages by running:

```bash
pip install -r requirements.txt
```

### Step 5: Set Up the Database and Run Migrations

Set up the database (if applicable) and run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser Account

Create a superuser account to access the admin panel (if needed):

```bash
python manage.py createsuperuser
```

### Step 7: Run the Django Application

Finally, run the Django application using the following command:

```bash
python manage.py runserver
```

If you encounter any migration-related problems, ensure your database settings are correct and then rerun the migration commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

Now, you should be able to access the Vendor Management System at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.
```


```
# API Documentation: Vendor Management
## Please download the Postman API collection so that you can easily test the APIs below. 

[Click here to download the thunder-collection_Purchase_Order.json file](/thunder-collection_Purchase_Order.json)

[Click here to download the thunder-collection_Vendor_Management.json file](/thunder-collection_Vendor_Management.json)

## 1. Create Vendor
- **URL:** http://127.0.0.1:8000/api/vendors/
- **Method:** POST
- **Request Body:**
  ```json
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
  ```
- **Authentication:**
  - Type: Bearer Token
  - Token: []

## 2. Update Vendor
- **URL:** http://127.0.0.1:8000/api/vendors/{vendor_id}/
- **Method:** PUT
- **Request Body:**
  ```json
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
  ```
- **Authentication:** (same as above)

## 3. Get All Vendors List
- **URL:** http://127.0.0.1:8000/api/vendors/
- **Method:** GET
- **Authentication:** (same as above)

## 4. Get Particular Vendor by ID
- **URL:** http://127.0.0.1:8000/api/vendors/{vendor_id}/
- **Method:** GET
- **Authentication:** (same as above)

## 5. Delete Particular Vendor by ID
- **URL:** http://127.0.0.1:8000/api/vendors/{vendor_id}/
- **Method:** DELETE
- **Authentication:** (same as above)

## 6. Retrieve Performance Metrics for a Vendor with ID
- **URL:** http://localhost:8000/api/vendors/{vendor_id}/performance/
- **Method:** GET
- **Authentication:** (same as above)

---

# API Documentation: Purchase Order

## 1. Create a Purchase Order
- **URL:** http://localhost:8000/api/purchase_orders/
- **Method:** POST
- **Authentication:** Bearer Token
- **Request Body:**
  ```json
  {
      "vendor": 17,
      "order_date": "2024-04-30T12:00:00",
      "delivery_date": "2024-05-30T12:00:00",
      "items": {"item1": "description1", "item2": "description2"},
      "quantity": 10,
      "status": "pending"
  }
  ```
- **Response:** JSON

## 2. List all Purchase Orders
- **URL:** http://localhost:8000/api/purchase_orders/
- **Method:** GET
- **Authentication:** Bearer Token
- **Response:** JSON Array
- **Authentication:** (same as above)

## 3. Filtering by Vendor
- **URL:** http://localhost:8000/api/purchase_orders/?vendor_id=17
- **Method:** GET
- **Authentication:** Bearer Token
- **Parameters:**
  - vendor_id: ID of the vendor to filter by
- **Response:** JSON Array

## 4. Retrieve Details of a Specific Purchase Order
- **URL:** http://localhost:8000/api/purchase_orders/{po_id}/
- **Method:** GET
- **Authentication:** Bearer Token
- **Response:** JSON

## 5. Update a Purchase Order
- **URL:** http://localhost:8000/api/purchase_orders/{po_id}/
- **Method:** PUT
- **Authentication:** Bearer Token
- **Request Body:**
  ```json
  {
      "vendor": 17,
      "order_date": "2024-04-30T12:00:00",
      "delivery_date": "2024-05-30T12:00:00",
      "items": {"item1": "description1", "item2": "description4"},
      "quantity": 20,
      "status": "completed"
  }
  ```
- **Response:** JSON

## 6. Delete a Purchase Order
- **URL:** http://localhost:8000/api/purchase_orders/7/
- **Method:** DELETE
- **Authentication:** Bearer Token
- **Response:** Success/Failure Message

## 7. Update Acknowledgment
- **URL:** http://localhost:8000/api/purchase_orders/{po_id}/acknowledge/
- **Method:** PUT
- **Authentication:** Bearer Token
- **Response:** JSON
- **Authentication:** (same as above)
```
