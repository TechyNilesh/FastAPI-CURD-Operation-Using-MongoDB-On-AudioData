from pymongo import MongoClient,errors
from .config import *


def mongodb_connect(mongodb_uri,port):
    try:
        c =  MongoClient(mongodb_uri,port)
        print("successfully to connected to server {}".format(mongodb_uri))
        return c
    except errors.ConnectionFailure:
         print("Failed to connect to server {}".format(mongodb_uri))

client = mongodb_connect(mongodb_uri, port)
#print(client.list_database_names())
db = client['audiodata']

# defining collection
audio_collection = db['data']

## database CURD Operation Started ##

# Retrieve all audio present in the database
async def retrieve_all_audios(audioFileType:str):
    students = []
    for student in audio_collection.find({'audioFileType':audioFileType},{'_id': 0}):
        #print(student)
        students.append(student)
    return students

# Retrieve a audio with a matching ID
async def retrieve_audio(id,audioFileType) -> dict:
    audio = audio_collection.find_one({'audioFileType':audioFileType,"uniq_id": id},{'_id': 0})
    return audio

# Add a new audio into to the database
async def add_audio(audio_data: dict) -> dict:
    audio = audio_collection.insert_one(audio_data)
    new_audio = audio_collection.find_one({"_id": audio.inserted_id},{'_id': 0})
    return new_audio

# Delete a audio from the database
async def delete_audio(id,audioFileType):
    audio = audio_collection.find_one({'audioFileType':audioFileType,"uniq_id": id},{'_id': 0})
    if audio:
        audio_collection.remove({"uniq_id": id})
        return True

# Update a audio with a matching ID and AudioType
async def update_audio(id: int,audioFileType:str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    audio = audio_collection.find_one({'audioFileType':audioFileType,"uniq_id": id},{'_id': 0})
    if audio:
        updated_audio = audio_collection.update(
            {'audioFileType':audioFileType,"uniq_id": id}, {"$set": data}
        )
        if updated_audio:
            return True
        return False