from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from core.tokens import account_activation_token


class PriorlevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Priorlevel
        fields = ['url', 'idpriorlevel', 'typepriorlevel']


class PriorknowledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Priorknowledge
        fields = ['url', 'idpriorknowledge', 'namepriorknowledge',
                  'priorlevel', 'fk_idconcept']


class RangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Range
        fields = ['url', 'idrange', 'namerange',
                  'fk_idassessmentparameter', 'initialvalue', 'limitvalue']


class SingleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Single
        fields = ['url', 'idsingle', 'fk_idassessmentparameter', 'threshold']


class ScopoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scopo
        fields = ['url', 'idscopo', 'typescopo']


class TypethresholdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Typethreshold
        fields = ['url', 'idtypethreshold', 'nametypethreshold']


class AssessmentparameterSerializer(serializers.HyperlinkedModelSerializer):
    single = SingleSerializer(many=True, read_only=True)
    ranges = RangeSerializer(many=True, read_only=True)

    class Meta:
        model = Assessmentparameter
        fields = ['url', 'idassessmentparameter', 'typethreshold', 'scopo',
                  'fk_idknowledgedomain', 'fk_idmodule', 'fk_idconcept', 'single', 'ranges']


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
                  'difficultyLevel', 'learningStyle', 'visible', 'path', 'namefile', 'resolution', 'description', 'time', 'textfull', 'textshort', 'urllink', 'mediatypes']


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
                  'fk_idmodule', 'fk_idconcept', 'fk_informationitem', 'memberamount', 'description', 'visible', 'questions', 'mobilemedias']


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
                  'fk_informationitemtype', 'fk_idconcept', 'visible', "informationitemtypes", 'phaseprocedures']


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
    assessmentparameter = AssessmentparameterSerializer(
        many=True, read_only=True)
    priorknowledge = PriorknowledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Concept
        fields = ['url', 'idconcept', 'nameconcept', 'fk_idknowledgedomain',
                  'fk_idmodule', 'visible', 'sourceconcept', 'targetconcept', 'mobilemedias', 'informationitems', 'instructionalelements', 'assessmentparameter', 'priorknowledge']


class SubModuleSerializer(serializers.HyperlinkedModelSerializer):
    concepts = ConceptSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)
    assessmentparameter = AssessmentparameterSerializer(
        many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'visible', 'concepts', 'mobilemedias', 'instructionalelements', 'assessmentparameter']


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    submodules = SubModuleSerializer(many=True, read_only=True)
    concepts = ConceptSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)
    assessmentparameter = AssessmentparameterSerializer(
        many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['url', 'idmodule', 'fk_idmodule', 'namemodule', 'subtitle',
                  'idknowledgedomain', 'visible', 'submodules', 'concepts', 'mobilemedias', 'instructionalelements', 'assessmentparameter']


class KnowledgedomainSerializer(serializers.HyperlinkedModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    mobilemedias = MobilemediaSerializer(many=True, read_only=True)
    instructionalelements = InstructionalelementSerializer(
        many=True, read_only=True)
    assessmentparameter = AssessmentparameterSerializer(
        many=True, read_only=True)

    class Meta:
        model = Knowledgedomain
        fields = ['url', 'idknowledgedomain', 'nameknowledgedomain',
                  'subtitle', 'lastversion', 'fk_iduser', 'modules', 'mobilemedias', 'instructionalelements', 'assessmentparameter']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    knowledgedomains = KnowledgedomainSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        subject = "Email de confirmação | Confirme seu cadastro na plataforma EducomML"
        message = render_to_string('email_template.html', {
            'user': user,
            'domain': 'localhost:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return user

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name',
                  'last_name', 'password', 'is_active', 'knowledgedomains']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
