from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import CustomeUser, Parcel, DelveryProof
from .serializers import CustomeUserSerializer, ParcelSerializer, DelveryProofSerializer
from rest_framework.response import Response
import cloudinary.uploader
from .permissions import IsAdmin, AddParcelPermission, DeleteParcelPermission, ReadParcelPermission, ReadUserPermission, DeleteUserPermission, AddUserPermission

   

class CustomeUserViewset(ModelViewSet):
    queryset = CustomeUser.objects.all()
    serializer_class = CustomeUserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AddUserPermission]
        elif self.action == "destroy":
            permission_classes = [DeleteUserPermission]    
        elif self.action in ["list", "retrieve"]:
            permission_classes = [ReadUserPermission]
        else:
            permission_classes = [IsAdmin]    

        return [permissions() for permissions in permission_classes]    

    

class ParcelViewset(ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AddParcelPermission]
        elif self.action == "destroy":
            permission_classes = [DeleteParcelPermission]    
        elif self.action in ["list", "retrieve"]:
            permission_classes = [ReadParcelPermission]
        else:
            permission_classes = [IsAdmin]    

        return [permissions() for permissions in permission_classes]  

class DelveryProofViewset(ModelViewSet):
    queryset = DelveryProof.objects.all()
    serializer_class = DelveryProofSerializer
    def create(self, request, *args, **kwargs):
        file = request.FILES.get("image")
        if not file:
            return Response({"error": "image missing"}, status=400)
        
        upload_result = cloudinary.uploader.upload(file)
        image_url = upload_result["secure_url"]
        
        data ={
            "parcel":request.data.get("parcel"),
            "image":image_url
        } 
        serializer = DelveryProofSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
      

