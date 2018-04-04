Kirubel Tadesse

This repository uses nodejs to collect different information about a given web site.

### Collected web address
- the web addressed that are being tested are lested on the `univ_college.csv` 

### Testing Script
- `webtest_analysis.js` is a nodejs program that test each web address using the [webpagetest](https://webpagetest.org) and periodically check when the result is avaliable. This program uses my private API for testing the web addresses.
- There are different specification we make for our testing avaliable resourse are listed [here](https://webpagetest.org/getLocations.php)

```
		wpt.runTest(w_addes[i], {
			connectivity: 'cable',                //specifing connection
			location: 'Dulles:Chrome',			  // location	
			firstViewOnly: false,
			runs: 1,
			pollResults: 5,
			video: true
		}, function processTeststatus(err, result) { 
			console.log(err || result)
	//		console.log('Data id: ', result.data.id)

			//collecting all the test_ids
			data_id.push(result.data.id)

			// check result status
			check_status();
			// console.log("inside",data_id)
		}
```

- Since the test result for a single website return a huge amount of information in the next function I select the neccessory parameters out of the result and save the ressult to a file. 

**Load Time:** The time between the initial request and the browser load event
**First Byte:** The time it takes for the server to respond with the first byte of the response (in other words, the time it takes for the back-end to load)
**Start Render:** The time until the browser starts painting content to the screen
**Speed Index:** A custom metric introduced by WebPageTest to rate pages based on how quickly pages are visually populated (see here for full details on the metric)
**DOM Elements:** Number of DOM elements in the page
**Document Complete:** Set of metrics relative to the time until the browser load event, with Time, Requests and Bytes In representing the load time, number of requests and number of bytes received, respectively
**Fully Loaded:** Similar to Document Complete, but the metrics are relative to the time at which WebPageTest determines that the page has fully finished loading content. This is relevant and different from the above, because pages may decide to load additional content after the browser load event
```
	var q_data = querystring.stringify({
			'web address:': result.data.url,
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
			'Waterfall view:': result.data.runs[1].firstView.images.waterfall,
			
			},';',':');
```
- when the result are ready the program will write(append) it to a file called `test_result.txt`or `data.csv` here. 

### Result Analysis 
- the python script `Analysis.py` include the Analysis of the result. Organize the data into 14 column and various row based on the data size.










