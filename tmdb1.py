import requests # to make TMDB API calls
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


api_key = open('api_key.txt','r').read()


# =============================================================================
# query = 'https://api.themoviedb.org/3/discover/movie?api_key=' +  api_key + '&primary_release_year=2017&sort_by=revenue.desc'
# 
# response = requests.get(query)
# 
# rev2017 = response.json()
# 
# print(rev2017['results'])
# r = rev2017['results']
# df = pd.DataFrame(r)
# print(df.head())
# print(df.columns)
# 
# print(df[['title','popularity','id']])
# 
# 
# columns = ["title","production_countries","budget",'revenue']
# df1 = pd.DataFrame(columns = columns)
# 
# for m_id in df['id']:
#     movie_id = str(m_id)
#     film_query = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+api_key+'&language=en-US'
#     response = requests.get(film_query)
#     m = response.json()
#     print(m.keys())
#     title = m['title']
#     prod_c = m['production_countries'][0]['name']
#     budget = m['budget']
#     revenue = m['revenue']
#     l1 = [title,prod_c,budget,revenue]
#     df1.loc[len(df1)] = l1
# # =============================================================================
# #     df11 = df[["title","production_countries","budget",'revenue']]
# #     df1 = df1.append(df11)
# # =============================================================================
#     
# print(df1.head())
# df1['multiple'] = df1['revenue']/df1['budget']
# print(df1.to_csv('mov.csv'))
# 
# #multiple wise two most successful films from the above list
# #above list for last 10 years
# 
# #combined list for last 10 years
# 
# =============================================================================
#Trying movies with Deepika Padukone
# =============================================================================
# query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&with_cast=53975"
# 
# response = requests.get(query)
# 
# ind = response.json()
# 
# r = ind['results']
# df = pd.DataFrame(r)
# print(df.head())
# print(df.columns)
# print(df[['title','original_language']])
# 
# 
# 
# =============================================================================

# =============================================================================
# #Most popular hindi movies of all time 
# #find out their revenue and multiple year wise 
# #like above
# 
# query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&with_original_language=hi"
# response = requests.get(query)
# ind = response.json()
# 
# r = ind['results']
# df = pd.DataFrame(r)
# print(df.head())
# print(df.columns)
# print(df[['title','original_language']])
# 
# 
# =============================================================================

#Lets find out about tv shows and series
# =============================================================================
# query = "https://api.themoviedb.org/3/discover/tv?api_key="+api_key+"&sort_by=popularity.desc&page=1&with_original_language=hi&with_watch_monetization_types=flatrate"
# response = requests.get(query)
# ind = response.json()
# r = ind['results']
# df = pd.DataFrame(r)
# print(df.head())
# print(df.columns)
# print(df[['name','original_language','id']])
# 
# 
# 
# 
# #family man
# query = "https://api.themoviedb.org/3/tv/93352?api_key="+api_key
# response = requests.get(query)
# ind = response.json()
# print(ind.keys())
# print(ind)
# 
# dftv = pd.DataFrame(ind)
# print(dftv.columns)
# =============================================================================

