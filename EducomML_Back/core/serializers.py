from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MediatypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mediatype
        fields = ['url', 'idmediatype', 'namemediatype']


class MobilemediaSerializer(serializers.HyperlinkedModelSerializer):
    mediatypes = MediatypeSerializer(many=True, read_only=True)

    class Meta:
        model = Mobilemedia
        fields = ['url', 'idmobilemedia', 'label', 'fk_informationitem', 'fk_idmediatype', 'fk_idknowledgedomain', 'fk_module', 'fk_idinstructionalelement', 'fk_idconcept',
                  'difficultyLevel', 'learningStyle', 'path', 'namefile', 'resolution', 'description', 'time', 'textfull', 'textshort', 'urllink', 'mediatypes']


class ReferencetypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Referencetype
        fields = ['url', 'idreferencetype', 'namererefencetype']


class ReferenceSerializer(serializers.HyperlinkedModelSerializer):
    referencetypes = ReferencetypeSerializer(many=True, read_only=True)

    class Meta:
        model = Reference
        fields = ['url', 'idreference', "namereference", 'sourceconcept',
                  'targetconcept', 'fk_referencetype', "referencetypes"]


class ConceptSerializer(serializers.HyperlinkedModelSerializer):
    sourceconcept = ReferenceSerializer(many=True, read_only=True)
    targetconcept = ReferenceSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)

    class Meta:
        model = Concept
        fields = ['url', 'idconcept', 'nameconcept', 'fk_idknowledgedomain',
                  'fk_idmodule', 'sourceconcept', 'targetconcept', 'mobilemedias']


class SubModuleSerializer(serializers.HyperlinkedModelSerializer):
    concepts = ConceptSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'concepts', 'mobilemedias']


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    submodules = SubModuleSerializer(many=True, read_only=True)
    concepts = ConceptSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'submodules', 'concepts', 'mobilemedias']


class KnowledgedomainSerializer(serializers.HyperlinkedModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)

    class Meta:
        model = Knowledgedomain
        fields = ['url', 'idknowledgedomain', 'nameknowledgedomain',
                  'subtitle', 'lastversion', 'author', 'modules', 'mobilemedias']
