import io
import sys
import xml.etree.ElementTree as ET

import docx
from docx.opc.constants import RELATIONSHIP_TYPE as rt

def read_xml_namespaces(xml):
    source = io.BytesIO(xml)
    ns_tree = ET.iterparse(source, events=['start-ns'])
    ns = dict([elem for event, elem in ns_tree])
    return ns

def read_footnote_xml(xml):
    ns = read_xml_namespaces(xml)
    ns_w = ns['w']

    tree = ET.parse(io.BytesIO(xml))
    root = tree.getroot()
    footnotes_elems = root.findall('.//w:footnote[@w:id]', namespaces=ns)

    footnotes = []
    for fn in footnotes_elems:
        id_ = fn.attrib.get(f'{{{ns_w}}}id')
        if id_ is not None:
            if int(id_) > 0:
                texts = fn.findall('.//w:t', namespaces=ns)
                note = ''.join(i.text for i in texts).strip()
                footnotes.append((id_, note))
    return footnotes


doc = docx.Document(sys.argv[1])

for relation in doc.part.rels.values():
    if relation.reltype == rt.FOOTNOTES:
        footnote_xml = relation.target_part.blob
        footnotes = read_footnote_xml(footnote_xml)

for id_, note in footnotes:
    print(f'{id_}: {note}')
