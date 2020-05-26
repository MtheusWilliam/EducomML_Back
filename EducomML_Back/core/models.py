
from django.db import models


class Answersalternatives(models.Model):
    # Field name made lowercase.
    idanswersalternatives = models.BigIntegerField(
        db_column='idAnswersAlternatives', primary_key=True)
    # Field name made lowercase.
    idobjanswer = models.CharField(
        db_column='idObjAnswer', max_length=256, blank=True, null=True)
    answers = models.CharField(max_length=256, blank=True, null=True)
    # Field name made lowercase.
    istrue = models.BooleanField(db_column='isTrue', blank=True, null=True)
    # Field name made lowercase.
    fk_idquestion = models.ForeignKey(
        'Question', models.DO_NOTHING, db_column='fk_idQuestion')

    class Meta:
        managed = False
        db_table = 'AnswersAlternatives'


class Concept(models.Model):
    # Field name made lowercase.
    idconcept = models.BigIntegerField(db_column='idConcept', primary_key=True)
    # Field name made lowercase.
    nameconcept = models.CharField(db_column='nameConcept', max_length=256)
    # Field name made lowercase.
    fk_idconcept = models.BigIntegerField(
        db_column='fk_idConcept', blank=True, null=True)
    # Field name made lowercase.
    fk_idkonwledgedomain = models.ForeignKey(
        'Knowledgedomain', models.DO_NOTHING, db_column='fk_idKonwledgeDomain')
    # Field name made lowercase.
    fk_idmodule = models.ForeignKey(
        'Module', models.DO_NOTHING, db_column='fk_idModule')
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Concept'


