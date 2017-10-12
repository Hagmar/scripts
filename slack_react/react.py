#!/usr/bin/env python3

import re
from string import ascii_lowercase as l

s = input().lower()
r = re.findall(':[-\w_]+:', s)
s = re.sub(':[-\w_]+:', '{}', s)
print(''.join((':-{}:'.format(c) if c in l else c for c in s)).format(*r))
