
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core import views
from rest_framework_jwt.views import *

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('knowledgedomain', views.KnowledgedomainViewSet)
router.register('module', views.ModuleViewSet)
router.register('concept', views.ConceptViewSet)
router.register('reference', views.ReferenceViewSet)
router.register('referencetype', views.ReferencetypeViewSet)
router.register('mobilemedia', views.MobilemediaViewSet)
router.register('mediatype', views.MediatypeViewSet)
router.register('informationitem', views.InformationitemViewSet)
router.register('informationitemtype', views.InformationitemtypeViewSet)
router.register('phaseprocedure', views.PhaseprocedureViewSet)

router.register('instructionalelement', views.InstructionalelementViewSet)
router.register('instrucelementtype', views.InstrucelementtypeViewSet)
router.register('question', views.QuestionViewSet)
router.register('questiontype', views.QuestiontypeViewSet)
router.register('resolutionquestion', views.ResolutionquestionViewSet)
router.register('answersalternatives', views.AnswersalternativesViewSet)

router.register('assessmentparameter', views.AssessmentparameterViewSet)
router.register('single', views.SingleViewSet)
router.register('range', views.RangeViewSet)
router.register('typethreshold', views.TypethresholdViewSet)
router.register('scopo', views.ScopoViewSet)
router.register('priorknowledge', views.PriorknowledgeViewSet)
router.register('priorlevel', views.PriorlevelViewSet)
app_name = "EducomML_Back"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userId/', views.UserId),
    path('reset-password/', views.ResetPassword),
    path('update-password/', views.UpdatePassword),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('email_confirmation/<uidb64>/<token>/',
         views.AccountVerification.as_view(), name="email_confirmation"),
    path('reset_password/<uidb64>/<token>/',
         views.ResetPasswordRedirect.as_view() , name="reset_password"),
    path('', include(router.urls)),
]
