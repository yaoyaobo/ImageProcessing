# -*-encoding=utf-8 -*-
from xlwt import*
xls = Workbook(encoding="utf-8")
sheet1 = xls.add_sheet("alexnet")
sheet1.write(0, 0, 'Epoch')
sheet1.write(0, 1, 'train_loss')
sheet1.write(0, 2, 'test_accuracy')

keywords = ["test_accuracy"]

with open('C:\\Users\\24047\\Desktop\\fsdownload\\alexnet_log.txt', 'r') as f:
    lines = f.readlines()
    nums = 1
    for keyword in keywords:
        for line in lines:
            if keyword in line:
                epochs = line.split(' ')
                epoch = line.split(' ')[1]
                epoch = epoch.split(']')[0]
                train_loss = line.split(' ')[2]
                train_loss_val = line.split(' ')[3]
                test_accuracy = line.split(' ')[5]
                test_accuracy_val = line.split(' ')[6]
                print(epoch)
                #print(epochs)
                # print(train_loss_val)
                # print(test_accuracy_val)
                # index = epoch.split('')[-1]
                # index = index.split(']')[0]
                #print(test_accuracy_val)
                # print(val)
                sheet1.write(nums, 0, epoch)
                sheet1.write(nums, 1, train_loss_val)
                sheet1.write(nums, 2, test_accuracy_val)
                nums += 1

xls.save("C:\\Users\\24047\\Desktop\\fsdownload\\alexnet_loss_accuracy.xlsx")