# -*- coding: utf-8 -*-
"""
巨大な辞書を作るときの tips

* http://stackoverflow.com/questions/16256913/improving-performance-of-very-large-dictionary-in-python
"""

def create_dict(keys):
    """
    >>> keys = {'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'black'}
    >>> create_dict(keys)
    {'pink': None, 'red': None, 'black': None, 'green': None, 'yellow': None, 'orange': None, 'blue': None}
    """
    d = dict.fromkeys(keys)  # dict is pre-sized to 32 empty slots
    d.update(dict(d))  # This makes room for additional keys and makes the set collision-free.
    return d
