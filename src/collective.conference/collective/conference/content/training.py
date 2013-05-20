# -*- coding:utf-8 -*-
from five import grok
from zope import schema
from collective.conference import _
from plone.directives import form
from plone.directives import dexterity


class ITraining(form.Schema):
    """
    A training in a conference
    """

    estimated_duration = schema.TextLine(
        title=_(u'Estimated duration'),
        description=_(u'How long you want to talk (in minutes)'),
        required=True,
        default=u'120',
    )

    preferred_period = schema.Choice(
        title=_(u"Preferred period"),
        required=True,
        description=_(u"Your preferred period of day to your training"),
        vocabulary='collective.conference.periods',
    )

    language_talk = schema.Choice(
        title=_(u"Language"),
        required=True,
        description=_(u"Language this training will be given"),
        vocabulary='collective.conference.languages',
    )

    infrastructure_requirements = schema.Text(
        title=_(u"Infrastructure's requirements"),
        required=False,
        description=_(u"What do you need to have in the classroom ?"),
    )

    global_theme = schema.Choice(
        title=_(u"Global theme"),
        required=True,
        description=_(u"What is the subject of your training ?"),
        vocabulary='collective.conference.theme',
    )

    level = schema.Choice(
        title=_(u"Level"),
        required=True,
        description=_(u"Level of this training"),
        vocabulary='collective.conference.levels',
    )

    observations = schema.Text(
        title=_(u"Observations"),
        required=False,
        description=_(u"Do you want to give us any other information ?"),
    )


class Training(dexterity.Item):
    grok.implements(ITraining)