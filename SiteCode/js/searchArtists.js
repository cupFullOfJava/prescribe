function getArtists(ArtistString, callback){
	var searchString = ArtistString.split(" ").join("%20");
	$.ajax({
		url: "https://api.spotify.com/v1/search?q="+searchString+"&type=artist",
		dataType: "json",
		success: function(response) {
			callback(response.artists)	 
		}
	})
}

function printArtists(Artists){
	console.log(JSON.stringify(Artists))
	artistinfo = JSON.parse(JSON.stringify(Artists.items[0]))
	console.log(Object.keys(Artists))
	console.log(JSON.stringify(artistinfo))
	console.log(Object.keys(artistinfo))

}
