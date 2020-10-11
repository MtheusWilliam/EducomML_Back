from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from django.db import models
from django.core.mail import EmailMessage


class User(AbstractUser):
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.email

    def email_user(self, subject, message,*args, **kwargs):
        msg = EmailMessage(
            '{}'.format(subject),
            '{}'.format(message),
            to=[self.email],
        )
        msg.send()
        return msg

class Assessmentparameter(models.Model):
    # Field name made lowercase.
    idassessmentparameter = models.AutoField(
        db_column='idAssessmentParameter', primary_key=True)
    # Field name made lowercase.
    typethreshold = models.ForeignKey(
        'Typethreshold', blank=False, null=False, db_column='typeThreshold', on_delete=models.CASCADE)
    scopo = models.ForeignKey(
        'Scopo', blank=False, null=False, db_column='scopo', on_delete=models.CASCADE)
    fk_idknowledgedomain = models.ForeignKey(
        'Knowledgedomain', blank=False, null=True, db_column='fk_idKnowledgeDomain', on_delete=models.CASCADE, related_name="assessmentparameter")
    fk_idmodule = models.ForeignKey(
        'Module', blank=False, null=True, db_column='fk_idModule', on_delete=models.CASCADE, related_name="assessmentparameter")
    fk_idconcept = models.ForeignKey(
        'Concept', blank=False, null=True, db_column='fk_idConcept', on_delete=models.CASCADE, related_name="assessmentparameter")

    class Meta:
        db_table = 'AssessmentParameter'
        ordering = ['idassessmentparameter']


class Answersalternatives(models.Model):
    # Field name made lowercase.
    idanswersalternatives = models.AutoField(
        db_column='idAnswersAlternatives', primary_key=True)
    # Field name made lowercase.
    idobjanswer = models.CharField(
        db_column='idObjAnswer', max_length=256, blank=True, null=True)
    answers = models.CharField(
        db_column='answers', max_length=256, blank=False, null=False)
    # Field name made lowercase.
    istrue = models.BooleanField(db_column='isTrue', blank=False, null=False)
    # Field name made lowercase.
    fk_idquestion = models.ForeignKey(
        'Question', blank=False, null=False, db_column='fk_idQuestion', on_delete=models.CASCADE, related_name="answersalternatives")
    orderansweralternatives = models.BigIntegerField(
        db_column='orderAnswerAlternatives', blank=True, null=True)

    class Meta:
        db_table = 'AnswersAlternatives'
        ordering = ['orderansweralternatives']


