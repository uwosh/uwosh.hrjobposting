from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from uwosh.hrjobposting import hrjobpostingMessageFactory as _


class IUnclassifiedJob(Interface):
    """Content type for unclassified positions"""

    # -*- schema definition goes here -*-
    positiondescription = schema.Bytes(
        title=_(u"Position Description"),
        required=True,
        description=_(u""),
    )
#
    department = schema.TextLine(
        title=_(u"Department"),
        required=True,
        description=_(u""),
    )
#
    responsibilities = schema.SourceText(
        title=_(u"Responsibilities"),
        required=True,
        description=_(u""),
    )
#
    requirements = schema.SourceText(
        title=_(u"Requirements (Degree/Experience)"),
        required=True,
        description=_(u""),
    )
#
    preferences = schema.SourceText(
        title=_(u"Preferences"),
        required=True,
        description=_(u""),
    )
#
    startdate = schema.TextLine(
        title=_(u"Starting Date"),
        required=True,
        description=_(u""),
    )
#
    salary = schema.Text(
        title=_(u"Salary"),
        required=True,
        description=_(u""),
    )
#
    terms = schema.Text(
        title=_(u"Terms of Appointment"),
        required=True,
        description=_(u""),
    )
#
    deadline = schema.TextLine(
        title=_(u"Application Deadline"),
        required=True,
        description=_(u""),
    )
#
    howtoapply = schema.Text(
        title=_(u"How to Apply"),
        required=True,
        description=_(u""),
    )
#
