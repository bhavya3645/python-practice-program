def introduction():
    global Name
    global cls
    global fname
    global rlnum
    Name = str(input('enter your name='))
    cls = int(input('ENTER YOUR CLASS='))
    fname = str(input('ENTER YOUR FATHER NAME='))
    rlnum = int(input('ENTER YOUR ROLLNUMBER='))
def subjects():
    global science
    global mathamatics
    global eglish
    global hindi
    global sscience
    science = int(input('ENTER YOUR SCIENCE MARKS------='))
    mathamatics = int(input('enter markes of MATHEMATICS='))
    english = int(input('enter markes of ENGLISH--------='))
    hindi = int(input('enter markes of HINDI------------='))
    sscience = int(input('enter markes of SOCIAL SCIENCE='))
def percentage():
    global tot
    global per
    tot=(science+mathamatics+english+hindi+sscience)
    per=(tot/5)
def condition():
    if per>=80:
        print('A grade')
    elif per<=79:
        print('B grade')
print("Name Of Student is --------=", Name)
print("Class Of Student is---------=", cls)
print("Father Name Of Student Is =", fname)
print("RollNumber Of Student Is -=", rlnum)
print("*********obtained markes**********")
print("The Marks Obtained In science=", science)
print("The Marks Obtained In mathamatics=", mathamatics)
print("The Marks Obtained In ENGLISH----=", english)
print("The Marks Obtained In Hindi=", hindi)
print("The Marks Obtained In Social Science=", sscience)
print("***********percentage************")
print("Obtained total markes is = ", tot)
print('percentage=', per)
introduction()
subjects()
percentage()
condition()
