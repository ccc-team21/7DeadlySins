/*
Team 21 Deadly Sin Analysis
City: Melbourne
Team Members:
    Anupa Alex – 1016435
    Luiz Fernando Franco - 1019613
    Suraj Kumar Thakur - 999886
    Waneya Iqbal - 919750
    Yan Li – 984120
*/
//Map function to find count of all word counts posts in a suburb
function (doc) {
	//Only tweets that have coordinates 0 are considered
	if(doc.coordinates!=null){
	  doc.text.toLowerCase().split(" ").forEach(function (word) {	    
	       emit(doc.suburb_id, lust);
	  });
	 
	}
}