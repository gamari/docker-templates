from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("authentication.urls")),
]

# TODO 静的ファイルの設定を行う