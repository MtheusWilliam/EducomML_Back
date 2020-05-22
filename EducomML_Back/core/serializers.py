from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Knowledgedomain


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class KnowledgedomainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Knowledgedomain
        fields = ['url', 'idknowledgedomain', 'nameknowledgedomain',
                  'subtitle', 'lastversion', 'author']
