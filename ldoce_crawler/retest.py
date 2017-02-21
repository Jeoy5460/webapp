#!/usr/bin/python
import re
with open("a.url", 'r') as fd:
    for ln in fd:
        obj = re.match(r'(.*)[-](.*)',ln)
        if not obj:
            print ln


