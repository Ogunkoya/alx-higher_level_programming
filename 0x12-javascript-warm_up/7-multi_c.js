#!/usr/bin/node

let printXt = parseInt(process.argv[2]);
if (isNaN(printXt) || process.argv[2] == undefined) {
	console.log('MIssing number of occurences');
} else {
	while (printXt > 0) {
		console.log('C is fun');
		printXt--;	
	}
}
