from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, get_user_model
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import *

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
def UserId(request):
    username = request.data.get('username')
    User = get_user_model().objects.get(username=username)
    response = Response()
    id = User.id
    name = User.first_name+" "+User.last_name 
    response.data = {
        'url': "http://localhost:8000/users/"+str(id)+"/",
        'complete_name': name
    }
    return response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_class = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class KnowledgedomainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Knowledgedomain.objects.all()
    serializer_class = KnowledgedomainSerializer
    authentication_class = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConceptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReferenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReferencetypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Referencetype.objects.all()
    serializer_class = ReferencetypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class MobilemediaViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Mobilemedia.objects.all()
    serializer_class = MobilemediaSerializer
    permission_classes = [permissions.IsAuthenticated]


class MediatypeViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Mediatype.objects.all()
    serializer_class = MediatypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class InformationitemViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Informationitem.objects.all()
    serializer_class = InformationitemSerializer
    permission_classes = [permissions.IsAuthenticated]


class InformationitemtypeViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Informationitemtype.objects.all()
    serializer_class = InformationitemtypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhaseprocedureViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Phaseprocedure.objects.all()
    serializer_class = PhaseprocedureSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstructionalelementViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Instructionalelement.objects.all()
    serializer_class = InstructionalelementSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstrucelementtypeViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Instrucelementtype.objects.all()
    serializer_class = InstrucelementtypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestiontypeViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Questiontype.objects.all()
    serializer_class = QuestiontypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResolutionquestionViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Resolutionquestion.objects.all()
    serializer_class = ResolutionquestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnswersalternativesViewSet(viewsets.ModelViewSet):
    """
    point that allows groups to be viewed or edited.
    """
    authentication_class = [JSONWebTokenAuthentication,
                            authentication.SessionAuthentication, authentication.BasicAuthentication]
    queryset = Answersalternatives.objects.all()
    serializer_class = AnswersalternativesSerializer
    permission_classes = [permissions.IsAuthenticated]
