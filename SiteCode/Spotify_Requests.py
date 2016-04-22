import requests
from GetBio import getArtistBio


###
# Searches for artists in the Spotify API, Returns the name and Spotify ID of the artist if the search was successful
# returns None if the search is unsuccessful
###
def search_artist(artist_name):
    search_url = "https://api.spotify.com/v1/search?q="+artist_name+"&type=artist"
    artists = requests.get(search_url)
    try:
        for artist in artists.json()['artists']['items']:
            if artist['name'].lower() == artist_name:
                return {'name': artist['name'], 'id': artist['id']}
            else:
                return None
    except KeyError:
        return None


###
# Takes a Spotify ID as input, and returns a list of dictionaries corresponding with artist names, IDs, and links
# to images for all artists deemed similar to the original artist by Spotify.
###
def get_related(artist_id):
    url = "https://api.spotify.com/v1/artists/"+artist_id+"/related-artists"
    related_artists = requests.get(url).json()['artists']
    results = []
    for related in related_artists:
        if len(related['images']) > 0:
            results.append(
                    {
                        'name': related['name'],
                        'id': related['id'],
                        'picture': related['images'][0]['url']
                    }
            )
        else:
            results.append(
                    {
                        'name': related['name'],
                        'id': related['id'],
                    }
            )
    return results


###
# Gets the relevant data for a particular artist
###
def get_artist(artist_id):
    url = "https://api.spotify.com/v1/artists/"+artist_id
    artist = requests.get(url).json()
    return {"name": artist['name'],
            "id": artist['id'],
            'picture': artist['images'][0]['url']}
