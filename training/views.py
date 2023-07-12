from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Training
from .serializers import TrainingSerializer

class TrainingListView(APIView):

    def get(self, _request):
        allTraining = Training.objects.all()
        serialized_training = TrainingSerializer(allTraining, many=True)
        return Response(serialized_training.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        training_to_add = TrainingSerializer(data=request.data)
        try:
            training_to_add.is_valid()
            training_to_add.save()
            return Response(training_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    
class TrainingDetailView(APIView):
    
    def get_training(self, pk):
        try:
            return Training.objects.get(pk=pk)
        except Training.DoesNotExist:
            raise NotFound(detail="Cannot find any training with that primary key")
        
    def get(self, _request, pk):
        training = self.get_training(pk=pk)
        serialized_single_training = TrainingSerializer(training)
        return Response(serialized_single_training.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        training_to_edit = self.get_training(pk=pk)
        updated_training = TrainingSerializer(training_to_edit, data=request.data)
        try:
            updated_training.is_valid()
            updated_training.save()
            return Response(updated_training.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        training_to_delete = self.get_training(pk=pk)
        training_to_delete.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
