from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import CustomeUser, Parcel, DelveryProof
from .serializers import CustomeUserSerializer, ParcelSerializer, DelveryProofSerializer
from rest_framework.response import Response

class CustomeUserViewset(ModelViewSet):
    queryset = CustomeUser.objects.all()
    serializer_class = CustomeUserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ParcelViewset(ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class DelveryProofViewset(ModelViewSet):
    queryset = DelveryProof.objects.all()
    serializer_class = DelveryProofSerializer    

