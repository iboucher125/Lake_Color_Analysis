import sys
import matplotlib.pyplot as plt
import numpy as np

'''
Returns dictionaires containing dominate wavelength and turbidity data for years 2019-2022
    DomWave - dictionary contianing dominate wavelength data
    turbidity - dictionary contianing turbidity data
'''
def getData(input):
    DomWave = {}
    turbidity = {}
    months = []
    input.readline()

    for line in input:
        data = line.split(',')
        # DOMINANT WAVELENGTH
        if data[2] not in months:
            months.append(data[2])
        if int(data[3]) not in DomWave:
            if data[0] == '':
                 DomWave[int(data[3])] = [None]
            else:
                DomWave[int(data[3])] = [int(float(data[0]))]
        else:
            if data[0] == '':
                 DomWave[int(data[3])].append(None)
            else:
                DomWave[int(data[3])].append(int(float(data[0])))

        # TURBIDITY
        if int(data[3]) not in turbidity:
            if data[1] == '':
                turbidity[int(data[3])] = [None]
            else:
                turbidity[int(data[3])] = [float(data[1])]
        else:
            if data[1] == '':
                turbidity[int(data[3])].append(None)
            else:
                turbidity[int(data[3])].append(float(data[1]))

    return DomWave, turbidity, months

'''
Generates graph of Tubidity x Dominate Wavelength for a given lake.
* Use complete data
'''
def makeDWTurGraph(DomWave, turbidity, lake_name):
    plt.title(label="Tubidity x Dominate Wavelength -- " + lake_name, fontsize=15, color='black')
    all_dw = []
    all_tur = []
    for key in DomWave:
        all_dw = all_dw + DomWave[key]
        all_tur = all_tur + turbidity[key]
    
    #define data
    x = np.array(all_dw)
    y = np.array(all_tur)

    ylog_data = np.log(y)
    curve_fit = np.polyfit(x, ylog_data, 1)

    # Convert the polynomial back into an exponential
    a = np.exp(curve_fit[1])
    b = curve_fit[0]
    x_fitted = np.linspace(np.min(x), np.max(x), 100)
    y_fitted = a * np.exp(b * x_fitted)
    plt.plot(x_fitted, y_fitted, 'k', label='Fitted curve')

    #add points to plot
    plt.scatter(x, y)

    plt.xlabel('Dominate Wavelength')
    plt.ylabel('Tubidity')
    plt.savefig("./figures/Evaluate_" + lake_name + "_DWTur.png")

'''
Generates graph of Time x Dominate Wavelength for a given lake.
* Use averege data
'''
def makeDWTimeGraph(DomWave, months, lake_name):
    plt.title(label="Time x Dominate Wavelength -- " + lake_name, fontsize=15, color='black')
    for key in DomWave:
        plt.plot(months, DomWave[key], label=key)
        plt.xlabel('Time')
        plt.ylabel('Dominate Wavelength')
        plt.legend()
        plt.savefig("./figures/Evaluate_" + lake_name + "_DWTime.png")

'''
Generates graph of Time x Turbidity for a given lake.
* Use averege data
'''
def makeTurTimeGraph(turbidity, months, lake_name):
    plt.title(label="Time x Turbidity -- " + lake_name, fontsize=15, color='black')
    for key in turbidity:
        plt.plot(months, turbidity[key], label=key)
        plt.xlabel('Time')
        plt.ylabel('Turbidity')
        plt.legend()
        plt.savefig("./figures/Evaluate_" + lake_name + "_TurTime.png")
    

def main():
    input = open("./data/" + sys.argv[1], 'r',)
    lake_name = sys.argv[2]
    graph_type = sys.argv[3]
    DomWave, turbidity, months = getData(input)
    if graph_type == 'd':
        makeDWTimeGraph(DomWave, months, lake_name)
    elif graph_type == 't':
        makeTurTimeGraph(turbidity, months, lake_name)
    elif graph_type == 'b':
        makeDWTurGraph(DomWave, turbidity, lake_name)
    input.close()

main()