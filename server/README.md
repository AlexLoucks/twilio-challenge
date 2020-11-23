# Github Repo Stars API Server

### Running instructions:
* It is assumed that the machine running this has docker and make installed. If not, follow the instalation instructions [here](https://docs.docker.com/get-docker/), and run `brew install make` to install make in order to make use of the Makefile. <br/>

1. Clone this repo:
    ```git clone https://github.com/AlexLoucks/twilio-challenge.git```

2. Navigate to the server subfolder:
    ```
    cd twilio-challenge/server
    ```

3. See build and run options:
    ```
    make help
    ```
4. **Simple build/run:**
    ```
    make build
    make run
    ```
The following response signifies that your server is up and running:
* Serving Flask app "src.app" (lazy loading)
* Environment: dev
* Debug mode: on
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 203-528-956

4. **TESTING**
Bring a container up as described above.
Start firing requests at it. For the purpose of this excercise, I have created a few empty testing repos. Feel free to use them in your tests, or test them on different ones. However, it has been assumed that this API is intended for use on public repos, so it doesn't include authentication options. 

* **Tesing happy-path scenario:**
    ```
    curl -X POST 0.0.0.0:5000/stars/count -H "Accept: application.json" -H "Content-Type: application/json" -d '{"repositoryList":["AlexLoucks/test-repo-1", "AlexLoucks/test-repo-2"]}'
    ```

    Expected result:
    ```json
    {
    "starsCount": {
        "AlexLoucks/test-repo-1": 0, 
        "AlexLoucks/test-repo-2": 1
    }, 
    "totalStars": 1
    }
 

* **Tesing invalid input - missing repo List:**
	```
    curl -X POST 0.0.0.0:5000/stars/count -H "Accept: application.json" -H "Content-Type: application/json" -d '{}'
    ```

	Expected result:
	```json
	{
	"Input Error": {
	    "repositoryList": [
	    "Missing data for required field."
	    ]
	}
	}

* **Tesing invalid input - empty repo List:**
    ```
    curl -X POST 0.0.0.0:5000/stars/count -H "Accept: application.json" -H "Content-Type: application/json" -d '{"repositoryList":[]}'
    ```
	
	Expected result:
	```json
	{
	"Input Error": {
	    "repositoryList": [
	    "Repository list must have at least one item"
	    ]
	}
	}

* **Tesing invalid input - malformed repo name in repo List:**
    ```
    curl -X POST 0.0.0.0:5000/stars/count -H "Accept: application.json" -H "Content-Type: application/json" -d '{"repositoryList":["AlexLoucks/", "AlexLoucks/test-repo-2"]}'
    ```
	
	Expected result:
	```json
	{
	"Input Error": {
	    "repositoryList": [
	    "The repo named AlexLoucks/ does not match the expected pattern ogranziation/repository from chars [A-Za-z0-9_.-]"
	    ]
	}
	}

* **Tesing invalid input - non-existent repo name in repo List:**
    ```
    curl -X POST 0.0.0.0:5000/stars/count -H "Accept: application.json" -H "Content-Type: application/json" -d '{"repositoryList":["AlexLoucks/test-repo-1", "AlexLoucks/test-repo-7"]}'
    ```
	
	Expected result:
	```json
	{
	"Internal Server Error": "Error calling the github API for repo: AlexLoucks/test-repo-7, Github call status: 404, body: {'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#get-a-repository'}"
	}

4. **UNIT TESTING**
From the server subfolder, run: 
```
make build-test 
make run-test
```
A summary of unit tests and coverage should be displayed. 
<br />

4. **INTEGRATION TESTS**
Unit tests cover a small part of integration testing by providing mock responses from the Github API. Further discussion is needed in implementing further integration tests. Ideas to be taken into consideration:
- the establishment of test repos - can be somewhat challenging given the ease of modifying them (ie adding a new star to a test repo will break the integration test)
- the dependency on the Github API, which can be updated by Github developers and thus break our application. 
