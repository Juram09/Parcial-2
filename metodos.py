import math
# 1. Integral entre 2 y 4 de sin(2x)e^-x dx
# 2. Integral entre 0 y 5 de cos(x^4) dx

def primerPunto():
    print("---Primer punto---")
    x=[2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
    xmed=[2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3, 3.5, 3.7, 3.9]
    fx=[]
    fxmed=[]
    pmedio=0
    fxtrap=[]
    ptrap=0
    fxsimp=[]
    psimp=0
    h=0.2

    for i in range (0,10):
        fxmed.append(math.sin(2*xmed[i])*math.exp(-xmed[i]))
    for i in x:
        fx.append(math.sin(2*i)*math.exp(-i))

    for i in range(0,11):
        if i==0 or i==10:
            fxtrap.append(fx[i])
            fxsimp.append(fx[i])
        else:
            if(i%2==1):
                fxsimp.append(fx[i]*2)
            else:
                fxsimp.append(fx[i]*4)
            fxtrap.append(fx[i]*2)

    for i in fxmed:
        pmedio+=i
    for i in fxtrap:
        ptrap+=i
    for i in fxsimp:
        psimp+=i
    pmedio*=h
    ptrap*=h/2
    psimp*=h/3  
    print("Punto medio: ", pmedio)
    print("Trapecio: ", ptrap)
    print("Simpson 1/3: ",psimp)

def segundoPunto():
    print("---Segundo punto---")
    xmed=[]
    fxmed=[]
    hmed=1/6
    pmedio=0
    xtrap=[]
    fxtrap=[]
    fxfxtrap=[]
    htrap=1/4
    ptrap=0
    xsimp=[]
    fxsimp=[]
    fxfxsimp=[]
    hsimp=1/2   
    psimp=0
    
    for i in range (0,30):
        xmed.append(((0+(1/6)*i)+(0+(1/6)*(i+1)))/2)
    for i in range(0,21):
        xtrap.append(0+(1/4)*i)
    for i in range(0,11):
        xsimp.append(0+(1/2)*i)
        
    for i in xmed:
        fxmed.append(math.cos(i**4))
    for i in xtrap:
        fxtrap.append(math.cos(i**4))
    for i in xsimp:
        fxsimp.append(math.cos(i**4))
    for i in range(0,21):
        if i==0:
            fxfxtrap.append(fxtrap[i])
            fxfxsimp.append(fxsimp[i])
        elif i==20:
            fxfxtrap.append(fxtrap[i])
        elif i==10:
            fxfxsimp.append(fxsimp[i])
        else:
            fxfxtrap.append(fxtrap[i]*2)
            if(i<11):
                if(i%2==1):
                    fxfxsimp.append(fxsimp[i]*2)
                else:
                    fxfxsimp.append(fxsimp[i]*4)
                
    for i in fxmed:
        pmedio+=i
    for i in fxfxtrap:
        ptrap+=i
    for i in fxfxsimp:
        psimp+=i
    pmedio*=hmed
    ptrap*=htrap/2
    psimp*=hsimp/3

    print("Punto medio: ", pmedio)
    print("Trapecio: ", ptrap)
    print("Simpson 1/3: ",psimp)

primerPunto()
segundoPunto()