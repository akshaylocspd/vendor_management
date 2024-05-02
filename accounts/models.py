from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
import uuid

class VendorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a Vendor with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        vendor = self.model(email=email, **extra_fields)
        vendor.set_password(password)
        vendor.save(using=self._db)
        return vendor

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password=password, **extra_fields)

class Vendor(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, editable=False)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = VendorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'contact_details', 'address', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

    def calculate_on_time_delivery_rate(self):
        completed_orders = self.purchaseorder_set.filter(status='completed')
        if not completed_orders.exists():
            return 0.0
        on_time_deliveries = completed_orders.filter(delivery_date__lte=timezone.now()).count()
        return (on_time_deliveries / completed_orders.count()) * 100

    def calculate_quality_rating_avg(self):
        completed_orders = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        if not completed_orders.exists():
            return 0.0
        quality_ratings = completed_orders.aggregate(avg_quality=models.Avg('quality_rating'))
        return quality_ratings['avg_quality']

    def calculate_average_response_time(self):
        acknowledged_orders = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        if not acknowledged_orders.exists():
            return 0.0
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() / 60
                          for order in acknowledged_orders]
        return sum(response_times) / len(response_times)    

    def calculate_fulfillment_rate(self):
        total_orders = self.purchaseorder_set.count()
        if total_orders == 0:
            return 0.0
        fulfilled_orders = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        return (fulfilled_orders.count() / total_orders) * 100

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = str(uuid.uuid4())[:8].upper()  # Generate a random unique code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
