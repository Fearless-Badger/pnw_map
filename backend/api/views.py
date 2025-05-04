from urllib.parse import urlencode
from rest_framework import generics, status
from .models import Event, Student, Registration
from .serializers import EventSerializer,  StudentSerializer, RegistrationSerializer
from django.contrib.auth.hashers import check_password

import requests
import traceback

from Functions.url_helpers import sign_url
from Functions.helpers import validate_address_format

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view



class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        address_key = settings.GOOGLE_ADDRESS_VALIDATION_KEY

        # Extract address fields from the request
        address = {
            "addressLines": [request.data.get("street_address", "").rstrip(",")],
            "regionCode": "US",
            "locality": request.data.get("city", "").rstrip(","),
            "administrativeArea": request.data.get("state", "").rstrip(","),
            "postalCode": request.data.get("zip_code", "").strip(),
        }

        # Validate the address using the helper function
        verdict, google_data = validate_address_format(address, address_key)

        # Check if the address is valid
        if not verdict.get("addressComplete", False):
            return Response(
                {
                    "result": False,
                    "message": "Invalid or incomplete address. Please provide a valid address.",
                    "address": f'{address}',
                    "full_response": f'{google_data}'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # If valid -> save the student
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "result": True,
                "message": "",
                "address": f'{address}',
                "full_response": f'{google_data}',
                'serializer_data': f'{serializer.data}'
            },
            status=status.HTTP_201_CREATED
        )

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class RegistrationListCreateView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

@api_view(['POST'])
def register_student(request):
    try:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"Error in register_student: {str(e)}")
        print(traceback.format_exc())
        return Response(
            {"error": str(e), "detail": "An error occurred while processing your request"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def login_student(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response(
                {"error": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        if check_password(password, student.password):
            # Return student data (excluding password)
            return Response({
                "student_id": student.student_id,
                "email": student.email,
                "fname": student.fname,
                "lname": student.lname
            })
        else:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )
    except Exception as e:
        print(f"Error in login_student: {str(e)}")
        print(traceback.format_exc())
        return Response(
            {"error": str(e), "detail": "An error occurred while processing your request"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
