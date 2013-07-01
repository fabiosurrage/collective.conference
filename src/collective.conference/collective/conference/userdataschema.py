from zope.interface import Interface, implements
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from collective.conference import MessageFactory as _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

gender_options = SimpleVocabulary(
    [SimpleTerm(value=u'f', title=_(u'Female')),
     SimpleTerm(value=u'm', title=_(u'Male'))])


def validateAccept(value):
    if not value == True:
        return False
    return True


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    fullname = schema.TextLine(
        title=_(u'label_fullname', default=u'Full name'),
        description=_(u'help_fullname',
                      default=u"Fill in your full name."),
        required=True,
        )
    identity_document = schema.TextLine(
        title=_(u'label_identity_document', default=u'Identity document'),
        description=_(u'help_identity_document',
                      default=u"Fill in your ID (for Brazillians only)."),
        required=False,
        )
    issuing_authority = schema.TextLine(
        title=_(u'label_issuing_authority', default=u'Issuing authority'),
        description=_(u'help_issuing_authority',
                      default=u"Fill in the issuing authority of the ID (for Brazillians only)."),
        required=False,
        )
    cpf = schema.TextLine(
        title=_(u'label_cpf', default=u'CPF'),
        description=_(u'help_cpf',
                      default=u"Fill in your CPF (for Brazillians only)."),
        required=False,
        )
    gender = schema.Choice(
        title=_(u'label_gender', default=u'Gender'),
        description=_(u'help_gender',
                      default=u""),
        source=gender_options,
        required=True,
        default=u'm',
        )
    passaport_number = schema.TextLine(
        title=_(u'label_passaport_number', default=u'Passaport number'),
        description=_(u'help_passaport_number',
                      default=u"Fill in your passaport number (for non-Brazillians only)."),
        required=False,
        )
    passaport_name = schema.TextLine(
        title=_(u'label_passaport_name', default=u'Passaport name'),
        description=_(u'help_passaport_name',
                      default=u"Your name as written in your passaport (for non-Brazillians only)."),
        required=False,
        )
    company_name = schema.TextLine(
        title=_(u'label_company_name', default=u'Company name'),
        description=_(u'help_company_name',
                      default=u"Where do you work?"),
        required=False,
        )
    company_website = schema.TextLine(
        title=_(u'label_company_website', default=u'Company website'),
        description=_(u'help_company_website',
                      default=u""),
        required=False,
        )
    mini_resume = schema.Text(
        title=_(u'label_mini_resume', default=u'Mini resume'),
        description=_(u'help_mini_resume',
                      default=u""),
        required=False,
        )
    need_special_care = schema.Text(
        title=_(u'label_need_special_care', default=u'Special care'),
        description=_(u'help_need_special_care',
                      default=u"Do you need special care?"),
        required=False,)
    social_networks = schema.TextLine(
        title=_(u'label_social_networks', default=u'Social networks'),
        description=_(u'help_social_networks',
                      default=u"Give us your Twitter, Facebook, G+... ids."),
        required=False,
        )
    student_or_APyB_affiliated = schema.Bool(
        title=_(u'label_student_or_APyB_affiliated', default=u'Student or APyB affiliated'),
        description=_(u'help_student_or_APyB_affiliated',
                      default=u"Check this box if you are a student or an APyB affiliated (for lower prices in the fees)."),
        required=True,
        )
    address = schema.TextLine(
        title=_(u'label_address', default=u'Address'),
        description=_(u'help_address',
                      default=u"The address of your home."),
        required=False,
        )
    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        description=_(u'help_city',
                      default=u"Fill in the city you live in."),
        required=True,
        )
    state = schema.TextLine(
        title=_(u'label_state', default=u'State'),
        description=_(u'help_state',
                      default=u"Fill in the state of your city."),
        required=True,
        )
    country = schema.TextLine(
        title=_(u'label_country', default=u'Country'),
        description=_(u'help_country',
                      default=u"Fill in the country you live in."),
        required=True,
        )
    zip_code = schema.TextLine(
        title=_(u'label_zip_code', default=u'Zip'),
        description=_(u'help_zip_code',
                      default=u"The zip code of your address."),
        required=False,
        )
    citizenship = schema.TextLine(
        title=_(u'label_citizenship', default=u'Citizenship'),
        description=_(u'help_citizenship',
                      default=u"Fill in your citizenship."),
        required=True,
        )
    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        description=_(u'help_phone',
                      default=u"Inform your telephone number (+xx-xxx-xxxx-xxxx)."),
        required=False,
        )
    mobile_phone = schema.TextLine(
        title=_(u'label_mobile_phone', default=u'Mobile phone'),
        description=_(u'help_mobile_phone',
                      default=u"Inform your mobile phone number in case we need to contact you (+xx-xxx-xxxx-xxxx)."),
        required=True,
        )
    accept = schema.Bool(
        title=_(u'label_accept', default=u'I accept the terms of the event conduct code.'),
        description=_(u'help_accept',
                      default=u"Check this box if you have found,"
                      " read and accepted the terms of the event conduct code. http://2013.ploneconf.org/the-event/code-of-conduct"),
        required=True,
        constraint=validateAccept,
        )

