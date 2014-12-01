"""Definition of the Transfer Job content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from uwosh.hrjobposting import hrjobpostingMessageFactory as _

from uwosh.hrjobposting.interfaces import ITransferJob
from uwosh.hrjobposting.config import PROJECTNAME

TransferJobSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.FileField(
        'positiondescription',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Position Description"),
            description=_(u"Field description"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),


    atapi.StringField(
        'postdate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Posting Date"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.StringField(
        'department',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Department"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.TextField(
        'schedule',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Work Schedule"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.TextField(
        'qualifications',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Special Qualifications"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.StringField(
        'payrange',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Pay Range"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.StringField(
        'deadline',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Application Deadline"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.TextField(
        'howtoapply',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"How to Apply"),
            description=_(u""),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TransferJobSchema['title'].storage = atapi.AnnotationStorage()
TransferJobSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TransferJobSchema, moveDiscussion=False)


class TransferJob(base.ATCTContent):
    """Content type for a Transfer Position"""
    implements(ITransferJob)

    meta_type = "TransferJob"
    schema = TransferJobSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    positiondescription = atapi.ATFieldProperty('positiondescription')

    postdate = atapi.ATFieldProperty('postdate')

    department = atapi.ATFieldProperty('department')

    schedule = atapi.ATFieldProperty('schedule')

    qualifications = atapi.ATFieldProperty('qualifications')

    payrange = atapi.ATFieldProperty('payrange')

    deadline = atapi.ATFieldProperty('deadline')

    howtoapply = atapi.ATFieldProperty('howtoapply')


atapi.registerType(TransferJob, PROJECTNAME)
