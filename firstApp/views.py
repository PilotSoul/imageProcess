import os

from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage

import json

def index(request):
    context = {'a': 1}
    return render(request, 'index.html', context)

#для запросов
def predictImage(request):
    if request.method == 'POST':
        fileObj = request.FILES['filePath']
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name, fileObj)
        url = fs.url(filePathName)
        image_file = "C:/Users/Admin/Desktop/GitP/imageProcess" + url
        file_exists = os.path.isfile(image_file)
        if file_exists:
            forGreyscale = Image.open(image_file )
            name_ch_file = image_file[:-4] + "_greyscale" + image_file[-4:]
            ch_file = forGreyscale.convert(mode='L')
            ch_file = ch_file.rotate(90).save(name_ch_file)
            ch_file_exists = os.path.isfile(name_ch_file)
            if ch_file_exists:
                displayFileMod = url[:-4] + "_greyscale" + url[-4:]
                return render(request, 'index.html', {
                    'status': 'ok',
                    'image_processed': 'successfully',
                    'displayFileMod': displayFileMod,

                })
            else:
                return render(request, 'index.html', {
                    'status': 'not ok',
                    'image_processed': 'unsuccessfully',
                })





