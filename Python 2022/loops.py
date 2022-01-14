#loop in python
 
# Food = ["apple","banana","cake"]
# for i in Food:s
#     print(i)

# single_food =  "appleqeqeqe"
# for i in single_food:
#     print(i)


# dict1 = {"name":"sumon","age":22,"roll":243243}

# for i,j in dict1.items():
#     print(i,j)


# lists  = [int,float,"sumon","galib",32,4,4]

# for item in lists:
#     if str(item).isnumeric():
#         print(item)

#While loop


# i =1
# while i<6:
#     print(i)
#     i = i+1
    
    
#Break statement

# i =1
# while i<6:
#     print(i)
#     if i == 3:
#         break
#     i = i+1
    
#continue Statement
# i =1
# while i<6:
#   i +=1  
#   if i == 3:
#         continue
#   print(i)

#break And Continue
while(True):
    inp =int(input("Enter a number \n"))
    if inp>200:
        print("Your Right")
        break
    else:
        print("try again")
        continue