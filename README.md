
# SpotifyXCanvas


<img src="https://cdn.discordapp.com/attachments/951616423745167370/967844859622858802/icon32x.png" data-canonical-src="https://cdn.discordapp.com/attachments/951616423745167370/967844859622858802/icon32x.png" width="400" height="400" />

> If you'd like to contact me please looked at my [ReadMe](https://github.com/carsonful/carsonful) on how to reach me.
> An example. https://open.spotify.com/playlist/2vwgqcsUDuXbAdevQvthTi
---
### Table of Contents
All sections regarding this repository.
- [Tutorial](#tutorial)
- [Description](#description)
- [How To Use](#how-to-use)
- [References](#resources)
- [License](#license)
- [Author Info](#author-info)



---
## Tutorial

If you'd like to recreate this program, you can access the **extensions** folder and 
then the **discussionreplies.py file**. You will have to change the group and discussion id's to your specific discussion.

#### Link Example:
https://xxxx.instructure.com/groups/12345/discussion_topics/1234567

The **5** digit is your group id.
The **7** digit is your discussion id.



```py
course = canvas.get_group(12345)

def getreplies():
#saves discussion object into var
  disc = course.get_discussion_topic(1234567)
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
```

Make sure to put in your own ID's that way you can fetch the replies of the discussion.

[Back To The Top](#spotifyxcanvas)

---

## Description

This program allows a user to read a discussion in canvas, and retrieve its entries, a discussion with replies
of song names will be broken up into a list and searched by the spotify api, this is then added to the playlist,
it does not allow duplicate songs to be added


For example:


<img src="https://cdn.discordapp.com/attachments/951616423745167370/967849126270226442/Opera_Snapshot_2022-04-24_140640_open.spotify.com.png" data-canonical-src="https://cdn.discordapp.com/attachments/951616423745167370/967849126270226442/Opera_Snapshot_2022-04-24_140640_open.spotify.com.png" width="700" height="400"/>

> This is a screen shot of the playlist after running the program.

<img src="https://cdn.discordapp.com/attachments/951616423745167370/967849126588989470/Opera_Snapshot_2022-04-24_140536_sdhc.instructure.com.png" data-canonical-src="https://cdn.discordapp.com/attachments/951616423745167370/967849126588989470/Opera_Snapshot_2022-04-24_140536_sdhc.instructure.com.png" width="700" height="400"/>

> This was the input from the discussion.


---
#### Resources

- JSON
- Spotify API
- CanvasAPI


[Back To The Top](#spotifyxcanvas)

---

## How To Use

#### Installation
To be able to execute this code you will need **these** modules:
**SEE REQUIREMENTS.TXT FOR MODULES**
1. Make sure `requirements.txt` is in your environment.
2. cd to your directory where the file is.
3. run the command `pip install -r requirements.txt` in your shell.

#### Canvas API Reference

```py
# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://example.com"
# Canvas API key
API_KEY = "p@$$w0rd"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
```
[Back To The Top](#spotifyxcanvas)

---

## References
- [Spotify API](https://developer.spotify.com/documentation/) Docs
- [Canvas API](https://canvas.instructure.com/doc/api/) Docs
- [JSON](https://docs.python.org/3/library/json.html) Docs


[Back To The Top](#spotifyxcanvas)

---

## License

MIT License

Copyright (c) [2022] [Carson Fulmer]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#spotifyxcanvas)

---

## Author Info

- LinkedIn - [Carson Fulmer](https://www.linkedin.com/in/carsonfulmer/)
- Website - [Carson Fulmer](http://carsonfulmer.com)

[Back To The Top](#spotifyxcanvas)
