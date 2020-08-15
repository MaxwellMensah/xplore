#importing the necessary libraries
import pandas as pd

#function to handle the data exploration
def xplore(data):
    #writing the pop-up vscode  guide as a block comment
    '''
    xplore is a python package for light-weight python projects in data science and analytics, AI and ML.\n
    The xplore() function takes the arg 'data', which is a variable assigned to the file path/url of a labelled dataset.\n
    xplore converts the labelled dataset to a DataFrame and performs some predefined exploratory data analysis on the dataset.
    '''
    #converting the structured data to a dataframe
    data = pd.DataFrame(data)
    print('------------------------------------')
    print('The fist 5 entries of your dataset are:\n')
    print(data.head()) #printing the first 5 entries of the dataset
    print('')

    print('------------------------------------')
    print('The description of you dataset is:\n')
    print(data.describe) #printing a descriptipn of the dataset
    print('')

    print('------------------------------------')
    print('The total number of null values from individual columns of your data set are:\n')
    print(data.isnull().sum()) #printing the total number of null values in the dataset
    print('')

    print('------------------------------------')
    print('The shape of your dataset in the order of rows and columns is:\n')
    print(data.shape) #printing the shape of the dataset
    print('')

    print('------------------------------------')
    print('The features of your dataset are:\n')
    print(data.columns) #printing features
    print('')

    print('------------------------------------')


#data = pd.read_csv('fifa_ranking.csv')
#xplore(data)