class Informationitem(models.Model):
    # Field name made lowercase.
    idinformationitem = models.BigIntegerField(
        db_column='idInformationItem', primary_key=True)
    # Field name made lowercase.
    nameinformationitem = models.CharField(
        db_column='nameInformationItem', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    fk_informationitemtype = models.ForeignKey(
        'Informationitemtype', models.DO_NOTHING, db_column='fk_InformationItemType', blank=True, null=True)
    # Field name made lowercase.
    fk_idconcept = models.ForeignKey(
        Concept, models.DO_NOTHING, db_column='fk_idConcept', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InformationItem'


class Informationitemtype(models.Model):
    # Field name made lowercase.
    idinformationitemtype = models.IntegerField(
        db_column='idInformationItemType', primary_key=True)
    # Field name made lowercase.
    nameinformationitem = models.CharField(
        db_column='nameInformationItem', max_length=256)

    class Meta:
        managed = False
        db_table = 'InformationItemType'


class Instrctionalelement(models.Model):
    idinstructionalelement = models.BigIntegerField(
        db_column='idInstructionalElement', primary_key=True)  # Field name made lowercase.
    # This field type is a guess.
    label = models.TextField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    fk_instructionalelementtype = models.ForeignKey(
        Informationitemtype, models.DO_NOTHING, db_column='fk_InstructionalElementType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstrctionalElement'


class Instructionalelementtype(models.Model):
    # Field name made lowercase.
    idinstrucelementtype = models.BigIntegerField(
        db_column='idInstrucElementType', primary_key=True)
    # Field name made lowercase.
    nameinstrucelementtype = models.CharField(
        db_column='nameInstrucElementType', max_length=256)
    # Field name made lowercase.
    idcategory = models.BigIntegerField(
        db_column='idCategory', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InstructionalElementType'


class Knowledgedomain(models.Model):
    # Field name made lowercase.

    idknowledgedomain = models.AutoField(
        db_column='idKnowledgeDomain', primary_key=True)
    # idknowledgedomain = models.IntegerField(
    #   db_column='idKnowledgeDomain', primary_key=True)
    # Field name made lowercase.
    nameknowledgedomain = models.CharField(
        db_column='nameKnowledgeDomain', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    subtitle = models.CharField(
        db_column='subTitle', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    lastversion = models.CharField(
        db_column='lastVersion', max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KnowledgeDomain'


class Mediatype(models.Model):
    # Field name made lowercase.
    idmediatype = models.IntegerField(
        db_column='idMediaType', primary_key=True)
    # Field name made lowercase.
    namemedia = models.CharField(db_column='nameMedia', max_length=256)

    class Meta:
        managed = False
        db_table = 'MediaType'


class Mobilemedia(models.Model):
    # Field name made lowercase.
    idmobilemedia = models.BigIntegerField(
        db_column='idMobileMedia', primary_key=True)
    description = models.TextField()
    label = models.CharField(max_length=256, blank=True, null=True)
    # Field name made lowercase.
    fk_informationitem = models.BigIntegerField(
        db_column='fk_Informationitem', blank=True, null=True)
    # Field name made lowercase.
    fk_idmediatype = models.IntegerField(
        db_column='fk_idMediaType', blank=True, null=True)
    # Field name made lowercase.
    fk_idknowledgedomain = models.BigIntegerField(
        db_column='fk_idKnowledgeDomain', blank=True, null=True)
    # Field name made lowercase.
    fk_module = models.ForeignKey(
        'Module', models.DO_NOTHING, db_column='fk_Module', blank=True, null=True)
    fk_idinstructionalelement = models.BigIntegerField(
        db_column='fk_idInstructionalElement', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    fk_idconcept = models.BigIntegerField(
        db_column='fk_idConcept', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MobileMedia'


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
        Knowledgedomain, models.DO_NOTHING, db_column='idKnowledgeDomain', blank=True, null=True,related_name='modules')
    # Field name made lowercase.
    fk_idmodule = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='fk_IdModule', blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Module'


class Phaseprocedure(models.Model):
    # Field name made lowercase.
    idphaseprocedure = models.IntegerField(
        db_column='idPhaseProcedure', primary_key=True)
    order = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    # Field name made lowercase.
    fk_informationitem = models.ForeignKey(
        Informationitem, models.DO_NOTHING, db_column='fk_InformationItem')

    class Meta:
        managed = False
        db_table = 'PhaseProcedure'


class Question(models.Model):
    # Field name made lowercase.
    idquestion = models.BigIntegerField(
        db_column='idQuestion', primary_key=True)
    # Field name made lowercase.
    orderquestion = models.CharField(
        db_column='orderQuestion', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    typequestion = models.IntegerField(
        db_column='typeQuestion', blank=True, null=True)
    # Field name made lowercase.
    fk_idmobilemedia = models.ForeignKey(
        Mobilemedia, models.DO_NOTHING, db_column='fk_idMobileMedia', blank=True, null=True)
    fk_idinstrctionalelement = models.BigIntegerField(
        db_column='fk_idInstrctionalElement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Question'


class Reference(models.Model):
    # Field name made lowercase.
    idreference = models.BigIntegerField(
        db_column='idReference', primary_key=True)
    # Field name made lowercase.
    sourceconcept = models.ForeignKey(
        Concept, models.DO_NOTHING, db_column='sourceconcept', related_name='sourceconcept')
    # Field name made lowercase.
    targetconcept = models.ForeignKey(
        Concept, models.DO_NOTHING, db_column='targetconcept', related_name='targetconcept')
    # Field name made lowercase.
    fk_referencetype = models.ForeignKey(
        'Referencetype', models.DO_NOTHING, db_column='fk_ReferenceType', blank=True, null=True)
    # Field name made lowercase.
    namereference = models.CharField(
        db_column='nameReference', max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reference'


class Referencetype(models.Model):
    # Field name made lowercase.
    idreferencetype = models.BigIntegerField(
        db_column='idReferenceType', primary_key=True)
    # Field name made lowercase.
    namererefencetype = models.CharField(
        db_column='nameRerefenceType', max_length=256)

    class Meta:
        managed = False
        db_table = 'Referencetype'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
