# cudos-maej-ai
A discord bot for assisting with information about CUDOS.


## Built With

- Langchain
- Discord.py

## Models
- Ollama
- all-minilm


## Getting Started

- **To get a local copy of the repository please run the following commands on your terminal:**
  Clone the project
  ```
  git clone https://github.com/mmsesay/cudos-maej-ai.git
  ```
  Navigate into the directory
  ```
  cd cudos-maej-ai
  ```
  Create a virtual environment if you don't have one.
  ```
  python3 -m venv venv
  ``` 
  Activate the virtual environment
  ```
  source venv/bin/activate
  ```
  Install the project dependencies
  ```
  pip install -r requirements.txt
  ```
  
## Required .env file:
It is required to provide a .env file at the root of the project with the keys below and their values. 
This .env file should contain following required keys:
```
DISCORD_BOT_TOKEN=
```
```
CLIENT_ID=
```    

## Run the app:
 Run the project
 ```
 python3 app.py
 ```
