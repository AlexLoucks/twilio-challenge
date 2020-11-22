# Twilio challenge write-up

Overview: This server/client has been created with the assumption that this is only an initial step in creating  a much comprehensive product, and it's thus structured to allow for easy addition of new functionality. 
### Github Repo Stars API Server Requirements

| Server Requirements | Implementation Description            | Expected result of actions |
|---------------------|---------------------------------------|----------------------------|
| Dockerized          | The tester can automatically generate a Docker image, and run a container containing the server via make. <br />To do this, go into the server folder: <br /> ```cd twilio-challenge/server```<br />  And run the following commands: <br /> ```make build``` <br /> ```make run``` <br /> This should bring up a container on which the server is running. | The following output is expected: <pre>Serving Flask app "src.app"  <br />  Environment: dev<br />  Debug mode: on <br/>  Running on http://0.0.0.0:5000/  <br />  Restarting with stat <br />  Debugger is active! <br />  Debugger PIN: 203-528-956 </pre> For a complete list of possible <br /> actions, run the following command:  <br /> ```make help```|
|README| A detailed README.md file has been added to the server subfolder explaining how to bring it up. || 
|Error Handling | Several types of errors have been taking into consideration at server level. <br /> 1. Input  validation errors covered by using [marshmellow schema validation](https://marshmallow.readthedocs.io/en/stable/)<br />2. Github API errors which are returned in the response. | 1. Input validation error example: ```{'Error calling the stars API for the given repo list, status': 400, 'body': {'Input Error': {'repositoryList': ['The repo named AlexLoucks/ does not match the expected pattern ogranziation/repository from chars [A-Za-z0-9_.-]']}}}``` <br /><br />2.Github API error example: ```{ "Internal Server Error": "Error calling the github API for repo: AlexLoucks/test-repo, Github call status: 404, body: {'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#get-a-repository'}"}```|
|Tests| Detailed test instructions have been included in the server and client README.mds||
|Calls GitHub| For the purpose of this excersise, it has been assumed that the API will only be used for querying metadata about public repositories, passed as a List of the form ["organiztion/repository"]| A successfull call will return a map containing the number of stars for each repo, as well as the total number of stars for the repos in the list, similar to: ``` {"starsCount": { "AlexLoucks/test-repo-1": 0, "AlexLoucks/test-repo-2": 1}"totalStars": 1 } ```|

### Github Repo Stars API Client Requirements
| Server Requirements | Implementation Description            | 
|---------------------|---------------------------------------|
|Runnable             | Two different way of running the client have been provided: <br /> 1. For Python users, the client can be installed as a Python library and included in their Python application (see Jupyter Notebook as a demo). <br />2. As an executable file, from terminal.  |
|README| A detailed README.md file has been added to the client subfolder explaining how to use it. |
|Input Validation| The client is a light-weight package which performs minimal input validation - testing for not null input. For the purpose of this excercise, the API server does the heavy-lifting in terms of validating the input, and the client just forwards the result from the API to the user. This decision has been made keeping our clients in mind, which can decide to use our API by either calling it directly, or via our client. Both user-types should benefit from the same rigourous input validation. |
|Calls Server| Self-explanatory - the client makes http calls to the server. (The server location/port can be set in the config file, or passed to the client at initialization time. default: ```0.0.0.0/5000```)|
|Error Handling| The client validates the server's response and forwards the error to the user for appropriate action.|
|Tests| See README.md for detailed testing instructions |



