from rest_framework import serializers
from .models import task


# Converts from datatype: Python to datatype: Json

class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = task
        #fields = ('id', 'title', 'description', 'done')
        fields = '__all__' # Takes into account all available fields