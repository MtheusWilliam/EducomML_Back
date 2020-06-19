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


class AnswersalternativesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answersalternatives
        fields = ['url', 'idanswersalternatives', 'idobjanswer',
                  'answers', 'istrue', 'fk_idquestion', 'orderansweralternatives']


class ResolutionquestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resolutionquestion
        fields = ['url', 'idresolutionquestion', 'correctitem',
                  'correctanswer', 'fk_idquestion']


class QuestiontypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questiontype
        fields = ['url', 'idquestiontype', 'namequestiontype']


class MediatypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mediatype
        fields = ['url', 'idmediatype', 'namemediatype']


class MobilemediaSerializer(serializers.HyperlinkedModelSerializer):
    mediatypes = MediatypeSerializer(many=True, read_only=True)

    class Meta:
        model = Mobilemedia
        fields = ['url', 'idmobilemedia', 'label', 'fk_informationitem', 'fk_idmediatype', 'fk_idknowledgedomain', 'fk_module', 'fk_idinstructionalelement', 'fk_idconcept', 'fk_idquestion',
                  'difficultyLevel', 'learningStyle', 'path', 'namefile', 'resolution', 'description', 'time', 'textfull', 'textshort', 'urllink', 'mediatypes']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    resolutionquestion = ResolutionquestionSerializer(
        many=True, read_only=True)
    answersalternatives = AnswersalternativesSerializer(
        many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(
        many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['url', 'idquestion', 'orderquestion', 'descriptionquestion',
                  'typequestion', 'fk_idinstructionalelement', 'resolutionquestion', 'answersalternatives', 'mobilemedias']


class InstrucelementtypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrucelementtype
        fields = ['url', 'idinstrucelementtype', 'nameinstrucelementtype',
                  'idcategory']


class InstructionalelementSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(
        many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(
        many=True, read_only=True)

    class Meta:
        model = Instructionalelement
        fields = ['url', 'idinstructionalelement', 'label', 'fk_instructionalelementtype', 'fk_idknowledgedomain',
                  'fk_idmodule', 'fk_idconcept', 'fk_informationitem', 'memberamount', 'description', 'questions', 'mobilemedias']


class PhaseprocedureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phaseprocedure
        fields = ['url', 'idphaseprocedure', 'order',
                  'description', 'fk_informationitem']


class InformationitemtypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Informationitemtype
        fields = ['url', 'idinformationitemtype',
                  'nameinformationitemtype']


class InformationitemSerializer(serializers.HyperlinkedModelSerializer):
    informationitemtypes = InformationitemtypeSerializer(
        many=True, read_only=True)
    phaseprocedures = PhaseprocedureSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Informationitem
        fields = ['url', 'idinformationitem', 'nameinformationitem',  'descriptioninformationitem',
                  'fk_informationitemtype', 'fk_idconcept', "informationitemtypes", 'phaseprocedures']


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
    informationitems = InformationitemSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)

    class Meta:
        model = Concept
        fields = ['url', 'idconcept', 'nameconcept', 'fk_idknowledgedomain',
                  'fk_idmodule', 'sourceconcept', 'targetconcept', 'mobilemedias', 'informationitems', 'instructionalelements']


class SubModuleSerializer(serializers.HyperlinkedModelSerializer):
    concepts = ConceptSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'concepts', 'mobilemedias', 'instructionalelements']


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    submodules = SubModuleSerializer(many=True, read_only=True)
    concepts = ConceptSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'submodules', 'concepts', 'mobilemedias', 'instructionalelements']


class KnowledgedomainSerializer(serializers.HyperlinkedModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)

    class Meta:
        model = Knowledgedomain
        fields = ['url', 'idknowledgedomain', 'nameknowledgedomain',
                  'subtitle', 'lastversion', 'author', 'modules', 'mobilemedias', 'instructionalelements']
