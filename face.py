#人脸检测及识别
from aip import AipFace
from picamera import PiCamera
import RPi.GPIO as GPIO
import base64
import time
import requests
import matplotlib.image as mpimg

# 百度人脸识别API账号信息
APP_ID = '19994025'
API_KEY = '22BhLKKQPSLs2yWfSDsf3Kgu'
SECRET_KEY = 'aTlh3nCowsiLqkW8lGB3Uc6vsp935dgQ'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)  # 创建一个客户端用以访问百度云
# 图像编码方式
IMAGE_TYPE = 'BASE64'
# 人脸检测的文件名
detected_image_name = 'faceimage.jpg'
# 人脸裁剪的文件名
cut_image_name = 'facecutimage.jpg'
# 用户组
GROUP = 'lin'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=22BhLKKQPSLs2yWfSDsf3Kgu&client_secret=aTlh3nCowsiLqkW8lGB3Uc6vsp935dgQ'
# 人脸检测url
request_url_detected = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
# 人脸注册url
request_url_add = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
access_token_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
# access token
response = requests.get(access_token_host)
access_token = response.json()['access_token']

def get_image(image_name):
    '''
    :param image_name: 图片文件名
    :return: 无
    '''
    camera = PiCamera()  # 定义一个摄像头对象
    camera.resolution = (800, 600)  # 摄像界面为800*600
    time.sleep(0.2)
    camera.start_preview()  # 开始摄像
    time.sleep(2)
    camera.capture(image_name)  # 拍照并保存
    time.sleep(0.2)
    camera.close()


# 拍照
def get_quick_image(image_name):
    '''
    :param image_name: 图片文件名
    :return: 无
    '''
    camera = PiCamera()  # 定义一个摄像头对象
    camera.resolution = (800, 600)  # 摄像界面为800*600
    time.sleep(0.2)
    camera.start_preview()  # 开始摄像
    time.sleep(0.2)
    camera.capture(image_name)  # 拍照并保存
    time.sleep(0.2)
    camera.close()


# 对图片的格式进行转换
def transimage(image_name):
    '''
    :param image_name: 图片文件名
    :return: 经过base64编码后的图片
    '''
    f = open(image_name, 'rb')
    img = base64.b64encode(f.read())
    return img


# 获取access token
def get_access_token():
    '''
    :return: 百度的access_token
    '''
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    response = requests.get(host)
    if response:
        return response.json()['access_token']


# 人脸检测
def face_detected():
    '''
    :return: json人脸检测的结果
    '''
    global request_url_detected
    global access_token
    global detected_image_name
    params = {"image": transimage(detected_image_name), "image_type": IMAGE_TYPE, "quality_control": "LOW",
              "face_field": "gender,age,quality"}
    # access_token = '[调用鉴权接口获取的token]'
    # access_token = get_access_token()
    request_url = request_url_detected + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        return response.json()


# 人脸裁剪
def face_cut(image_name, detected_result):
    '''
    :param image_name: 人脸图像文件名
    :param detected_result: 人脸检测结果（json）
    :return: 无
    '''
    global cut_image_name
    location = detected_result['result']['face_list'][0]['location']
    image = mpimg.imread(image_name)
    cut_image = image[(int(location['top']) - 40):(int(location['top']) + int(location['height'])),
                (int(location['left']) - 10):(int(location['left']) + int(location['width']) + 10)]
    mpimg.imsave(cut_image_name, cut_image)


# 人脸注册
def face_add(image_name, username, username_pinyin):
    '''
    :param image_name: 人脸图像文件名
    :param username: 注册人的姓名
    :param username_pinyin: 注册人姓名的拼音
    :return: json的注册结果
    '''
    global request_url_add
    global access_token
    params = {"image": transimage(image_name), "image_type": IMAGE_TYPE, "group_id": "lin", "user_id": username_pinyin,
              "user_info": username, "quality_control": "LOW"}
    # access_token = get_access_token()
    request_url = request_url_add + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        return response.json()


# 人脸识别
def face_recognition(image_name):
    '''
    :param image_name: 人脸图像文件名
    :return: json的识别结果
    '''
    global access_token
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    params = {'image': transimage(image_name), 'image_type': IMAGE_TYPE, 'group_id_list': GROUP}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        # print (response.json())
        return response.json()

# get_image(detected_image_name)
