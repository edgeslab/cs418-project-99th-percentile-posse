import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

tobacco_use = pd.read_csv('Behavioral_Risk_Factor_Data__Tobacco_Use__2011_to_present_.csv')

tobacco_use = tobacco_use[tobacco_use.Data_Value_Footnote_Symbol != '*']

def drop_columns(tobacco_use):
    return tobacco_use.drop(columns = ['LocationDesc', 'TopicType', 'Data_Value_Type', 'Data_Value_Std_Err', 
                                    'Low_Confidence_Limit', 'High_Confidence_Limit', 'GeoLocation', 'TopicId',
                                    'MeasureId', 'StratificationID1', 'StratificationID2', 'StratificationID3',
                                    'StratificationID4', 'SubMeasureID', 'DisplayOrder', 'DataSource',
                                      'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'TopicTypeId'])
tu_df = (tobacco_use.pipe(drop_columns))

tu_df.head(10)