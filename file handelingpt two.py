
file_read = open('codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()




file_write = open('codingal.txt','w')
file_write.write("I am going to change the content")
file_write.write("So it got changed !!! ")
file_write.close()



file_append = open('codingal.txt','a')
file_append.write("Okay it,s so interestingggg....")
file_append.close()