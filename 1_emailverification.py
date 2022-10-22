
email = input("Enter Your Email : ")
k = 0
j = 0
d = 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i==i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i== "_" or i== "." or i== "@":
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email because email have space or captile letter or another sign")
            else:
                print("Wrong Email because '.' is not right position")
        else:
            print("Wrong Email because @ is not in email or @ is more than 1") 
    else:
        print("Wrong Email because first charecter is not alphabate")
else:
    print("Wrong Email because length ins less than 6 ")


# (^) we are use ----xor (^)----- operater because if both conditon is true than false , if bothe condition is false than false , if only one condition  is true then True