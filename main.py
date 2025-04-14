# Lets import from public API
# importing  our libraries
import requests
import pandas as p

url = 'https://randomuser.me/api/?results=100'
response = requests.get(url)

data = response.json()

df_user = p.json_normalize(data['results'])
print(df_user.head())


df_cleaned = df_user[['name.first', 'name.last', 'email', 'gender',
                      'location.city', 'location.country', 'dob.age', 'login.username']]

df_cleaned.columns = ['first_name', 'last_name', 'email',
                      'gender', 'city', 'country', 'age', 'username']

users_from_canada = df_cleaned[df_cleaned['country'] == 'Canada']
print(users_from_canada)
users_from_canada.to_csv("Canadian_users.csv", index=False)

df_cleaned.to_csv('api_users.csv', index=False)
print('Saved API data to api_users.csv')
