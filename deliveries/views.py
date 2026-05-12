from rest_framework.viewsets import ModelViewSet
from .models import CustomeUser, Parcel, DelveryProof
from .serializers import CustomeUserSerializer, ParcelSerializer, DelveryProofSerializer

class CustomeUserViewset(ModelViewSet):
    queryset = CustomeUser.objects.all()
    serializer_class = CustomeUserSerializer

class ParcelViewset(ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class DelveryProofViewset(ModelViewSet):
    queryset = DelveryProof.objects.all()
    serializer_class = DelveryProofSerializer    

