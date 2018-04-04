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

- Since the test result for a single website return a huge amount of information in the next function we select the neccessory parameters out of the result and save the ressult to a file. 
- when the result are ready the program will write(append) it to a file called `test_result.txt`. 

### Result Analysis 
- the python script `Analysis.py` include the Analysis create currently under progress








