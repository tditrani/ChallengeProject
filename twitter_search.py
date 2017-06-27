#!/usr/bin/env python


import twitter

#Get the term to search for
search_term = raw_input("Term to search for: ")

#Initilize the Api with the necisary info
api = twitter.Api(consumer_key='uNzYbptRPxMLQnoZ73daQuPHw',
                  consumer_secret='NExhIi50MBCkt6bkTTK62MEAbcZcUyvBir9wK81vcCwMBen15y',
                  access_token_key='2776231794-RluWf6txQBnDUDWB6Uq5TEbOwZ9dNnajBBQa5b2',
                  access_token_secret='s4kjjSfykRDunrd6S2eptmqFdSrspJh7dpUYZZ5kkKJWm'
                  )
#Search twitter
result = api.GetSearch(term=search_term)

text_array = []

#Put the text from the related tweets into one array
for u in result:
    text_array.append(u.text)

print(text_array)









