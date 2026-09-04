from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many = True)

        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    def post(self, request):
        serializer = DoctorSerializer(data = request.data)

        if serializer.is_valid():
            doctor = serializer.save()

            return Response(
                DoctorSerializer(doctor).data,
                status = status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_doctor(self, pk):
        try:
            return Doctor.objects.get(id=pk)
        except Doctor.DoesNotExist:
            return None

    def get(self, request, pk):
        doctor = self.get_doctor(pk)

        if doctor is None:
            return Response(
                {"error": "Doctor not found."},
                status = status.HTTP_404_NOT_FOUND
            )

        serializer = DoctorSerializer(doctor)
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    def put(self, request, pk):
        doctor = self.get_doctor(pk)

        if doctor is None:
            return Response(
                {"error": "Doctor not found."},
                status = status.HTTP_404_NOT_FOUND
            )

        serializer = DoctorSerializer(
            doctor,
            data = request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        doctor = self.get_doctor(pk)

        if doctor is None:
            return Response(
                {"error": "Doctor not found."},
                status = status.HTTP_404_NOT_FOUND
            )

        doctor.delete()

        return Response(
            status = status.HTTP_204_NO_CONTENT
        )
    
