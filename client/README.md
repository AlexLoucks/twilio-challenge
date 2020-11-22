# Github Repo Stars API Server

### Running instructions:
* It is assumed that a docker container running the server is up and available. For now, the code will reach out to the container, assuming it runs at address 0.0.0.0:5000

### Options:
There are two ways to run this client.
1. **For Python users**
install the package as a library, and import it in your code. 
```
cd twilio-challenge/client
pip install -e .
```
Then, it can be used as seen in the demo file attached: Python_stars_library_testing.ipynb

2. **As an executable from commandline**
```
cd twilio-challenge/client
./pyinstaller_start <List of repositories>
```

Example:
```./pyinstaller_start AlexLoucks/test-repo-1 AlexLoucks/test-repo-2```

**Note:** currently, the Python library allows the user to specify its own host:port. The same functionalit can be estended to the executable, by generating a new one in which the port and host are passed first from commandline. 

### TESTING:
1. Run the commands in the Jupyter Notebook attached (Python_stars_library_testing.ipynb) for using the client in a Python app
2. Run it from the terminal and pass a list of repo names as args. 
