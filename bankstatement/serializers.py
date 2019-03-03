from rest_framework import routers, serializers, viewsets
from . models import files

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = files
        #fields = ('firstname', 'lastname', 'files_id')
        fields = '__all__'