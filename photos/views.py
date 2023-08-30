from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Photo
from .serializers import PhotoSerializer

class PhotoListView(APIView):

    def get(self, _request):
        allphoto = Photo.objects.all()
        serialized_photo = PhotoSerializer(allphoto, many=True)
        return Response(serialized_photo.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        photo_to_add = PhotoSerializer(data=request.data)
        try:
            photo_to_add.is_valid()
            photo_to_add.save()
            return Response(photo_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    
class PhotoDetailView(APIView):
    
    def get_photo(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound(detail="Cannot find any photo with that primary key")
        
        
    def delete(self, _request, pk):
        photo_to_delete = self.get_photo(pk=pk)
        photo_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
