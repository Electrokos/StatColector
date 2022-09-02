import pandas as pd

print("Type name of file in same foder as script:")
filename = str(input()) + '.csv'
df = pd.read_csv(filename)
sapData = pd.read_csv('SAPData'+filename)


print('\nDescription:\n')
print('\nCommunication Done:\n')
print(df['Category'].describe())
df['Category'].describe().to_csv('Descr_CommDone_Category_base.csv')
print(df['Category'].value_counts())
df['Category'].value_counts().to_csv('Descr_CommDone_Category_count.csv')
print(df['Direction'].describe())
df['Direction'].describe().to_csv('Descr_CommDone_Direction_base.csv')
print(df['Direction'].value_counts())
df['Direction'].value_counts().to_csv('Descr_CommDone_Direction_count.csv')
print('Total spam/junk: ' + str(df[(df.Reason == 'Miscellaneous')].shape[0]))
#df[(df.Reason == 'Miscellaneous')].shape[0].to_csv('Total spam/junk')
print('\nPerson Involved:\n')
print(df['Creator'].describe())
df['Creator'].describe().to_csv('Descr_CommDone_Creator_base.csv')
print('\nTime spended SAP:\n')
print('days \t' + str(sapData['daysPerWeek'].sum()) )
print('hours \t' + str(sapData['hours'].sum()) )

print('\nTotal Counter:\n')
dfErsteller = df['Creator'].value_counts()
print(dfErsteller)
ErstellerList = dfErsteller.index.values
print()
masData = []
for x in ErstellerList:
	print(x[:-2])
	#resultTab['Spam'] = df[(df.Creator  == x) & (df.Reason == 'Miscellaneous' )].shape[0]
	print('Counter Spam and Junk' ': \t' + str(df[(df.Creator  == x) & (df.Reason == 'Miscellaneous' )].shape[0]))
	#result['Counter Spam and Junk'] = df[(df.Creator  == x) & (df.Reason == 'Miscellaneous' )].shape[0])
	print('Counter Income E-mail' ': \t' + str(df[(df.Creator  == x) & (~(df.Reason == 'Miscellaneous' )) & (df.Category == 'E-mail' ) & (df.Direction == 'Inbound' ) ].shape[0]) )
	print('Counter Outcome E-mail' ': \t' + str(df[(df.Creator  == x) & (~(df.Reason == 'Miscellaneous' )) & (df.Category == 'E-mail' ) & (df.Direction == 'Outbound' ) ].shape[0]) )
	print('Counter Income Call' ': \t' + str(df[(df.Creator  == x) & (df.Category == 'Telephone call' ) & (df.Direction == 'Inbound' ) ].shape[0]) )
	print('Counter Outbound Call' ': \t' + str(df[(df.Creator  == x) & (df.Category == 'Telephone call' ) & (df.Direction == 'Outbound' ) ].shape[0]) ) 
	arrr = df['Reference'][df.Creator  == x].unique()
	f = open(str( x[:-2] ) + '_ticket.txt', 'w')
	f.write(str( arrr.astype('int')) )
	f.close() 
	#print( arrr.astype('int'))
	print('Counter Tickets' ': \t' + str(arrr.shape[0]) )
	print('Hours spended in SAP' ': ' + str(sapData[(sapData.Person  == x[:-2]) ]['hours'].sum() ) )
	print()
# str(df[(df.Creator == x) & (df.Reference == df[Reference].unique() )].shape[0] ) 

