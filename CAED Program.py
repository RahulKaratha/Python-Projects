import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
#PYTHON PROGRAM TO CONSTRUCT PROJECTION OF POINTS

print("\t\tPYTHON PROGRAM TO CONSTRUCT PROJECTION OF POINTS")
print("\t\t================================================")
while True:
        
    point=input("\nEnter point:")
    point=point.lower()
    print("\n==========================================================")
    print("\n\n\tHorizontal Plane")
    print("\t----------------\n")

    dist1=int(input("Enter Distance (in mm):"))
    orient1=input("Above(A) or Below(B):")

    print("\n==========================================================")

    print("\n\n\tVertical Plane")
    print("\t---------------\n")

    dist2=int(input("Enter Distance (in mm):"))
    orient2=input("Infront(I) or Behind(B):")



    def mark(y=70,tickf=10):
        ax.set_xlim(0,20)     
        if y<20:
            ax.set_ylim(-y-10,y+10)
        else:                                     #Sets the limits of the graph
            ax.set_ylim(-y-30,y+30)

        plt.grid(True)

        ax.spines["bottom"].set_position("zero")                   #Sets axis to origin
        ax.spines["left"].set_position("zero")

        ax.spines["top"].set_visible(False)                        #Removes axes
        ax.spines["right"].set_visible(False)

        func=lambda x, pos: "" if np.isclose(x,0)  else int(x)      #Gets rid of xeros in origin

    #  ax.xaxis.set_major_formatter(ticker.FuncFormatter(func))    
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(func))

    #   ax.xaxis.set_major_locator(ticker.MultipleLocator(10))       #Gives tick of 1 interval
        ax.yaxis.set_major_locator(ticker.MultipleLocator(tickf)) 
        
        plt.xticks([])

        plt.title("All dimensions in mm")
        plt.text(17,3,"HP")
        plt.text(17,-7,"VP")
    if orient1 in "Aa" and orient2 in "Ii":   #First Quadrant
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)


        x=[10,10]
        y=[dist1,-dist2]
        plt.plot(x,y)
        plt.scatter(10,dist1,color="black")
        plt.text(10,dist1+5,point+"'",fontsize=20)
        plt.scatter(10,-dist2,color="gray")
        plt.text(10,-dist2-5,point,fontsize=20,color="gray")

        if (dist1%10!=0 or dist2%10!=0) and (dist1%5==0 or dist2%5==0):
            mark(max([dist1,dist2]),5)
        elif dist1%5!=0 or dist2%5!=0:
            mark(max([dist1,dist2]),1)
        else:
            mark(max([dist1,dist2]))
        plt.show()

    if orient1 in "Aa" and orient2 in "Bb":   #Second Quadrant
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)

        x=[10,10,10,10]
        y=[0,dist1,0,dist2]
        plt.plot(x,y)
        plt.scatter(10,dist1,color="black")
        plt.text(10.25,dist1,point+"'",fontsize=15)
        plt.scatter(10,dist2,color="gray",label=point)
        plt.text(9.25,dist2-2.5,point,fontsize=15,color="gray")

        if (dist1%10!=0 or dist2%10!=0) and (dist1%5==0 or dist2%5==0):
            mark(max([dist1,dist2]),5)
        elif dist1%5!=0 or dist2%5!=0:
            mark(max([dist1,dist2]),1)
        else:
            mark(max([dist1,dist2]))
        plt.show()

    if orient1 in "Bb" and orient2 in "Bb":   #Third Quadrant

        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        
        x=[10,10]
        y=[-dist1,dist2]
        plt.plot(x,y)

        plt.scatter(10,-dist1,color="black",)
        plt.text(10,-dist1-5,point+"'",fontsize=20)    
        plt.scatter(10,dist2,color="gray",label=point)
        plt.text(10,dist2+5,point,fontsize=20,color="gray")
    

        if (dist1%10!=0 or dist2%10!=0) and (dist1%5==0 or dist2%5==0):
            mark(max([dist1,dist2]),5)
        elif dist1%5!=0 or dist2%5!=0:
            mark(max([dist1,dist2]),1)
        else:
            mark(max([dist1,dist2]))

        plt.show()

    if orient1 in "Bb" and orient2 in "Ii":   #Fourth Quadrant
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)    
        
        
        
        x=[10,10,10,10]
        y=[0,-dist1,0,-dist2]
        plt.plot(x,y)
        plt.scatter(10,-dist1,color="black")
        plt.text(10.25,-dist1,point+"'",fontsize=15)
        plt.text(9.25,-dist2-2.5,point,fontsize=15,color="gray")
        plt.scatter(10,-dist2,color="gray")
    

        if (dist1%10!=0 or dist2%10!=0) and (dist1%5==0 or dist2%5==0):
            mark(max([dist1,dist2]),5)
        elif dist1%5!=0 or dist2%5!=0:
            mark(max([dist1,dist2]),1)
        else:
            mark(max([dist1,dist2]))
    
        plt.show()    

    print("\n\nType anything to continue plotting")
    choice=input("Press enter to exit:")

    if choice=="":
        break

