import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
import statsmodels.formula.api as sm
import seaborn as sns
import math as m
from scipy import stats
from datetime import datetime
from io import StringIO

def read_f(Car_Bra, Car_Info):
    f = open("C:/Users/kmes9/vscode/python/AnIntro_Statistics_Python/Data/93cars.dat.txt") 
    all = []
    Car_Bra = []
    Car_Info = []
    lines = f.readlines()  # read each line in the file, and covert to array
    for line in lines:
        #print(line.split())
        all.append(line.split())
    f.close()
    for i in range(len(all)):
        if i%2 == 0:
            Car_Bra.append(all[i])
        else:
            Car_Info.append(all[i])
    return Car_Bra, Car_Info

    #print(all_1)
    #print(all_2)

def df_CarBrand():
    Manuf = []
    Model = []
    Type = []
    MiniPric = []
    MidPric = []
    MaxPric = []
    CityMPG = []
    HighwayMPG = []
    AirBag = []
    DriveTrain = []
    NumCyl = []
    EngSize = []
    Hp = []
    Rpm = []
    # covert data into integer or float
    car_1 = []
    car_2 = []
    for i in range(len(read_f(car_1,car_2)[0])):
        NumCyl_d = [np.nan if x == "*" else x for x in read_f(car_1,car_2)[0][i]]
        Manuf.append(read_f(car_1,car_2)[0][i][0])
        Model.append(read_f(car_1,car_2)[0][i][1])
        Type.append(read_f(car_1,car_2)[0][i][2])
        MiniPric.append(float(read_f(car_1,car_2)[0][i][3]))
        MidPric.append(float(read_f(car_1,car_2)[0][i][4]))
        MaxPric.append(float(read_f(car_1,car_2)[0][i][5]))
        CityMPG.append(int(read_f(car_1,car_2)[0][i][6]))
        HighwayMPG.append(int(read_f(car_1,car_2)[0][i][7]))
        AirBag.append(int(read_f(car_1,car_2)[0][i][8]))
        DriveTrain.append(int(read_f(car_1,car_2)[0][i][9]))
        NumCyl.append(float(NumCyl_d[10])) #have *
        EngSize.append(float(read_f(car_1,car_2)[0][i][11]))
        Hp.append(int(read_f(car_1,car_2)[0][i][12]))
        Rpm.append(int(read_f(car_1,car_2)[0][i][13]))

    # covert data into dataframe
    df_Brand = pd.DataFrame({
        "Manufacturer":Manuf,
        "Model":Model,
        "Type":Type,
        "MiniPrice":MiniPric,
        "MidPrice":MidPric,
        "MaxPrice":MaxPric,
        "CityMPG":CityMPG,
        "HighwayMPG":HighwayMPG,
        "AirBagStd":AirBag,
        "DriveTrainTye":DriveTrain,
        "NoCylinders":NumCyl,
        "EngineSize":EngSize,
        "Horsepower":Hp,
        "RPM":Rpm,
    })
    return df_Brand

def df_CarInfo():
    Car_Prop_name = ["EngRev", "ManTransAva", "FuelTankCap", "PassCap", "Length", "Wheelbase", "Width", "UTurnSpace", "RearSeatRoom", "LugCap", "Weight", "Domestic"]
    EngRev = []
    ManTransAva = []
    FuelTankCap = []
    PassCap = []
    Length = []
    Wheelbase = []
    Width = []
    UTurnSpace = []
    RearSeatRoom = []
    LugCap = []
    Weight = []
    Domestic = []
    Car_Prop = [EngRev, ManTransAva, FuelTankCap, PassCap, Length, Wheelbase, Width, UTurnSpace, RearSeatRoom, LugCap, Weight, Domestic]
    # covert data into integer or float
    car_1 = []
    car_2 = []
    for i in range(len(read_f(car_1,car_2)[1])):
        All_Prop = [np.nan if x == "*" else x for x in read_f(car_1,car_2)[1][i]]
        for j in range(len(Car_Prop)):
            Car_Prop[j].append(float(All_Prop[j]))

    # covert data into dataframe
    df_Prop = pd.DataFrame({
        "EngRevoluAva.":Car_Prop[0],
        "ManTransCap":Car_Prop[1],
        "FuelTankCap":Car_Prop[2],
        "PassCap":Car_Prop[3],
        "Length":Car_Prop[4],
        "Wheelbase":Car_Prop[5],
        "Width":Car_Prop[6],
        "UTurnSpace":Car_Prop[7],
        "RearSeatRoom":Car_Prop[8],
        "LugCap":Car_Prop[9],
        "Weight":Car_Prop[10],
        "Domestic":Car_Prop[11],
    })
    return df_Prop

def plot_bar(axis,data,labels):
    axis.bar(labels, data, width=0.5)
    axis.set_xticklabels(labels=labels, color='#00f',fontsize=15, fontweight='bold')
    axis.set_xticks(np.arange(0, len(labels)))
    axis.set_yticklabels(labels=np.arange(0, 11,1),fontsize=15, fontweight='bold')
    axis.set_yticks(np.arange(0, 11))
    axis.set_ylim(0, 10)

def plot_hist(axis, data, labels):
    axis.hist(data, bins=8)
    axis.set_xticklabels(labels=labels, fontsize=15, fontweight='bold')
    axis.set_xticks(labels)
    #axis.set_yticklabels(labels=np.arange(0, 11,1),fontsize=15, fontweight='bold')
    axis.set_yticks(np.arange(0, 55, 5))
    axis.set_ylim(0, 50)
    for label in axis.get_yticklabels():
        label.set_fontsize(15)
        label.set_fontname('Arial')
        label.set_fontweight('bold')

def plot_t_dist(axis, data):
    """Overlay a normal curve for the mean of n cans, scaled to histogram counts."""
    mean = np.mean(data)
    std = np.std(data)
    x = np.linspace(0, 400, 300)
    #se = std / np.sqrt(n) 
    #df = n - 1
    bin_width = (400) / 8
    pdf = stats.t.pdf(x, 92, loc=mean, scale=std)
    #print(pdf)
    axis.plot(x, pdf * len(data) * bin_width, 'r--', lw=2)

def main():
    fig, ax = plt.subplots(2,1,figsize=(21, 7))
    car_1 = []
    car_2 = []    
    df_allInfo = pd.concat([df_CarBrand(), df_CarInfo()], axis=1)
    num_manuf = df_allInfo['Manufacturer'].value_counts()
    num_manuf_lar2 = num_manuf[num_manuf > 2]
    plot_bar(ax[0],num_manuf_lar2,num_manuf_lar2.index)
    #ax[0].set_xlabel('Car Brands',fontsize=15, fontweight='bold')
    ax[0].set_ylabel('Numebrs',fontsize=15, fontweight='bold')
    xlabel = np.arange(0,400,50)
    plot_hist(ax[1], df_allInfo["Horsepower"], xlabel)
    plot_t_dist(ax[1], df_allInfo["Horsepower"])
    ax[1].set_xlabel('Horespower',fontsize=15, fontweight='bold')
    ax[1].set_ylabel('Numebrs',fontsize=15, fontweight='bold')
    plt.savefig('my_plot.png', dpi=300, bbox_inches='tight', transparent=False)
    #plt.show()

if __name__ == '__main__':
    '''car_1 = []
    car_2 = []
    #print(read_f(car_1, car_2)[0][0][0])
    #print(df_CarBrand())
    df_allInfo = pd.concat([df_CarBrand(), df_CarInfo()], axis=1)
    num_manuf = df_allInfo['Manufacturer'].value_counts()
    print(num_manuf.index)'''
    main()