from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np 
df=pd.read_csv('movies.csv')
df=df[df['soup'].notna()]
count=CountVectorizer(stop_words='english')
countmatrix=count.fit_transform(df['soup'])
cosinesim=cosine_similarity(countmatrix,countmatrix)
df=df.reset_index()
indices=pd.Series(df.index,index=df['title'])
def getrecommendation(title):
    idx=indices[title]
    simscores=list(enumerate(cosinesim[idx]))
    simscores=sorted(simscores,key=lambda x:x[1],reverse=True)
    simscores=simscores[1:11]
    movie_indices=[1[0]for i in simscores]
    return df[['title','poster_link','release_date','run_time','vote_average','overview']].iloc[movie_indices].values.tolist()