
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from url_count.serilaizer import Webcount
from FirebaseClient.firebaseManager import FirebaseDataManager 
class UrlOperations (GenericViewSet):
    def url_word_count(self, request):
        result = {"message": None, "error": None}
        serializer_class = Webcount
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        url =  serializer.data
        firebase = FirebaseDataManager()
        try:
            response = requests.get(url['url'])
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            text_elements = soup.find_all(text=True)
            word_count = 0
            for text in text_elements:
                words = text.split()
                word_count += len(words)
                result["message"] = word_count
                
            data =  {
                "url": url['url'],
                "word_count": word_count,
                "like": url['like']
            }
            firebase.store_data(data)
            return Response(result, status.HTTP_200_OK)

        except Exception as e:
            result["error"] = e
            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete_data(self, request):
        result = {"message": None, "error": None}
        serializer_class = Webcount
        request_body = request.query_params
        serializer = serializer_class(data=request_body)
        serializer.is_valid(raise_exception=True)
        url =  serializer.data
        firebase = FirebaseDataManager()
        try:
            data = {
                    "url": url['url']

                }
            firebase.delete_data(data)
            result["message"] = "successfully deleted"
            return Response(result, status.HTTP_200_OK)
        except Exception as e:
            result["error"] = e
            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_data(self, request):
        result = {"message": None, "error": None}
        firebase = FirebaseDataManager()
        try:
            data =  firebase.fetch_data()
            result["message"] = data
            return Response(result, status.HTTP_200_OK)
        except Exception as e:
            result["error"] = e
            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update_like(self, request):
        result = {"message": None, "error": None}
        request_body = request.query_params
        serializer_class = Webcount
        serializer = serializer_class(data=request_body)
        serializer.is_valid(raise_exception=True)
        url =  serializer.data
        firebase = FirebaseDataManager()
        try:
            data = {
                    "url": url['url'],
                    "like":url['like']
                }
            firebase.update_data(data)
            result["message"] = "successfully updated like"
            return Response(result, status.HTTP_200_OK)
        except Exception as e:
            result["error"] = e
            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)
    