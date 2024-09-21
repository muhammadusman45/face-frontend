# # from flask import Flask, request, jsonify
# # # import face_recognition
# # import base64
# # import numpy as np
# # import cv2

# # app = Flask(__name__)

# # @app.route ('/' , methods=['GET'])
# # def get
# # @app.route('/upload', methods=['POST'])
# # def upload_image():
# #     data = request.get_json()
# #     print(data)
# #     print("hello world")
# #     # image_data = data['image']

# #     # # Decode base64 image
# #     # image_data = image_data.split(',')[1]
# #     # img_bytes = base64.b64decode(image_data)
# #     # np_img = np.frombuffer(img_bytes, np.uint8)
# #     # img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

# #     # # Detect face
# #     # face_locations = face_recognition.face_locations(img)

# #     # if face_locations:
# #     #     return "Face detected", 200
# #     # else:
# #     #     return "No face detected", 200

# # if __name__ == '__main__':
# #     app.run(debug=True)
# # from flask import Flask , request
# # from flask_restx import Api, Resource
# # import face_recognition
# # app = Flask(__name__)
# # api = Api(app, doc = '/docs') 
# # ns = api.namespace('hello', description='Hello World operations')
# # @ns.route('/')
# # class HelloWorld(Resource):
    
# # ATTENDANCE_DIR = 'attendance_records'
# # os.makedirs(ATTENDANCE_DIR, exist_ok=True)

# # # List of known face encodings and names
# # known_face_encodings = []
# # known_face_names = []
    
# #      def load_known_faces():
# #     # Load saved face encodings and names from files or database
# #     # Example: known_face_encodings.append(encoding)
# #     pass

# #     def save_attendance(name):
# #     with open(os.path.join(ATTENDANCE_DIR, f"{name}.txt"), 'a') as file:
# #         file.write(f"{name} attended\n")

# # @app.route('/upload', methods=['POST'])
# # def upload_image():
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file part'}), 400
    
# #     file = request.files['file']
# #     if file.filename == '':
# #         return jsonify({'error': 'No selected file'}), 400
    
# #     image = Image.open(io.BytesIO(file.read()))
# #     image_np = np.array(image)
    
# #     # Find faces in the uploaded image
# #     face_locations = face_recognition.face_locations(image_np)
# #     face_encodings = face_recognition.face_encodings(image_np, face_locations)
    
# #     for face_encoding in face_encodings:
# #         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
# #         name = "Unknown"
        
# #         if True in matches:
# #             first_match_index = matches.index(True)
# #             name = known_face_names[first_match_index]
        
# #         save_attendance(name)
    
# #     return jsonify({'status': 'Attendance recorded'}), 200

# #     def get(self):
# #         """Returns a Hello, World! message"""
# #         return {'message': 'Hello, World!'}

# #     def post(self):
# #         """Receives text and echoes it back"""
# #         data = request.get_json()
# #         if 'text' in data:
# #             return {'received_text': data['text']}
# #         else:
# #             return {'error': 'No text provided'}, 400

# # if __name__ == '__main__':
# #     app.run(debug=True)



# # if __name__ == '__main__':
# #     app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_restx import Api, Resource
# import face_recognition
# import os
# from PIL import Image
# import io
# import numpy as np
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app) 
# api = Api(app, doc='/docs')
# ns = api.namespace('hello', description='Hello World operations')

# ATTENDANCE_DIR = 'attendance_records'
# os.makedirs(ATTENDANCE_DIR, exist_ok=True)

# # List of known face encodings and names
# known_face_encodings = []
# known_face_names = []

# # def load_known_faces():
#     # Load the known images and create face encodings
#     # image = face_recognition.load_image_file('images/obama.png')
#     # face_encoding = face_recognition.face_encodings(image)[0]  # Get the first face's encoding

#     # # Append the face encoding and the corresponding name
#     # known_face_encodings.append(face_encoding)
#     # known_face_names.append("Barack Obama")

# # def load_known_faces():
# #     # Load saved face encodings and names from files or database
# #     # Example: known_face_encodings.append(encoding)
# #     pass
# # # Call the function to load known faces when the application starts
# # # load_known_faces()

# # def load_known_faces():
# #     # image = face_recognition.load_image_file('images/usman.png')
# #     # face_encoding = face_recognition.face_encodings(image)[0]
# #     # print("obama images----->" , face_encoding)
# #     # known_face_encodings.append(face_encoding)
# #     # known_face_names.append("usman")
# #      known_faces = {
# #         'usman': 'images/usman.png',
# #         'john': 'images/usman-2.png',  # Add more face images here
# #     }
    
