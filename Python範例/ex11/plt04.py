import matplotlib.pyplot as plt
font = {'family' : 'DFKai-SB'}  
plt.rc('font', **font) 

listIYearX = [2014, 2015, 2016, 2017, 2018, 2019]

listIPhoneY = [43000, 31000, 70500, 68000, 85000, 24000]
plt.plot(listIYearX, listIPhoneY, color='blue', ls='--',
         lw=6, label="iPhone")

listAsusY = [23000, 36000, 40500, 58000, 65000, 44000]
plt.plot(listIYearX, listAsusY, color='red', ls='-.', lw=6, label="ASUS")

listMiY = [13000, 26000, 50500, 68000, 75000, 54000]
plt.plot(listIYearX, listMiY, color='green', ls='-', lw=6, label="小米")
plt.title("手機歷年銷售量")
plt.xlim(2013, 2020)
plt.ylim(0, 110000)
plt.xlabel('年度')
plt.ylabel('銷售量')
plt.legend()
plt.show()