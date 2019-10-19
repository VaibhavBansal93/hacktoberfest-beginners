import numpy as np
import math
from matplotlib import pyplot as plt
import pylab
infant = 1
young = 15
adult = 25
senior = 35
old = 55

def triangular(a,b,c,x):
    if x<=a:
        return 0
    elif x>a and x<=b:
        return (x-a)/(b-a)
    elif x>b and x<c:
        return (c-x)/(c-b)
    return 0

def membership_infant(age):
    return triangular(0,infant,2,age)

def membership_young(age):
    return triangular(10,15,20,age)

def membership_adult(age):
    return triangular(18,25,30,age)

def membership_senior(age):
    return triangular(30,35,55,age)

def membership_old(age):
    return triangular(50,55,80,age)

def main():    
    #ages = np.array( [int(x) for x in input('Enter ages : ').split()] )
    ages = np.arange(1,70,1)
    infants = np.array( [membership_infant(x) for x in ages])
    youngs = np.array( [membership_young(x) for x in ages])
    seniors = np.array( [membership_adult(x) for x in ages])
    adults = np.array( [membership_senior(x) for x in ages])
    olds = np.array( [membership_old(x) for x in ages])

    plt.xlabel('Ages')
    plt.ylabel('MembershiP values')
    pylab.plot(ages,infants,'b',label='Infant')
    pylab.plot(ages,youngs,'g',label='Young')
    pylab.plot(ages,adults,'r',label='Adult')
    pylab.plot(ages,seniors,'c',label='Senior')
    pylab.plot(ages,olds,'m',label='Old')
    pylab.legend(loc='upper left')
    pylab.show()
    
main()    