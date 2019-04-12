import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

tobacco_use = pd.read_csv('Behavioral_Risk_Factor_Data__Tobacco_Use__2011_to_present_.csv')

tobacco_use = tobacco_use[tobacco_use.Data_Value_Footnote_Symbol != '*']
#Removing rows from df which have a small sample size, denoted by '*' in the Data_Value_Footnote_Symbol column

tobacco_use = tobacco_use[tobacco_use.YEAR != '2011-2012']
tobacco_use = tobacco_use[tobacco_use.YEAR != '2012-2013']
tobacco_use = tobacco_use[tobacco_use.YEAR != '2013-2014']
tobacco_use = tobacco_use[tobacco_use.YEAR != '2014-2015']
tobacco_use = tobacco_use[tobacco_use.YEAR != '2015-2016']
tobacco_use = tobacco_use[tobacco_use.YEAR != '2016-2017']
tobacco_use = tobacco_use[tobacco_use.YEAR != 2011]

def drop_columns(tobacco_use): #Function to drop the columns that we do not need
    return tobacco_use.drop(columns = ['LocationDesc', 'TopicType', 'Data_Value_Type', 'Data_Value_Std_Err', 
                                    'Low_Confidence_Limit', 'High_Confidence_Limit', 'GeoLocation', 'TopicId',
                                    'MeasureId', 'StratificationID1', 'StratificationID2', 'StratificationID3',
                                    'StratificationID4', 'SubMeasureID', 'DisplayOrder', 'DataSource',
                                      'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'TopicTypeId'])

tu_df = (tobacco_use.pipe(drop_columns)) #Calling function to drop unneeded columns from df

tu_df.head(10) #Display first 10 elements of the dataframe
