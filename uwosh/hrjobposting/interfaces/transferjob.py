from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from uwosh.hrjobposting import hrjobpostingMessageFactory as _


class ITransferJob(Interface):
    """Content type for a Transfer Position"""

    # -*- schema definition goes here -*-
    positiondescription = schema.Bytes(
        title=_(u"Position Description"),
        required=True,
        description=_(u""),
    )
#
    postdate = schema.TextLine(
        title=_(u"Posting Date"),
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
    schedule = schema.Text(
        title=_(u"Work Schedule"),
        required=True,
        description=_(u""),
    )
#
    qualifications = schema.Text(
        title=_(u"Special Qualifications"),
        required=True,
        description=_(u""),
    )
#
    payrange = schema.TextLine(
        title=_(u"Pay Range"),
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
