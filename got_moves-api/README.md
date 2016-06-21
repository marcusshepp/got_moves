A playground for all things cardistry.


## Step 1:
### classic moves API
```
A searchable database of moves. User searches for perticular move with typeahead.
Then the search endpoint returns performances of that move.
Default ordering is by upvotes but the API allows for the user to construct their own filter.
Top performance should be considerably more "popping" than the other performances.
```

    - moves should be seperate from videos/performances
    - you can claim a `best performance` by posting your vid to a move
    - moves have many categories
    - categories are split into OH/TH
    - moves have many videos   
    - moves have credits to cardists/creators
    - moves have `best of` day/week/month/year/all time
    - videos are ranked by upvotes
    - videos can also be down voted -- downvoting takes away exp from cardist who down voted
    - videos can be flagged for `incorrect preformance`, `inappropriate content`, `not properly categorized`
    - videos can be uploaded from instagram && YouTube
    - videos can be commented on
    - comments can be commented on
    


- technical notes
	- API
		- django rest framework
	- frontend
		- angular
		- SASS, Grunt, Bower


- list of top level features:
	- Cardist Profile
		- blog-like posts
		- ranks
		- privileges
			- each privilege gives more capability on the site
	- Feed
	- Classic Moves
	- Community Wiki ?? 


- possible names for site:
	- got moves?


- Ideas for how to rank up:
	- number of comments
	- number of comment upvotes
	- number of comments on users videos
	- consecutive days that user has visited the site
	- downvotes?
 	- number / types of privileges


- cardistry battles
	- timed
	- specific moves


- possible rankings
    Admiral - (Theoretical - non-canon.)
    Vice Admiral - (Theoretical - non-canon.)
    Rear Admiral - (Only Flag Rank that appears in series canon.)
    Commander - Equivalent to a Commodore, Commanding Officer of a Battlestar Group.
    Colonel
    Lieutenant Colonel (Jack Fisk "Razor")
    Major
    Captain
    Lieutenant
    Lieutenant Junior Grade
    Ensign
    -------
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Diamond",
    "Master",
    "Challenger",
    "Virt",
    "Pioneer",
