import sys
import matplotlib.pyplot as plt
import numpy as np

def getTurData(input_file):
    data = []
    input_file.readline()
    for line in input_file:
        data.append(float(line.strip("\n")))
    data.sort()
    return data

def getData(input_file):
    data = {}
    input_file.readline()

    for line in input_file:
        curr_data = line.split(',')
        dw = int(float(curr_data[0]))
        tur = float(curr_data[1])
        year = int(curr_data[2])
        julian = int(curr_data[3].strip("\n"))
        if year not in data:
            data[year] = {'domwave':[dw], 'turbidity':[tur], 'Julian':[julian]}
        else:
            data[year]['domwave'].append(dw)
            data[year]['turbidity'].append(tur)
            data[year]['Julian'].append(julian)

    return data

def getDataTO(input_file):
    input_file.readline()
    tur = []
    ordinal = []

    for line in input_file:
        curr_data = line.split(',')
        tur.append(float(curr_data[0]))
        ordinal.append(int(curr_data[1]))
    return tur,ordinal

def getSingleLakeData(data, data_type):
    complete_data = []
    for key in data:
        if key == 2022:
            complete_data = complete_data + data[key][data_type]

    return complete_data

def predict(tur, lake_name):
    dw = []
    # DomWave=constant + b1*ln(turbidity)
    for item in tur:
        if lake_name == "Peyto":
            dw.append(int(500.697 + 27.054*np.log(item)))
        elif lake_name == "Zigadenus":
            dw.append(int(501.438 + 23.346*np.log(item)))
    return dw

def plot(tur, dw, lake_name):
    plt.title(label=lake_name, fontsize=20, color='black')
    x = np.array(tur)
    y = np.array(dw)
    plt.plot(x,y)
    plt.xlabel('Tubidity (NTU)')
    plt.ylabel('Dominate Wavelength (nm)')
    plt.savefig("./figures/" + lake_name + "_PredictedDW.png")

def plotPredAct(tur, dw, lake_name, lake_dw, lake_tur):
    plt.title(label=lake_name, fontsize=20, color='black')
    x1 = np.array(tur)
    y1 = np.array(dw)
    plt.plot(x1,y1, color='tab:orange', label="Predicted")
    
    #define data
    x2 = np.array(lake_tur)
    y2 = np.array(lake_dw)

    #add points to plot
    plt.scatter(x2, y2, color='tab:blue', label="Actual")

    plt.xlabel('Tubidity (NTU)')
    plt.ylabel('Dominate Wavelength (nm)')
    plt.savefig("./figures/" + lake_name + "_PredActDW.png")

def plotSingleYear(pred_dw, all_ord, lake_dw, lake_ord, lake_name):
    plt.title(label=lake_name, fontsize=20, color='black')
    x1 = np.array(all_ord)
    y1 = np.array(pred_dw)
    plt.plot(x1,y1, color='tab:orange', label="Predicted")

    #define data
    x2 = np.array(lake_ord)
    y2 = np.array(lake_dw)

    #add points to plot
    plt.scatter(x2, y2, color='tab:blue', label="Actual")
    plt.xlabel('Ordinal Date')
    plt.ylabel('Dominate Wavelength (nm)')
    plt.savefig("./figures/" + lake_name + "_PredAct2022.png")

def main():
    '''
    python3 predict.py Zigadenus_Turbidity.csv Zigadenus.csv Zigadenus_TO.csv Zigadenus 
    python3 predict.py Peyto_Turbidity.csv Peyto.csv Peyto_TO.csv Peyto 
    '''
    tur_file = open("./data/" + sys.argv[1], 'r',)
    lake_file = open("./data/" + sys.argv[2], 'r',)
    lake_to_file = open("./data/" + sys.argv[3], 'r',)
    lake_name = sys.argv[4]
    lake = getData(lake_file)
    # tur = getTurData(tur_file)
    # dw = predict(tur, lake_name)
    # Generates R^2 graph
    # plot(tur, dw, lake_name)

    # lake_dw = getSingleLakeData(lake, 'domwave')
    # lake_tur = getSingleLakeData(lake, 'turbidity')
    # # Generates R^2 graph with actual data plotted (from all years)
    # plotPredAct(tur, dw, lake_name, lake_dw, lake_tur)

    # Generates graph dw X time graph for year 2022
    lake_dw = getSingleLakeData(lake, 'domwave')
    lake_ord = getSingleLakeData(lake, 'Julian')
    all_tur, all_ord = getDataTO(lake_to_file)
    pred_dw = predict(all_tur, lake_name)
    plotSingleYear(pred_dw, all_ord, lake_dw, lake_ord, lake_name)


main()

