def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)


def sq(x):
    """
    output: sq returns the square of its input
    input x: a number (int or float)
    """
    return x*x
print 'sq(4) is', sq(4)


def interp (low,high,frac):
    """
    output: interp returns the fraction between low and high
    input low: a lower number
    input high: a higher number
    input frac: a fraction
    """
    return frac*(high-low)+low
print 'interp(2,8,.5) is', interp(2,8,.5)

def checkends(s):
    if s[0]==s[-1]:
        return True
    else:
        return False

print checkends('hannah')

print checkends(' ')



def convertFromSeconds( s ):
    days = s/(24*60*60)
    s = s%(24*60*60)
    hours = s/(60*60)
    s = s % (60*60)
    minutes = s/60

    seconds = s%60
    return [days, hours, minutes, seconds]

dhms = convertFromSeconds(200000)
print dhms

def flipside(word):
    length=len(word)
    return word[length/2:]+word[:length/2]

print flipside("carpets")



def front3(s):
    return s[:3]*3

#print s(1,2,3,4,5,6)


