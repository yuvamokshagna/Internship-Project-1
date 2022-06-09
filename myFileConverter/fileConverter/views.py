from urllib import response
from django.shortcuts import redirect, render
from django.http import FileResponse, HttpResponse

from .forms import MusicFileForm

from .audiotomidi import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            initial_obj = form.save(commit=False)
            initial_obj.save()
            initial_obj.document
            run(initial_obj.document, "out/ConvertedMIDIFile.mid")
            # convert_files(filename)
            return render(request, 'fileConverter/convert.html')
    else:
        form = MusicFileForm()
    return render(request, 'fileConverter/index.html', {
        'form': form
    })



def dowload(request):
    fsock = open('out/ConvertedMIDIFile.mid', 'rb')
    response = HttpResponse(fsock, content_type='audio/mpeg')
    response['Content-Disposition'] = "attachment; filename=convertedMIDIFile.mid"
    return response

