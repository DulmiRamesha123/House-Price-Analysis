import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

#from google.colab import files
#uploaded = files.upload()

#import io
#df = pd.read_csv(io.BytesIO(uploaded['kc_house_data.csv']))
# Dataset is now stored in a Pandas Dataframe
df = pd.read_csv('kc_house_data.csv')
df.head()

#read last 5 rows
df.tail(5)

#describe the data(statistical analysis)
df.describe()

df.info()

df.isnull().sum()

"""**There is no missing values so no need to handle them**"""

#the id,date, column no need for analysis so drop it
df=df.drop(['id','date','yr_built','yr_renovated', 'zipcode'],axis=1)

df.head(5)

# Explore which numeric columns have high linear correlation
corr_matrix = df.corr()
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, cmap='Blues')

#Pearson's Correlation Coefficient: helps you find out the relationship between two quantities. 
#It gives you the measure of the strength of association between two variables. 
#The value of Pearson's Correlation Coefficient can be between -1 to +1. 
#1 means that they are highly correlated and 0 means no correlation.

df.corr()

"""**Ditribution of data**"""

plt.figure(figsize = (20, 20))
sns.set(style="darkgrid")
plotnumber = 1

for column in df:
    if plotnumber <= 30:
        ax = plt.subplot(5, 6, plotnumber)
        sns.histplot(df[column],kde=True)
        plt.xlabel(column)
        
    plotnumber += 1

plt.show()

count = df['condition'].value_counts().values
sns.barplot(x = [1,2,3,4,5], y = count)
plt.title('condition variable count')

count = df['condition'].value_counts().values
count

count = df['grade'].value_counts().values
sns.barplot(x = [1,2,3,4,5,6,7,8,9,10,11,12], y = count)
plt.title('grade')

count = df['grade'].value_counts().values
count

count = df['bedrooms'].value_counts().values
count

plt.figure(figsize = (20, 20))
plotnumber = 1

for column in df:
    if plotnumber <= 15:
        ax = plt.subplot(5, 6, plotnumber)
        sns.boxplot(x=df[column])
        plt.xlabel(column)
        
    plotnumber += 1
plt.title("Outliers")
plt.show()

#For each k value , we will initialise k-means and use 
#the interia attribute to identify sum of squared distance of 
#samples to the nearest cluster center

sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters = k) #in each iteration create a model with clusters = k
    km.fit(df[['view','condition']])
    sse.append(km.inertia_)#Interia will give the sse

sse

plt.xlabel('Number of Clusters')
plt.ylabel('Within - cluster Sum of squared error') 
plt.plot(k_rng,sse)

#Initialize the clusters
km = KMeans(5)

from sklearn.preprocessing import MinMaxScaler

"""Before clustering"""

plt.scatter(df['bedrooms'],df['bathrooms'])
plt.xlabel('bedrooms')
plt.ylabel('bathrooms')

plt.scatter(df['lat'],df['long'])
plt.xlabel('lat')
plt.ylabel('long')

"""After custering"""

km=KMeans(5)
y_predicted=km.fit_predict(df[['bedrooms','bathrooms']])
y_predicted

df['Cluster']=y_predicted
df.head()

km.cluster_centers_

plt.scatter(df['bedrooms'],df['bathrooms'],c=df['Cluster'],cmap='rainbow')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centrold')

"""Apply kMeans clustering for Whole data set"""

cdf = df[['bedrooms','bathrooms','floors','sqft_living','sqft_lot','sqft_above','sqft_basement','condition']]
x = cdf.iloc[:, :7]
y = cdf.iloc[:, -1]

kmean=KMeans(n_jobs = -1, n_clusters = 5, init='k-means++')
kmean.fit(x, y)

import pickle
pickle.dump(kmean,open('kmeans1.pkl','wb'))

