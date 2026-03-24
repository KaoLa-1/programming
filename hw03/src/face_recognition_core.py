import face_recognition
import cv2
import numpy as np

class FaceRecognitionCore:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
    
    def add_known_face(self, image_path, name):
        """添加已知人脸"""
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if face_encodings:
            self.known_face_encodings.append(face_encodings[0])
            self.known_face_names.append(name)
            return True
        return False
    
    def recognize_faces(self, image):
        """识别图片中的人脸"""
        # 转换图片格式
        if isinstance(image, np.ndarray):
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            rgb_image = face_recognition.load_image_file(image)
        
        # 检测人脸位置
        face_locations = face_recognition.face_locations(rgb_image)
        # 计算人脸编码
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            # 与已知人脸比较
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            
            # 找到最佳匹配
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            
            face_names.append(name)
        
        return face_locations, face_names
    
    def draw_faces(self, image, face_locations, face_names):
        """在图片上绘制人脸框和名称"""
        if isinstance(image, str):
            image = cv2.imread(image)
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # 绘制人脸框
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            # 绘制名称
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        return image