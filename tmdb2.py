#TMDB2

import requests # to make TMDB API calls
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


api_key = open('api_key.txt','r').read()


#FIND OUT PROBABLE SUCCESS PARAMETERS OF THIS FILM 
#popularity of cast members 
#average of their movie ratings
#average of their movie budgets, revenues and multiples

#getting person ids
#1) Do it from the downloaded json files
#2) To use the API search function

cast_name = "Allu arjun"

def person_finder(cast_name):
    query = "https://api.themoviedb.org/3/search/person?api_key="+api_key+"&language=en-US&query="+cast_name+"&page=1&include_adult=false"
    response = requests.get(query)
    r = response.json()
    a = r['results']
    # =============================================================================
    # print(r['results'])
    # =============================================================================
    df = pd.DataFrame(a)
    print(df.columns)
    df.sort_values(by='popularity', ascending = False, inplace = True)
    print(df.head()[['name','id','popularity']])
    pid = df['id'][0]
    pop = df['popularity'][0]
    t1 = [df['name'][0],pid,pop]
    return(t1)

#movie casts and ids
#movie - hum do humare do
#cast 
cast = ["Rajkummar Rao", "Kriti Sanon", "Ratna Pathak Shah", "Paresh Rawal"]

cast_list = []
for name in cast:
    b = person_finder(name)
    name1 = b[0]
    pid = b[1]
    pop = b[2]
    l1 = [name,pid,pop]
    cast_list.append(l1)
    
df_cast = pd.DataFrame(cast_list, columns = ['name','id','popularity'])

df_cast.sort_values(by="popularity",ascending = False, inplace = True)
print(df_cast.head())

#Cast Movies 

all_cast_movies = []

#movie_ratings, votes, budgets, revenues and multiples

for cast_id in df_cast['id']:
    print(cast_id)
    p_query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=release_date.asc&include_adult=false&include_video=false&with_cast="+str(cast_id)
    response = requests.get(p_query)
    r = response.json()
    print(r.keys())
    print(r['total_pages'])
    print(r['total_results'])
    print(r['page'])
    total_pages = r['total_pages']

# =============================================================================
#     df = pd.DataFrame(r['results'])
#     print(df.columns)
#     print(df.head())
#     print(df.shape)
# =============================================================================
    
#go pagewise and obtain movie ids of all movies of all cast members
    for page in range(1,total_pages+1):
        print(page)
        p_query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=release_date.asc&include_adult=false&include_video=false&page="+str(page)+"&with_cast="+str(cast_id)
        response = requests.get(p_query)
        r = response.json() 
        df = pd.DataFrame(r['results'])
        print(df.columns)
        print(df.head())
        print(df.shape)        
        for mid in df['id']:
            all_cast_movies.append(mid)
            
        
print(len(all_cast_movies))

all_movies_list = []
for mid in all_cast_movies:
    m_query = "https://api.themoviedb.org/3/movie/"+str(mid)+"?api_key="+api_key
    response = requests.get(m_query)
    r = response.json()
# =============================================================================
#     print(r.keys())
# =============================================================================
    movie_name =r['title']
    print(movie_name)
    budget = r['budget']
    revenue = r['revenue']
    popularity = r['popularity']
    vote_average = r['vote_average']
    m1 = [movie_name,budget,revenue,popularity,vote_average]
    print(m1)
    all_movies_list.append(m1)
    
movies_df = pd.DataFrame(all_movies_list, columns = ["name","budget","revenue","popularity","vote_avg"])
print(movies_df.head())
movies_df['multiple'] = movies_df['revenue']/movies_df['budget']
movies_df = movies_df.replace([np.inf, -np.inf], np.nan).dropna(axis=0)


movies_df.to_csv("cast_movies.csv")



average_budget = movies_df['budget'].mean()
average_revenue = movies_df['revenue'].mean()
average_popularity = movies_df['popularity'].mean()
average_multiple = movies_df['multiple'].mean()

print("average budget of their films is {}, average revenue is {},average_multiple is {} and average popularity is {} ".format(average_budget,average_revenue,average_multiple, average_popularity))










