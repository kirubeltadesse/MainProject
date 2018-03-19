//var WebPageTest = require('webpagetest')
//var wpt = new WebPageTest('https://www.webpagetest.org/','A.57c0ecce925470118d73687951af28ee')
//
///*
//// Creating a customMetrics
//
//var customMetrics = [
//	'[iframes]',
//	'return document.getElementsByTagName("iframe").length',
//	'[ads],    							//looking for advertisment provider
//	'return Array.prototype.slice.call(document.getElementsByTagName("a")).filter(function (node) { return node.getAttribute("href").indexOf("ad.doubleclick.net") !== -1 }).length'
//	]
//*/
//
//
//wpt.runTest('https://css-tricks.com',{
//	connectivity: 'cable',                //specifing connection
//	location: 'Dulles:Chrome',			  // location	
//	firstViewOnly: false,
//	runs: 1,
//	pollResults: 5,
//	video: true
//}, function processTestResult(err, result){ 
//	//console.log(err || result) //this will return the specific testId etc...
//	console.log('Load time:', result.data.average.firstView.loadTime)
//	console.log('First byte:', result.data.average.firstView.TTFB)
//	console.log('Start render:', result.data.average.firstView.render)
//	console.log('Speed Index:', result.data.average.firstView.SpeedIndex)
//	console.log('DOM elements:', result.data.average.firstView.domElements)
//
//	
//	console.log('(Doc complete) Requests:', result.data.average.firstView.requestsDoc)
//	console.log('(Doc complete) Byets in:', result.data.average.firstView.bytesInDoc)
//
//
//	console.log('(Fully loaded) Time:', result.data.average.firstView.fullyLoaded)
//	console.log('(Fully loaded) Requests:', result.data.average.firstView.requestsFull)
//	console.log('(Fully loaded) Bytes in:', result.data.average.firstView.bytesIn)
//
//	console.log('Waterfall view:', result.data.runs[1].firstView.images.waterfall)
//
//	// custome Metrics values
//	//console.log('Iframes:', result.data.average.firstView.iframes)
//	//console.log('Ads:', result.data.average.firstView.ad)
//})
//
//wpt.getTestStatus('180317_YS_ccecf2bcdde379e930fd2b0f3c6d625d'
//, function processTestStatus(err, result){
//	console.log(err || result)
//})
//
/*****************************************
Instade of printing out to the console 
we need to save the json,csv, or xml file 
in order to do analysis and visualization.
*****************************************/
const fs = require('fs');

fs.open('file.txt', 'w', (err, fd) => {
	if (err) throw err;
	fs.close(fd, (err) => {
		if (err) throw err;
	});
	});
var stream = fs.createWriteStream("my_file.txt");
stream.once('open', function(fd){
	stream.write("my first row\n");
	stream.write("my second row\n");
	stream.end();
});

