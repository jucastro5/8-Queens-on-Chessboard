import numpy as np
import matplotlib.pyplot as plt

def buffon(iterations = 100, noprint=False):
    if noprint==False: print("\ntossin' {} needles....".format(iterations))
    #how long the needle is. .5 is half the length between the floorboards.
    #setting it to 1 (or length between floorboards) results in pi/2.
    r = .5
    accuracy=.0001
    x = []
    y = []
    x2 = []
    y2 = []
    position = 0
    count = 0
    #visualsing the lines on the floor
    xlines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #plotting configuration
    test = plt.figure(figsize=(20,20))
    t1 = test.add_subplot(2,2,1)
    t2 = test.add_subplot(2,1,2)
    plt.subplots_adjust(wspace=.2, hspace=.2)
    t2.set_xlim([0, iterations])
    t2.set_ylim([np.pi-1, np.pi+1])
    t2.set_title('\u03C0 Estimate Over {} Iterations (\u03C0 = Red Line)'.format(iterations))
    t1.set_xlim([-.2,10.2])
    t1.set_ylim([0,10])
    t1.set_title('The Floor with {} needles'.format(iterations))
    #drawing vertical floorboards
    for lines in xlines:
        t1.axvline(color='green', alpha=.4, x=lines)
    #pi reference line
    t2.axhline(y=np.pi, color='r', linestyle='-')
    #create x/y coordinates for points
    for i in range(1, iterations+1):
        pointx = (np.random.choice(np.arange(1, 9, accuracy)))
        pointy= (np.random.choice(np.arange(1, 9, accuracy)))
        theta = np.random.choice(np.arange(0, 2*np.pi+accuracy, accuracy))
        x.append(pointx)
        y.append(pointy)
        x.append(pointx + (r * np.cos(theta)))
        y.append(pointy + (r * np.sin(theta)))
    #selecting x,y pairs for plotting needle visualization
    for i in range(0, len(x)-1, 2):
        #checking if lines cross (x values change)
        if str((x[i+1]))[0] != str((x[i]))[0]:
            t1.plot(x[i:i+2], y[i:i+2], color='red', linewidth=.5)
            count+=1
            #collecting data for secondary (cot) graph
            position += 1
            x2.append(position)
            y2.append(position/count)
        #colors needle blue if it did not cross
        else:
            t1.plot(x[i:i+2], y[i:i+2], color='blue', linewidth=.5)
            position += 1
            #collecting data for secondary (cot) graph
            if count != 0:
                y2.append(position/count)
                x2.append(position)
            else:
                x2.append(0)
                y2.append(0)
    #plot secondary (cot) graph
    t2.plot(x2, y2)
    plt.savefig('n={}_buffon.png'.format(iterations))
    #info print out
    if count > 1 and noprint==False:
        print('_____________________________________________\n')
        print('Needles dropped: {0}'.format(iterations))
        print('Needles that crossed: {0}'.format(count))
        print('\u03C0 estimation (total needles/needles crossed):\n{0}'.format(iterations/count))
        print('Graph saved in local directory')
        print('_____________________________________________')

x = int(input('num iterations? '))
buffon(x)
