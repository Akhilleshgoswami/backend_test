import time
import firebase_admin
from firebase_admin import credentials, firestore
import os
from urllib.parse import urlparse
global firebase_client 
cred = credentials.Certificate(os.path.abspath(os.path.dirname(__file__)) + "/firebase.json")
firebase_admin.initialize_app(cred)
firebase_client =   firestore.client()
class FirebaseDataManager(object):

    # def update_data(self, order_id, collection, data):
    #     self.firebase_client = self.get_firebase_client()
    #     self.firebase_client.collection(collection).document(order_id).update(data)
    def get_site_name(sefl,url):
        parsed_url = urlparse(url)
        site_name = parsed_url.netloc
        site_name = site_name.replace(".", "")
        return str(site_name)

    def store_data(self, data):
            url = self.get_site_name(data['url'])
            firebase_client.collection("Urls").document(url).set(data)

    def delete_data(self,data):
        url = self.get_site_name(data['url'])
        firebase_client.collection('Urls').document(url).delete()
       
    def fetch_data(self):

# Fetch all documents in the collection
        collection_ref = firebase_client.collection('Urls')
        
        # Fetch all documents in the collection
        documents = collection_ref.get()
        result = []
        
        # Iterate over the documents
        for doc in documents:
            # Access the document ID and data
            document_id = doc.id
            document_data = doc.to_dict()
            print("Document ID:", document_id)
            result.append(document_data)
        print("Result:", result)
    
        return result
    def update_data(self,data):
        url = self.get_site_name(data['url'])
        print(data)
        doc_ref = firebase_client.collection("Urls").document(url)
        doc_ref.update({
            "like": not data['like'],
        })
    # def fetch_collections(self, collection_name):
    #     self.firebase_client = self.get_firebase_client()
    #     collection_obj = self.firebase_client.collection(collection_name)
    #     collection_data = collection_obj.stream()
    #     return collection_data
