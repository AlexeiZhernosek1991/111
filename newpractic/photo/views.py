from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


# def photo(request):
#     return render(request, 'reverse.html')


def photo(request):
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['f']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'reverse.html', {
            'file_url': file_url
        })
    return render(request, 'reverse.html')
# Create your views here.
