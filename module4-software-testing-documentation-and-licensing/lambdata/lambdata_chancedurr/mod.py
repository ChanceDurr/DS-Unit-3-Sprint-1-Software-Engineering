import pandas as pd
import unittest

def checkNulls(dataframe):
    df = dataframe
    nulls = df.isnull().sum()
    for col, null in nulls.items():
    	print(f"'{col}' has {null} null value(s).")


def addListToDataframe(alist, dataframe, colName='new_column'):
    newCol = pd.DataFrame(alist, columns=[colName])
    dataframe = dataframe.join(newCol)
    return dataframe


class Shirt():

    def __init__(self, style='tee', sleeve='short', size='large', material='cotton'):
        self.style = style
        self.sleeve = sleeve
        self.size = size
        self.material = material

    def description(self):
        print(f'Style: {self.style}')
        print(f'Size: {self.size}')
        print(f'Material: {self.material}')
        print(f'Sleeve: {self.sleeve}')


class Complex:
	
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def subtract(self):
        return self.i - self.r

    def divide(self):
        if self.r == 0:
            return 'Cannot divide by Zero'
        else:
            return self.i / self.r

    def multiply(self):
        return self.i * self.r
    	
    def add(self):
        return self.i + self.r
