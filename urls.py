from django.urls import path 

from . import views

from . views import archive
from article import views

urlpatterns = [
     path ('', archive),
     
     
    

    
]