class Concept(models.Model):

    # Field name made lowercase.
    idconcept = models.AutoField(db_column='idConcept', primary_key=True)
    # Field name made lowercase.
    nameconcept = models.CharField(
        db_column='nameConcept', max_length=100, blank=False, null=False)
    # Field name made lowercase.
    fk_idconcept = models.BigIntegerField(
        db_column='fk_idConcept', blank=True, null=True)
    # Field name made lowercase.
    fk_idknowledgedomain = models.ForeignKey(
        'Knowledgedomain', db_column='fk_idKnowledgeDomain', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_idmodule = models.ForeignKey(
        'Module', db_column='fk_idModule', related_name='concepts', on_delete=models.CASCADE)
    visible = models.BooleanField(
        db_column='visible', default=True, blank=True, null=True)

    class Meta:
        db_table = 'Concept'
        ordering = ['idconcept']


class Informationitem(models.Model):
    # Field name made lowercase.
    idinformationitem = models.AutoField(
        db_column='idInformationItem', primary_key=True)
    # Field name made lowercase.
    nameinformationitem = models.CharField(
        db_column='nameInformationItem', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    descriptioninformationitem = models.TextField(
        db_column='descriptionInformationItem', blank=True, null=True)
    # Field name made lowercase.
    fk_informationitemtype = models.ForeignKey(
        'Informationitemtype', models.DO_NOTHING, db_column='fk_InformationItemType', blank=False, null=False, related_name='informationitemtypes')
    # Field name made lowercase.
    fk_idconcept = models.ForeignKey(
        'Concept', db_column='fk_idConcept', blank=False, null=False, on_delete=models.CASCADE, related_name='informationitems')
    visible = models.BooleanField(
        db_column='visible', default=True, blank=True, null=True)

    class Meta:
        db_table = 'InformationItem'
        ordering = ['idinformationitem']


class Informationitemtype(models.Model):
    # Field name made lowercase.
    idinformationitemtype = models.AutoField(
        db_column='idInformationItemType', primary_key=True)
    # Field name made lowercase.
    nameinformationitemtype = models.CharField(
        db_column='nameInformationItemType', max_length=256)

    class Meta:
        db_table = 'InformationItemType'


class Instrucelementtype(models.Model):
    # Field name made lowercase.
    idinstrucelementtype = models.AutoField(
        db_column='idInstrucElementType', primary_key=True)
    # Field name made lowercase.
    nameinstrucelementtype = models.CharField(
        db_column='nameInstrucElementType', max_length=256)
    # Field name made lowercase.
    idcategory = models.BigIntegerField(
        db_column='idCategory', blank=True, null=True)

    class Meta:
        db_table = 'InstrucElementType'


class Instructionalelement(models.Model):
    idinstructionalelement = models.AutoField(
        db_column='idInstructionalElement', primary_key=True)  # Field name made lowercase.
    # This field type is a guess.
    label = models.CharField(
        db_column='label', max_length=256, blank=False, null=False)
    fk_instructionalelementtype = models.ForeignKey(
        'Instrucelementtype', models.DO_NOTHING, db_column='fk_InstructionalElementType', blank=True, null=True)  # Field name made lowercase.
    fk_idknowledgedomain = models.ForeignKey(
        'Knowledgedomain', db_column='fk_idKnowledgeDomain', blank=True, null=True, on_delete=models.CASCADE, related_name='instructionalelements')  # Field name made lowercase.
    fk_idmodule = models.ForeignKey(
        'Module', db_column='fk_idModule', blank=True, null=True, on_delete=models.CASCADE, related_name='instructionalelements')  # Field name made lowercase.
    fk_idconcept = models.ForeignKey(
        'Concept', db_column='fk_idConcept', blank=True, null=True, on_delete=models.CASCADE, related_name='instructionalelements')  # Field name made lowercase.
    fk_informationitem = models.ForeignKey(
        'Informationitem', db_column='fk_idInformationItem', blank=True, null=True, on_delete=models.CASCADE, related_name='instructionalelements')  # Field name made lowercase.
    memberamount = models.BigIntegerField(
        db_column='memberAmount', blank=True, null=True)
    description = models.TextField(
        db_column='description', blank=True, null=True)
    visible = models.BooleanField(
        db_column='visible', default=True, blank=True, null=True)

    class Meta:
        db_table = 'InstructionalElement'
        ordering = ['idinstructionalelement']


class Knowledgedomain(models.Model):
    # Field name made lowercase.

    idknowledgedomain = models.AutoField(
        db_column='idKnowledgeDomain', primary_key=True)
    # idknowledgedomain = models.IntegerField(
    #   db_column='idKnowledgeDomain', primary_key=True)
    # Field name made lowercase.
    nameknowledgedomain = models.CharField(
        db_column='nameKnowledgeDomain', max_length=100, blank=False, null=False)
    # Field name made lowercase.
    subtitle = models.CharField(
        db_column='subTitle', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    lastversion = models.CharField(
        db_column='lastVersion', max_length=45, blank=True, null=True)
    fk_iduser = models.ForeignKey(
        User, db_column='fk_idUser', blank=False, null=False, related_name='knowledgedomains', on_delete=models.CASCADE)

    class Meta:
        db_table = 'KnowledgeDomain'
        ordering = ['idknowledgedomain']


class Mediatype(models.Model):
    idmediatype = models.AutoField(db_column='idMediaType', primary_key=True)
    # Field name made lowercase.
    namemediatype = models.CharField(
        db_column='nameMediaType', max_length=256, blank=True, null=False)

    class Meta:
        db_table = 'MediaType'


class Module(models.Model):
    # Field name made lowercase.
    idmodule = models.AutoField(
        db_column='idModule', primary_key=True)
    # Field name made lowercase.
    namemodule = models.CharField(
        db_column='nameModule', max_length=100, blank=False, null=False)
    # Field name made lowercase.
    subtitle = models.CharField(
        db_column='subTitle', max_length=100, blank=True, null=True)
    idknowledgedomain = models.ForeignKey(
        Knowledgedomain, db_column='idKnowledgeDomain', blank=True, null=False, related_name='modules', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_idmodule = models.ForeignKey(
        'self', db_column='fk_IdModule', blank=True, null=True, related_name='submodules', on_delete=models.CASCADE)
    visible = models.BooleanField(
        db_column='visible', default=True, blank=True, null=True)

    class Meta:
        db_table = 'Module'
        ordering = ['idmodule']


class Mobilemedia(models.Model):
    # Field name made lowercase.
    idmobilemedia = models.AutoField(
        db_column='idMobileMedia', primary_key=True)
    label = models.CharField(
        db_column='label', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    fk_informationitem = models.ForeignKey(
        'Informationitem', db_column='fk_Informationitem',  blank=True, null=True, related_name='mobilemedias', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_idmediatype = models.ForeignKey(
        'Mediatype', models.DO_NOTHING, db_column='fk_idMediaType',  blank=True, null=False, related_name='mediatype')
    fk_iduser = models.ForeignKey(
        User, db_column='fk_idUser',  blank=True, null=True, related_name='profileimage', on_delete=models.CASCADE)
    fk_idknowledgedomain = models.ForeignKey(
        'Knowledgedomain', db_column='fk_idKnowledgeDomain',  blank=True, null=True, related_name='mobilemedias', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_module = models.ForeignKey(
        'Module', db_column='fk_Module',  blank=True, null=True, related_name='mobilemedias', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_idinstructionalelement = models.ForeignKey(
        'Instructionalelement', db_column='fk_idInstructionalElement',  blank=True, null=True, on_delete=models.CASCADE, related_name='mobilemedias')
    # Field name made lowercase.
    fk_idconcept = models.ForeignKey(
        'Concept', db_column='fk_idConcept',  blank=True, null=True, related_name='mobilemedias', on_delete=models.CASCADE)
    fk_idquestion = models.ForeignKey(
        'Question', db_column='fk_idQuestion', blank=True, null=True, on_delete=models.CASCADE, related_name='mobilemedias')
    fk_idphaseprocedure = models.ForeignKey(
        'Phaseprocedure', db_column='fk_idPhaseProcedure', blank=True, null=True, on_delete=models.CASCADE, related_name='mobilemedias')
    difficultyLevel = models.IntegerField(
        db_column='difficultyLevel', blank=True, null=True)
    learningStyle = models.IntegerField(
        db_column='learningStyle', blank=True, null=True)
    # Field name made lowercase.
    path = models.CharField(
        db_column='path', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    namefile = models.CharField(
        db_column='nameFile', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    resolution = models.CharField(
        db_column='resolution', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='description', blank=True, null=True)
    # Field name made lowercase.
    time = models.CharField(
        db_column='time', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    textfull = models.TextField(
        db_column='textFull', blank=True, null=True)
    # Field name made lowercase.
    textshort = models.TextField(
        db_column='textShort', blank=True, null=True)
    # Field name made lowercase.
    urllink = models.CharField(
        db_column='url', max_length=256, blank=True, null=True)
    visible = models.BooleanField(
        db_column='visible', default=True, blank=True, null=True)

    class Meta:
        db_table = 'MobileMedia'
        ordering = ['idmobilemedia']


class Phaseprocedure(models.Model):
    # Field name made lowercase.
    idphaseprocedure = models.AutoField(
        db_column='idPhaseProcedure', primary_key=True)
    order = models.IntegerField(
        db_column='order', blank=False, null=False)
    description = models.CharField(max_length=256, blank=True, null=True)
    # Field name made lowercase.
    fk_informationitem = models.ForeignKey(
        Informationitem, db_column='fk_InformationItem', related_name='phaseprocedures', on_delete=models.CASCADE)

    class Meta:
        db_table = 'PhaseProcedure'
        ordering = ['order']


class Priorknowledge(models.Model):
    # Field name made lowercase.
    idpriorknowledge = models.AutoField(
        db_column='idPriorKnowledge', primary_key=True)
    namepriorknowledge = models.CharField(
        db_column='namePriorKnowledge', max_length=256, blank=False, null=False)
    priorlevel = models.ForeignKey(
        'Priorlevel', db_column='priorLevel', on_delete=models.CASCADE, blank=False, null=False)
    # Field name made lowercase.
    fk_priorsourceconcept = models.ForeignKey(
        'Concept', db_column='fk_priorSourceConcept', blank=False, null=False, related_name='priorknowledge', on_delete=models.CASCADE)
    fk_priortargetconcept = models.ForeignKey(
        'Concept', db_column='fk_priorTargetConcept', related_name='targetpriorknowledge', blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PriorKnowledge'
        ordering = ['idpriorknowledge']


class Priorlevel(models.Model):
    # Field name made lowercase.
    idpriorlevel = models.AutoField(
        db_column='idPriorLevel', primary_key=True)
    typepriorlevel = models.CharField(
        db_column='typePriorLevel', max_length=256, blank=False, null=False)

    class Meta:
        db_table = 'PriorLevel'
        ordering = ['idpriorlevel']


class Question(models.Model):
    # Field name made lowercase.
    idquestion = models.AutoField(
        db_column='idQuestion', primary_key=True)
    # Field name made lowercase.
    descriptionquestion = models.TextField(
        db_column='descriptionQuestion', blank=False, null=False
    )
    # Field name made lowercase.
    orderquestion = models.IntegerField(
        db_column='orderQuestion', blank=True, null=True)
    # Field name made lowercase.
    typequestion = models.ForeignKey(
        'QuestionType', models.DO_NOTHING, db_column='typeQuestion', blank=False, null=False)
    # Field name made lowercase.
    fk_idinstructionalelement = models.ForeignKey(
        'InstructionalElement', db_column='fk_idInstructionalElement', blank=True, null=True, on_delete=models.CASCADE, related_name='questions')  # Field name made lowercase.

    class Meta:
        db_table = 'Question'
        ordering = ['orderquestion']


class Questiontype(models.Model):
    # Field name made lowercase.
    idquestiontype = models.AutoField(
        db_column='idQuestionType', primary_key=True)
    # Field name made lowercase.
    namequestiontype = models.CharField(
        db_column='nameQuestionType', max_length=256, blank=False, null=False)

    class Meta:
        db_table = 'QuestionType'


class Range(models.Model):
    # Field name made lowercase.
    idrange = models.AutoField(
        db_column='idRange', primary_key=True)
    # Field name made lowercase.
    namerange = models.CharField(
        db_column='nameRange', max_length=256, blank=False, null=False)
    # Field name made lowercase.
    fk_idassessmentparameter = models.ForeignKey(
        'Assessmentparameter', blank=False, null=False, db_column='fk_idAssessmentParameter', on_delete=models.CASCADE, related_name="ranges")
    # Field name made lowercase.
    initialvalue = models.IntegerField(
        db_column='initialValue', blank=False, null=False)
    # Field name made lowercase.
    limitvalue = models.IntegerField(
        db_column='limitValue', blank=False, null=False)

    class Meta:
        db_table = 'Range'


class Resolutionquestion(models.Model):
    # Field name made lowercase.
    idresolutionquestion = models.AutoField(
        db_column='idResolutionQuestion', primary_key=True)
    # Field name made lowercase.
    correctitem = models.TextField(
        db_column='correctItem', blank=True, null=True)
    # Field name made lowercase.
    correctanswer = models.TextField(
        db_column='correctAnswer', blank=True, null=True)
    # Field name made lowercase.
    fk_idquestion = models.ForeignKey(
        'Question', db_column='fk_idQuestion', blank=True, null=True, on_delete=models.CASCADE, related_name='resolutionquestion')  # Field name made lowercase.

    class Meta:
        db_table = 'ResolutionQuestion'


class Reference(models.Model):
    # Field name made lowercase.
    idreference = models.AutoField(
        db_column='idReference', primary_key=True)
    # Field name made lowercase.
    sourceconcept = models.ForeignKey(
        Concept, db_column='sourceConcept', related_name='sourceconcept', on_delete=models.CASCADE)
    # Field name made lowercase.
    targetconcept = models.ForeignKey(
        Concept, db_column='targetConcept', related_name='targetconcept', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_referencetype = models.ForeignKey(
        'Referencetype', models.DO_NOTHING, db_column='fk_ReferenceType', blank=True, null=False, related_name='referencetype')
    # Field name made lowercase.
    namereference = models.CharField(
        db_column='nameReference', max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'Reference'


class Referencetype(models.Model):
    # Field name made lowercase.
    idreferencetype = models.AutoField(
        db_column='idReferenceType', primary_key=True)
    # Field name made lowercase.
    namererefencetype = models.CharField(
        db_column='nameRerefenceType', max_length=256)

    class Meta:
        db_table = 'Referencetype'


class Single(models.Model):
    # Field name made lowercase.
    idsingle = models.AutoField(
        db_column='idSingle', primary_key=True)
    # Field name made lowercase.
    fk_idassessmentparameter = models.ForeignKey(
        'Assessmentparameter', blank=False, null=False, db_column='fk_idAssessmentParameter', on_delete=models.CASCADE, related_name="single")
    # Field name made lowercase.
    threshold = models.CharField(
        db_column='threshold', max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'Single'

# testingheroku


class Scopo(models.Model):
    # Field name made lowercase.
    idscopo = models.AutoField(
        db_column='idScopo', primary_key=True)
    # Field name made lowercase.
    typescopo = models.CharField(
        db_column='typeScopo', max_length=256, blank=False, null=False)

    class Meta:
        db_table = 'Scopo'
        
class Typethreshold(models.Model):
    # Field name made lowercase.
    idtypethreshold = models.AutoField(
        db_column='idTypeThreshold', primary_key=True)
    # Field name made lowercase.
    nametypethreshold = models.CharField(
        db_column='nameTypeThreshold', max_length=256, blank=False, null=False)

    class Meta:
        db_table = 'TypeThreshold'


