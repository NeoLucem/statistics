import pandas as pd

# read the document
data = pd.read_csv('raw_data.csv')
datas = pd.read_csv('raw_data.csv')
n = 105

#draw the frequency distribution
bins = [40, 50, 60, 70, 80, 90]
labels = ['40-50', '50-60', '60-70', '70-80', '80-90']
data['Number Bracket'] = pd.cut(data['data'], bins, labels=labels)
data = pd.crosstab(index=data['Number Bracket'], columns='Frequency')
print("\n Frequency distribution", data)

#draw the relative frequency distribution
data['RFD'] = data['Frequency']/105
print("\n Relative frequency distribution", data)

#draw the cumulative frequency distribution
data['CFD'] = data['Frequency'].cumsum()
print("\n Cumulative frequency distribution", data)

#draw the cumulative relative frequency distribution
data['CRFD'] = data['RFD'].cumsum()
print("\n Cumulative relative frequency distribution", data)

#compute the mean
data['Mean'] = data.mean(True)
print("\n", data)

#compute the median
median = datas.median()
print("\n The median is", median)

#compute the mode
mode = datas.mode()
print("\n The mode is", mode)

print(datas.min())

