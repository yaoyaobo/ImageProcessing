import xml.dom.minidom
import numpy as np
import cv2 as cv
import os
import time

yolo_dir = 'F:\\1\\'  # YOLO文件路径
weightsPath = os.path.join(yolo_dir, '2020_1_6.weights')  # 权重文件
configPath = os.path.join(yolo_dir, 'yolov3-voc.cfg')  # 配置文件
labelsPath = os.path.join(yolo_dir, 'voc.names')  # label名称
imgPath = R"F:\\1\\dzjym\\"  # 测试图像路径
xml_Path = R'F:\\1\\dzjym_xml\\' #XML保存路径
CONFIDENCE = 0.3  # 过滤弱检测的最小概率
THRESHOLD = 0.3  # 非最大值抑制阈值


def creat_xml(image_name, image_path, xml_path, width, height, managerList):
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root)
    nodefolder = doc.createElement('folder')
    nodefolder.appendChild(doc.createTextNode("VOC2007"))
    root.appendChild(nodefolder)
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(image_name))
    root.appendChild(nodefilename)
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(image_path))
    root.appendChild(nodepath)
    nodesource = doc.createElement('source')
    nodedatabase = doc.createElement('database')
    nodedatabase.appendChild(doc.createTextNode("Unknown"))
    nodesource.appendChild(nodedatabase)
    root.appendChild(nodesource)
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement('width')
    nodewidth.appendChild(doc.createTextNode(str(width)))
    nodeheight = doc.createElement('height')
    nodeheight.appendChild(doc.createTextNode(str(height)))
    nodedepth = doc.createElement('depth')
    nodedepth.appendChild(doc.createTextNode(str(3)))
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    root.appendChild(nodesize)
    for i in range(len(managerList)):
        nodeobject = doc.createElement('object')
        nodename = doc.createElement('name')
        nodename.appendChild(doc.createTextNode(managerList[i][0]))
        nodepose = doc.createElement('pose')
        nodepose.appendChild(doc.createTextNode('Unspecified'))
        nodetruncated = doc.createElement('truncated')
        nodetruncated.appendChild(doc.createTextNode('0'))
        nodedifficult = doc.createElement('difficult')
        nodedifficult.appendChild(doc.createTextNode('0'))
        nodebndbox = doc.createElement('bndbox')
        nodexmin = doc.createElement('xmin')
        nodexmin.appendChild(doc.createTextNode(managerList[i][1]))
        nodeymin = doc.createElement('ymin')
        nodeymin.appendChild(doc.createTextNode(managerList[i][2]))
        nodexmax = doc.createElement('xmax')
        nodexmax.appendChild(doc.createTextNode(managerList[i][3]))
        nodeymax = doc.createElement('ymax')
        nodeymax.appendChild(doc.createTextNode(managerList[i][4]))
        nodebndbox.appendChild(nodexmin)
        nodebndbox.appendChild(nodeymin)
        nodebndbox.appendChild(nodexmax)
        nodebndbox.appendChild(nodeymax)
        nodeobject.appendChild(nodename)
        nodeobject.appendChild(nodepose)
        nodeobject.appendChild(nodetruncated)
        nodeobject.appendChild(nodedifficult)
        nodeobject.appendChild(nodebndbox)
        root.appendChild(nodeobject)
    fp = open(os.path.join(xml_path, image[:-3] + 'xml'), 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

if __name__ == '__main__':

    # 加载网络、配置权重
    net = cv.dnn.readNetFromDarknet(configPath, weightsPath)  # #  利用下载的文件
    print("loading YOLO ...")  # # 可以打印下信息
    for image in os.listdir(imgPath):
        src_img = os.path.join(imgPath, image)
        managerList = []
        # 加载图片、转为blob格式、送入网络输入层
        img = cv.imread(src_img)
        blobImg = cv.dnn.blobFromImage(img, 1.0/255.0, (960, 704), None, True, False)   # # net需要的输入是blob格式的，用blobFromImage这个函数来转格式
        net.setInput(blobImg)  # # 调用setInput函数将图片送入输入层

        # 获取网络输出层信息（所有输出层的名字），设定并前向传播
        outInfo = net.getUnconnectedOutLayersNames()  # # 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
        start = time.time()
        layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
        end = time.time()
        print(image + "took {:.6f} seconds".format(end - start))  # # 可以打印下信息

        # 拿到图片尺寸
        (H, W) = img.shape[:2]
        # 过滤layerOutputs
        # layerOutputs的第1维的元素内容: [center_x, center_y, width, height, objectness, N-class score data]
        # 过滤后的结果放入：
        boxes = [] # 所有边界框（各层结果放一起）
        confidences = [] # 所有置信度
        classIDs = [] # 所有分类ID

        # # 1）过滤掉置信度低的框框
        for out in layerOutputs:  # 各个输出层
            for detection in out:  # 各个框框
                # 拿到置信度
                scores = detection[5:]  # 各个类别的置信度
                classID = np.argmax(scores)  # 最高置信度的id即为分类id
                confidence = scores[classID]  # 拿到置信度

                # 根据置信度筛查
                if confidence > CONFIDENCE:
                    box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        # # 2）应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
        idxs = cv.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
        # 得到labels列表
        with open(labelsPath, 'rt') as f:
            labels = f.read().rstrip('\n').split('\n')
        if len(idxs) > 0:
            for i in idxs.flatten():  # indxs是二维的，第0维是输出层，所以这里把它展平成1维
                managerList.append([labels[classIDs[i]], str(boxes[i][0]), str(boxes[i][1]), str(boxes[i][0]+boxes[i][2]),str(boxes[i][1]+boxes[i][3])])
        if len(boxes):
            creat_xml(image, src_img, xml_Path, W, H, managerList)

    print("执行完毕！！！")
