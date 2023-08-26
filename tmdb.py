#TMDB
import pandas as pd
import requests     #to request the query
import time
# =============================================================================
# 
# df = pd.read_json('person_ids_10_16_2021.json',lines=True)
# print(df.head())
# print(df.columns)
# print(df.shape)
# df.to_csv('persons.csv')
# =============================================================================

#Deepika Padukone id = 53975

#find Deepika Padukone id and Amitabh Bachchan id from above dataframe

#condition

#df['name'] =="Deepika Padukone"
# =============================================================================
# deepika_id = df[(df['name'] =="Deepika Padukone")]['id']
# print(int(deepika_id))
# deepika_id = int(deepika_id)
# =============================================================================

api_key = open('api_key.txt','r').read()

#QUERYING THE API 
# =============================================================================
# #for highest revenue movies of 2020 in english language
# 
# query = 'https://api.themoviedb.org/3/discover/movie?api_key='+api_key+'&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year=2020'
# 
# response = requests.get(query)
# print(response)
# #respone is in json format
# 
# rev2020 = response.json()
# 
# 
# #dictionary - key:value pairs
# #to explore the response further print the leys of the dictionary
# print(rev2020.keys())
# print(rev2020['results'])
# 
# #try results in a dataframe 
# 
# r = rev2020['results']
# df = pd.DataFrame(r)
# print(df.head())
# print(df.columns)
# print(df[["title",'popularity','id']])
# 
# 
# #creating blank df
# columns = ['title','production_countries','budget','revenue']
# df11 = pd.DataFrame(columns = columns)
# 
# #querying the movie list for above movie ids
# 
# for m_id in df['id']:
#     m_id = str(m_id)
#     query = 'https://api.themoviedb.org/3/movie/'+m_id+'?api_key='+api_key+'&language=en-US'
#     response = requests.get(query)
#     mm = response.json()
#     print(mm)
#     print(mm.keys())
#     title = mm['title']
#     
#     pc = mm['production_countries']
#     if len(pc)==0:
#         production_countries = ""
#     else:
#         production_countries = pc[0]['name']
#     budget = mm['budget']
#     revenue = mm['revenue']
#     l1 = [title,production_countries,budget,revenue]
#     #appending the list to df11
#     df11.loc[len(df11)] = l1
#        
# 
# 
# df11['multiple'] =""
# n = len(df11)
# 
# for i in range(n):
#     if df11.loc[i,'budget'] !=0:
#         df11.loc[i,'multiple'] = df11.loc[i,'revenue']/df11.loc[i,'budget']
#     else:
#         df11.loc[i,'multiple'] = 0
#     
# print(df11.head())
# df11.to_csv('movies2020.csv')
# =============================================================================
    
#Deepika Padukone movies 
# =============================================================================
# query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&with_people="+str(deepika_id)
# response = requests.get(query)
# r = response.json()
# print(r)
# 
# a = r['results']
# df12 = pd.DataFrame(a)
# print(df12.head())
# print(df12.columns)
# print(df12[["title",'popularity','id']])
# =============================================================================

#Top grossing hindi films 
query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&with_original_language=hi"
# =============================================================================
# response = requests.get(query)
# r = response.json()
# print(r)
# 
# a = r['results']
# df12 = pd.DataFrame(a)
# print(df12.head())
# print(df12.columns)
# print(df12[["title",'popularity','id']])
# =============================================================================



#explore the api further 
#find top amitabh films of all times and their earning multiples
#find most popular hind films of all times 
#most popular hindi tv shows of all times



#MOST POPULAR INDIANS 
# =============================================================================
# #Getting Deepika PAdukone info
# 
# query = "https://api.themoviedb.org/3/person/53975?api_key="+api_key+"&language=en-US"
# response = requests.get(query)
# r = response.json()
# print(r)
# 
# 
# df12 = pd.DataFrame(r)
# print(df12.head())
# print(df12.columns)
# #print(df12[["title",'popularity','id']])
# =============================================================================
#Getting all persons details
dfp = pd.read_csv("pid.csv")
print(dfp.head())
dfp.sort_values(by = "popularity",ascending =False, inplace = True)

print(dfp.head())
dfp = dfp.head(1000)

indians = []

# =============================================================================
# for pid in dfp['id']:
#     query = "https://api.themoviedb.org/3/person/"+str(pid)+"?api_key="+api_key+"&language=en-US"
#     response = requests.get(query)
#     r = response.json()
#     print(r['place_of_birth'])
#     a = r['place_of_birth']
#     if a == None:
#         next
#     elif "India" in a:
#         print(r['name'])
#         l1 = [r['name'],r['id']]
#         indians.append(l1)
#         
# print(indians)
# dfi = pd.DataFrame(indians,columns = ['name','id'])
# dfi.to_csv("indians.csv")
# =============================================================================

