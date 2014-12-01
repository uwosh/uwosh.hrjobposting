"""Definition of the Unclassified Job content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from uwosh.hrjobposting import hrjobpostingMessageFactory as _

from uwosh.hrjobposting.interfaces import IUnclassifiedJob
from uwosh.hrjobposting.config import PROJECTNAME

UnclassifiedJobSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    
    # -*- Your Archetypes field definitions here ... -*-
    
    atapi.FileField(
        'positiondescription',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Position Description"),
            description=_(u""),
        ),
        required=False,
        validators=('isNonEmptyFile'),
    ),

    
    atapi.StringField(
        'department',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Department"),
            description=_(u""),
        ),
        required=False,
    ),

    
    atapi.TextField(
        'responsibilities',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Responsibilities"),
            description=_(u""),
        ),
        required=False,
    ),

    
    atapi.TextField(
        'requirements',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Requirements"),
            description=_(u""),
        ),
        required=False,
    ),

    
    atapi.TextField(
        'preferences',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Preferences"),
            description=_(u""),
        ),
        required=False,
    ),

    
    atapi.StringField(
        'startdate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Starting Date"),
            description=_(u"g"),
        ),
        required=False,
        default=_(u"MM/DD/YYYY, or as soon as possible"),
    ),

    
    atapi.TextField(
        'salary',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Salary"),
            description=_(u""),
        ),
        required=False,
#        default=_(u"competitive"),
    ),

    
    atapi.TextField(
        'terms',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Terms of Appointment"),
            description=_(u""),
        ),
        required=False,
    ),

    
    atapi.StringField(
        'deadline',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Application Deadline"),
            description=_(u""),
        ),
        required=False,
        default=_(u"Review of files will begin MM/DD/YYYY, and continue until position is filled."),
    ),

    
    atapi.TextField(
        'howtoapply',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"How to Apply"),
            description=_(u""),
            default_content_type = 'text/restructured',
            default_output_type = 'text/x-html-safe',
            allowable_content_types=('text/plain', 'text/restructured', 'text/html',),
        ),
        required=False,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

UnclassifiedJobSchema['title'].storage = atapi.AnnotationStorage()
UnclassifiedJobSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(UnclassifiedJobSchema, moveDiscussion=False)


class UnclassifiedJob(base.ATCTContent):
    """Content type for unclassified positions"""
    implements(IUnclassifiedJob)
    
    meta_type = "UnclassifiedJob"
    schema = UnclassifiedJobSchema
    
    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    positiondescription = atapi.ATFieldProperty('positiondescription')
    
    department = atapi.ATFieldProperty('department')
    
    responsibilities = atapi.ATFieldProperty('responsibilities')
    
    requirements = atapi.ATFieldProperty('requirements')
    
    preferences = atapi.ATFieldProperty('preferences')
    
    startdate = atapi.ATFieldProperty('startdate')
    
    salary = atapi.ATFieldProperty('salary')
    
    terms = atapi.ATFieldProperty('terms')
    
    deadline = atapi.ATFieldProperty('deadline')
    
    howtoapply = atapi.ATFieldProperty('howtoapply')


atapi.registerType(UnclassifiedJob, PROJECTNAME)
