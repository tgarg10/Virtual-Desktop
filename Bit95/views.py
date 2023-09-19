from django.http import HttpResponse
from django.shortcuts import render
from Bit95.models import Files, Deleted_Files

import requests


def home(request):
    if request.method == "POST":
        file_names = list(Files.objects.values_list('name'))
        deleted_file_names = list(Deleted_Files.objects.values_list('name'))

        ## saving Files ##
        if 'input_file_name' in request.POST and (request.POST['input_file_name']+'.txt',) not in file_names:
            new_file = Files()
            new_file.name = request.POST['input_file_name'] + '.txt'
            new_file.data = request.POST["file_data"]
            new_file.save()

        if 'hidden_image_name' in request.POST and (request.POST['hidden_image_name']+'.jpg',) not in file_names:
            new_file = Files()
            new_file.name = 'Date12.jpg' ## use this just to detect if image is to be saved then save it using requests module from nasa api
            new_file.data = request.POST['hidden_image_name']
            new_file.save()
        ## right click to delete file ##
        if 'hidden_file_name' in request.POST and (request.POST['hidden_file_name'],) not in deleted_file_names and request.POST['hidden_file_name'] != '':
            delete_file_name = request.POST['hidden_file_name']

            # removing record from File Model
            remove_file_deleted = Files.objects.get(name=delete_file_name)
            remove_file_deleted.delete()

            deleted_files = Deleted_Files()
            deleted_files.name = delete_file_name
            deleted_files.type = remove_file_deleted.type
            deleted_files.data = remove_file_deleted.data
            deleted_files.date_time_created = remove_file_deleted.date_time_created
            deleted_files.save()

        ## right click to restore file ##
        if 'hidden_file_name2' in request.POST and (request.POST['hidden_file_name2'],) not in file_names and request.POST['hidden_file_name2'] != '':
            restore_file_name = request.POST['hidden_file_name2']

            remove_from_recyclebin = Deleted_Files.objects.get(name=restore_file_name)
            remove_from_recyclebin.delete()

            files = Files()
            files.name = restore_file_name
            files.type = remove_from_recyclebin.type
            files.data = remove_from_recyclebin.data
            files.date_time_created = remove_from_recyclebin.date_time_created
            files.save()

    try: files = list(Files.objects.all().values_list()) 
    except: files = []
    
    try: deleted_files = list(Deleted_Files.objects.all().values_list())
    except: deleted_files = []

    ## viewing NASA Image of the Day ##
    api_key = "p9gmwsLowAl5YIQmJO6q9Tx5mM8Z20awbJ6Bl6FW"
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key='+api_key).json()
    image_date = response['date']
    image_explanation = response['explanation']
    image_title = response['title']
    image_url = response['url']

    return render(request, 'home.html', {'files': files, 'deleted_files': deleted_files,
            'image_date': image_date, "image_explanation": image_explanation, "image_title": image_title, "image_url": image_url
            })

# To -do
'''
1. show opened tabs in taskbar
2. Replace file if it already exists in folder Error message

3. Make pop up overlap
4. make right click 'open' work
5. make right click custom (specific to each document)

# gui
6. recycle bin icon on tab
7. Nasa Logo on tab and home page
'''
