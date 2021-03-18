print("consider eqn like ax+by+cx=d ")
a1,b1,c1,d1=[ int(x) for x in input("coeff of exp1: ").split()]
a2,b2,c2,d2=[ int(x) for x in input("coeff of exp2: ").split()]
a3,b3,c3,d3=[ int(x) for x in input("coeff of exp3: ").split()]
iterations=int(input("number of iterations: "))

def process(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3):
    x=0
    y=0
    z=0
    for i in range(interations):
        x=(1/a1)*(d1-b1*y-c1*z)
        y=(1/b2)*(d2-a2*x-c2*z)
        z=(1/c3)*(d3 -a3*x-b3*y)
        print("iteraton  "+str(i+1))
        print("x = "+str(x))
        print("y = "+str(y))
        print("z = "+str(z)+"\n\n")

process(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3)
