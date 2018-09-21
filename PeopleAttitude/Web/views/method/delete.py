# -*- coding: utf-8 -*-
import re
import random
import string
strings=re.findall(r'(?<=\.)\w+$','asda.sd.txt')
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print (ran_str+'.'+strings[0])