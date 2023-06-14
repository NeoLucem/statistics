import pandas as pd

data = pd.read_csv('raw_data.csv')
print(data.shape)
print(data.head(105))

bins = [40, 50, 60, 70, 80, 90]
labels = ['40-50', '50-60', '60-70', '70-80', '80-90']

data['Number Bracket'] = pd.cut(data['data'], bins, labels=labels)
print(data)

data = pd.crosstab(index=data['Number Bracket'], columns='Frequency')
print(data)

data['Cumulative Frequency'] = data['Frequency'].cumsum()
print("the cumulative frequency distribution is ")
print(data)

data['CRFD'] = data['Frequency'].cumsum()/105
print("the cumulative  relative frequency distribution is ")
print(data)

data['RFD'] = data['CRFD'].cumsum()
print('the relative frequency distribution is ')
print(data)

data['MidPoint'] = [45.5, 55.5, 65.5, 75.5, 85.5]
print("the mid points are")
print(data)

data['Mean'] = ((data['Frequency'] * data['MidPoint']).cumsum())/105
print("the mean is")
print(data)

#compute the middle point
middlePoint = (105 + 1)/2
print("the middle item is")
print(middlePoint)

#compute the median
print("the median is")
print(data.median())

