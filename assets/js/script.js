var markedForOpen = null;
var doOpen = null;

function markForOpen(abbrv) {
	var temp = document.getElementById(abbrv);
	if(temp == markedForOpen) {
		doOpen = false;
	}
	else {
		markedForOpen = temp;
		doOpen = true;
	}
}

function openMarked() {
	var elts = document.getElementsByTagName("div");
	for (var i=0; i< elts.length; i++) {
		if(elts[i].className == "collapsible") elts[i].style.display = "none";
	}
	if(doOpen) {
		markedForOpen.style.display = "block";
		doOpen = false;
	} else {markedForOpen = false;}
}
