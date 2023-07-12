from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Committee
from .serializers import CommitteeSerializer

class CommitteeListView(APIView):

    def get(self, _request):
        committees = Committee.objects.all()
        serialized_committees = CommitteeSerializer(committees, many=True)
        return Response(serialized_committees.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        committee_to_add = CommitteeSerializer(data=request.data)
        try:
            committee_to_add.is_valid()
            committee_to_add.save()
            return Response(committee_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    
class CommitteeDetailView(APIView):
    
    def get_committee(self, pk):
        try:
            return Committee.objects.get(pk=pk)
        except Committee.DoesNotExist:
            raise NotFound(detail="Cannot find a committee member with that primary key")
        
    def get(self, _request, pk):
        committee = self.get_committee(pk=pk)
        serialized_single_committee = CommitteeSerializer(committee)
        return Response(serialized_single_committee.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        committee_to_edit = self.get_committee(pk=pk)
        updated_committee = CommitteeSerializer(committee_to_edit, data=request.data)
        try:
            updated_committee.is_valid()
            updated_committee.save()
            return Response(updated_committee.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        committee_to_delete = self.get_committee(pk=pk)
        committee_to_delete.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
