# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Mytasks

# create a serializer class
class MytasksSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Mytasks
		fields = ('id', 'title','description','completed')
