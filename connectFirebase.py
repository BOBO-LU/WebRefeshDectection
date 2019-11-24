import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('python-pm25-firebase-adminsdk-x1ujd-175abb1446.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
print(db)