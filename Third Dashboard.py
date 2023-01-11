#SecondDashboard
#Capture Respondent classified by Gender.

df_g = df_d['Gender'].value_counts().to_frame()
df_g.reset_index(inplace=True)
df_g.columns = ['Gender','Gender_count']
df_g_labels = df_g['Gender'].to_list()
df_g_values = df_g['Gender_count'].to_list()

fig,ax = plt.subplots(nrows=2,ncols=2)
ax[0][0].pie(df_g_values,autopct = '%1.1f%%')
ax[0][0].legend(labels = df_g_labels)
ax[0][0].set_title('Respondent classified by Gender')


#Respondent Count for Countries

df_c = df_d['Country'].value_counts().to_frame()
df_c.reset_index(inplace=True)
df_c.columns = ['Country','Country_count']
df_c_labels = df_c['Country'].to_list()
df_c_labels_numeric = np.arange(1,len(df_c_labels)+1)
df_c_values = df_c['Country_count'].to_list()

ax[0][1].scatter(df_c_labels_numeric,df_c_values,s=0.2)
ax[0][1].set_title('Respondent Count for Countries')


# Respondent Count by Age.
df_a = df_d['Age'].value_counts().to_frame()
df_a.reset_index(inplace=True)
df_a.columns = ['Age','Age_count']
df_a = df_a.sort_values(by='Age',ascending=True)
df_a_labels = df_a['Age'].to_list()
df_a_values = df_a['Age_count'].to_list()

ax[1][0].plot(
    df_a_labels,
    df_a_values
)
ax[1][0].set_title(' Respondent Count by Age.')
ax[1][0].set_ylabel('Quantity')
ax[1][0].set_xlabel('Age')
plt.show()
plt.close()
