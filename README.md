Spellchecker
===
A client has asked us to write a custom API to help them determine if a word is spelled according to their corporate standards. If not, the API should return some suggestions.

### Project Setup
#### Dependencies
1. Python 3. Any version of Python 3 should work.
2. Docker/Docker-compose. If you do not have docker installed, follow instructions in Non-dockerized: Setting up the server.

#### Docker: Setting up the server
1. Make sure have docker/docker-compose installed and running otherwise follow non-dockerized setup.
2. From your terminal go to main project directory i.e. the Spellchecker project directory that contains the `docker-compose.yml` file.
3. Type `docker-compose up --build` to start the server. You will see docker building device registry and starting the Flask server.
4. Go to your browser and copy-paste `http://localhost:31337`. If you see a welcome message then you've successfully setup the server and ready to start using the API.

#### Non-dockerized: Setting up the server
1. Create a virtual environment using below command.
    ```shell script
    $ python3 -m venv venv
    ```
2. Activate your virtual environment.
    ```shell script
    $ source/venv/bin/active
    ```
3. If you are on Windows or need more help with virtual environments follow this [link.](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)
4. From your terminal go to main project directory i.e. the Spellchecker project directory that contains the `docker-compose.yml` file.
5. Then go the `spellchecker` directory that contains `requirements.txt`.
6. Install all the requirements using below command and make sure your virtual environment is active.
    ```shell script
    $ pip install requirements.txt
    ```
7. Start the Flask server using below command. You should see
    ```shell script
    $ python3 api.py
    ```
8. Go to your browser and copy-paste `http://localhost:31337`. If you see a welcome message then you've successfully setup the server and ready to start using the API.

### API Usage
As mentioned in the client requirements the endpoint:
- Is `/spellcheck/{word}`
- Runs on port `31337`.
- Returns `404` if the word is not found
- Returns `200` if the word is found
    - The body of the response includes acceptable spelling suggestions if the word is misspelled.

Below are some examples of implementation, go to your browser and copy-paste below `URL` to give it a try or perform `GET` calls using Postman or any programming language. 
   ```
    URL: http://localhost:31337/spellcheck/car
    
    Response Code: 200
    Response Body:
    {"suggestions": [], "correct": true}
   ```
    
   ```
    URL: http://localhost:31337/spell/caR
    
    Response Code: 200
    Response Body:
    {
        "suggestions": [
            "car",
            "carabao",
            "carabaos",
            "carabineer",
            ...
        ],
        "correct": false
    }
   ```
    
   ```
    URL: http://localhost:31337/spell/karaoke
    Response Code: 404
    Response Body:
    {"message": "Word: karaoke not found."}
   ```

#### Test cases
To run the test cases go to `Spellchecker/spellchecker` in a different terminal window and type below command. Make sure your Flask server is running.
   ```
    $ python3 tests.py 
   ```
If you get `requests` module import error make sure you install it using below command.
   ```
    $ pip3 install requests==2.25.0
   ```

### Client requirements
#### Data
Client has provided a dictionary of acceptable words in `dictionary.txt` contained in this archive at `Spellchecker/spellchecker/dictionary.txt`.

#### Details on word conformity
The client has specified that word does not conform if it:
- It has repeating characters (i.e. balllooooon)
- It is missing one or more vowels (i.e. balln)
- It has mixed-casing (i.e. BAllOOn)
    - Note: “Hello” and “HELLO” are correct and should not be considered mixed-casing.
- It has a combination of a, b and c type errors (i.e. bllllLLlln)

#### Project structure
- `Spellchecker/spellchecker/models.py` file contains the code for checking word conformity and provides suggestions using Prefix Trie data structure.
- `Spellchecker/spellchecker/validators.py` handles API validation or any user errors.
- `Spellchecker/spellchecker/api.py` is the main entry point where API endpoints are defined and server can be started. 
 
### Contact
- Jubin Soni
- jubinsoni27@gmail.com