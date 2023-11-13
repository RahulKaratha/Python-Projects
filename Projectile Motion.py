print("\tPYTHON PROGRAM TO SOLVE PROJECTILE MOTION PROBLEMS")
print("=========================================================================\n\n")
import math as m
import numpy as np
import matplotlib.pyplot as plt

def sin(o):
    r=m.radians(o)
    return m.sin(r)

def tan(o):
    r=m.radians(o)
    return m.tan(r)

def cos(o):
    r=m.radians(o)
    return m.cos(r)
    
while True:
    print("------------------------------------------------------------------------")
    print("\t\t\t\tMENU")
    print("------------------------------------------------------------------------\n")

    print("1.Time of Flight")
    print("2.Horizontal Range")
    print("3.Maximum Height")
    print("4.Path")
    print("5.Exit")

    choice=int(input("\nEnter Choice[1-5]:"))
    print("=========================================================================\n")

    if choice==1:
        u=eval(input("\nEnter initial velocity:"))
        o=eval(input("Enter angle thrown:"))
        
        t=(2*u*sin(o))/9.8
        print("\n\nTime of Flight=",t)
        print("=========================================================================\n")

    if choice==2:
        u=eval(input("\nEnter initial velocity:"))
        o=eval(input("Enter angle thrown:"))
        
        r=u*u*sin(2*o)/9.8
        print("\n\nHorizontal Range=",r)
        print("=========================================================================\n")
        
    if choice==3:
        u=eval(input("\nEnter initial velocity:"))
        o=eval(input("Enter angle thrown:"))
        
        h=(u*sin(o))**2/(9.8*2)
        print("\n\nMaximum Height=",h)

        r=u*u*sin(2*o)/9.8
        x=np.linspace(0,r)


        
        y=(x*tan(o))-((9.8*x*x)/(2*u*u*cos(o)*cos(o)))

        if y==h:
            X=x
        
        plt.plot(x,y)
        plt.title("Trajectory of Body")
        plt.xlabel("Distance Travelled in metres")
        plt.ylabel("Height in metres")
        plt.grid(True)

        plt.scatter(X,h,label="Point")
        plt.legend()
        plt.show()        

        
        print("=========================================================================\n")

    if choice==4:
        u=eval(input("\nEnter initial velocity:"))
        o=eval(input("Enter angle thrown:"))

        X=eval(input("Enter horizontal distance travelled:"))

        A=X*tan(o)
        B=(9.8*X*X)
        C=2*u*u*cos(o)*cos(o)
        
        Y=A-(B/C)
        

        print("\n\nBody is at height",Y,"m for",X,"m distance travelled")
        print("=========================================================================\n")



        r=u*u*sin(2*o)/9.8
        x=np.linspace(0,r)
         
        y=(x*tan(o))-((9.8*x*x)/(2*u*u*cos(o)*cos(o)))
     
        plt.plot(x,y)
        plt.title("Trajectory of Body")
        plt.xlabel("Distance Travelled in metres")
        plt.ylabel("Height in metres")
        plt.grid(True)

        plt.scatter(X,Y,label="Point")
        plt.legend()
        plt.show()

    if choice==5:
        print("\t\t\t\t\tTHANK YOU")
        print("=========================================================================\n")
        break


        