# #     for name, file_path in known_faces.items():
# #         image = face_recognition.load_image_file(file_path)
# #         face_encoding = face_recognition.face_encodings(image)[0]  # Get face encoding
# #         known_face_encodings.append(face_encoding)
# #         known_face_names.append(name)
# def load_known_faces():
#     known_faces = {
#         'usman': 'images/usman.png',
#         'john': 'images/usman-2.png',  # Add more face images here
#     }
    
#     for name, file_path in known_faces.items():
#         image = face_recognition.load_image_file(file_path)
#         face_encoding = face_recognition.face_encodings(image)[0]  # Get face encoding
#         known_face_encodings.append(face_encoding)
#         known_face_names.append(name)        

# def save_attendance(name):
#     with open(os.path.join(ATTENDANCE_DIR, f"{name}.txt"), 'a') as file:
#         file.write(f"{name} attended\n")

# @ns.route('/')
# class HelloWorld(Resource):
#     def get(self):
#         """Returns a Hello, World! message"""
#         return {'message': 'Hello, World!'}

#     def post(self):
#         """Receives text and echoes it back"""
#         data = request.get_json()
#         if 'text' in data:
#             return {'received_text': data['text']}
#         else:
#             return {'error': 'No text provided'}, 400

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
       
#     # print("files ----->" , request.files['file'].filesname)
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     # Open and convert the image to RGB
#     image = Image.open(io.BytesIO(file.read()))
#     image = image.convert('RGB')  # Convert to RGB mode
#     image_np = np.array(image)
    
#     # Find faces in the uploaded image
#     face_locations = face_recognition.face_locations(image_np)
#     face_encodings = face_recognition.face_encodings(image_np, face_locations)
#     print("image ----->" , face_encodings)
#     tolerance = 0.5
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding , tolerance=tolerance)
#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         name = "Unknown"
#         print(matches)
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]
        
#             save_attendance(name)
#             message = f"Attendance recorded for {name}"
#         else:
#             message = "No known face matched, attendance not recorded"
    
#     return jsonify({'status': message}), 200

# if __name__ == '__main__':
#     load_known_faces()  # Load known faces when starting the server
#     app.run(debug=True)



############## run code   ###########

from flask import Flask, request, jsonify
from flask_restx import Api, Resource
import face_recognition
import os
from PIL import Image
import io
import numpy as np
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
api = Api(app, doc='/docs')
ns = api.namespace('hello', description='Hello World operations')

ATTENDANCE_DIR = 'attendance_records'
os.makedirs(ATTENDANCE_DIR, exist_ok=True)

IMAGE_DIR = 'uploaded_images'
os.makedirs(IMAGE_DIR, exist_ok=True)  
known_face_encodings = []
known_face_names = []
 
def load_known_faces():
   
    known_faces_dir = 'uploaded_images'

    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            file_path = os.path.join(known_faces_dir, filename)
            
            
            image = face_recognition.load_image_file(file_path)
            face_encodings = face_recognition.face_encodings(image)
            
            if face_encodings:  
                face_encoding = face_encodings[0]  
                
                
                name = os.path.splitext(filename)[0]
                
                
                known_face_encodings.append(face_encoding)
                known_face_names.append(name)
            else:
                print(f"No face found in {file_path}")
def save_attendance(name):
    with open(os.path.join(ATTENDANCE_DIR, f"{name}.txt"), 'a') as file:
        file.write(f"{name} attended\n")

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        """Returns a Hello, World! message"""
        return {'message': 'Hello, World!'}

    def post(self):
        """Receives text and echoes it back"""
        data = request.get_json()
        if 'text' in data:
            return {'received_text': data['text']}
        else:
            return {'error': 'No text provided'}, 400

@app.route('/upload', methods=['POST'])
def image_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image = Image.open(io.BytesIO(file.read()))
    image = image.convert('RGB')  
    image_np = np.array(image)

    
    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(image_np, face_locations)
    
    tolerance = 0.5
    message = "No faces found in the image"  

    if face_encodings:
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                save_attendance(name)
                message = f"Attendance recorded for {name}"
                break  # Exit loop after first match (optional based on your needs)
            else:
                message = "No known face matched, attendance not recorded"
    else:
        message = "No faces found in the image"

    
    return jsonify({'status': message}), 200

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    
    image_path = os.path.join(IMAGE_DIR, file.filename)
    file.save(image_path)

    return jsonify({'message': 'Image uploaded successfully!', 'image_path': image_path}), 200

if __name__ == '__main__':
    load_known_faces()  
    app.run(debug=True)
