from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Knowledgedomain, Module, Concept


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ConceptSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Concept
        fields = ['url', 'idconcept', 'nameconcept', 'fk_idknowledgedomain',
                  'fk_idmodule']


class SubModuleSerializer(serializers.HyperlinkedModelSerializer):
    concepts = ConceptSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'concepts']


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    submodules = SubModuleSerializer(many=True, read_only=True)
    concepts = ConceptSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'submodules', 'concepts']


class KnowledgedomainSerializer(serializers.HyperlinkedModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Knowledgedomain
        fields = ['url', 'idknowledgedomain', 'nameknowledgedomain',
                  'subtitle', 'lastversion', 'author', 'modules']
