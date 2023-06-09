from django.urls import path
from  url_count.views import UrlOperations

urlpatterns = [
    path("word_count", UrlOperations.as_view({"post": "url_word_count"})),
    path("delete", UrlOperations.as_view({"delete": "delete_data"})),
    path("fetch", UrlOperations.as_view({"get": "get_data"})),
    path("update_likes", UrlOperations.as_view({"put": "update_like"}))
     
    ]
