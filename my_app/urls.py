

from django.conf.urls import url
from . import views as vi
from learn_django.Converter import FourDigitYearConverter
from django.urls import path
urlpatterns = [
    path('index',vi.index,name='index',kwargs={"arg":"world"}),
    path('<int:question_id>/', vi.detail, name='detail'),
    path('year/<yyyy:year_data>/',vi.year,name='year'),
    path('photo/',vi.photo),
    path('run/',vi.run),
]