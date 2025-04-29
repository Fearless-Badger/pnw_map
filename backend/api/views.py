from urllib.parse import urlencode
from rest_framework import generics, status
from .models import Event, Student, Registration
from .serializers import EventSerializer,  StudentSerializer, RegistrationSerializer

import requests

from Functions.url_helpers import sign_url
from Functions.helpers import validate_address_format


from django.conf import settings
from rest_framework.response import Response



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
