from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Event
from .serializers import EventSerializer

class EventListView(APIView):

    def get(self, _request):
        events = Event.objects.all()
        serialized_events = EventSerializer(events, many=True)
        return Response(serialized_events.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        event_to_add = EventSerializer(data=request.data)
        try:
            event_to_add.is_valid()
            event_to_add.save()
            return Response(event_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    
class EventDetailView(APIView):
    
    def get_event(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise NotFound(detail="Cannot find an event with that primary key")
        
    def get(self, _request, pk):
        event = self.get_event(pk=pk)
        serialized_single_event = EventSerializer(event)
        return Response(serialized_single_event.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        event_to_edit = self.get_event(pk=pk)
        updated_event = EventSerializer(event_to_edit, data=request.data)
        try:
            updated_event.is_valid()
            updated_event.save()
            return Response(updated_event.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        event_to_delete = self.get_event(pk=pk)
        event_to_delete.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
