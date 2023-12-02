# views.py
from django.shortcuts import render
import pandas as pd
from .forms import UploadFileForm 
import csv 
from io import TextIOWrapper

# Create your views here.

def upload_file(request):
    if request.method =='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect( 'upload_success')
    else:
        form = UploadFileForm()  # Fix: Corrected form name to UploadFileForm
    return render(request, 'upload.html', {'form': form})  # Fix: Added 'request'

def handle_uploaded_file(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    for row in reader:
        _, created = ModalData.objects.get_or_create(
            columns1=row[0],
            columns2=row[1],
            columns3=row[2],
            columns4=row[3],
            columns5=row[4],

            columns6=row[5],
            columns7=row[6],
            columns8=row[7],
            columns9=row[8],
            columns10=row[9],

            columns11=row[10],
            columns12=row[11],
            
        )

def upload_success(request):
    return render(request, 'upload_success.html')  # Fix: Added 'request'
