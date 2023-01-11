import pandas as pd
import matplotlib.pyplot as plt




df_d = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m5_survey_data_demographics.csv')

df_t = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m5_survey_data_technologies_normalised.csv')




df_top_10_l = df_t['LanguageWorkedWith'].value_counts().to_frame().sort_values(by='LanguageWorkedWith',ascending=False).head(10)
df_top_10_l.reset_index(inplace=True)
df_top_10_l.columns = ['Language','Language_count']

df_top_10_d = df_t['DatabaseWorkedWith'].value_counts().to_frame().sort_values(by='DatabaseWorkedWith',ascending=False).head(10)
df_top_10_d.reset_index(inplace=True)
df_top_10_d.columns = ['Database','Database_count']

df_top_10_p = df_t['PlatformWorkedWith'].value_counts().to_frame().sort_values(by='PlatformWorkedWith',ascending=False).head(10)
df_top_10_p.reset_index(inplace=True)
df_top_10_p.columns = ['Platform','Platform_count']


df_top_10_w = df_t['WebFrameWorkedWith'].value_counts().to_frame().sort_values(by='WebFrameWorkedWith',ascending=False).head(10)
df_top_10_w.reset_index(inplace=True)
df_top_10_w.columns = ['WebFrame','WebFrame_count']



fig,ax = plt.subplots(nrows=2,ncols=2)
ax[0][0].bar(df_top_10_l['Language'],df_top_10_l['Language_count'])
ax[0][0].set_xlabel('Languagee')
ax[0][0].set_ylabel('Amount')
ax[0][0].set_title('Top 10 LanguageWorkedWith')


ax[0][1].bar(df_top_10_d['Database'],df_top_10_d['Database_count'])
ax[0][1].set_xlabel('Databasee')
ax[0][1].set_ylabel('Amountt')
ax[0][1].set_title('Top 10 Database')

ax[1][0].pie(df_top_10_p['Platform_count'],labels=df_top_10_p['Platform'],autopct = '%1.1f%%')
ax[1][0].set_title('TOP 10 Platform')
ax[1][0].legend(bbox_to_anchor=(1.3, 1))




ax[1][1].pie(df_top_10_w['WebFrame_count'],labels=df_top_10_w['WebFrame'],autopct = '%1.1f%%')
ax[1][1].set_title('TOP 10 WebFrame')
ax[1][1].legend(bbox_to_anchor=(1.1, 1))

plt.show()

![image](https://user-images.githubusercontent.com/56845008/211799267-054f6322-39bc-4472-a6dc-240bbd708f63.png)
