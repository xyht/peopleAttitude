# -*- coding: utf-8 -*-
import os
import shutil
import re
import random
import string
import cv2
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .method.ww import getData
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def setupload(request):
    return render(request, 'upload.html')


# 接收文件
@csrf_exempt
def getupload(request):
    if request.method == "POST":
        filenames = ''.join(random.sample(string.ascii_letters + string.digits, 8))+'.'+ (re.findall(r'(?<=\.)\w+$', str(request.FILES['file'])))[0]
        morenames = ''.join(random.sample(string.ascii_letters + string.digits, 8))+'.'+ (re.findall(r'(?<=\.)\w+$', str(request.FILES['more'])))[0]
        handle_upload_file(request.FILES['file'], filenames)
        handle_upload_file(request.FILES['more'], morenames)
        path1 = 'F:/Python/Django/PeopleAttitude/Web/access/out_put/'+ filenames
        path2 = 'F:/Python/Django/PeopleAttitude/Web/access/out_put/'+ morenames
        os.system(
            'F: && cd F:\VS\openpose-1.2.1-win64-binaries && bin\\OpenPoseDemo.exe --image_dir F:\\Python\\Django\\PeopleAttitude\\Web\\access --write_images F:\\Python\\Django\\PeopleAttitude\\Web\\access\\out_put\\ --write_keypoint_json F:\\Python\\Django\\PeopleAttitude\\Web\\access\\out_put\\')

        path1 = str(path1).replace('.'+ (re.findall(r'(?<=\.)\w+$', str(request.FILES['file'])))[0], "_keypoints.json")
        path2 = str(path2).replace('.' + (re.findall(r'(?<=\.)\w+$', str(request.FILES['more'])))[0], "_keypoints.json")

        # data = getData(path1,path2)
        print(path2)
        print(path1)
        data = getData(path1,path2)
        shutil.rmtree('F:/Python/Django/PeopleAttitude/Web/access')
        mkdir('F:/Python/Django/PeopleAttitude/Web/access/out_put')
        return HttpResponse(('%.2f' % (data)))  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中

    return HttpResponse("ok")


def handle_upload_file(file, filename):
    path = 'Web/access/'  # 上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)


# 接收视频
@csrf_exempt
def getuploadvideo(request):
    if request.method == "POST":
        filenames = ''.join(random.sample(string.ascii_letters + string.digits, 8))+'.'+ (re.findall(r'(?<=\.)\w+$', str(request.FILES['file'])))[0]
        morenames = ''.join(random.sample(string.ascii_letters + string.digits, 8))+'.'+ (re.findall(r'(?<=\.)\w+$', str(request.FILES['more'])))[0]
        # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        # print(ran_str + '.' + strings[0])
        handle_upload_file(request.FILES['file'], filenames)
        handle_upload_file(request.FILES['more'], morenames)
        path1 = 'F:/Python/Django/PeopleAttitude/Web/access/out_put/'+ filenames
        path2 = 'F:/Python/Django/PeopleAttitude/Web/access/out_put/'+ morenames
        fatherpath1 = 'F:/Python/Django/PeopleAttitude/Web/access/'+ filenames
        fatherpath2 ='F:/Python/Django/PeopleAttitude/Web/access/'+ morenames
        path1 = str(path1).replace('.'+ (re.findall(r'(?<=\.)\w+$', str(request.FILES['file'])))[0], "")
        path2 = str(path2).replace('.' + (re.findall(r'(?<=\.)\w+$', str(request.FILES['more'])))[0], "")
        mkdir(path1)
        mkdir(path2)
        getPhoto(fatherpath1,path1)
        getPhoto(fatherpath2,path2)
        len1 = (len([name for name in os.listdir(path1) if os.path.isfile(os.path.join(path1, name))]))
        len2 = (len([name for name in os.listdir(path2) if os.path.isfile(os.path.join(path2, name))]))
        rank = getVideoData(len1,path1,filenames,len2,path2,morenames)
        print(rank)
        shutil.rmtree('F:/Python/Django/PeopleAttitude/Web/access')
        mkdir('F:/Python/Django/PeopleAttitude/Web/access/out_put')
        return HttpResponse(('%.2f' % (rank)))  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中

    return HttpResponse("ok")


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False


def getPhoto(fatherpath1,path1):
    vc = cv2.VideoCapture(fatherpath1)
    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        rval, frame = vc.read()
        cv2.imwrite(path1 + '/' + str(c) + '.jpg', frame)
        c = c + 1
        cv2.waitKey(1)
    vc.release()


def getVideoData(len,path,name,len2,path2,name2):
    len=int(len/10)*10
    len2 = int(len2/10)*10
    length = int(len/10)
    length2 = int(len2/10)
    list1 = []
    list2 = []
    nameList1= []
    nameList2= []
    for i in range(1,len+1,length):
        list1.append(i)
    for i in range(1,len2+1,length2):
        list2.append(i)
    os.system(
        'F: && cd F:\VS\openpose-1.2.1-win64-binaries && bin\\OpenPoseDemo.exe --image_dir '+path+' --write_images '+path+' --write_keypoint_json '+path+'')
    os.system(
        'F: && cd F:\VS\openpose-1.2.1-win64-binaries && bin\\OpenPoseDemo.exe --image_dir ' + path2 + ' --write_images ' + path2 + ' --write_keypoint_json ' + path2 + '')
    for i in range(10):
        nameList1.append(path+'/'+str(list1[i])+'_keypoints.json')
        nameList2.append(path2+'/'+str(list2[i])+'_keypoints.json')

    print(nameList1)
    print(nameList2)


    rank = 0
    for i in range(10):
        rank=getData(nameList2[i],nameList1[i])+rank
    rank = rank/10
    return rank