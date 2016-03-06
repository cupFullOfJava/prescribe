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
	console.log(Artists.name)

}
