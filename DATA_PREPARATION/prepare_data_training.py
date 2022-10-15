"""
Preparing the imbalance data to balance data by checking the input features and desired output

Supervisied Machine Learning

1. Classifaction problem
  # Specific Binary 
       
1. preparing the data into three parts
   1.1. Train data  (70%-80% of the total dataset)
   1.2. Validation data (20%-10% of the total dataset)
   1.3. Test data (10%-20% of the total dataset) 
"""

import numpy  as np
import pandas as pd

data = pd.read_csv('../Dataset/magic04.data')
print(data.head(5))

"""
Name the columns by understanding the 7. Attribute information:

    1.  fLength:  continuous  # major axis of ellipse [mm]
    2.  fWidth:   continuous  # minor axis of ellipse [mm] 
    3.  fSize:    continuous  # 10-log of sum of content of all pixels [in #phot]
    4.  fConc:    continuous  # ratio of sum of two highest pixels over fSize  [ratio]
    5.  fConc1:   continuous  # ratio of highest pixel over fSize  [ratio]
    6.  fAsym:    continuous  # distance from highest pixel to center, projected onto major axis [mm]
    7.  fM3Long:  continuous  # 3rd root of third moment along major axis  [mm] 
    8.  fM3Trans: continuous  # 3rd root of third moment along minor axis  [mm]
    9.  fAlpha:   continuous  # angle of major axis with vector to origin [deg]
    10.  fDist:    continuous  # distance from origin to center of ellipse [mm]
    11.  class:    g,h         # gamma (signal), hadron (background)

"""
dataframe_colums = ['fLength','fWidth','fSize','fConc','fConc1','fAsym','fM3Long','fM3Trans',
                                  'fAlpha','fDist','class']

data = pd.read_csv('../Dataset/magic04.data',names=dataframe_colums)

print(data.head(5))


















