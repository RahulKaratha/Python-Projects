

def matrix():
    print("\n\n==============================================================================")
    print("\t\tMATRIX FORMATION")
    print(2*"=======================================")
    m=int(input("\nEnter number of rows(m):"))
    n=int(input("\nEnter number of columns(n):"))

    matrix=[]
    print("\n")
    for i in range(1,m+1):
        rows=[]
        print(2*"=======================================")
        for j in range(1,n+1):
            ele=int(input("Enter element a["+str(i)+" "+str(j)+"]:"))
            rows.append(ele)
        matrix.append(rows)
    print("\n\n")
    print(2*"========================================")
    print("\t\t\t\tMATRIX")
    print(2*"========================================")

    for rows in matrix:
       print("\t\t\t\n")
       for ele in rows:
         print("\t\t",ele,end=" ")
    print("\n================================================================================")
    return matrix


def matrixadd():

    print("\t\t\t\tMATRIX ADDITION")
    print("================================================================================")

    A=eval(input("\nEnter First Matrix:"))
    B=eval(input("Enter Second Matrix:"))
    print("\n\n")
    print("\t\t\t\tA + B")
    
    result=[]
    for i in range(0,3):
        rows=[]
        for j in range(0,3):
            a=A[i][j]+B[i][j]
            rows.append(a)
        result.append(rows)
    
    print("\n\n================================================================================")
    print("\t\t\t\tRESULT")
    print("\t\t\t\t------")
    for rows in result:
       print("\t\t\t\n")
       for ele in rows:
         print("\t\t",ele,end=" ")
    print("\n\n================================================================================")

    return(result)


def matrixsub():

    print("\t\t\t\tMATRIX SUBTRACTION")
    print("================================================================================")

    A=eval(input("\nEnter First Matrix:"))
    B=eval(input("Enter Second Matrix:"))
    print("\n\n")
    print("\t\t\t\tA - B")
    
    result=[]
    for i in range(0,3):
        rows=[]
        for j in range(0,3):
            a=A[i][j]-B[i][j]
            rows.append(a)
        result.append(rows)
    
    print("\n\n================================================================================")
    print("\t\t\t\tRESULT")
    print("\t\t\t\t------")
    for rows in result:
       print("\t\t\t\n")
       for ele in rows:
         print("\t\t",ele,end=" ")
    print("\n\n================================================================================")

    return(result)

def matrixmult():
     
    print("\t\t\t\tMATRIX MULTIPLICATION")
    print("================================================================================")

    A=eval(input("\nEnter First Matrix:"))
    B=eval(input("Enter Second Matrix:"))
    print("\n\n")
    print("--------------------------------------------------------------------------------")
    print("\t\t\t\tA x B")
    print("--------------------------------------------------------------------------------")

    columns=len(A[0])
    rows=len(A)

   
    result=[]
    for i in range(0,rows):
        row1=[]
        row2=[]
        row3=[]
        for j in range(0,columns):
            for k in range(0,rows):       
                ele=A[i][j]*B[j][k]
                if k==0:
                    row1.append(ele)
                if k==1:
                    row2.append(ele)
                if k==2:
                    row3.append(ele)
        if row3==[]:
           result.append([sum(row1),sum(row2)])
        else:            
           result.append([sum(row1),sum(row2),sum(row3)])
            
            
       

    print("\n\n================================================================================")
    print("\t\t\t\tRESULT")
    print("\t\t\t\t------")
    for rows in result:
       print("\t\t\t\n")
       for ele in rows:
         print("\t\t",ele,end=" ")
    print("\n\n================================================================================")

    return(result)

def determinant():
      
    print("\t\t\t\tDETERMINANT")
    print("================================================================================")

    mat=eval(input("\nEnter Matrix:"))
    

    columns=len(mat[0])
    rows=len(mat)

    if columns!=rows:
        print("\n\n\t\t\t\tINVALID")

    else:
        if rows==2:
            det=(mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])
            print("\nDETERMINANT="+str(det))

        if rows==3:
            det=(mat[0][0]*((mat[1][1]*mat[2][2])-(mat[1][2]*mat[2][1])))-(mat[0][1]*((mat[1][0]*mat[2][2])-(mat[1][2]*mat[2][0])))+(mat[0][2]*((mat[1][0]*mat[2][1])-(mat[2][0]*mat[1][1])))
            print("\nDETERMINANT="+str(det))
    print("\n\n================================================================================")

