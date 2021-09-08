import os.path
import matplotlib.pyplot as plt
import numpy as np
import sys


def analyse(inputCsvFile):
    # = 'C:\\Users\\id922927\\Documents\\innovation\\echo udp pl1040 np100000 Nokia.csv'

    with open(inputCsvFile) as file_name:
        data = np.loadtxt(file_name, delimiter=",")

    latency = data[:, 2]
    jitter = data[:, 3]

    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))
    fig.subplots_adjust(hspace=0.8)

    t = np.arange(1, len(latency)+1)
    colormat = np.where(latency > 22, 'r', 'g')
    axs[0].bar(t, latency, color=colormat)

    axs[0].set_title(os.path.basename(inputCsvFile))
    axs[0].set_ylabel('Response time (ms)')
    axs[0].set_xlabel('Packet count')

    counts, bins = np.histogram(jitter)
    axs[1].hist(jitter, 100)
    axs[1].set_title("Jitter Histogram")
    axs[1].set_xlabel('latency (ms)')
    axs[1].set_ylabel('Packet count')

    axs[2].violinplot(latency)
    axs[2].set_title("Latency Violin Diagram")
    axs[2].set_xlabel('')
    axs[2].set_ylabel('latency (ms)')

    text = 'Packet statistics:\n'
    text += 'Max latency %.2f   ' % np.amax(latency)
    text += 'Min latency %.2f   ' % np.amin(latency)
    text += 'Average latency %.2f\n' % np.average(latency)
    text += 'Max jitter %.2f   ' % np.amax(jitter)
    text += 'Min jitter %.2f   ' % np.amin(jitter)
    text += 'Average jitter %.2f\n' % np.average(jitter)
    plt.figtext(0, 0, text, verticalalignment='bottom')

    plt.show()


def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)
    if(len(sys.argv) >= 2):
        analyse(sys.argv[1])


if __name__ == '__main__':
    main()
