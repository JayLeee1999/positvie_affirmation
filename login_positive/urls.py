from django.contrib import admin
from django.urls import path
from community.views import positive

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('positive/', positive, name='positive'),
    path('', positive, name='positive'),
]

