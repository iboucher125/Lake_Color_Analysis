import sys
import matplotlib.pyplot as plt

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
Generates graph of Month x Dominate Wavelength for a given lake.
'''
def makeDWTimeGraph(DomWave, months, lake_name):
    plt.title(label="Month x Dominate Wavelength -- " + lake_name, fontsize=15, color='black')
    for key in DomWave:
        plt.plot(months, DomWave[key], label=key)
        plt.xlabel('Month')
        plt.ylabel('Dominate Wavelength')
        plt.legend()
        plt.savefig("./figures/Evaluate_" + lake_name + "_DWTime.png")

'''
Generates graph of Month x Turbidity for a given lake.
'''
def makeTurTimeGraph(turbidity, months, lake_name):
    plt.title(label="Month x Turbidity -- " + lake_name, fontsize=15, color='black')
    for key in turbidity:
        plt.plot(months, turbidity[key], label=key)
        plt.xlabel('Month')
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
    input.close()

main()