from canvasapi import Canvas
import os
from dotenv import load_dotenv
import re
import json

# loads environment tokens so u cant steal ^_^
load_dotenv()


# HTML parser that removes html tags
CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

#loads keys from environment that is used to auth who I 
# who i am

API_KEY = os.environ['KEY']
API_URL = os.environ['URL']

#Initiate canvas object

canvas = Canvas(API_URL, API_KEY)

#get group of discussion
course = canvas.get_group(41747)

#prints the name of the discussion

def getreplies():
#saves discussion object into var
  disc = course.get_discussion_topic(2504581)
  #gets entries of discussion object
  y = disc.get_topic_entries()
  # changes pagnated list to iterable and sliceable one
  iterables = [str(i) for i in y]
  final = []

  # for loops that removes html tags and removes student number from back 
  for i, unclean in enumerate(iterables):
      reply = cleanhtml(unclean)
      l = len(reply)
      removenumber = reply[:l-10]
      finalstring = removenumber.replace('SONG:', '')
      final.append(finalstring)

  return final
