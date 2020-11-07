f = open("/media/manawadu/New Volume/ts/test.txt", "r")

for x in f:
    print(x)
    tmp=x.split("/home/manawadu/Downloads/ts/", 1)[1]
    tmp2="/media/manawadu/New Volume/ts/"+tmp
    f1 = open("test.txt", "a")
    f1.write(tmp2)
    f1.close()
    # train.close()
    # print(x.split("Images 2.0/", 1)[1])
  # print(x)


# f = open("train.txt", "a")
# x="mayura"
# f.write(x+"\n")
# f.close()
# my_string="hello python world , i'm a beginner "
# print (my_string.split("world",1)[1] )