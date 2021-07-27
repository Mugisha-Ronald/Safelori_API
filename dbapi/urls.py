from django.urls import path
from .views import Record, Login, Logout, ServiceProviderViewset,TruckViewset,OrderViewset,ServiceProviderUserViewset,ServiceProviderTruckViewset

urlpatterns = [
    path('signup/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('serviceprovider/', ServiceProviderViewset.as_view(), name="serviceprovider"),
    path('trucks/', TruckViewset.as_view(), name="trucks"),
    path('order/', OrderViewset.as_view(), name="order"),
    path('serviceprovideruser/', ServiceProviderUserViewset.as_view(), name="serviceprovideruser"),
    path('serviceprovidertruck/', ServiceProviderTruckViewset.as_view(), name="serviceprovidertruck"),
]