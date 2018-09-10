from django.shortcuts import render, HttpResponse
import os

# Create your views here.


def index(requests):
    return render(requests, 'Upload/index.html')


def submit(requests):
    if requests.method == 'POST':
        file = requests.FILES.get('file', None)
        if not file:
            return HttpResponse("No file for upload")
        path = open(os.path.join('.%susr%suploads' % (os.path.sep, os.path.sep), file.name), 'wb+')
        for chunk in file.chunks():
            path.write(chunk)
        path.close()
        return render(requests, 'Upload/success.html')