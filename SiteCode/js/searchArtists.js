function getArtists(ArtistString, callback){
	var searchString = ArtistString.split(" ").join("%20");
	$.ajax({
		url: "https://api.spotify.com/v1/search?q="+searchString+"&type=artist",
		dataType: "json",
		error: function(response) {
			console.log(response)
		},
		success: function(response) {
			callback(response.artists, ArtistString)	 
		}
	})
}

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

function printRelated(response){
	for(i = 0; i < response.artists.length; i++){
		document.write('<h2>\t'+response.artists[i].name+"\n</h2>")
	}	
}
