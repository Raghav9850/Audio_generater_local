# converter/views.py
import pyttsx3
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

@csrf_exempt
def convert_text_to_speech(request):
    if request.method == "POST":
        text = request.POST.get("text")
        audio_file_path = "static/converter/converted_audio.mp3"

        # Convert text to speech and save to static directory
        engine.save_to_file(text, audio_file_path)
        engine.runAndWait()

        # Use the relative URL for static files in the template
        audio_file_url = "/" + audio_file_path  # Prefix with "/" to create a valid URL
        return render(request, 'converter/index.html', {"audio_file": audio_file_url})

    return render(request, 'converter/index.html')

def download_audio(request):
    file_path = "static/converter/converted_audio.mp3"
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse("File not found", status=404)
