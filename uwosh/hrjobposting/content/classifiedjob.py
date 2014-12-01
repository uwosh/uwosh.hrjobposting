"""Definition of the Classified Job content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from uwosh.hrjobposting import hrjobpostingMessageFactory as _

from uwosh.hrjobposting.interfaces import IClassifiedJob
from uwosh.hrjobposting.config import PROJECTNAME

ClassifiedJobSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.FileField(
        'positiondescription',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Position Description"),
            description=_(u"Upload a position description PDF"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),


    atapi.TextField(
        'jobinfo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Job Information"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'jobsummary',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Summary"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'jobduties',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Job Duties"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'jobskills',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Job Knowledge, Skills and Abilities"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'howtoapply',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"How to Apply"),
            description=_(u""),
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ClassifiedJobSchema['title'].storage = atapi.AnnotationStorage()
ClassifiedJobSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ClassifiedJobSchema, moveDiscussion=False)


class ClassifiedJob(base.ATCTContent):
    """A Classified Job Post"""
    implements(IClassifiedJob)

    meta_type = "ClassifiedJob"
    schema = ClassifiedJobSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    positiondescription = atapi.ATFieldProperty('positiondescription')

    jobinfo = atapi.ATFieldProperty('jobinfo')

    jobsummary = atapi.ATFieldProperty('jobsummary')

    jobduties = atapi.ATFieldProperty('jobduties')

    jobskills = atapi.ATFieldProperty('jobskills')

    howtoapply = atapi.ATFieldProperty('howtoapply')

   


atapi.registerType(ClassifiedJob, PROJECTNAME)
