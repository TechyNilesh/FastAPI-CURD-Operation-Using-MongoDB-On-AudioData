# FastAPI CURD Operation Using MongoDB On AudioData
![PyMongo](https://img.shields.io/badge/PyMongo-3.10.1-green) ![FastAPI](https://img.shields.io/badge/FastAPI-0.63.0-blue) ![Schematics](https://img.shields.io/badge/Schematics-2.1.0-yellow) ![Uvicorn](https://img.shields.io/badge/Uvicorn_Server-0.13.4-red)

This is a  FastAPI based Web API that simulates the behavior of an audio file server while using a MongoDB database.

### Problem Statement

 [ Click Here Download Detailed Document of Problem Description](https://github.com/TechyNilesh/FastAPI-CURD-Operation-Using-MongoDB-On-AudioData-/blob/8aa0ce67b10048dd0a07721c82f425f9dea63fc3/documents/Python_Test.pdf "Detailed Document Problem Description")

### Colne the repository

- Clone the repo from github: `git clone https://github.com/TechyNilesh/FastAPI-CURD-Operation-Using-MongoDB-On-AudioData.git`

- In terminal go to folder: `cd FastAPI-CURD-Operation-Using-MongoDB-On-AudioData`

### Requirements
```
schematics==2.1.0
uvicorn==0.13.4
pymongo==3.10.1
fastapi==0.63.0
secrets==1.0.2
```
Run Following commond to install requirement on your machine:

`> pip install -r requirements.txt
`
### Running API Server
We are using Uvicorn for running FastAPI Server. 
> Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

For starting the server you need to run following commond in working directory:

`> python main.py`

### Accessing the API

Server are running on localhost `127.0.0.1` and port number `8000`, you can just type on your browser or Postman Tool:

`http://127.0.0.1:8000/`

We are using Postman Tool for testing the API, You can performe diffrent CURD operation using followings:

**Create:**  for creating a new file you need run `http://127.0.0.1:8000/create/`  with Method `POST` and `request-body` formate is following for each file:

**Note:**  You do not  need to  define `upload_time` and `id` field its autometiclly created by backend server. 
```
## song

 {
  "audioFileType":"song",
  "audioFileMetadata":{
      "name":"<song name>",
      "duration":<duration of the song in second>
      }
  }

## podcast

 {
  "audioFileType":"podcast",
  "audioFileMetadata":{
      "name":"<podcast name>",
      "host":"<podcast host name>",
      "participants": ["<name_1>","<name_2>"......"<name_10>"],
      "duration":<duration of the podcast in second>
      }
  }

## audiobook

 {
  "audioFileType":"audiobook",
  "audioFileMetadata":{
      "title":"<title of the audiobook>",
      "author":"<auther name of the audiobook>",
      "narrator":"<narrator name>",
      "duration":<duration of the audiobook in second>
      }
  }
```
**Update:** for updating a old file you need run `http://127.0.0.1:8000/update/<audioFileType>/<audioFileID>`  with Method `PUT` and `request-body` formate is same as create formate for each file.

**Read:** To reading the file in the database you have two option:
1. Read all data by audioFileType: for reading data by audioFileType you need to run `http://127.0.0.1:8000/get/<audioFileType>/`  with Method `GET`, It will return all audio data belonging to the particuler audio file type.
2. Read by audioFileID: for reading data by audioFileID you need to run `http://127.0.0.1:8000/get/<audioFileType>/<audioFileID>`  with Method `GET`, It will return single audio data belonging to the particuler audio id.

**Delete:** For deleting the file you need run `http://127.0.0.1:8000/delete/<audioFileType>/<audioFileID>`  with Method `DELETE`, It will delete the particular file.

This is a whole process of running the FastAPI Server with MongoDB Database, If you have any query, you can reach out me through My Linkedin: [@TechyNilesh](https://www.linkedin.com/in/techynilesh/ "@TechyNilesh")
