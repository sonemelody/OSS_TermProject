import csv
import matplotlib.pyplot as plt
f = open('C:/Users/cat08/Desktop/오픈소스소프트웨어/TermProject/subway.csv')
data = csv.reader(f)

next(data)
next(data)

mx_time_in = 0       
mx_time_out = 0   
mx_time_station_in = ''
mx_time_station_out = ''
mn_time_in = 0     
mn_time_out = 0     
mn_time_station_in = ''
mn_time_station_out = ''
mx_in = [0] * 24
mx_out = [0] * 24
mx_in_station = [''] * 24
mx_out_station = [''] * 24 
mn_in = [0] * 24
mn_out = [0] * 24
mn_in_station = [''] * 24
mn_out_station = [''] * 24 
s_in = [0] * 24 
s_out = [0] * 24

t = int(input('몇 시의 승하차 인원이 궁금하세요? : '))

for row in data :    
    row[4:] = map(int, row[4:])
    
    if row[4+(t-4)*2] > mx_time_in :              
        mx_time_in = row[4+(t-4)*2]
        mx_time_station_in = row[3]+'('+ row[1]+')'
    if row[4+(t-4)*2] < mx_time_in :              
        mn_time_in = row[4+(t-4)*2]
        mn_time_station_in = row[3]+'('+ row[1]+')'
    if row[5+(t-4)*2] > mx_time_in :              
        mx_time_out = row[5+(t-4)*2]
        mx_time_station_out = row[3]+'('+ row[1]+')'
    if row[5+(t-4)*2] < mx_time_in :              
        mn_time_out = row[5+(t-4)*2]
        mn_time_station_out = row[3]+'('+ row[1]+')'
        
    for i in range(24) :
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]
    for j in range(24) :
        a = row[j * 2 + 4]
        b = row[j * 2 + 5]
        if a > mx_in[j] :
            mx_in[j] = a
            mx_in_station[j] = f'{row[3]}({int(str(j+4))%24}시)'
        if a < mx_in[j] :
            mn_in[j] = a
            mn_in_station[j] = f'{row[3]}({int(str(j+4))%24}시)'
        if b > mx_out[j] :
            mx_out[j] = b
            mx_out_station[j] = f'{row[3]}({int(str(j+4))%24}시)'
        if b < mx_out[j] :
            mn_out[j] = b
            mn_out_station[j] = f'{row[3]}({int(str(j+4))%24}시)'
        
print('\n')           
print(t,"시에 승차 인원이 가장 많은 역은", mx_time_station_in, mx_time_in)
print(t,"시에 승차 인원이 가장 적은 역은", mn_time_station_in, mn_time_in)
print(t,"시에 하차 인원이 가장 많은 역은", mx_time_station_out, mx_time_out)
print(t,"시에 하차 인원이 가장 적은 역은", mn_time_station_out, mn_time_out)

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

plt.title('지하철 시간대별 승하차 인원 추이') 
plt.plot(s_in, label='승차')           
plt.plot(s_out, label='하차')            
plt.legend() 
plt.xticks(range(24), range(4,28))
plt.show()

plt.title('시간대별 승차 인원이 많은 역')
plt.bar(range(24), mx_in, color='b')
plt.xticks(range(24), mx_in_station, rotation=90)
plt.show()

plt.title('시간대별 승차 인원이 적은 역')
plt.bar(range(24), mn_in, color='b')
plt.xticks(range(24), mn_in_station, rotation=90)
plt.show()

plt.title('시간대별 하차 인원이 많은 역')
plt.bar(range(24), mx_out, color='r')
plt.xticks(range(24), mx_out_station, rotation=90)
plt.show()

plt.title('시간대별 하차 인원이 적은 역')
plt.bar(range(24), mn_out, color='r')
plt.xticks(range(24), mn_out_station, rotation=90)
plt.show()