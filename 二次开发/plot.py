import matplotlib.pyplot as plt
import io


def plot(xlist, ylist):
    xlist = '0,1,2,3'
    ylist = '0,1,2,3'
    xlist = [float(i) for i in xlist.split(',')]
    ylist = [float(i) for i in ylist.split(',')]
    plt.plot(xlist, ylist)

    # plt.show()
    buffer = io.BytesIO()
    plt.savefig('temp.png')
    plt.close()


if __name__ == '__main__':
    xlist = '0,1,2,3'
    ylist = '0,1,2,3'
    plot(xlist, ylist)