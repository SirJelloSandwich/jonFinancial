#Using python package manager pip, install missing modules. Maybe pandas and requests


###I know that I will need to use a for loop, pulling out the following: "
###The response will also contain a CB-AFTER header which will return the cursor id to use in your next request for the page after this one.
###The page after is an older page and not one that happened after this one in chronological time."

###I also know that I'll need to use a += to append the older data to the candle variable.

###How do I:

###1) pull the cursor id out of the header each loop
###2) not exceed the API limit
###3)ensure that I am not missing any trade_id's in the sequence
###4) parse the json into a usable format (I want the data to reside inside a pandas dataframe, so the command would be candle = pd.DataFrame(candle)
###5) repeat this process with other currency pairs back to the date the ETH-USD file begins (only a few months ago)
###6) finally, every night at a fixed time, check the API for new data, and add that data to the existing files

###Purpose:
###research market micro structure in the crypto-currency exchange space to identify possible algorithmic trading opportunities using econometrics and statistical analysis.