def inverse():
    print("\t\t\t\tINVERSE")
    print("================================================================================")

    mat=eval(input("\nEnter Matrix:"))

    print("--------------------------------------------------------------------------------")

    columns=len(mat[0])
    rows=len(mat)

    if columns!=rows:
        print("\n\n\t\t\t\tINVALID")

    else:
        if rows==2:
            det=(mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])

            a=mat[0][0]
            b=mat[0][1]
            c=mat[1][0]
            d=mat[1][1]

            inv=[["1/",d,-b],[det,-c,a]]
            for rows in inv:
                print("\t\t\t\n")
                for ele in rows:
                     print("\t\t",ele,end=" ")
            
            print("\n\n================================================================================")

        if rows==3:
            a=(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
            b=-((mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0]))
            c=(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])

            d=-((mat[0][1]*mat[2][2]-mat[0][2]*mat[2][1]))
            e=(mat[0][0]*mat[2][2]-mat[0][2]*mat[2][0])
            f=-((mat[0][0]*mat[2][1]-mat[0][1]*mat[2][0]))

            p=(mat[0][1]*mat[1][2]-mat[0][2]*mat[1][1])
            q=-((mat[0][0]*mat[1][2]-mat[0][2]*mat[1][0]))
            r=(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])

            detr= det=(mat[0][0]*((mat[1][1]*mat[2][2])-(mat[1][2]*mat[2][1])))-(mat[0][1]*((mat[1][0]*mat[2][2])-(mat[1][2]*mat[2][0])))+(mat[0][2]*((mat[1][0]*mat[2][1])-(mat[2][0]*mat[1][1])))
            D="1/"+str(detr)
            inv=[["",a,d,p],[D,b,e,q],["",c,f,r]]

            for rows in inv:
               print("\t\t\t\n")
               for ele in rows:
                   print("\t\t",ele,end=" ")

            print("\n\n================================================================================") 


def adjoint():
    print("\t\t\t\tADJOINT")
    print("================================================================================")

    mat=eval(input("\nEnter Matrix:"))

    print("--------------------------------------------------------------------------------")

    columns=len(mat[0])
    rows=len(mat)

    if columns!=rows:
        print("\n\n\t\t\t\tINVALID")

    else:
         if rows==2:
            a=mat[0][0]
            b=mat[0][1]
            c=mat[1][0]
            d=mat[1][1]

            adj=[[d,-b],[-c,a]]
            for rows in adj:
                print("\t\t\t\n")
                for ele in rows:
                     print("\t\t",ele,end=" ")
            
            print("\n\n================================================================================")

         if rows==3:
            a=(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
            b=-((mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0]))
            c=(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])

            d=-((mat[0][1]*mat[2][2]-mat[0][2]*mat[2][1]))
            e=(mat[0][0]*mat[2][2]-mat[0][2]*mat[2][0])
            f=-((mat[0][0]*mat[2][1]-mat[0][1]*mat[2][0]))

            p=(mat[0][1]*mat[1][2]-mat[0][2]*mat[1][1])
            q=-((mat[0][0]*mat[1][2]-mat[0][2]*mat[1][0]))
            r=(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])

            
            adj=[[a,d,p],[b,e,q],[c,f,r]]

            for rows in adj:
               print("\t\t\t\n")
               for ele in rows:
                   print("\t\t",ele,end=" ")

            print("\n\n================================================================================")

def cofactor():
    print("\t\t\t\tMINORS AND COFACTORS ")
    print("================================================================================")

    mat=eval(input("\nEnter Matrix:"))

    print("--------------------------------------------------------------------------------")

    columns=len(mat[0])
    rows=len(mat)

    if columns!=rows:
        print("\n\n\t\t\t\tINVALID")

    else:
            a=(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
            b=((mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0]))
            c=(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])

            d=((mat[0][1]*mat[2][2]-mat[0][2]*mat[2][1]))
            e=(mat[0][0]*mat[2][2]-mat[0][2]*mat[2][0])
            f=((mat[0][0]*mat[2][1]-mat[0][1]*mat[2][0]))

            p=(mat[0][1]*mat[1][2]-mat[0][2]*mat[1][1])
            q=((mat[0][0]*mat[1][2]-mat[0][2]*mat[1][0]))
            r=(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])

            print("\t\t\t\t\tMINORS AND COFACTORS")
            print("--------------------------------------------------------------------------------\n")
            print("M11=",a)
            print("M12=",b)
            print("M13=",c)

            print("\nM21=",d)
            print("M22=",e)
            print("M23=",f)

            print("\nM31=",p)
            print("M32=",q)
            print("M33=",r)


            print("\n\n")
            print("A11=",a)
            print("A12=",-b)
            print("A13=",c)

            print("\nA21=",-d)
            print("A22=",e)
            print("A23=",-f)

            print("\nA31=",p)
            print("A32=",-q)
            print("A33=",r) 

            
            
            print("================================================================================")
           


