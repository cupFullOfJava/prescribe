# Method to call wikipedia and find an artist or band and return a brief summary
# of their work and life. To do this it takes the input of the user and
# uses the string librarie's capwords function to capitalize the correct words
# in their search, it then searches wikipedia using that. If the user input is found
# in the list returned it finds the index of that and summarizes that page.
# If it doesn't find an exact match it returns the most relevant wikipedia page.

import wikipedia
import string

def getArtistBio(artist):
    if artist == "B. Deff and the Cat Daddys":
        return open('.bio','r').read()
    else:
        artist = '_'.join(artist.title().strip().split())
        try:
            page = wikipedia.page(artist+"_(band)").summary
            return page
        except wikipedia.PageError:
            try:
                page = wikipedia.page(artist+"_(rapper)").summary
                return page
            except wikipedia.PageError:
                try:
                    page = wikipedia.page(artist).summary
                    return page
                except:
                    return "No Bio Found"

