from urllib.parse import urlencode
from rest_framework import generics, status
from .models import Event, Student, Registration
from .serializers import EventSerializer,  StudentSerializer, RegistrationSerializer

import requests

from Functions.url_helpers import sign_url
from django.conf import settings
from rest_framework.response import Response


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        address_key = settings.GOOGLE_ADDRESS_VALIDATION_KEY
        signing_secret = settings.GOOGLE_ADDRESS_VALIDATION_SECRET

        # Extract address fields from the request
        address = {
            "addressLines": [request.data.get("street_address", "").rstrip(",")],
            "regionCode": "US",
            "locality": request.data.get("city", "").rstrip(","),
            "administrativeArea": request.data.get("state", "").rstrip(","),
            "postalCode": request.data.get("zip_code", "").strip(),
        }

        # Prepare the Address Validation API request
        base_url = "https://addressvalidation.googleapis.com/v1:validateAddress"
        params = {
            "key": address_key,
        }
        

        url = f'{base_url}?{urlencode(params)}'

        # Make the API request
        response = requests.post(url, json={"address": address})
        google_data = response.json()

        # Check if the address is valid
        verdict = google_data.get("result", {}).get("verdict", {})
        if not verdict.get("addressComplete", False):
            return Response(
                {
                    "error": "Invalid or incomplete address. Please provide a valid address.",
                    "address": f'{address}',
                    "signed_url": f'{url}',
                    "address_key": f'{address_key}',
                    "secret": f'{signing_secret}',
                    'full_response': f'{google_data}'
                 },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # if valid -> save the student
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class RegistrationListCreateView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
