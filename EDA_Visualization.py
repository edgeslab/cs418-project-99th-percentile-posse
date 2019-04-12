tu_df = tobacco_use[tobacco_use.LocationAbbr != 'US']
tu_df = tobacco_use[tobacco_use.Response != 'Former']
tu_df = tobacco_use[tobacco_use.Response != 'Never']
tu_df = tobacco_use[tobacco_use.TopicDesc == 'Cigarette Use (Adults)']
tu_df.sort_values(by=['YEAR'])

bars = sns.barplot(x='YEAR', y='Data_Value', data=tu_df)

bars.set_title('Cigarette Use from 2011-2017')
bars.set_xlabel('Year')
bars.set_ylabel('Percentage of Cigarette Smokers')