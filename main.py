import random
movie = {"Title":"Star Wars: Episode III - Revenge of the Sith","Year":"2005","Rated":"PG-13","Released":"19 May 2005","Runtime":"140 min","Genre":"Action, Adventure, Fantasy","Director":"George Lucas","Writer":"George Lucas, John Ostrander, Jan Duursema","Actors":"Hayden Christensen, Natalie Portman, Ewan McGregor","Plot":"Nearly three years have passed since the beginning of the Clone Wars. The Republic, with the help of the Jedi, take on Count Dooku and the Separatists. With a new threat rising, the Jedi Council sends Obi-Wan Kenobi and Anakin Skywalker to aid the captured Chancellor. Anakin feels he is ready to be promoted to Jedi Master. Obi-Wan is hunting down the Separatist General, Grievous. When Anakin has future visions of pain and suffering coming Padmé's way, he sees Master Yoda for counsel. When Darth Sidious executes Order 66, it destroys most of all the Jedi have built. Experience the birth of Darth Vader. Feel the betrayal that leads to hatred between two brothers. And witness the power of hope.","Language":"English","Country":"United States","Awards":"Nominated for 1 Oscar. 26 wins & 63 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.6/10"},{"Source":"Rotten Tomatoes","Value":"79%"},{"Source":"Metacritic","Value":"68/100"}],"Metascore":"68","imdbRating":"7.6","imdbVotes":"765,615","imdbID":"tt0121766","Type":"movie","DVD":"01 Nov 2005","BoxOffice":"$380,270,577","Production":"N/A","Website":"N/A","Response":"True"}

def whatIs(m, t):
  try:
    if t == 'Title':
        autoSentence(m, t, f"{m[t]}")

    elif t == 'Released':
      temp = movie['Released']
      temp = temp[7:11]
      
      if(temp == "2022"):
        autoSentence(t,f"{m['Title']} was released was released {m[t]} which was released this year.")
        
      else:
        autoSentence(t,f"{m['Title']} was released was released {m[t]}.")
        
    elif t == 'Actors':
      temp = getRandom("acclaiemed", "popular", " ")
      autoSentence(t, f"{m['Title']} stars {temp} actors: {m[t]}.")
      
    elif t == 'Plot':
      autoSentence(t, f"The {t} of the {m['Title']} is: {m[t]}")
      
    elif t == 'Director':
      temp = getRandom("brilliant", "dashing", "marvelous")
      autoSentence(t, f"The {temp} {t} {m[t]} directed {m['Title']}.")
      
    elif t == 'Metascore':
      temp = m[t]
      if int(temp) == 100:
        autoSentence(t, f"{m['Title']} has a perfect {t} score of {temp}%!")
        
      elif int(temp[0]) <= 6:
        autoSentence(t, f"{m['Title']} has a terrible {t} level is {temp}%. Spend your time on another film.")
        
      elif int(temp[0]) >= 7:
        autoSentence(t, f"The {t} of {m['Title']} is {temp}. I would suggest this movie to others.")
        
    elif t == 'Awards':
      autoSentence(t, f"{m['Title']} has recived {m[t]} for {t}.")
      
    elif t =='Writer':
      temp = getRandom("talented", "fabulous", " ")
      autoSentence(t, f"The {t} of {m['Title']} is the {temp} {m[t]}.")
  except:
    # This code is useless. Just so that in case something fails
    b = 1
     
    
def autoSentence(t, sentence):
  print(t + ": " + sentence)


def blog(m):
  headLine(m)
  
  for thing in m:
    temp = whatIs(m, thing)
  print()
  temp = m['Metascore']
  
  if (temp) == 100:
    autoSentence("My review", f"{m['Title']} was a amazing movie. I recommend it. The acting from {m} is amazing. The plot written by {m['Writer']} was great and the cinematography by {m['Director']} was brilliant.")
    
  elif int(temp[0]) >= 6:
    autoSentence("My review", f"{m['Title']} was a terrible movie. All personel that worked on this movie should be shamed. The disgusting plot written by {m['Writer']} and directed by {m['Director']}. The actors performance was terrible, {m['Actors']}.(in all reality, i actually love this movie, im so upset it has such a bad score)")
    
  elif int(temp[0]) <= 7:
    autoSentence("My review", f"{m['Title']} this movie is pretty acclaimed. The director {m['Director']} should be very happy with this movie. {m['Actors']} did a great job in this film and really support the writing of {m['Writer']}. If this movie sounds intresting I suggest watching it.")

def headLine(m):
  temp = getRandom(f"HERE ARE SOME FACTS ABOUT {m['Title']}!", f"LET'S LOOK BACK ON {m['Title']}!", f"{m['Title']}!")
  print(temp)
  print()


def getRandom(c1, c2, c3):
  if (c2 != " " and c3 != " "):
    ran = random.randint(0, 2)
    if ran == 0:
      return c1
    elif ran == 1:
      return c2
    else:
      return c3
  elif(c3 != ""):
    ran = random.randint(0, 1)
    if ran == 0:
      return c1
    elif ran == 1:
      return c2
      
blog(movie)