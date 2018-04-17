from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template

from App.forms import DocumentForm
from App.models import Post, Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })


def index(request):
    temp = get_template('index.html');
    posts = Post.objects.all()
    current_time = datetime.now
    html = temp.render(locals())
    return HttpResponse(html)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')