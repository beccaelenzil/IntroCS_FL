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

print checkends('1,2,3,4,5')

print checkends(' ')


def flipside(word):
    length=len(word)
    if length%2==0:
        return word[length/2]+word[:length/2]
    else:
