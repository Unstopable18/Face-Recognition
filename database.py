import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("D:\Python\Face-Recognition\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitioncv-default-rtdb.firebaseio.com/"
})
ref=db.reference('employee')


data ={
    "312654":{
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year":2017,
        "total_attendance": 6,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
    "852741":{
        "name": "Emily Blunt",
        "major": "Economics",
        "starting_year":2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
    "963852":{
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year":2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
    "darshani":{
        "name": "Darshani kakade",
        "major": "Frontend",
        "starting_year":2020,
        "total_attendance": 10,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
     "dhananjay":{
        "name": "Dhananjay kalaskar",
        "major": "AI-ML",
        "starting_year":2021,
        "total_attendance": 8,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
     "gaurav":{
        "name": "Gaurav Mule",
        "major": "AI-ML",
        "starting_year":2021,
        "total_attendance": 8,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
     "mrunali":{
        "name": "Mrunali gadhave",
        "major": "HR",
        "starting_year":2021,
        "total_attendance": 20,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
     "nikesh":{
        "name": "Nikesh Gondhchawar",
        "major": "Hardware",
        "starting_year":2017,
        "total_attendance": 50,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
     },
     "yuvraj":{
        "name": "Fuvraj Sune",
        "major": "Frontend",
        "starting_year":2020,
        "total_attendance": 10,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
     },

}
for key,value in data.items():
    ref.child(key).set(value)  
