import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

ax = sns.stripplot(x="Sample_Size", y="Age", hue="Education", data=tobacco_use, jitter=True)
ax.set_title('Ages 20+ with higher level of education are our biggest audience ')