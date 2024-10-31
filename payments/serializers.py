# payments/serializers.py
from rest_framework import serializers
from management.models import Course
from rest_framework import serializers
from .models import Order, Course
from management.serializers import CourseSerializer

class OrderSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id','user', 'course', 'tran_id', 'amount', 'ordered', 'order_date']
