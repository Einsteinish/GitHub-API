# GitHub-API : commit activity stats with Python
REST API v3 with Python's requests
requests.get('https://api.github.com/repos/%s/stats/commit_activity' % repo)
where repo = 'kubernetes/kubernetes' for example.


## Prerequisites

Python 3.7.0

Python's "requests" module : use "pip install requests"


## Optional - virtualenv

$ virtualenv venv

$ source venv/bin/activate

$ pip install -r requirements



## Inputs

The following inputs are all optional.

repo = 'kubernetes/kubernetes' (username/repo)

week = 48 (how many past weeks, default=52)

sort = dsc or asc (default: asc)


## Testing and Caching

We can test the API with "curl":

$ curl -i https://api.github.com/repos/kubernetes/kubernetes/stats/commit_activity


We may want to wait for 1-2 minutes before we run our Python code.

"Computing repository statistics is an expensive operation, so we try to return cached data whenever possible. If the data hasn't been cached when you query a repository's statistics, you'll receive a 202 response; a background job is also fired to start compiling these statistics. Give the job a few moments to complete, and then submit the request again. If the job has completed, that request will receive a 200 response with the statistics in the response body"



# Sample 

## Output 1

(venv) $ python ask_ki.py -w=22 -s=asc -r=kubernetes/kubernetes

Inputs: repo=kubernetes/kubernetes weeks=22 sort=asc

--- Commits (average) ---

Sunday 4.0

Saturday 4.8

Monday 20.5

Tuesday 23.1

Wednesday 23.3

Friday 23.9

Thursday 25.9


--- The most commits ---

Thursday 25.9



## Output 2


(venv) $ python ask_ki.py -w=48 -s=asc -r=kubernetes/kubernetes

Inputs: repo=kubernetes/kubernetes weeks=48 sort=asc


--- Commits (average) ---

Sunday 4.8

Saturday 6.1

Monday 24.8

Friday 25.7

Tuesday 26.9

Wednesday 28.9

Thursday 29.2


--- The most commits ---

Thursday 29.2



## Output 3

(venv) $ python ask_ki.py -w=52 -s=dsc

Inputs: repo=kubernetes/kubernetes weeks=52 sort=dsc


--- Commits (average) ---

Wednesday 29.2

Thursday 28.4

Tuesday 27.1

Friday 25.3

Monday 25.3

Saturday 6.2

Sunday 5.3


--- The most commits ---

Wednesday 29.2



## Output 4

(venv) $ python ask_ki.py -s=asc

Inputs: repo=kubernetes/kubernetes weeks=52 sort=asc


--- Commits (average) ---

Sunday 5.3

Saturday 6.2

Monday 25.3

Friday 25.3

Tuesday 27.1

Thursday 28.4

Wednesday 29.2


--- The most commits ---

Wednesday 29.2



## Output 5

(venv) $ python ask_ki2.py

Inputs: repo=kubernetes/kubernetes weeks=52 sort=dsc


--- Commits (average) ---

Wednesday 29.2

Thursday 28.4

Tuesday 27.1

Friday 25.3

Monday 25.3

Saturday 6.2

Sunday 5.3


--- The most commits ---

Wednesday 29.2

(venv) $ 


## Refs
[GitHub developer - REST API v3](https://developer.github.com/v3/)
