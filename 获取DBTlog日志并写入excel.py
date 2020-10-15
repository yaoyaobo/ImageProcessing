# -*-encoding=utf-8 -*-
from xlwt import*
xls = Workbook(encoding="utf-8")
sheet1 = xls.add_sheet("resnet_101")
sheet1.write(0, 0, 'Epoch')
sheet1.write(0, 1, 'accuracy')

keywords = ["train:accuracy"]

with open('K:\\小论文\\log\\resnet_50_log.txt', 'r') as f:
    lines = f.readlines()
    nums = 1
    for keyword in keywords:
        for line in lines:
            if keyword in line:
                epoch = line.split('')[0]
                index = epoch.split('')[-1]
                index = index.split(']')[0]
                val = line.split("")[-1]
                sheet1.write(nums, 0, index)
                sheet1.write(nums, 1, val)
                nums+=1

xls.save("epoch_accuracy_loss_resnet101.xls")