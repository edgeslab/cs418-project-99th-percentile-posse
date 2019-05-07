# First Visualization
# Percentage of Young Adult Cigarette vs. E-Cigarette Users by the Year

sp_df = tobacco_use
sp_df = sp_df[sp_df.Gender == 'Overall']
sp_df = sp_df[sp_df.Race == 'All Races']
sp_df = sp_df[sp_df.Age == '18 to 24 Years']
sp_df = sp_df[sp_df.Education == 'All Grades']
sp_df = sp_df[sp_df.TopicDesc != 'Smokeless Tobacco Use (Adults)']
sp_df = sp_df[sp_df.TopicDesc != 'Cessation (Adults)']
sp_df.sort_values(by=['YEAR'])

sp = sns.stripplot(x="YEAR", y="Data_Value", hue="TopicDesc", data=sp_df, jitter=True)
sp.set_title('Percentage of Young Adult Cigarette vs. E-Cigarette Users by the Year')
sp.set_xlabel('Year')
sp.set_ylabel('Percentage of Current Users')

pp = sns.pointplot(x="YEAR", y="Data_Value", hue="TopicDesc", data=sp_df)
pp.set_title('Percentage of Young Adult Cigarette vs. E-Cigarette Users by the Year')
pp.set_xlabel('Year')
pp.set_ylabel('Percentage of Current Users')


# Second Visualization
# Cigarette Use from 2011-2017

bar_df = tobacco_use[tobacco_use.LocationAbbr != 'US']
bar_df = bar_df[bar_df.Response != 'Never']
bar_df = bar_df[bar_df.Response != 'Every Day']
bar_df = bar_df[bar_df.Response != 'Some Days']
box_df = box_df[box_df.Race == 'All Races']
box_df = box_df[box_df.Education == 'All Grades']
box_df = box_df[box_df.Gender == 'Overall']
box_df = box_df[box_df.Age != 'All Ages']
bar_df = bar_df[bar_df.TopicDesc == 'Cigarette Use (Adults)']
bar_df.sort_values(by=['YEAR'])

bars = sns.barplot(x='YEAR', y='Data_Value', hue='Response', data=bar_df)

bars.set_title('Cigarette Use from 2011-2017')
bars.set_xlabel('Year')
bars.set_ylabel('Percentage of Cigarette Smokers')


# Third Visualization
# Percentage of Cigarette Smokers by Age in 2011 and 2017

box_df = tobacco_use[tobacco_use.LocationAbbr != 'US']
box_df = box_df[box_df.MeasureDesc == 'Current Smoking']
box_df = box_df[box_df.TopicDesc == 'Cigarette Use (Adults)']
box_df = box_df[box_df.Race == 'All Races']
box_df = box_df[box_df.Education == 'All Grades']
box_df = box_df[box_df.Gender == 'Overall']
box_df = box_df[box_df.Age != 'All Ages']
box_df = box_df[box_df.Age != '18 to 44 Years']
box_df = box_df[box_df.Age != 'Age 20 and Older']
box_df = box_df[box_df.Age != 'Age 25 and Older']
box_df = box_df[box_df.YEAR != '2012']
box_df = box_df[box_df.YEAR != '2013']
box_df = box_df[box_df.YEAR != '2014']
box_df = box_df[box_df.YEAR != '2015']
box_df = box_df[box_df.YEAR != '2016']

box = sns.boxplot(x='Data_Value', y='Age', hue='YEAR', data=box_df, palette='Blues')

box.set_title('Percentage of Cigarette Smokers by Age in 2011 and 2017')
box.set_xlabel('Percent of Cigarette Smokers')
