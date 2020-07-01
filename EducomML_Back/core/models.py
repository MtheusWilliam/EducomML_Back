
from django.db import models
from django.contrib.auth.models import User, Group


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
        managed = False
        db_table = 'AnswersAlternatives'
        ordering = ['orderansweralternatives']


class Concept(models.Model):

    # Field name made lowercase.
    idconcept = models.AutoField(db_column='idConcept', primary_key=True)
    # Field name made lowercase.
    nameconcept = models.CharField(db_column='nameConcept', max_length=256)
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
        managed = False
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
        managed = False
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
        managed = False
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
        managed = False
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
        managed = False
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
        db_column='nameKnowledgeDomain', max_length=45, blank=True, null=False)
    # Field name made lowercase.
    subtitle = models.CharField(
        db_column='subTitle', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    lastversion = models.CharField(
        db_column='lastVersion', max_length=45, blank=True, null=True)
    fk_iduser = models.ForeignKey(
        User, db_column='fk_idUser', blank=False, null=False, related_name='knowledgedomains', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'KnowledgeDomain'
        ordering = ['idknowledgedomain']


class Mediatype(models.Model):
    idmediatype = models.AutoField(db_column='idMediaType', primary_key=True)
    # Field name made lowercase.
    namemediatype = models.CharField(
        db_column='nameMediaType', max_length=256, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'MediaType'


class Module(models.Model):
    # Field name made lowercase.
    idmodule = models.AutoField(
        db_column='idModule', primary_key=True)
    # Field name made lowercase.
    namemodule = models.CharField(db_column='nameModule', max_length=256)
    # Field name made lowercase.
    subtitle = models.CharField(
        db_column='subTitle', max_length=45, blank=True, null=True)
    idknowledgedomain = models.ForeignKey(
        Knowledgedomain, db_column='idKnowledgeDomain', blank=True, null=False, related_name='modules', on_delete=models.CASCADE)
    # Field name made lowercase.
    fk_idmodule = models.ForeignKey(
        'self', db_column='fk_IdModule', blank=True, null=True, related_name='submodules', on_delete=models.CASCADE)
    visible = models.BooleanField(
        db_column='visible', default=True, blank=True, null=True)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'MobileMedia'
        ordering = ['idmobilemedia']


class Phaseprocedure(models.Model):
    # Field name made lowercase.
    idphaseprocedure = models.AutoField(
        db_column='idPhaseProcedure', primary_key=True)
    order = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    # Field name made lowercase.
    fk_informationitem = models.ForeignKey(
        Informationitem, db_column='fk_InformationItem', related_name='phaseprocedures', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'PhaseProcedure'
        ordering = ['order']


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
        managed = False
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
        managed = False
        db_table = 'QuestionType'


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
        managed = False
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
        managed = False
        db_table = 'Reference'


class Referencetype(models.Model):
    # Field name made lowercase.
    idreferencetype = models.AutoField(
        db_column='idReferenceType', primary_key=True)
    # Field name made lowercase.
    namererefencetype = models.CharField(
        db_column='nameRerefenceType', max_length=256)

    class Meta:
        managed = False
        db_table = 'Referencetype'
