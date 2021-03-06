import numpy as np
import re
import sys
import operator
import matplotlib.pyplot as plt

def parse_transposes(fn):
    size = re.compile('(\d+) x (\d+)')
    tp = re.compile('Throughput: ([\d\.]+) GB')
    sizes = []
    tps = []
    with open(fn, 'r') as f:
        for l in f:
            s = size.search(l)
            if s:
                sizes.append((int(s.group(1)), int(s.group(2))))
            else:
                t = tp.search(l)
                if t:
                    tps.append(float(t.group(1)))
    return sizes, tps

def top_n(kv, n=5):
    return sorted(kv, reverse=True, key=operator.itemgetter(0))[:n]

if __name__ == '__main__':
    sizes, tps = parse_transposes(sys.argv[1])
    np.savez(sys.argv[1], sizes=sizes, tps=tps) 
    print("Median throughput: %s GB/s" % np.median(tps))
    print("Max throughputs:")
    for tp, size in top_n(zip(tps, sizes)):
        print("  %s GB/s, at dimension %s" % (tp, size))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    n, bins, patches = ax.hist(tps, 50, label=sys.argv[1])
    ax.set_xlabel('GB/s')
    ax.set_title("Skinny Matrix Transpose Throughput")
    ax.legend()
    plt.show()
