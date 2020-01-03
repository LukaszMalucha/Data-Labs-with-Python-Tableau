from django.shortcuts import redirect
from db_manager.utils import database_upload
from django.shortcuts import redirect

from db_manager.utils import database_upload


# Create your views here.


def db_upload(request):
    """ Uncomment if refreshing data needed"""
    database_upload()
    return redirect('/')