from django.urls import path
from crudapp import views

app_name = 'crudapp'

urlpatterns = [
    path('add/' , views.addUser , name='add' ),
    path('' , views.userListPage , name='list' )

]
