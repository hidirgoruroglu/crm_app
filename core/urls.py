from django.urls import path
from .views import index, logout_view, register_view, customer_record_view, delete_record_view, add_record_view, update_record_view


urlpatterns = [
    path("",index,name="index"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("add_record/", add_record_view, name="add_record"),
    path("record/<int:id>/", customer_record_view, name="customer_record"),
    path("delete_record/<int:id>/", delete_record_view, name="delete_record"),
    path("update_record/<int:id>/", update_record_view, name="update_record"),
]
