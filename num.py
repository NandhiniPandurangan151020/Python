class MultipleFunctions:
    def SubfieldsInAI():
        list= ["Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are:")
        for temp in list:
            print(temp)
            
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even Number")
            num1=num,"is Even Number"
        else:
            print(num,"is Odd Number")
            num1=num,"is Odd Number"
        
                

    def Eligible():
        gender = input("Your gender: ")
        age = int(input("Your age: "))
        if (gender == 'Male'):
            if (age >= 21):
                print("Eligible")
                message = 'Eligible'
            else:
                print("Not Eligible")
                message = 'Not Eligible'
        elif (gender == 'Female'):
            if (age >= 18):
                print("Eligible")
                message = 'Eligible'
            else:
                print("Not Eligible")
                message = 'Not Eligible'
            
        

    def percentage():
        n1 = int(input("subject1: "))
        n2 = int(input("subject2: "))
        n3 = int(input("subject3: "))
        n4 = int(input("subject4: "))
        n5 = int(input("subject5: "))
        
        total = n1 + n2 + n3 + n4 + n5
        print("Total : ", total)
        
        percentage = total / 5
        print("Percentage : {:.9f}".format(percentage))
        
        

    def Triangle():
        n1 = int(input("Height: "))
        n2 = int(input("Breadth: "))
        n=(n1*n2)/2
        print("Area Forumula: (Height*Breadth)/2")
        print("Area of Triangle",n)
        N1 = int(input("Height1: "))
        N2 = int(input("Height2: "))
        N3 = int(input("Breadth: "))
        N=N1+N2+N3
        print("Perimeter Forumula: Height1+Height2+Breadth")
        print("Perimeter of Triangle",N)
        
