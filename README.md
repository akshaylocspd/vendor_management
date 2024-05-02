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