def linear():
    
     
    print("\t\tSOLUTION FOR SYSTEM OF LINEAR EQUATIONS")
    print("================================================================================\n")

    A=input("Enter First Linear Equation:")
    B=input("Enter Second Linear Equation:")
    C=input("Enter Third Linear Equation:")

    coeff=[]
    V=[]

       

    for eq in [A,B,C]:
        if "x" in eq:
           p=eq.index("x")

        if "y" in eq:
            q=eq.index("y")

        if "z" in eq:
           r=eq.index("z")

           
        s=eq.index("=")
        D=eq[s+1::]

        A=B=C=0
        if "x" in eq:
            A=eq[:p:]

        if "x" in eq and "y" in eq:
            B=eq[p+1:q:]

        if "y" in eq and "x" not in eq:
            B=eq[:q:]

        if "y"  in eq and "z" in eq  :
            C=eq[q+1:r:]

        if "z" and "x" in eq and "y" not in eq:
            C=eq[p+1:r:]

        if A=="":
            A=1
        if A=="-":
            A=-1
        if B=="+" or B=="":
            B=1
        if B=="-":
            B=-1
        if C=="+":
            C=1
        if C=="-":
            C=-1

        coeff.append([int(A),int(B),int(C)])
        V.append([int(D)])
       


     
    a=(coeff[1][1]*coeff[2][2]-coeff[1][2]*coeff[2][1])
    b=-((coeff[1][0]*coeff[2][2]-coeff[1][2]*coeff[2][0]))
    c=(coeff[1][0]*coeff[2][1]-coeff[1][1]*coeff[2][0])

    d=-((coeff[0][1]*coeff[2][2]-coeff[0][2]*coeff[2][1]))
    e=(coeff[0][0]*coeff[2][2]-coeff[0][2]*coeff[2][0])
    f=-((coeff[0][0]*coeff[2][1]-coeff[0][1]*coeff[2][0]))

    p=(coeff[0][1]*coeff[1][2]-coeff[0][2]*coeff[1][1])
    q=-((coeff[0][0]*coeff[1][2]-coeff[0][2]*coeff[1][0]))
    r=(coeff[0][0]*coeff[1][1]-coeff[0][1]*coeff[1][0])

    detr= det=(coeff[0][0]*((coeff[1][1]*coeff[2][2])-(coeff[1][2]*coeff[2][1])))-(coeff[0][1]*((coeff[1][0]*coeff[2][2])-(coeff[1][2]*coeff[2][0])))+(coeff[0][2]*((coeff[1][0]*coeff[2][1])-(coeff[2][0]*coeff[1][1])))


    inv=[[a,d,p],[b,e,q],[c,f,r]]

    print("\n\n--------------------------------------------------------------------------------")
    print("\t\t\t\tSOLUTION")
    print("--------------------------------------------------------------------------------")

    for i in range(0,3):
        row1=[]
        for j in range(0,3):
            for k in range(0,1):       
                ele=inv[i][j]*V[j][k]
                if k==0:
                   row1.append(ele)

        if i==0:
            print("X=",sum(row1)/detr)
        if i==1:
            print("Y=",sum(row1)/detr)
        if i==2:
            print("Z=",sum(row1)/detr)
    print("================================================================================")    

print("\t\t\tPython program for Matrix functions")
print("==============================================================================\n")


while True:
    print("\t\t\t\t\tMENU\n")
    print("==============================================================================\n")

    print("\t\t\t\t1.Matrix Creation")
    print("\t\t\t\t2.Matrix Addition")
    print("\t\t\t\t3.Matrix Subtraction")
    print("\t\t\t\t4.Matrix Multiplication")
    print("\t\t\t\t5.Determinant")
    print("\t\t\t\t6.Inverse Matrix")
    print("\t\t\t\t7.Adjoint Matrix")
    print("\t\t\t\t8.Co-Factors and Minors")
    print("\t\t\t\t9.System of Three Linear Equations")
    print("\t\t\t\t10.Exit\n")
    print("------------------------------------------------------------------------------")
    choice=int(input("\n\t\t\t\tWhat do you want to do?:"))
    print("\n==============================================================================\n")

    if choice==1:
       matrix()
    if choice==2:
       matrixadd()
    if choice==3:
       matrixsub()
    if choice==4:
       matrixmult()
    if choice==5:
       determinant()
    if choice==6:
       inverse()
    if choice==7:
       adjoint()
    if choice==8:
       cofactor()
    if choice==9:
       linear()
    if choice==10:
        print("\t\t\t\t\tTHANK YOU")
        print("\n==============================================================================\n")
        break




            
    
            

            
        
           
    

    
    
