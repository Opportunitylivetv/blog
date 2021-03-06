"""$Id: en.py 595 2006-04-03 13:10:07Z rubys $"""

__author__ = "Sam Ruby <http://intertwingly.net/> and Mark Pilgrim <http://diveintomark.org/>"
__version__ = "$Revision: 595 $"
__date__ = "$Date: 2006-04-03 09:10:07 -0400 (Mon, 03 Apr 2006) $"
__copyright__ = "Copyright (c) 2002 Sam Ruby and Mark Pilgrim"
__license__ = "Python"

import feedvalidator
from feedvalidator.logging import *

line = "line %(line)s"
column = "column %(column)s"
occurances = " (%(msgcount)s occurrences)"

messages = {
  SAXError:                "XML parsing error: %(exception)s",
  NotHtml:                 "Invalid HTML: %(message)s",
  UnicodeError:            "%(exception)s (maybe a high-bit character?)",
  UndefinedElement:        "Undefined %(parent)s element: %(element)s",
  MissingNamespace:        "Missing namespace for %(element)s",
  MissingElement:          "Missing %(parent)s element: %(element)s",
  MissingOptionalElement:  "%(parent)s should contain a %(element)s element",
  MissingRecommendedElement: "%(parent)s should contain a %(element)s element",
  MissingAttribute:        "Missing %(element)s attribute: %(attr)s",
  UnexpectedAttribute:     "Unexpected %(attribute)s attribute on %(element)s element",
  NoBlink:                 "There is no blink element in RSS; use blogChannel:blink instead",
  InvalidValue:            "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidWidth:            "%(element)s must be between 1 and 144",
  InvalidHeight:           "%(element)s must be between 1 and 400",
  InvalidHour:             "%(element)s must be an integer between 0 and 24",
  InvalidDay:              "%(element)s must be Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday",
  InvalidInteger:          "%(element)s must be an integer",
  InvalidPositiveInteger:  "%(element)s must be a positive integer",
  InvalidLatitude:         "%(element)s must be between -90 and 90",
  InvalidLongitude:        "%(element)s must be between -180 and 180",
  InvalidCommaSeparatedIntegers: "%(element)s must be comma-separated integers",
  InvalidHttpGUID:         "guid must be a full URL, unless isPermaLink attribute is false",
  InvalidUpdatePeriod:     "%(element)s must be hourly, daily, weekly, monthly, or yearly",
  NotBlank:                "%(element)s should not be blank",
  AttrNotBlank:            "The %(attr)s attribute of %(element)s should not be blank",
  DuplicateElement:        "%(parent)s contains more than one %(element)s",
  DuplicateSemantics:      "A channel should not include both %(core)s and %(ext)s",
  DuplicateItemSemantics:  "An item should not include both %(core)s and %(ext)s",
  DuplicateValue:          "%(element)s values must not be duplicated within a feed",
  NonstdPrefix:            '"%(preferred)s" is the preferred prefix for the namespace "%(ns)s"',
  ReservedPrefix:          'The prefix "%(prefix)s" generally uses the namespace "%(ns)s"',
  InvalidContact:          "%(element)s must include an email address",
  InvalidAddrSpec:         "%(element)s must be an email address",
  InvalidLink:             "%(element)s must be a valid URI",
  InvalidIRI:              "%(element)s must be a valid IRI",
  InvalidFullLink:         "%(element)s must be a full and valid URL",
  InvalidISO8601Date:      "%(element)s must be an ISO8601 date",
  InvalidISO8601DateTime:  "%(element)s must be an ISO8601 date-time",
  InvalidW3CDTFDate:        "%(element)s must be an W3CDTF date",
  InvalidRFC2822Date:      "%(element)s must be an RFC-822 date-time",
  InvalidRFC3339Date:      "%(element)s must be an RFC-3339 date-time",
  InvalidNPTTime:          "%(attr)s must be an NPT-time",
  InvalidLanguage:         "%(element)s must be an ISO-639 language code",
  InvalidURIAttribute:     "%(attr)s attribute of %(element)s must be a valid URI",
  InvalidURLAttribute:     "%(attr)s attribute of %(element)s must be a full URL",
  InvalidIntegerAttribute: "%(attr)s attribute of %(element)s must be a positive integer",
  InvalidBooleanAttribute: "%(attr)s attribute of %(element)s must be 'true' or 'false'",
  InvalidMIMEAttribute:    "%(attr)s attribute of %(element)s must be a valid MIME type",
  ItemMustContainTitleOrDescription: "item must contain either title or description",
  ContainsHTML:            "%(element)s should not contain HTML",
  ContainsEmail:           "%(element)s should not include email address",
  ContainsUndeclaredHTML:  "%(element)s should not contain HTML unless declared in the type attribute",
  NotEnoughHoursInTheDay:  "skipHours can not contain more than 24 hour elements",
  EightDaysAWeek:          "skipDays can not contain more than 7 day elements",
  SecurityRisk:            "%(element)s should not contain %(tag)s tag",
  SecurityRiskAttr:        "%(element)s should not contain %(attr)s attribute",
  ContainsRelRef:          "%(element)s should not contain relative URL references",
  ContainsSystemEntity:    "Feeds must not contain SYSTEM entities",
  InvalidContentMode:      "mode must be 'xml', 'escaped', or 'base64'",
  InvalidMIMEType:         "Not a valid MIME type",
  NotEscaped:              "%(element)s claims to be escaped, but isn't",
  NotInline:               "%(element)s claims to be inline, but may contain html",
  NotBase64:               "%(element)s claims to be base64-encoded, but isn't",
  InvalidURN:              "%(element)s is not a valid URN",
  InvalidTAG:              "%(element)s is not a valid TAG",
  InvalidURI:              "%(element)s is not a valid URI",
  ObsoleteVersion:         "This feed is an obsolete version",
  ObsoleteNamespace:       "This feed uses an obsolete namespace",
  InvalidNamespace:        "%(element)s is in an invalid namespace: %(namespace)s",
  InvalidDoctype:          "This feed contains conflicting DOCTYPE and version information",
  DuplicateAtomLink:       "Duplicate alternate links with the same type and hreflang",
  MissingHref:             "%(element)s must have an href attribute",
  AtomLinkNotEmpty:        "%(element)s should not have text (all data is in attributes)",
  BadCharacters:           '%(element)s contains bad characters',
  BadXmlVersion:           "Incorrect XML Version: %(version)s",
  UnregisteredAtomLinkRel: "%(value)s is not a registered link relationship",
  HttpError:               "Server returned %(status)s",
  IOError:                 "%(exception)s (%(message)s; misconfigured server?)",
  ObscureEncoding:         "Obscure XML character encoding: %(encoding)s",
  NonstdEncoding:          "This encoding is not mandated by the XML specification: %(encoding)s",
  UnexpectedContentType:   '%(type)s should not be served with the "%(contentType)s" media type',
  EncodingMismatch:        'Your feed appears to be encoded as "%(encoding)s", but your server is reporting "%(charset)s"',
  UnknownEncoding:         "Unknown XML character encoding: %(encoding)s",
  NotSufficientlyUnique:   "The specified guid is not sufficiently unique",
  MissingEncoding:         "No character encoding was specified",
  UnexpectedText:          "Unexpected Text",
  ValidatorLimit:          "Unable to validate, due to hardcoded resource limits (%(limit)s)",
  TempRedirect:            "Temporary redirect",
  TextXml:                 "Content type of text/xml with no charset",
  Uncompressed:            "Response is not compressed",
  HttpProtocolError:       'Response includes bad HTTP header name: "%(header)s"',
  NonCanonicalURI:         'Identifier "%(uri)s" is not in canonical form (should be "%(curi)s")',
  InvalidRDF:              'RDF parsing error: %(message)s',
  InvalidDuration:         'Invalid duration: "%(value)s"',
  InvalidYesNo:            '%(element)s must be "yes", "no", or "clean"',
  TooLong:                 'length of %(len)d exceeds the maximum allowable for %(element)s of %(max)d',
  InvalidItunesCategory:   '%(text)s is not one of the predefined iTunes categories or sub-categories',
  InvalidKeywords:         'Use commas to separate keywords',
  InvalidTextType:         'type attribute must be "text", "html", or "xhtml"',
  MissingXhtmlDiv:         'Missing xhtml:div element',
  MissingSelf:             'Missing atom:link with rel="self"',
  DuplicateEntries:        'Two entries with the same id',
  MisplacedMetadata:       '%(element)s must appear before all entries',
  MissingTextualContent:   'Missing textual content',
  MissingContentOrAlternate: 'Missing content or alternate link',
  MissingSourceElement:    "Missing %(parent)s element: %(element)s",
  MissingTypeAttr:         "Missing %(element)s attribute: %(attr)s",
  HtmlFragment:            "%(type)s type used for a document fragment",
  DuplicateUpdated:        "Two entries with the same value for atom:updated",
  UndefinedNamedEntity:    "Undefined named entity: %(value)s",
  ImplausibleDate:         "Implausible date: %(value)s",
  UnexpectedWhitespace:    "Whitespace not permitted here",
  SameDocumentReference:   "Same-document reference",
  SelfDoesntMatchLocation: "Self reference doesn't match document location",
  InvalidOPMLVersion:      'The "version" attribute for the opml element must be 1.0 or 1.1.',
  MissingXmlURL:           'An <outline> element whose type is "rss" must have an "xmlUrl" attribute.',
  InvalidOutlineVersion:   'An <outline> element whose type is "rss" may have a version attribute, whose value must be RSS, RSS1, RSS2, or scriptingNews.',
  InvalidOutlineType:      'The type attribute on an <outline> element should be a known type.',
  InvalidExpansionState:   '<expansionState> is a comma-separated list of line numbers.',
  InvalidTrueFalse:        '%(element)s must be "true" or "false"',
  MissingOutlineType:      'An <outline> element with more than just a "text" attribute should have a "type" attribute indicating how the other attributes are to be interpreted.',
  MissingTitleAttr:        'Missing outline attribute: title',
  MissingUrlAttr:          'Missing outline attribute: url',
  NotUTF8:                 'iTunes elements should only be present in feeds encoded as UTF-8',
  MissingItunesElement:    'Missing recommended iTunes %(parent)s element: %(element)s',
  UnsupportedItunesFormat: 'Format %(extension)s is not supported by iTunes',
  InvalidCountryCode:      "Invalid country code: \"%(value)s\"",
  InvalidCurrencyUnit:     "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidFloat:            "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidFloatUnit:        "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidFullLocation:     "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidGender:           "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidIntUnit:          "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidLabel:            "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidLocation:         "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidMaritalStatus:    "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidPaymentMethod:    "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidPercentage:       '%(element)s must be a percentage',
  InvalidPriceType:        "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidRatingType:       "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidReviewerType:     "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidSalaryType:       "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidServiceType:      "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidValue:            "Invalid value for %(attr)s: \"%(value)s\"",
  InvalidYear:             "Invalid value for %(attr)s: \"%(value)s\"",
  TooMany:                 "%(parent)s contains more than ten %(element)s elements",
  InvalidPermalink:        "guid must be a full URL, unless isPermaLink attribute is false",
  NotInANamespace:         "Missing namespace for %(element)s",
  UndeterminableVocabulary:"Missing namespace for %(element)s",
  SelfNotAtom:             '"self" link references a non-Atom representation',
  InvalidFormComponentName: 'Invalid form component name',
  ImageLinkDoesntMatch:    "Image link doesn't match channel link",
  ImageUrlFormat:          "Image not in required format",
  ProblematicalRFC822Date: "Problematical RFC 822 date-time value",
  DuplicateEnclosure:      "item contains more than one enclosure",
  MissingItunesEmail:      "The recommended <itunes:email> element is missing",
  MissingGuid:             "%(parent)s should contain a %(element)s element",
  UriNotIri:               "IRI found where URL expected",
  ObsoleteWikiNamespace:   "Obsolete Wiki Namespace",
  DuplicateDescriptionSemantics: "Avoid %(element)s",
  InvalidCreditRole:       "Invalid Credit Role",
  InvalidMediaTextType:    'type attribute must be "plain" or "html"',
  InvalidMediaHash:        'Invalid Media Hash',
  InvalidMediaRating:      'Invalid Media Rating',
  InvalidMediaRestriction: "media:restriction must be 'all' or 'none'",
  InvalidMediaRestrictionRel: "relationship must be 'allow' or 'disallow'",
  InvalidMediaRestrictionType: "type must be 'country' or 'uri'",
  InvalidMediaMedium:      'Invalid content medium: "%(value)s"',
  InvalidMediaExpression:  'Invalid content expression: "%(value)s"',
  DeprecatedMediaAdult:    'media:adult is deprecated',
}
