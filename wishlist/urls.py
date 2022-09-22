from django.urls import path
from wishlist.views import show_wishlist
# sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import data_show_xml
from wishlist.views import data_show_json
from wishlist.views import data_show_xml_by_id
# sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import data_show_json_by_id
from wishlist.views import register  # sesuaikan dengan nama fungsi yang dibuat
# sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import login_user
# sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', data_show_xml, name='data_show_xml'),
    path('json/', data_show_json, name='data_show_json'),
    path('json/<int:id>', data_show_xml_by_id,
         name='data_show_xml_by_id'),
    path('xml/<int:id>', data_show_json_by_id,
         name='data_show_json_by_id'),
    # sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'),
    # sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'),
    # sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'),
]
