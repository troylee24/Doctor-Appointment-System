from .models import Appointment, Doctor, Patient
from .serializers import AppointmentSerializer, DoctorSerializer, PatientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django_filters import rest_framework as filters

@api_view(['GET'])
def api_root(request):
    return Response({
        'doctors': reverse('doctor-list', request=request),
        'patients': reverse('patient-list', request=request),
        'appointments': reverse('appointment-list', request=request)
    })

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentFilter(filters.FilterSet):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'time', 'kind']

class AppointmentList(mixins.ListModelMixin, generics.GenericAPIView):  
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppointmentFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            doctor = serializer.validated_data.get('doctor')
            date = serializer.validated_data.get('date')
            time = serializer.validated_data.get('time').strftime(format="%H:%M")
            same_day_time_apps = Appointment.objects.filter(doctor=doctor, date=date, time=time)
            if same_day_time_apps.count() == 3:
                return Response(
                    {'doctor': ["Doctor already has 3 appointments scheduled at {}, {}".format(time ,date)]},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save(time=time)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Appointment.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer