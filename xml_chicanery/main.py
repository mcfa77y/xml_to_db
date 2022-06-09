
from re import sub
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
jdbor:Jdbor = parser.parse(xml_path, Jdbor)

# print the first 2 elements from the date_lg.xml
for disorder in jdbor.disorder_list.disorder[:2]:
    # pp.pprint(disorder.__dict__)
    # pp.pprint(disorder)
    # print(f'id: {disorder.id}')
    # print(f'orphacode: {disorder.orpha_code}')
    result = []
    result.append(disorder.id)
    result.append(disorder.orpha_code)
    result.append(disorder.name.value)
    insert_command = f"INSERT INTO disorder (id, OrphaCode, name) VALUES ({result});"
    # for summary_information in disorder.summary_information_list.summary_information:
    #     for synonym in disorder.synonym_list.synonym:
    #         sub_result = []
    #         sub_result.append(disorder.id)
    #         sub_result.append(disorder.orpha_code)
    #         sub_result.append(disorder.summary_information)
    #         sub_result.append(disorder.synonym)
    #         result.append(sub_result)
    print(result)


