import json
import sys
from pprint import pformat
from typing import Any, Dict

def pretty_format(data: Dict[str, Any]) -> str:
    return pformat(data, width=1)

def main(raw_data: str) -> None:
    data = pretty_format(json.loads(raw_data))
    data.append('mypy')  # error: "str" has no attribute "append"

if __name__ == '__main__':
    raw_data: str = sys.argv[1]
    main(raw_data)
