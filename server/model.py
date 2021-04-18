from schematics.models import Model
from schematics.types import StringType,IntType,DateTimeType,ListType
import secrets
from datetime import datetime

class song(Model):
    #user_id = IntType(required=True)
    name = StringType(required=True,max_length=100)
    duration = IntType(required=True)
    upload_time = DateTimeType(required=True)

class podcast(Model):
    #user_id = IntType(required=True)
    name = StringType(required=True,max_length=100)
    duration = IntType(required=True)
    upload_time = DateTimeType(required=True)
    host = StringType(required=True,max_length=100)
    participants = ListType(StringType,required=False, max_size=10)

class audiobook(Model):
    #user_id = IntType(required=True)
    title = StringType(required=True,max_length=100)
    author = StringType(required=True,max_length=100)
    narrator = StringType(required=True,max_length=100)
    duration = IntType(required=True)
    upload_time = DateTimeType(required=True)

# erro response body

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

# An instance of class 
new_song = song()
new_podcast = podcast()
new_audiobook = audiobook()

# funtion to create and assign values to the instanse of class created
def create_song(name:str, duration:int):
    uniq_id = int(secrets.token_hex(4),16)
    new_song.name = name
    new_song.duration = duration
    new_song.upload_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return {'uniq_id':uniq_id,'audioFileType':'song','audioFileMetadata':dict(new_song)}

def create_podcast(name:str, duration:int,host:str,participants:list):
    uniq_id = int(secrets.token_hex(4),16)
    new_podcast.name = name
    new_podcast.duration = duration
    new_podcast.upload_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    new_podcast.host = host
    new_podcast.participants = participants
    return {'uniq_id':uniq_id,'audioFileType':'podcast','audioFileMetadata': dict(new_podcast)}

def create_audiobook(title:str, author:str,narrator:str,duration:int):
    uniq_id = int(secrets.token_hex(4),16)
    new_audiobook.title = title
    new_audiobook.author = author
    new_audiobook.narrator = narrator
    new_audiobook.duration = duration
    new_audiobook.upload_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return {'uniq_id':uniq_id,'audioFileType':'audiobook','audioFileMetadata': dict(new_audiobook)}