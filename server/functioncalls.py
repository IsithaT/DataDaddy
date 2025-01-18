def calculateMean(data: list) -> float:
    return sum(data)/len(data)

def calculateMedian(data: list) -> float:
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data)//2] + data[len(data)//2-1])/2
    else:
        return data[len(data)//2]

def calculateMode(data: list) -> float:
    mode = max(set(data), key = data.count)
    return mode

def calculateVariance(data: list) -> float:
    mean = calculateMean(data)
    return sum((x-mean)**2 for x in data)/len(data)

def calculateStandardDeviation(data: list) -> float:
    return calculateVariance(data)**0.5

def graphDisplay (data: list) -> str:
    data.sort()
    plt.hist(data, bins = 10, color = 'blue', edgecolor = 'black')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.show()
    return 'Graph displayed'

def graphToImage(data: list) -> image:
    data.sort()
    plt.hist(data, bins = 10, color = 'blue', edgecolor = 'black')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    fig = plt.gcf()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    img = Image.open(buf)
    return img