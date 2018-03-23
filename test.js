var WebPageTest = require('webpagetest')
var fs = require('fs');
const querystring = require('querystring');
var wpt = new WebPageTest('https://www.webpagetest.org/','A.57c0ecce925470118d73687951af28ee')

// reading from a file
var data = fs.readFileSync('univ_college.json')
var Unv_web = JSON.parse(data);

//to see what is being read
console.log(Unv_web);

/*
// Creating a customMetrics

var customMetrics = [
	'[iframes]',
	'return document.getElementsByTagName("iframe").length',
	'[ads],    							//looking for advertisment provider
	'return Array.prototype.slice.call(document.getElementsByTagName("a")).filter(function (node) { return node.getAttribute("href").indexOf("ad.doubleclick.net") !== -1 }).length'
	]
*/

/*
wpt.runTest('https://css-tricks.com',{
	connectivity: 'cable',                //specifing connection
	location: 'Dulles:Chrome',			  // location	
	firstViewOnly: false,
	runs: 1,
	pollResults: 5,
	video: true
}, function processTestResult(err, result){ 
	//console.log(err || result) //this will return the specific testId etc...
	console.log('Load time:', result.data.average.firstView.loadTime)
	console.log('First byte:', result.data.average.firstView.TTFB)
	console.log('Start render:', result.data.average.firstView.render)
	console.log('Speed Index:', result.data.average.firstView.SpeedIndex)
	console.log('DOM elements:', result.data.average.firstView.domElements)

	
	console.log('(Doc complete) Requests:', result.data.average.firstView.requestsDoc)
	console.log('(Doc complete) Byets in:', result.data.average.firstView.bytesInDoc)


	console.log('(Fully loaded) Time:', result.data.average.firstView.fullyLoaded)
	console.log('(Fully loaded) Requests:', result.data.average.firstView.requestsFull)
	console.log('(Fully loaded) Bytes in:', result.data.average.firstView.bytesIn)

	console.log('Waterfall view:', result.data.runs[1].firstView.images.waterfall)

	var q_data = querystring.stringify({
	'Load time:': result.data.average.firstView.loadTime,
	'First byte:': result.data.average.firstView.TTFB,
	'Start render:': result.data.average.firstView.render,
	'Speed Index:': result.data.average.firstView.SpeedIndex,
	'DOM elements:': result.data.average.firstView.domElements,
	'(Doc complete) Requests:': result.data.average.firstView.requestsDoc,
	'(Doc complete) Byets in:': result.data.average.firstView.bytesInDoc,
	'(Fully loaded) Time:': result.data.average.firstView.fullyLoaded,
	'(Fully loaded) Requests:': result.data.average.firstView.requestsFull,
	'(Fully loaded) Bytes in:': result.data.average.firstView.bytesIn,
	},';', ':');


	// custome Metrics values
	//console.log('Iframes:', result.data.average.firstView.iframes)
	//console.log('Ads:', result.data.average.firstView.ad)
/*	bfinal = Buffer.concat([b1, b2, b3,b4,b5,b6,b7,b8,b9,b10]);
	var json = bfinal.toJSON(bfinal);
	console.log("The Buffer: ", bfinal)
	console.log("The Json: ", json)
*/
	//var data = JSON.stringify(q_data, null, 2)
/*
	fs.writeFile('words2.json', q_data, response);

	function response(err){
		console.log('saving response');
	}

})

wpt.getTestStatus('180317_YS_ccecf2bcdde379e930fd2b0f3c6d625d'
, function processTestStatus(err, result){
	console.log(err || result)

	var data = JSON.stringify(result, null, 2)
	fs.writeFile('words.json', data, finished);

	function finished(err){
		console.log('File save');
	}
})
*/
/*****************************************
Try to figure out how to feed multiple 
web addresses to the script at once from a 
text file instade of manually writing to the script
and also the result to the json file with out deleting what already exists
*****************************************/