#search people 

person = "Kriti Sanon"
query = "https://api.themoviedb.org/3/search/person?api_key="+api_key+"&language=en-US&query="+person+"&page=1&include_adult=false"

response = requests.get(query)
ind = response.json()
print(ind.keys())
print(ind['results'])
df =pd.DataFrame(ind['results'])
print(df.head(10)[['name','id','popularity']])
print(df['known_for'][0])
b = df['known_for'][0]
c = pd.DataFrame(b)
print(c.columns)
print(c.head())
print(c.shape)
for name in c['title']:
    print(name)

person = "Rajkummar Rao"
query = "https://api.themoviedb.org/3/search/person?api_key="+api_key+"&language=en-US&query="+person+"&page=1&include_adult=false"

response = requests.get(query)
ind = response.json()
print(ind.keys())
print(ind['results'])
df =pd.DataFrame(ind['results'])
print(df.head(10)[['name','id','popularity']])
print(df['known_for'][0])
b = df['known_for'][0]
c = pd.DataFrame(b)
print(c.columns)
print(c.head())
print(c.shape)
for name in c['title']:
    print(name)

person = "Prabhas"
query = "https://api.themoviedb.org/3/search/person?api_key="+api_key+"&language=en-US&query="+person+"&page=1&include_adult=false"

response = requests.get(query)
ind = response.json()
print(ind.keys())
print(ind['results'])
df =pd.DataFrame(ind['results'])
print(df.head(10)[['name','id','popularity']])
print(df['known_for'][0])
b = df['known_for'][0]
c = pd.DataFrame(b)
print(c.columns)
print(c.head())
print(c.shape)
for name in c['title']:
    print(name)
    
def person_finder(name):
    query = "https://api.themoviedb.org/3/search/person?api_key="+api_key+"&language=en-US&query="+name+"&page=1&include_adult=false"
    response = requests.get(query)
    ind = response.json()
    print(ind.keys())
# =============================================================================
#     print(ind['results'])
# =============================================================================
    df =pd.DataFrame(ind['results'])
    print(df.head(10)[['name','id','popularity']])
    df.sort_values(by = 'popularity', ascending = False,inplace = True)
    print(df['known_for'][0])
    b = df['known_for'][0]
    c = pd.DataFrame(b)
# =============================================================================
#     print(c.columns)
#     print(c.head())
#     print(c.shape)
# =============================================================================
    for name in c['title']:
        print(name)
    pid = df['id'][0]
    pop = df['popularity'][0]
    print(pid)
    print(pop)
    return(pid,pop)
    
a = person_finder("Prabhas")

#movie cast names and ids 
#Movie - Hum Do Humaare Do
#Rajkummar Rao, Kriti Sanon, Paresh Rawal, Ratna Pathak Shah

cast = ["Rajkummar Rao", "Kriti Sanon", "Paresh Rawal", "Ratna Pathak Shah"]
cast_list = []
for name in cast:
    b = person_finder(name)
    pid = b[0]
    pop = b[1]
    l1 = [name,pid,pop]
    cast_list.append(l1)

print(cast_list)

df_cast = pd.DataFrame(cast_list, columns = ["name","id","popularity"])
print(df_cast.head())

#Cast movies 

all_cast_movies = []

for cast_id in df_cast['id']: 
    print(cast_id)
    time.sleep(3)
    query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=release_date.asc&include_adult=false&include_video=false&page=1&with_cast="+str(cast_id)
    response = requests.get(query)
    ind = response.json()
    print(ind.keys())
    total_movies = ind['total_results']
    total_pages = ind['total_pages']
    print(total_movies)
    print(total_pages)
    print(ind['page'])

    
    for page in range(1,total_pages+1):    
        print(page)
        p_query = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=release_date.asc&include_adult=false&include_video=false&page="+str(page)+"&with_cast="+str(cast_id)
        response = requests.get(p_query)
        ind1 = response.json()
# =============================================================================
#         print(ind1.keys())
# =============================================================================
        total_movies = ind1['total_results']
        total_pages = ind1['total_pages']
        df_movies = pd.DataFrame(ind['results'])
        print(df_movies.columns)
        for movie_ids in df_movies['id']:
            print(movie_ids)
            all_cast_movies.append(movie_ids)
            print(len(all_cast_movies))


print(len(all_cast_movies))



