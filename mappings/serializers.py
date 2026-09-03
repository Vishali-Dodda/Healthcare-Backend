from rest_framework import serializers
from .models import PatientDoctorMapping


class PatientDoctorMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id",
            "patient",
            "doctor",
            "assigned_at",
        ]
        read_only_fields = [
            "id",
            "assigned_at",
        ]

    def validate(self, data):
        patient = data["patient"]
        doctor = data["doctor"]

        if PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return data