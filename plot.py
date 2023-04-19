import sys
import matplotlib.pyplot as plt
import numpy as np

'''
Returns dictionairy of dominate wavelength, turbidity, and Julian date for each year of data
for a given lake.
* data[year] = {'domwave':[], 'turbidity':[], 'Julian':[]}
'''
def getData(input):
    data = {}
    input.readline()

    for line in input:
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

def getSingleLakeData(data, data_type):
    complete_data = []
    for key in data:
        complete_data = complete_data + data[key][data_type]

    return complete_data

'''
Generates graph of Dominate Wavelength X Tubidity across three lakes.
* Code for plotting (exponential) line of best fit is commented out.
'''
def makeDWTurGraph(data1, lake_name1, data2, lake_name2, data3, lake_name3):
    lake_1_dw = getSingleLakeData(data1, 'domwave')
    lake_1_tur = getSingleLakeData(data1, 'turbidity')

    lake_2_dw = getSingleLakeData(data2, 'domwave')
    lake_2_tur = getSingleLakeData(data2, 'turbidity')

    lake_3_dw = getSingleLakeData(data3, 'domwave')
    lake_3_tur = getSingleLakeData(data3, 'turbidity')
    
    # LAKE #1
    #define data
    x1 = np.array(lake_1_tur)
    y1 = np.array(lake_1_dw)

    # ylog_data1 = np.log(y1)
    # curve_fit1 = np.polyfit(x1, ylog_data1, 1)

    # # Convert the polynomial back into an exponential
    # a1 = np.exp(curve_fit1[1])
    # b1 = curve_fit1[0]
    # x_fitted1 = np.linspace(np.min(x1), np.max(x1), 100)
    # y_fitted1 = a1 * np.exp(b1 * x_fitted1)
    # plt.plot(x_fitted1, y_fitted1, 'k', label=lake_name1)

    #add points to plot
    plt.scatter(x1, y1, label=lake_name1)

    # LAKE #2
    #define data
    x2 = np.array(lake_2_tur)
    y2 = np.array(lake_2_dw)

    # ylog_data2 = np.log(y2)
    # curve_fit2 = np.polyfit(x2, ylog_data2, 1)

    # # Convert the polynomial back into an exponential
    # a2 = np.exp(curve_fit2[1])
    # b2 = curve_fit2[0]
    # x_fitted2 = np.linspace(np.min(x2), np.max(x2), 100)
    # y_fitted2 = a2 * np.exp(b2 * x_fitted2)
    # plt.plot(x_fitted2, y_fitted2, 'k', label=lake_name2)

    #add points to plot
    plt.scatter(x2, y2, label=lake_name2)

    # LAKE #3
    #define data
    x3 = np.array(lake_3_tur)
    y3 = np.array(lake_3_dw)

    # ylog_data3 = np.log(y3)
    # curve_fit3 = np.polyfit(x3, ylog_data3, 1)

    # # Convert the polynomial back into an exponential
    # a3 = np.exp(curve_fit3[1])
    # b3 = curve_fit3[0]
    # x_fitted3 = np.linspace(np.min(x3), np.max(x3), 100)
    # y_fitted3 = a3 * np.exp(b3 * x_fitted3)
    # plt.plot(x_fitted3, y_fitted3, 'k', label=lake_name3)

    #add points to plot
    plt.scatter(x3, y3, label=lake_name3)
   
    plt.legend()
    plt.xlabel('Tubidity')
    plt.ylabel('Dominate Wavelength (nm)')
    plt.savefig("./figures/DWTur.png")

'''
Generates graph of Time x Dominate Wavelength for a given lake.
'''
def makeDWTimeGraph(data, lake_name):
    plt.title(label=lake_name, fontsize=20, color='black')
    for key in data:
        x = np.array(data[key]['Julian'])
        y = np.array(data[key]['domwave'])
        list=zip(*sorted(zip(*(x,y))))
        plt.plot(*list, label=key, marker = 'o')
    plt.xlabel('Julian Date')
    plt.ylabel('Dominate Wavelength (nm)')
    # plt.legend(bbox_to_anchor = (1.25, 0.6), loc='center right')
    # plt.tight_layout()
    plt.savefig("./figures/" + lake_name + "_DWTime.png")

def makeMultiDWTimeGraph(year, data1, lake_name1, data2, lake_name2, data3, lake_name3):
        plt.title(label=year, fontsize=20, color='black')
        x1 = np.array(data1[year]['Julian'])
        y1 = np.array(data1[year]['domwave'])
        list1=zip(*sorted(zip(*(x1,y1))))
        plt.plot(*list1, color='blue', label=lake_name1, marker = 'o')

        if year in data2:
            x2 = np.array(data2[year]['Julian'])
            y2 = np.array(data2[year]['domwave'])
            list2=zip(*sorted(zip(*(x2,y2))))
            plt.plot(*list2, color='orange', label=lake_name2, marker = 'o')

        if year in data3:
            x3 = np.array(data3[year]['Julian'])
            y3 = np.array(data3[year]['domwave'])
            list3=zip(*sorted(zip(*(x3,y3))))
            plt.plot(*list3, color='green', label=lake_name3, marker = 'o')

        plt.xlabel('Julian Date')
        plt.ylabel('Dominate Wavelength (nm)')
        # plt.legend(bbox_to_anchor = (1.53, 0.6), loc='center right')
        # plt.tight_layout()
        plt.savefig("./figures/multi_" + str(year) + "_DWTime.png")

