#salesforce_api.py
import numpy as np
filename='mnist.txt'
data=np.loadtxt(filename,delimiter=',',skiprows=1,usecols=[2,3])
print(data)
import numpy as np
filename='mnist.txt'
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
print(data)
Importing flat files using Pandas
import pandas as pd
filename='http://0.0.0.0:8000/Desktop/planet.csv'
data=pd.read_csv(filename)
print(data)
# print(data.head(2)) # check by default first 5 rows else parameterwise
# print(data.tail()) # for last rows
# print(data.values) #dataframe values
# print(data.columns) # for columns
# print(data.shape) #number of rows and cols
# print(data.info()) #additional info
# print(data.Name.value_counts(dropna=False)) #count the frequency by column name
# print(data['Name'].value_counts(dropna=False)) #same as pre
# print(data.describe()) #more statics
      Name       Mass  Radius  \
0  Mercury     0.3300    4879   
1    Venus     4.8700   12104   
2    Earth     5.9700   12756   
3     Mars     0.6420    6792   
4  Jupiter  1898.0000  142984   
5   Saturn   568.0000  120536   
6   Uranus    86.8000   51118   
7  Neptune   102.0000   49528   
8    Pluto     0.0146    2370   

                                         Description  \
0  Named Mercurius by the Romans because it appea...   
1  Roman name for the goddess of love. This plane...   
2  The name Earth comes from the Indo-European ba...   
3  Named by the Romans for their god of war becau...   
4  The largest and most massive of the planets wa...   
5  Roman name for the Greek Cronos, father of Zeu...   
6  Several astronomers, including Flamsteed and L...   
7  Neptune was "predicted" by John Couch Adams an...   
8  Pluto was discovered at Lowell Observatory in ...   

                                         Moreinfo  
0  https://en.wikipedia.org/wiki/Mercury_(planet)  
1             https://en.wikipedia.org/wiki/Venus  
2             https://en.wikipedia.org/wiki/Earth  
3              https://en.wikipedia.org/wiki/Mars  
4           https://en.wikipedia.org/wiki/Jupiter  
5            https://en.wikipedia.org/wiki/Saturn  
6            https://en.wikipedia.org/wiki/Uranus  
7           https://en.wikipedia.org/wiki/Neptune  
8             https://en.wikipedia.org/wiki/Pluto  
importing excel sheet
import pandas as pd
filename='http://0.0.0.0:8000/Desktop/planet.xlsx'
data=pd.ExcelFile(filename)
print(data.sheet_names)   #see all sheets name
print(data.parse('planet'))  #read by sheet name as string
print(data.parse(0))    #read by sheet index as float
['planet (copy)']
Importing SAS files using pandas
import pandas as pd
from sas7bdat import SAS7BDAT 
with SAS7BDAT('urbonpop.sas7bdat') as file:
    df_sas=file.to_data_frame()
Importing Stata files using pandas
import pandas as pd
data=pd.read_stata('urbonpop.dta')
Importing HDF5 files
import h5py
filename='ahdhfhdlbd.hdf5'
data=h5py.File(filename,'r')
print(type(data))


