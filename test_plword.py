#!/Users/jeff/.pyenv/shims/python

import pytest
from plword import plword

@pytest.mark.parametrize('s, word',
                        [('', ''),
                         ('jeff', 'effjay'),
                         ('12', '21ay'),
                         ('apple', 'appleway')])
def test_piglatin_translation(s, word):
    assert plword(s) == word
