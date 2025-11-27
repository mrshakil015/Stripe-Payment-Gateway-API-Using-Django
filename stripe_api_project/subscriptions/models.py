from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubscriptionPlanModel(models.Model):

    name = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    yearly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    udpated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'{self.name}'


    
class UserSubscriptionModel(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    PLAN_TYPES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_subscription')
    plan = models.ForeignKey('subscriptions.SubscriptionPlanModel', on_delete=models.CASCADE, null=True, related_name='subscriptions')
    plan_type = models.CharField(max_length=10, choices=PLAN_TYPES, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    start_date = models.DateField(null=True)
    expired_date = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    stripe_payment_intent_id = models.CharField(max_length=255, unique=True, null=True)
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=3, default='usd', null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    udpated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'{self.user}-{self.plan.name}'
    
    
    