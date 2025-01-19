import matplotlib.pyplot as plt
import numpy as np
import io
from collections import Counter
from matplotlib.ticker import FuncFormatter
import pandas as pd

csv = ""
def setcsv(inputcsv: str) -> str: 
    global csv
    csv = inputcsv

def calculateMean(colName: str) -> float:
    data = getColumnFromCSV(csv, colName)
    return sum(data)/len(data)

# def calculateMedian(data: list) -> float:
#     data.sort()
#     if len(data) % 2 == 0:
#         return (data[len(data)//2] + data[len(data)//2-1])/2
#     else:
#         return data[len(data)//2]

def calculateMode(data: list) -> float:
    mode = max(set(data), key = data.count)
    return mode

def calculateVariance(data: list) -> float:
    mean = calculateMean(data)
    return sum((x-mean)**2 for x in data)/len(data)

def calculateStandardDeviation(data: list) -> float:
    return calculateVariance(data)**0.5

# likely delete lol
def graphDisplay (data: list) -> str:
    data.sort()
    plt.hist(data, bins = 10, color = 'blue', edgecolor = 'black')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.show()
    return 'Graph displayed'

def histoToImage(data: list, xaxis: str, yaxis: str, title: str, density: bool=False, normal_dist: bool=False, histobin: int=10) -> bytes:
    def format_yaxis(y, _):
        if density:
            return y
        else:
            if int(y) == y:
                return str(int(y))
            return ''
    
    plt.clf()  # Clear any existing plots
    data.sort()
    plt.hist(data, bins = histobin, color = (33/255, 127/255, 85/255), edgecolor = '#7ed3aa', density = density)
    
    if normal_dist:
        mean = calculateMean(data)
        std_dev = calculateStandardDeviation(data)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = np.exp(-0.5*((x - mean) / std_dev)**2) / (std_dev * np.sqrt(2 * np.pi))
        plt.plot(x, p, color='#d62728', linewidth=2)
    
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_yaxis))
    fig = plt.gcf()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Clean up the plot
    return buf.getvalue()

def piechartToImage(data: dict, title: str) -> bytes:
    plt.clf()  # Clear any existing plots
    labels = data.keys()
    sizes = data.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    fig = plt.gcf()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Clean up the plot
    return buf.getvalue()

def scatterplotToImage(xdata: list, ydata: list, xaxis: str, yaxis: str, title: str, line_of_best_fit: bool=False) -> bytes:
    plt.clf()  # Clear any existing plots
    plt.scatter(xdata, ydata, color='#1f77b4')
    
    if line_of_best_fit:
        # Calculate line of best fit
        m, b = np.polyfit(xdata, ydata, 1)
        plt.plot(xdata, [m*x + b for x in xdata], color='#7ed3aa')
    
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    fig = plt.gcf()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Clean up the plot
    return buf.getvalue()

def bargraphToImage(data: dict, xaxis: str, yaxis: str, title: str) -> bytes:
    plt.clf()  # Clear any existing plots
    labels = data.keys()
    values = data.values()
    plt.bar(labels, values, color=(33/255, 127/255, 85/255))
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    fig = plt.gcf()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Clean up the plot
    return buf.getvalue()

def plotgraphToImage(xdata: list, ydata: list, xaxis: str, yaxis: str, title: str, show_points: bool=False) -> bytes:
    plt.clf()  # Clear any existing plots
    plt.plot(xdata, ydata, color=(33/255, 127/255, 85/255))
    
    if show_points:
        plt.scatter(xdata, ydata, color='red')  # Add points on the graph
    
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    fig = plt.gcf()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Clean up the plot
    return buf.getvalue()

def modedecimalplaces(data: list) -> int:
    def countdecimalplaces(number: float) -> int:
        if '.' in str(number):
            return len(str(number).split('.')[1])
        else:
            return 0

    decimalplaces = [countdecimalplaces(number) for number in data]
        
    modedecimal = Counter(decimalplaces).most_common(1)[0][0]
    return modedecimal

def getFirstColumnFromCSV(csv_string: str) -> list:
    cleaned_csv_string = csv_string.rstrip(',')  # Remove trailing comma
    df = pd.read_csv(io.StringIO(cleaned_csv_string.replace('\\n', '\n')))
    return [float(x) if isinstance(x, (np.integer, np.floating)) else x for x in df[df.columns[0]].tolist()]


def getFirstRowFromCSV(csv_string: str) -> list:
    cleaned_csv_string = csv_string.rstrip(",")  # Remove trailing comma
    df = pd.read_csv(io.StringIO(cleaned_csv_string.replace("\\n", "\n")))
    return df.columns.tolist()


def getColumnFromCSV(csv_string: str, col_name: str) -> list:
    cleaned_csv_string = csv_string.rstrip(',')  # Remove trailing comma
    df = pd.read_csv(io.StringIO(cleaned_csv_string.replace('\\n', '\n')))
    if col_name in df.columns:
        return [float(x) if isinstance(x, (np.integer, np.floating)) else x for x in df[col_name].tolist()]
    else:
        raise ValueError(f"Column '{col_name}' not found in CSV")

def getRowFromCSV(csv_string: str, row_name: str) -> list:
    cleaned_csv_string = csv_string.rstrip(',')  # Remove trailing comma
    df = pd.read_csv(io.StringIO(cleaned_csv_string.replace('\\n', '\n')), index_col=0)
    if row_name in df.index:
        return [float(x) if isinstance(x, (np.integer, np.floating)) else x for x in df.loc[row_name].tolist()]
    else:
        raise ValueError(f"Row '{row_name}' not found in CSV")




# def countMatchAmount (data: list, match) -> int:
#     for x in data:
#         if x == match:
#             count += 1
#     return count

def organizeDataCount(data: list) -> dict:
    return dict(Counter(data))
