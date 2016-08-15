# Kola section temperature data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data

data = pd.read_csv('/home/artemm/Documents/PythonProjects/Education/kolasection.csv', \
 delimiter='\t')

inp = data.iloc[1:50, 1:]
out = data.iloc[2:51, 1:]

print(data.head())
