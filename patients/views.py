from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient
from .serializers import PatientSerializer


class PatientListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.filter(user=request.user)

        serializer = PatientSerializer(patients, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            patient = serializer.save(user=request.user)

            return Response(
                PatientSerializer(patient).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_patient(self, request, pk):
        try:
            return Patient.objects.get(
                id=pk,
                user=request.user
            )
        except Patient.DoesNotExist:
            return None

    def get(self, request, pk):
        patient = self.get_patient(request, pk)

        if patient is None:
            return Response(
                {"error": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PatientSerializer(patient)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        patient = self.get_patient(request, pk)

        if patient is None:
            return Response(
                {"error": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PatientSerializer(
            patient,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        patient = self.get_patient(request, pk)

        if patient is None:
            return Response(
                {"error": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        patient.delete()

        return Response(
            {"message": "Patient deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )