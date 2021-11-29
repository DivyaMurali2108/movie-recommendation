import pandas as pd 
import numpy as np 
df=pd.read_csv('movies.csv')
C=df['vote_average'].mean()
m=df['vote_count'].quantile(0.9)
qmovies=df.copy().loc[df['vote_count']<=m]

def waitedrating(x,m=m,C=C):
    v=x['vote_count']
    r=x['vote_average']
    return (v/(v+m)*r)+(m/(m+v)*C)
qmovies['score']=qmovies.apply(waitedrating,axis=1)
qmovies=qmovies.sort_values('score',ascending=False)
output=qmovies[['title','poster_link',"release_date",'run_time','vote_average','overview']].head(20).values.tolist()

