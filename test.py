#import pandas as pd

import pandas as pd
import re
f=open("us.txt")
for line in f.readlines():
    s2=line.replace('"','',1)
    s2=s2[::-1].replace('"','',1)[::-1]
    s1=re.sub(r'("")','"',s2)
    print(s1, end="")