def makeMultiDWTimeSigGraph(year, data2, lake_name2, data3, lake_name3):
        plt.title(label=year, fontsize=20, color='black')
        if year in data2:
            x2 = np.array(data2[year]['Julian'])
            y2 = np.array(data2[year]['domwave'])
            list2=zip(*sorted(zip(*(x2,y2))))
            plt.plot(*list2, color='orange', label=lake_name2, marker = 'o')

        if year in data3:
            x3 = np.array(data3[year]['Julian'])
            y3 = np.array(data3[year]['domwave'])
            list3=zip(*sorted(zip(*(x3,y3))))
            plt.plot(*list3, color='green', label=lake_name3, marker = 'o')

        plt.xlabel('Julian Date')
        plt.ylabel('Dominate Wavelength (nm)')
        # plt.legend(bbox_to_anchor = (1.53, 0.6), loc='center right')
        # plt.tight_layout()
        plt.savefig("./figures/multi_" + str(year) + "_DWTimeSig.png")


'''
Generates duel axis graph of dominate wavelength and turbidity over time for a given lake.
* Each year is graphed separately.
'''
def makeDuel(data, lake_name):
    for key in data:
        x = np.array(data[key]['Julian'])
        y1 = np.array(data[key]['domwave'])
        y2 = np.array(data[key]['turbidity'])
        list2=zip(*sorted(zip(*(x,y2))))

        fig, ax1 = plt.subplots(figsize=(8, 6))
        ax2 = ax1.twinx()

        # ax1.plot(*list1, label="Dominate Wavelength", color='blue')
        ax1.bar(x, height= y1-min(y1), bottom=min(y1), label="Dominate Wavelength")
        ax2.plot(*list2, label="Tubidity", color='orange', marker = 'o')

        ax1.set_xlabel("Julian Date")
        ax1.set_ylabel("Dominate Wavelength (nm)")
        ax1.tick_params(axis="y")

        ax2.set_ylabel("Tubidity (NTU)")
        ax2.tick_params(axis="y")

        fig.legend(loc="upper right")
        plt.ylim(min(y2), max(y2))
        plt.savefig("./figures/" + lake_name + "_" + str(key) + "_DWTur.png")

def getCorrelation(data1, data2, data3):
    corr = {}
    lake_1_dw = getSingleLakeData(data1, 'domwave')
    lake_1_tur = getSingleLakeData(data1, 'turbidity')
    corr['opabin'] = np.corrcoef(lake_1_dw, lake_1_tur)

    lake_2_dw = getSingleLakeData(data2, 'domwave')
    lake_2_tur = getSingleLakeData(data2, 'turbidity')
    corr['peyto'] = np.corrcoef(lake_2_dw, lake_2_tur)

    lake_3_dw = getSingleLakeData(data3, 'domwave')
    lake_3_tur = getSingleLakeData(data3, 'turbidity')
    corr['zigadenus'] = np.corrcoef(lake_3_dw, lake_3_tur)

    dw = lake_1_dw + lake_2_dw + lake_3_dw
    tur = lake_1_tur + lake_2_tur + lake_3_tur
    corr['all'] = np.corrcoef(tur, dw)

    return corr

def main():
    input1 = open("./data/" + sys.argv[1], 'r',)
    data1 = getData(input1)

    input2 = open("./data/" + sys.argv[2], 'r',)
    data2 = getData(input2)

    input3 = open("./data/" + sys.argv[3], 'r',)
    data3 = getData(input3)

    lake_name1 = sys.argv[4]
    lake_name2 = sys.argv[5]
    lake_name3 = sys.argv[6]

    '''---Uncomment funciton calls individually to generate graphs to avoid incorrect plotting---'''

    '''What is driving color? --> 1 graph'''
    # makeDWTurGraph(data1, lake_name1, data2, lake_name2, data3, lake_name3)
    '''Variation amoung years within a lake --> 3 graphs'''
    # makeDWTimeGraph(data1, lake_name1)
    # makeDWTimeGraph(data2, lake_name2)
    # makeDWTimeGraph(data3, lake_name3)
    '''Duel axis graph of dominate wavelength and turbidity over time'''
    # makeDuel(data1, lake_name1)
    # makeDuel(data2, lake_name2)
    # makeDuel(data3, lake_name3)

    '''Variation among lakes within a year'''
    # makeMultiDWTimeGraph(2019, data1, lake_name1, data2, lake_name2, data3, lake_name3)
    # makeMultiDWTimeGraph(2020, data1, lake_name1, data2, lake_name2, data3, lake_name3)
    # makeMultiDWTimeGraph(2021, data1, lake_name1, data2, lake_name2, data3, lake_name3)
    # makeMultiDWTimeGraph(2022, data1, lake_name1, data2, lake_name2, data3, lake_name3)

    '''Correlation between turbidity and dominate wavlength'''
    # print(getCorrelation(data1, data2, data3))

    '''Significant'''
    makeMultiDWTimeSigGraph(2021, data2, lake_name2, data3, lake_name3)
    # makeMultiDWTimeSigGraph(2022, data2, lake_name2, data3, lake_name3)

    input1.close()
    input2.close()
    input3.close()

main()