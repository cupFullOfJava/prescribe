# Method to call wikipedia and find an artist or band and return a brief summary
# of their work and life. To do this it takes the input of the user and
# uses the string librarie's capwords function to capitalize the correct words
# in their search, it then searches wikipedia using that. If the user input is found
# in the list returned it finds the index of that and summarizes that page.
#If it doesn't find an exact match it returns the most relevant wikipedia page.

# P.S. We got that easter egg.

import wikipedia
import string

"""
def getArtistBio(artist):
    w
    artist = string.capwords(artist)+'_(band)'
    try:
        search = wikipedia.search(artist)
        #if artist == "Dem Boyz":
            #summary = They some bosses
            #return (summary)
        if artist in search:
            index = search.index(artist)
            summary = wikipedia.summary(search[index],sentences=5)
            return (summary)
        else:
            summary = wikipedia.summary(search[0],sentences=5)
            return (summary)
    except wikipedia.PageError:
        return "Sorry, No biography can be found"
"""


def getArtistBio(artist):
    artist = '_'.join(artist.title().strip().split())
    try:
        page = wikipedia.page(artist+"_(band)").summary
        return page
    except wikipedia.PageError:
        try:
            page = wikipedia.page(artist).summary
            return page
        except:
            return "No Bio Found"

