from fastapi import FastAPI,Request
from .connection import *
from .model import *

# Defining Fastapi Class
app = FastAPI()


# Our root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}

# Create endpoint with the POST method
@app.post("/create/")
async def create(request:Request):
    try:
        data = await request.json()
        if data['audioFileType'] == 'song':
            song_data =  dict(create_song(data['audioFileMetadata']['name'],data['audioFileMetadata']['duration']))
            new_song = await add_audio(song_data)
            return ResponseModel(new_song, "Song Data added successfully.")
        elif data['audioFileType'] == 'podcast':
            podcast_data  = create_podcast(data['audioFileMetadata']['name'],data['audioFileMetadata']['duration'],data['audioFileMetadata']['host'],data['audioFileMetadata']['participants'])
            new_podcast = await add_audio(podcast_data)
            return ResponseModel(new_podcast, "Podcast data added successfully.")
        elif data['audioFileType'] == 'audiobook':
            audiobook_data =  create_audiobook(data['audioFileMetadata']['title'], data['audioFileMetadata']['author'],data['audioFileMetadata']['narrator'], data['audioFileMetadata']['duration'])
            new_audiobook = await add_audio(audiobook_data)
            return ResponseModel(new_audiobook, "Audiobook data added successfully.")
    except KeyError:
        return ErrorResponseModel("An error occurred.",500,"Please check the Format of the input data!")

# get all endpoint by type with the GET method
@app.get("/get/{audioFileType}/")
async def read(audioFileType:str):
    audio_data = await retrieve_all_audios(str(audioFileType))
    if audio_data:
        return ResponseModel(audio_data, "Audio data retrieved successfully")
    return ResponseModel(audio_data, f"Empty list returned! Please check your audioFileType [{audioFileType}] is orrect?")

# get endpoint by type and id with the GET method
@app.get("/get/{audioFileType}/{audioFileID}/")
async def read(audioFileType:str,audioFileID:int):
    audio_data = await retrieve_audio(int(audioFileID),str(audioFileType))
    if audio_data:
        return ResponseModel(audio_data, "Audio data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, f"Audio file doesn't exist. Please check your audioFileID [{audioFileID}] is orrect?")

# Delete by ID endpoint with the delete method
@app.delete("/delete/{audioFileType}/{audioFileID}/", response_description="audio data deleted from the database")
async def delete_audio_data(audioFileType:str,audioFileID: str):
    deleted_audio = await delete_audio(int(audioFileID),str(audioFileType))
    if deleted_audio:
        return ResponseModel(
            "Audio with ID: {} removed".format(audioFileID), "Audio deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Audio with id {0} doesn't exist".format(audioFileID)
    )

# using PUT to update audio data
@app.put("/update/{audioFileType}/{audioFileID}/")
async def update_audio_data(audioFileType:str,audioFileID:int,request:Request):
    try:
        data  = await request.json()
        print(data)
        updated_audio = await update_audio(int(audioFileID),str(audioFileType),dict(data))
        if updated_audio:
            return ResponseModel(
                "Audio with ID: {} update is successful".format(audioFileID),
                "Audio updated successfully",
            )
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the Audio data.",
        )
    except KeyError:
        return ErrorResponseModel("An error occurred.",500,"Please check the Format of the input data for update!")