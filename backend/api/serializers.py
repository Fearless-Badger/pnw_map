from rest_framework import serializers
from .models import Event, Student, Registration
from django.contrib.auth.hashers import make_password

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'fname', 'mname', 'lname', 'email', 'password', 
                 'street_address', 'city', 'state', 'zip_code']
        extra_kwargs = {
            'password': {'write_only': True},
            'student_id': {'read_only': True}
        }

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
