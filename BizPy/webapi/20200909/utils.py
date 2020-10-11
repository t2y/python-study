import json
import re
from pprint import pprint 

RE_ENTITIES = re.compile(r'\[\[(.*?)\]\]', re.MULTILINE)


def get_entities(contents):
    entities = []
    matches = RE_ENTITIES.findall(contents)
    if matches is not None:
        for entity in matches:
            if '|' in entity:
                entity = entity.split('|')[0]
            entities.append(entity)
    return entities


def get_contents(data):
    for key in data['query']['pages']:
        revision = data['query']['pages'][key]['revisions'][0]
        contents = revision['*']
        return contents


def test(path='./contents.json'):
    data = json.load(open(path))
    contents = get_contents(data)
    entities = get_entities(contents)
    pprint(entities)


if __name__ == '__main__':
    test()
