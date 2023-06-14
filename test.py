import pandas as pd
import matplotlib.pyplot as plt
# read the document
data = pd.read_csv('raw_data.csv')
datas = pd.read_csv('raw_data.csv')

###draw the frequency distribution
bins = [48.3, 54.4, 60.4, 66.4, 72.4, 78.4, 84.4, 90.4]
labels = ['48.3-54.4', '54.4-60.4', '60.4-66.4', '66.4-72.4', '72.4-78.4',  '78.4-84.4', '84.4-90.4']
data['Class'] = pd.cut(data['data'], bins, labels=labels)
data = pd.crosstab(index=data['Class'], columns='Frequency')
#print("\n Frequency distribution", data)



###draw the relative frequency distribution
data['RFD'] = data['Frequency']/105
# print("\n Relative frequency distribution", data)


###draw the cumulative frequency distribution
data['CFD'] = data['Frequency'].cumsum()
# print("\n Cumulative frequency distribution", data)


###draw the cumulative relative frequency distribution
data['CRFD'] = data['RFD'].cumsum()
#print("\n Cumulative relative frequency distribution", data)


###compute the mean
data['Mean'] = data.mean(True)
print("\n", data)


###compute the median
median = datas.median()
print("\n The median is", median)


###compute the mode
mode = datas.mode()
print("\n The mode is", mode)


n = data['CFD'].max()
#print((data['Mean'].cumsum())/n)

plt.hist(datas, bins, histtype='bar', color='red', align='mid')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
