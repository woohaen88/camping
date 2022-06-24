from django.urls import path
from .views import (
    index,
    create,
    detail,
    update,
)

app_name = "camping"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("detail/<int:pk>/", detail, name="detail"),
    path("update/<int:pk>/", update, name="update"),
]