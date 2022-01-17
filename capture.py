import face
import SteeringGear
import message
import HC
def active_capture():
    flag = 0
    HC.HC_init()
    if HC.HC_detected() == 1:

        for i in range(90,181,30):
            SteeringGear.SG_op(i)
            face.get_quick_image(face.detected_image_name)
            detected_result = face.face_detected()
            if detected_result['error_msg'] == 'SUCCESS':
                print('检测到人脸')
                # sg.p.stop()
                # sg.GPIO.cleanup()
                face.face_cut(face.detected_image_name, detected_result)
                recognition_result = face.face_recognition(face.cut_image_name)
                if recognition_result['result']:
                    if recognition_result['result']['user_list'][0]['score'] >= 80:
                        print('识别成功')
                        message.send_message('你的朋友'+recognition_result['result']['user_list'][0]['user_info']+'到访')
                        return 'recognitionSuccess'
                    else:
                        print('识别失败')
                        message.send_message('我不认识你')
                else:
                    print('识别失败')
                flag = 1
                break
        if flag == 0:
            for i in range(90,-1,-30):
                SteeringGear.SG_op(i)
                face.get_quick_image(face.detected_image_name)
                detected_result = face.face_detected()
                if detected_result['error_msg'] == 'SUCCESS':
                    print('检测到人脸')
                    face.face_cut(face.detected_image_name, detected_result)
                    recognition_result = face.face_recognition(face.detected_image_name)
                    if recognition_result['result']:
                        if recognition_result['result']['user_list'][0]['score'] >= 80:
                            print('识别成功')
                            # print(recognition_result['result']['user_list'][0]['user_info'])
                            message.send_message('你的朋友'+recognition_result['result']['user_list'][0]['user_info']+'到访')
                            return 'recognitionSuccess'
                        else:
                            print('识别失败')
                            message.send_message('我不认识你')
                    else:
                        print('识别失败')
                        message.send_message('我不认识你')
                    break

        SteeringGear.SG_op(90)
    # sg.p.stop()
    # SteeringGear.GPIO.cleanup()
# face.get_quick_image(face.detected_image_name)