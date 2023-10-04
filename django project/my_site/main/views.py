from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from pytube import YouTube
import logging


logger = logging.getLogger(__name__)


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})

def home(request):
    message = None

    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        if video_url:
            try:
                yt = YouTube(video_url)
                video = yt.streams.get_highest_resolution()
                video.download()
                logger.info(f"Video downloaded: {video_url}")
                message = "Video download completed successfully."
            except Exception as e:
                logger.error(f"Error downloading video: {str(e)}")
                message = f"Error: {str(e)}"
        else:
            message = "Please provide a valid YouTube video URL."

    return render(request, "main/home.html", {"message": message})