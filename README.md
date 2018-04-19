##### Author: Kirubel Tadesse

# This project is for Networking Class

This repository uses nodejs to collect different information about a given website.

### Collected web address
- the web addressed that are being tested are listed on the folder `Servers` which include a list of University and the top web pages address from Alexa. 

### Testing Script
- `webtest_analysis.js` is a nodejs program that test each web address using the [webpagetest](https://webpagetest.org) and periodically check when the result is avaliable. This program uses *my private API* for testing the web addresses. The API address allows me to make 200 test per day!

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

- Since the test result for a single website return a huge amount of information (=~ 3MB of text data) in the next function I select the neccessory parameters out of the result and save the result to a file. 

- **Load Time:** The time between the initial request and the browser load event
- **First Byte:** The time it takes for the server to respond with the first byte of the response (in other words, the time it takes for the back-end to load)
- **Start Render:** The time until the browser starts painting content to the screen
- **Speed Index:** A custom metric introduced by WebPageTest to rate pages based on how quickly pages are visually populated (see [here](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index) for full details on the metric)
- **DOM Elements:** Number of DOM elements in the page
- **Document Complete:** Set of metrics relative to the time until the browser load event, with Time, Requests and Bytes In representing the load time, number of requests and number of bytes received, respectively
- **Fully Loaded:** Similar to Document Complete, but the metrics are relative to the time at which WebPageTest determines that the page has fully finished loading content. This is relevant and different from the above, because pages may decide to load additional content after the browser load event
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

### Data Collections 
- Runned different test at different time and the result seems to stay consistant
- Runned for the Iphone6s\_iOS11 from the same location 
```
		wpt.runTest(w_addes[i], {
			connectivity: '4G',                // 'cable' or '4G' (9 Mbps 170ms RTT) specifing connection
			location: 'Dulles:iOS',			  // 'Chrome' or IOS 	
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
		})
   }	
```
- unfortunity there were **35** test waiting online which mean my test was on pending stage for a vary long time.
- Runned the state from different location Milan, Italy and get a result.

- the python script `Analysis.py` include the Analysis of the result. Organize the data into 14 column and various row based on the data size.


### Analysis 
- What is the different relationship between the different matrics?
	- Proposed Methods
		- Spearman Partial Ranking Correlation Coefficiant 

### Some of the Challengings

1. Installing Nodejs with NPM
2. Writing the `webtest_analysis.js` 
	- Webpagetest AIP
		- understanding how to use it and the policies and limitation
	- passing the web address and waiting for the test result since the test result takes take my script was returning undefined result
	- parseing the result to different parameter that came used for evaluation
	- JavaScript is not that stright forward to write to a file sorting the result was a bit of a challenge
	
3. During Analysis preparing the data for pandas dataframe was kind of problem.


### Results 
- The test was performed several time both on the same list of servers. And the difference in those paramater in different time is the same. In other words, the difference is negligible.





