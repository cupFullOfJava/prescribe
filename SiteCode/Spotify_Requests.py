import requests


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
                return {'name': artist['name'].encode('utf-8'), 'id': artist['id'].encode('utf-8')}
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
        results.append(
                {
                    'name': related['name'].encode('utf-8'),
                    'id': related['id'].encode('utf-8'),
                    'picture': related['images'][0]['url'].encode('utf-8')
                }
        )
    return results


