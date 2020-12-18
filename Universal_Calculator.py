m = 1
while m == 1:
  def xmf():
    a = int(input('Mean that it is supposed to be: '))
    b = [int(x) for x in input("All dataset y values seperated by spaces: ").split()]
    c = int(input('Number of numbers in dataset: '))
    d = a * c
    e = sum(b)
    f = d - e
    print('Other number:', f)
  def RES():
    xval = [int(x) for x in input("All dataset x values seperated by spaces: ").split()]
    yval = [int(x) for x in input("All dataset y values seperated by spaces: ").split()]
    leqy = float(input('"Line of best fit" Y-Intercept: '))
    o = float(input('Slope: '))
    m = -1
    for i in xval:
        b = []
        n = 0
        l = 0
        n = i * o
        l = n + leqy
        m += 1
        k = yval[m] - l
        print(k)
  def LEQ():
    from fractions import Fraction
    xone = float(input('X1: '))
    yone = float(input('Y1: '))
    xtwo = float(input('X2: '))
    ytwo = float(input('Y2: '))
    WHAT = input('Domain (d), Range (r) or Equasion (e)? ')
    def Y():
      Y = ytwo-yone
      X = xtwo-xone
      #(-17,-19)
      #(-17,-25)
      PIE = Y/X
      y = yone
      WE = xone*PIE
      WWEE = y-WE
      print('y=',PIE,'x+',WWEE)
    def R():
      print('(',yone,'< X >',ytwo,')')
    def D():
      print('(',xone,'< X >',xtwo,')')
    if WHAT == str('d'):
      D()
    if WHAT == str('r'):
      R()
    if WHAT == str('e'):
      Y()
  def MODE():
    # Python program to print 
    # mode of elements 
    from collections import Counter 
  
    # list of elements to calculate mode 
    n_num = [float(x) for x in input("All dataset numbers seperated by spaces: ").split()]
    n = len(n_num) 
  
    data = Counter(n_num) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
    if len(mode) == n: 
        get_mode = "No mode found"
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
    print(get_mode)
    print('                                               ')
  def MED():
    DSin = [float(x) for x in input("All dataset numbers seperated by spaces: ").split()]
    DSin.sort()
    c = len(DSin)
    if c % 2 == 0:
      d = c / 2
      e = d - 1
      f = DSin[int(d)]
      g = DSin[int(e)]
      h = g + f
      j = h / 2
      print(j)
    else:
      d = c / 2
      print(DSin[int(d)])
    print('                                               ')
  def RANGE():
    DSin = [float(x) for x in input("All dataset numbers seperated by spaces: ").split()]
    DSin.sort()
    print('Lowest number:', DSin[0])
    print('Highest number:', DSin[-1])
    print('Range:', DSin[-1] - DSin[0])
    print('                                               ')
  def MEAN():
    DSin = [float(x) for x in input("All dataset numbers seperated by spaces: ").split()]
    DSin.sort()
    c = len(DSin)
    d = 0
    for i in DSin:
      d += i
    b = d / c
    print('Mean:', b)
    print('                                               ')
  def STDEV():
    import math
    k = []
    p = 0
    m = []
    c = 0
    DSin = [float(x) for x in input("All dataset numbers seperated by spaces: ").split()]
    DSin.sort()
    c = len(DSin)
    d = 0
    for i in DSin:
      d += i
    b = d / c
    for i in DSin:
      p = 0
      p = b - i
      s = abs(p)
      k.append(s)
    l = 0
    o = 0
    for i in k:
      l = i
      o = l * l
      m.append(o)
    u = 0
    for i in m:
      u += i
    t = u / d
    r = math.sqrt(t)
    print('Standard Deviation:', r)
    print('                                                 ')

    #Quadratics:

  def qc():
    choose = input('End (end), Standard to Vertex (stv), Vertex finder from a,b,c (vf), Quadratic Formula (x-intercepts) (qf): ')
    def vf(): #Vertex Finder
        a = float(input('a value: '))
        b = float(input('b value: '))
        c = float(input('c value: '))
        x = -b / (a * 2)
        y = a * (x * x) + b * x + c
        print('Vertex: ({},{})'.format(x,y))

    def stv(): #Standard To Vertex
         neg = 0
         a = float(input('a value: '))
         b = float(input('b value: '))
         c = float(input('c value: '))
         h = -b / (a * 2)
         k = a * (h * h) + b * h + c
         if h < 0:
             neg = 1
         else:
             neg = 0
         if a == 1:
             if neg == 1:
                 h = abs(h)
                 print('(x + {}) ^ 2 + {}'.format(h,k))
             else:
                 print('(x - {}) ^ 2 + {}'.format(h,k))
         else:
             if neg == 1:
                 h = abs(h)
                 print('{}(x + {}) ^ 2 + {}'.format(a,h,k))
             else:
                 print('{}(x - {}) ^ 2 + {}'.format(a,h,k))

    def vts(): #Vertex To Standard
        a = float(input('a value: '))
        h = float(input('h value: '))
        k = float(input('k value: '))
        b = h*(a*2)
        #c = a*h**2+k
        c = a*h**2+k
        print('b = {} c = {}'.format(b,c))

    def qf(): #Quadradic Fromula (x-intercepts)
        a = float(input('a value: '))
        b = float(input('b value: '))
        c = float(input('c value: '))
        e = (b**2) - (4*a*c)
        if e < 0:
            #e = (b**2) + (4*a*c)
            print('There are no x-intercepts')
            return
        f = ((-b)+math.sqrt(e))/(2*a)
        g = ((-b)-math.sqrt(e))/(2*a)
        print(f)
        print(g)

    if choose == 'end':
            go = 0
    if choose == 'stv':
            stv()
    if choose == 'vf':
            vf()
    if choose == 'qf':
            qf()
    if choose == 'vts':
            vts()

  pie = input('Mean (m), Standard Deviation (sd), Range (r), Median (med), Mode (md), Linear Equasion (leq), Residuals (res), Mean missing number finder (xmf), Quadratic calculator (qc), end: ')
  if pie == 'sd':
    STDEV()
  if pie == 'm':
    MEAN()
  if pie == 'r':
    RANGE()
  if pie == 'med':
    MED()
  if pie == 'md':
    MODE()
  if pie == 'end':
    m = 0
  if pie == 'leq':
    LEQ()
  if pie == 'res':
    RES()
  if pie == 'xmf':
    xmf()
  if pie == 'qc':
    qc()