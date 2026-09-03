from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMapSerializer
from patients.models import Patient

class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PatientDoctorMapSerializer(
            data=request.data
        )

        if serializer.is_valid():
            patient = serializer.validated_data["patient"]

            if patient.user != request.user:
                return Response(
                    {"error": "You can only assign doctors to your own patients."},
                    status=status.HTTP_403_FORBIDDEN
                )

            mapping = serializer.save()

            return Response(
                PatientDoctorMapSerializer(mapping).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = PatientDoctorMapSerializer(
            mappings,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class MappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            patient = Patient.objects.get(
                id=id
            )
        except Patient.DoesNotExist:
            return Response(
                {"error": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if patient.user != request.user:
            return Response(
                {
                    "error": "You can only access mappings for your own patients."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        mappings = PatientDoctorMapping.objects.filter(
            patient=patient
        )

        serializer = PatientDoctorMapSerializer(
            mappings,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, id):
        try:
            mapping = PatientDoctorMapping.objects.get(
                id=id
            )
        except PatientDoctorMapping.DoesNotExist:
            return Response(
                {"error": "Mapping not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if mapping.patient.user != request.user:
            return Response(
                {
                    "error": "You can only remove mappings for your own patients."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        mapping.delete()

        return Response(
            {"message": "Mapping deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )