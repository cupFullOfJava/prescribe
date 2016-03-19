/**
*
* The getArtists function accepts an "Artist String" and a higher order callback function as parameters.
* The "Artist String" is the string that is pulled from the search bar on the search page.
* The Artist String is stripped of trailing and leading whitespace, and any spaces between words is replaced
* with "%20" to match the format that the API accepts.
*
* The function then makes an asynchronous call to the spotify API host, if the call is successful it passes the
* resulting JSON data from the API to the callback function. If the call is unsuccessful then it logs the resulting error
* message to the console.
*
**/
function getArtists(ArtistString, callback) {
	var searchString = ArtistString.split(" ").join("%20");
	$.ajax({
		url: "https://api.spotify.com/v1/search?q="+searchString+"&type=artist",
		dataType: "json",
		error: function(response) {
			console.log("Artist String "+ArtistString);
			console.log("Search String "+searchString);
			console.log(response)
		},
		success: function(response) {
			callback(response.artists, ArtistString)	 
		}
	})
}

/**
*
* The getRelated function accepts an ArtistID from the Spotify API and a higher order callback function.
* It makes an asynchronous call the Spotify API using the ArtistID, if the call is successful then it
* calls the callback function on the resulgin JSON data, otherwise, it logs the resulting error message
* to the console.
*
**/
function getRelated(ArtistID, callback) {
	$.ajax({
		url: "https://api.spotify.com/v1/artists/"+ArtistID+"/related-artists",
		datatype: "json",
		error: function(response) {
			console.log(response)
		},
		success: function(response) {
			callback(response)
		}
	})
};

/**
*
* The printArtists function accepts a list of JSON formatted search results from the spotify API and
* the original string that the user typed into the search bar as input. It sets a flag to false and then
* iterates through all of the search results. If  the names of any of the artists in the search results
* are an exact match with the original search string, then the printRelated function is called on the 
* data set corresponding with that name.
*
**/
function printArtists(Artists, searchArtist){
	console.log("There are "+Artists.items.length+" artists returned");
	exactmatch = false
	for(i = 0; i< Artists.items.length; i++){
		if(Artists.items[i].name.toLowerCase() == searchArtist.toLowerCase().trim()){
			getRelated(Artists.items[i].id, printRelated)
			exactmatch = true
		}
	}
}

/**
*
* The printRelated function takes a JSON format response containing a list of artists and
* iterates through it, appending each one to the appropriate HTML feature.
*
**/
function printRelated(response){
	for(i = 0; i < response.artists.length; i++){
		$("#reclist").append("<li>"+response.artists[i].name+'</li>')
	}	
}
