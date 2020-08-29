from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import os

'''
Detect Faces - remote
This example detects faces in a remote image, gets their gender and age, 
and marks them with a bounding box.
'''
def azurecs_cv(image_path):
    subscription_key = 'xxx'
    endpoint = 'https://emotionanalytics.cognitiveservices.azure.com/'
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    print("===== Detect Faces - remote =====")
    # Get an image with faces
    remote_image_url_faces = image_path
    # Select the visual feature(s) you want.
    remote_image_features = ["faces"]
    # Call the API with remote URL and features
    detect_faces_results_remote = computervision_client.analyze_image(remote_image_url_faces, remote_image_features)

    # Print the results with gender, age, and bounding box
    print("Faces in the remote image: ")
    if (len(detect_faces_results_remote.faces) == 0):
        print("No faces detected.")
    else:
        for face in detect_faces_results_remote.faces:
            print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
                                                                     face.face_rectangle.left, face.face_rectangle.top, \
                                                                     face.face_rectangle.left + face.face_rectangle.width, \
                                                                     face.face_rectangle.top + face.face_rectangle.height))
    return

'''
Detect Faces & Emotions - remote
This example detects faces in a remote image, gets their emotion, gender and age, 
and marks them with a bounding box.
'''
def azurecs_face(image_path):
    '''
    Expand Detection of Faces - remote
    This example detects faces in a remote image, gets their emotions,
    and marks them with a bounding box.
    '''
    subscription_key = 'xxx'
    endpoint = 'https://emotionalfaceanalytics.cognitiveservices.azure.com/'
    face_client = FaceClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # Detect a face in an image that contains a single face
    single_face_image_url = image_path
    single_image_name = os.path.basename(single_face_image_url)
    # detected_faces = face_client.face.detect_with_url(single_face_image_url)
    # Supported face attributes include age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise.
    return_face_attributes = ['emotion','smile','gender','age']
    detected_emotional_faces = face_client.face.detect_with_url(url=single_face_image_url, return_face_attributes = return_face_attributes)
    if not detected_emotional_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    def get_emotion(emoObject):
        emoDict = dict()
        emoDict['anger'] = emoObject.anger
        emoDict['contempt'] = emoObject.contempt
        emoDict['disgust'] = emoObject.disgust
        emoDict['fear'] = emoObject.fear
        emoDict['happiness'] = emoObject.happiness
        emoDict['neutral'] = emoObject.neutral
        emoDict['sadness'] = emoObject.sadness
        emoDict['surprise'] = emoObject.surprise
        emo_name = max(emoDict, key=emoDict.get)
        emo_level = emoDict[emo_name]
        return emo_name, emo_level

    for face in detected_emotional_faces:
        emotion, confidence = get_emotion(face.face_attributes.emotion)
        print("Gender: {}".format(face.face_attributes.gender))
        print("Age: {}".format(face.face_attributes.age))
        print("Smile intensity: {}".format(face.face_attributes.smile))
        print("Sentiment: {} with confidence level {}".format(emotion, confidence))
        return emotion, confidence

    return None, 0.0