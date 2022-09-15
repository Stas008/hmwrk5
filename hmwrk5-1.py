# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

path = "input_1_task.txt"
with open(path) as file:
    first_string = file.readline()
sub_string = "абв"
result_string = ""
print (first_string)
splitted_string = first_string.split()
print(splitted_string)
for i in splitted_string:
    if sub_string not in i:
        result_string += i+ " "
print(result_string)
with open ("result_1_task_coded.txt","w") as data:
    data.write(result_string)