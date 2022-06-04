
import pretty_errors
import pprint
from xml_chicanery.model.from_xml import Jdbor

from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser


pp = pprint.PrettyPrinter(indent=4)

# Inputs
xsd_path = './input/from_web.xsd'
xml_path = './input/data_small.xml'
# xml_path = './input/data_large.xml'

config = ParserConfig(
    base_url=None,
    process_xinclude=False,
    fail_on_unknown_properties=False,
    fail_on_unknown_attributes=False,)

parser = XmlParser(context= XmlContext(), config=config)
jdbor = parser.parse(xml_path, Jdbor)

# print the first 2 elements from the date_lg.xml
for disorder in jdbor.disorder_list.disorder[:2]:
    pp.pprint(disorder.__dict__)
