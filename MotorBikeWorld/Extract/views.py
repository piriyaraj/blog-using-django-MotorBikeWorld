import os
from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from .modules import extracter,setmodels
from django.contrib.auth.models import User
# Create your views here.
from django.core.files.uploadedfile import UploadedFile

# fd = open("tempImg/2022 AJS Tempest Roadster 125 bikespeci.webp", 'rb')
# newBikeImage = models.Bikeimage()
# newBikeImage.image = UploadedFile(fd)
# newBikeImage.alt = "image of  its show front, back, side view and show bike specifications"
# newBikeImage.save()
url = "https://bikez.com/motorcycles/access_shade_xtreme_650_2022.php"


def test(request):
    title, key, value, images, contant = extracter.getdata(url)
    # create table object
    newBikeTable = models.Biketable()
    newBikeTable = setmodels.table(newBikeTable, key, value)
    newBikeTable.save()

    # create image object
    fd = open(images, 'rb')
    newBikeImage=models.Bikeimage()
    newBikeImage.image = UploadedFile(fd)
    newBikeImage.alt = "image of "+title.split(" |")[0]+" its show front, back, side view and show bike specifications"
    newBikeImage.save()

    # create post
    user = User.objects.get(id=1)
    newBikePost=models.Bikepost()
    newBikePost.title = title
    newBikePost.slug = title.split(" |")[0].replace(" ","_")
    newBikePost.content = contant
    newBikePost.status = 1
    newBikePost.image = newBikeImage
    newBikePost.table = newBikeTable
    newBikePost.author = user

    newBikePost.save()

    msg="how are you"
    return HttpResponse(msg, content_type='text/plain')
    pass