# from fastapi import FastAPI, Form
# from fastapi.middleware.cors import CORSMiddleware
# import yt_dlp
# import os

# app = FastAPI()

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins, or you can specify specific origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

# cur_dir = os.getcwd()

# @app.post("/download")
# def download_video(link: str = Form(...)):
#   # Using Form to receive form data
#     youtube_dl_options = {
#         "format": "best",  # Selects the best quality video available
#         "outtmpl": os.path.join(cur_dir, f"Video-{link[-11:]}.mp4")  # Saves the video as ABCsample.mp4
#     }
#     with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
#         ydl.download([link])
#     return{"status":"Download started"}



from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp
import os

app = FastAPI()

# Configure CORS to allow the frontend's origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Replace with your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

cur_dir = os.getcwd()

@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, f"Video-{link[-11:]}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download started"}
