
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.compose import make_column_transformer
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
mydata=pd.read_csv('https://github.com/sahbaa/student-sPerformance/blob/master/StudentsPerformance%20(1).csv')

for col in mydata.columns:
    print(col,pd.isnull(mydata[col]).sum())
    
cat_col=[col for col in mydata.columns if mydata[col].dtype=='object']
for cl in cat_col:
    print(cl,":",mydata[cl].unique())
for colum in mydata.columns:
    sns.countplot(x=colum,data=mydata)
    if mydata[colum].dtype=='int64':
        plt.xticks(np.arange(1,100,10))
    else:
        plt.xticks()
    if colum=='parental level of education':
        plt.xticks(fontsize=7)
    plt.show()
mydata.dtypes

#encoding
mydata['MeanScore']=mydata[['math score','reading score','writing score']].mean()
newdata=mydata.drop(['math score','reading score','writing score'],axis=1)
ohe=OneHotEncoder()
ohe.fit_transform(newdata[['gender','race/ethnicity','lunch','test preparation course']])[:20]

oe=OrdinalEncoder()
oe.fit_transform(newdata[['parental level of education']])[:20]
coltransformer=make_column_transformer((ohe,['gender','race/ethnicity','lunch','test preparation course']),(oe,['parental level of education']))
coltransformer.fit_transform(newdata)
