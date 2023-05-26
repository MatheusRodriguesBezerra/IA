from id3 import run

chosen = int(input("Qual teste deseja realizar?\n[1] para weather.csv\n[2] para restaurant.csv\n[3] para iris.csv\n"))
if(chosen == 1):
    run('weather')
elif(chosen == 2):
    run('restaurant')
else:
    run('iris')
    