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















