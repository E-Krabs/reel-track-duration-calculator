function calculate(){
	var lenTape = document.getElementById("lenTapeInput").value;
	var lenUnit = document.getElementById("lenUnitSelect").value;
	var ips = document.getElementById("ipsSelect").value;
	console.log(lenTape + ", " + lenUnit + ", " + ips);

	// convert units to inches
	var lenTapeIn;
	if(lenUnit == "ft"){
		lenTapeIn = lenTape * 12
	}
	else if(lenUnit == "m"){
		lenTapeIn = lenTape / 0.0254
	}
	else{
		lenTapeIn = lenTape;
	}

	// calculate time available
	var timeAvailable = lenTapeIn / ips
	var results = trnc2(timeAvailable) + 'sec, ' + trnc2(timeAvailable/60) + 'min, ' + trnc2(lenTapeIn) + 'in'
	console.log(results)
	document.getElementById("console").innerHTML = results;

	// retrieve file information
	var file = document.getElementById('m3u8Input').files[0];
	var reader = new FileReader();
	reader.onload = (event) => {
		var file = event.target.result;
		var tracks = file.split(/\r\n|\n/).slice(0, -1);
		console.log(tracks);

		var trackLenTotal = 0;
		var trackMax = 0;
		for(var i=0; i<tracks.length; i++){
			trackLenTotal += Number(tracks[i]);
			if(trackLenTotal > timeAvailable){
				trackLenTotal -= tracks[i];
				break
			};
			trackMax += 1;
		};

		var results = trackMax + "/" + tracks.length +", " + trnc2(trackLenTotal/60) + "min, " + trnc2((timeAvailable-trackLenTotal)/60) + "remaining";
		document.getElementById("return").innerHTML = results;
		console.log(results)
	};
	reader.onerror = (event) => {
		alert(event.target.error.name);
	};
	reader.readAsText(file);
}

function trnc2(num) {
    var truncated2 = num.toString().match(/^-?\d+(?:\.\d{0,2})?/)[0]
    return truncated2
}