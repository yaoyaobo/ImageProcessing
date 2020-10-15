import os
path = '/home/yaobo/background/'


#　　重命名
filename_list = os.listdir(path)
a = 0
j = 1
for i in filename_list:
    used_name = path + filename_list[a]
    new_name = path + "yao_e12_"+str(j)+'.jpg'
    os.rename(used_name, new_name)
    print("文件%s成功命名，新的文件名为%s" % (used_name, new_name))
    a += 1
    j += 1
