# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:03:54 2021

@author: Bashir
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combining two lists together as a dictionery with letters as the key and their corresponding values as points

letter_to_points = {key:item for key,item in zip(letters,points)}

#adding point for a blank
letter_to_points[""] = 0 

#function that calculates total score for a given word,a user plays
def score_word(word):
  point_total = 0
  word = word.upper() #accounts for both uppercase and lowercase words and letters
  for letter in word:
    point_total +=letter_to_points.get(letter,0)
  return point_total
#running the function with a word "BROWNIE" ,should return 15 points
brownie_points = score_word("BROwnie")
#print(brownie_points)


#In one game,player list includes the players and words list includes the words they played
#mapping the words played by every player in player_to_words dictionery
player  = ["player1","wordNerd","Lexi Con","Prof Reader"]

words = [["BLUE","TENNIS","EXIT"],["EARTH","EYES","MACHINE"],["ERASER","BELLY","HUSKY"],["ZAP","COMA","PERIOD"]]

player_to_words = {player:words for player,words in zip(player,words)}


#calculates each player points according to the words they played and store it into player_to_points_dictionery

def player_points(dict1):
  player_to_points = {}
  for item in dict1.items():
   player,words= item
   player_points = 0
   for word in words:
    player_points += score_word(word)
   player_to_points[player] = player_points
  return player_to_points
   
#add new words when a player plays one.Similary make rooms for a new player
def play_word(player,word):
  if player not in player_to_words:
      print("{} has joined the game\n".format(player))
      player_to_words[player] = []
      player_to_words[player].append(word)
  player_to_words[player].append(word)
  
#Example to add a word ,player1  and wordNerd play a word and then calculate the total score
print("Welcome to Scrabble")
print("In order to play:")
print("(1) Use play_word to play  new words")
print(("(2) Use player_points to see the scoreboard\n"))
play_word("player1","naseem")
play_word("wordNerd","Pelikan")
#Adding a new player
play_word("Bashir","elephant")
player_scores = player_points(player_to_words)
print("The following is the scoreboard :\n")
for player,score in player_scores.items():
    print("{} : {}:".format(player,score))

