function getArtists(ArtistString, callback){
	var searchString = ArtistString.split(" ").join("%20");
	$.ajax({
		url: "https://api.spotify.com/v1/search?q="+searchString+"&type=artist",
		dataType: "json",
		error: function(response) {
			console.log(response)
		},
		success: function(response) {
			callback(response.artists)	 
		}
	})
}

function printArtists(Artists){
	artistinfo = JSON.parse(JSON.stringify(Artists.items))
	console.log(JSON.stringify(artistinfo[0]))
}
