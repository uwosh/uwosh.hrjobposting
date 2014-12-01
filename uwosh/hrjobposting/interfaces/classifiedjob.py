from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from uwosh.hrjobposting import hrjobpostingMessageFactory as _


class IClassifiedJob(Interface):
    """A Classified Job Post"""

    # -*- schema definition goes here -*-
#
    positiondescription = schema.Bytes(
        title=_(u"Position Description"),
        required=True,
        description=_(u"Upload a position description PDF"),
    )
#
    jobinfo = schema.SourceText(
        title=_(u"Job Information"),
        required=True,
        description=_(u""),
    )
#
    jobsummary = schema.SourceText(
        title=_(u"Summary"),
        required=True,
        description=_(u""),
    )
#
    jobduties = schema.SourceText(
        title=_(u"Job Duties"),
        required=True,
        description=_(u""),
    )
#
    jobskills = schema.SourceText(
        title=_(u"Job Knowledge, Skills and Abilities"),
        required=True,
        description=_(u""),
    )
#
    howtoapply = schema.SourceText(
        title=_(u"How to Apply"),
        required=True,
        description=_(u""),
    )
#
