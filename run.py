f=open('script2',"w")
#pyramid 1
f.write("push\n")
f.write("rotate\n")
f.write("x 15\n")
f.write("rotate\n")
f.write("y 60\n")
f.write("move\n")
f.write("240 150 0\n")
f.write("box\n")
f.write("0 0 0 10 10 10\n")
for i in range(1,10):
    f.write("move\n")
    f.write("-5 -10 5\n")
    f.write("box\n")
    f.write("0 0 0 "+str(10+i*10)+ " 10 "+str(10+i*10)+"\n")
f.write("pop\n")
#pyramid 2
f.write("push\n")
f.write("rotate\n")
f.write("x 15\n")
f.write("rotate\n")
f.write("y 60\n")
f.write("move\n")
f.write("400 250 0\n")
f.write("box\n")
f.write("0 0 0 10 10 10\n")
for i in range(1,20):
    f.write("move\n")
    f.write("-5 -10 5\n")
    f.write("box\n")
    f.write("0 0 0 "+str(10+i*10)+ " 10 "+str(10+i*10)+"\n")
f.write("pop\n")
#pyramid 3
f.write("push\n")
f.write("rotate\n")
f.write("x 15\n")
f.write("rotate\n")
f.write("y 60\n")
f.write("move\n")
f.write("600 200 0\n")
f.write("box\n")
f.write("0 0 0 10 10 10\n")
for i in range(1,15):
    f.write("move\n")
    f.write("-5 -10 5\n")
    f.write("box\n")
    f.write("0 0 0 "+str(10+i*10)+ " 10 "+str(10+i*10)+"\n")
f.write("pop\n")
#sun
f.write("push\n")
f.write("move\n")
f.write("425 425 0\n")
f.write("sphere\n")
f.write("0 0 0 50\n")
f.write("pop")
f.write("display\n")
f.write("save\n")
f.write("pyramid.png\n")
f.close()
