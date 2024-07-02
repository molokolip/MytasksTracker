from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import MytasksSerializer

# import the Todo model from the models file
from .models import Mytasks

# create a class for the Todo model viewsets
class MytasksView(viewsets.ModelViewSet):

	# create a serializer class and 
	# assign it to the TodoSerializer class
	serializer_class = MytasksSerializer

	# define a variable and populate it 
	# with the Tasks list objects
	queryset = Mytasks.objects.all()
