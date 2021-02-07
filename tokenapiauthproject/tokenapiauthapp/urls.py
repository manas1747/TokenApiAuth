from django.urls import path, include
from .views import CityRecordList, CityRecordDetails, CountryRecordList, CountryRecordDetails, RegistrationDetails
from rest_framework.authtoken.views import obtain_auth_token

app_name = "tokenapiauthapp"


urlpatterns = [
    path('cityrecords/list/', CityRecordList.as_view()),
    path('cityrecords/', CityRecordDetails.as_view()),
    path('cityrecords/<city_name>/', CityRecordDetails.as_view()),

    path('countryrecords/list/', CountryRecordList.as_view()),
    path('countryrecords/', CountryRecordDetails.as_view()),
    path('countryrecords/<country_name>/', CountryRecordDetails.as_view()),

    path('accounts/register', RegistrationDetails.as_view()),
    path('accounts/login', obtain_auth_token, name="login"), # manas this is inbuilt view to return new token at every login request
]
