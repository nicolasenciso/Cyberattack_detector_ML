def FTPbruteForce(percentage):
    dataAttack = open('attacksDataAll/FTP-BruteForce.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 193360
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignFTPBrute.txt','r')
    sizeBenign = 667626
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------FTP Bruteforce-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def SSHbruteForce(percentage):
    dataAttack = open('attacksDataAll/SSH-BruteForce.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 187589
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignSSHBrute.txt','r')
    sizeBenign = 667626
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------SSHBruteforce-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DoSGoldenEye(percentage):
    dataAttack = open('attacksDataAll/DoS-GoldenEye.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 41508
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDos-GoldenEye.txt','r')
    sizeBenign = 996077
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DoS GoldenEye-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DoSslowLoris(percentage):
    dataAttack = open('attacksDataAll/DoS-SlowLoris.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 10990
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDosSlowLoris.txt','r')
    sizeBenign = 996077
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DoS Slow Loris-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DoSslowHTTPTest(percentage):
    dataAttack = open('attacksDataAll/DoS-SlowHTTPTest.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 139890
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDosSlowHTTPtest.txt','r')
    sizeBenign = 446772
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DoS Slow HTTP Test-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DoSHulk(percentage):
    dataAttack = open('attacksDataAll/DoS-Hulk.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 461912
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDosHulk.txt','r')
    sizeBenign = 446772
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DoS Hulk-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DDoSLOICHTTP(percentage):
    dataAttack = open('attacksDataAll/DDoS-LOICHTTP.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 576191
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            auxData = data.split(',')
            auxstr = ''
            del auxData[0]
            del auxData[1]
            del auxData[2]
            del auxData[0]
            auxstr = auxData[0]
            for i in range(1,len(auxData)):
                if i != len(auxData):
                    auxstr = auxstr + ',' + auxData[i] 
                else:
                    auxstr = auxstr + auxData[i]

            dataFinal.writelines(auxstr)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDDos-LOICHTTP.txt','r')
    sizeBenign = 446772
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            auxData = data.split(',')
            auxstr = ''
            del auxData[0]
            del auxData[1]
            del auxData[2]
            del auxData[0]
            auxstr = auxData[0]
            for i in range(1,len(auxData)):
                if i != len(auxData):
                    auxstr = auxstr + ',' + auxData[i] 
                else:
                    auxstr = auxstr + auxData[i]

            dataFinal.writelines(auxstr)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DDoSLOICHTTP-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DDoSLOICUDP(percentage):
    dataAttack = open('attacksDataAll/DDoS-LOICUDP.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 1730
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDDoS-LOICUDP.txt','r')
    sizeBenign = 360833
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DDoSLOICUDP-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def DDoSHOIC(percentage):
    dataAttack = open('attacksDataAll/DDoS-HOIC.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 686012
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignDDoS-HOIC.txt','r')
    sizeBenign = 360833
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------DDoSHOIC-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def BruteForceWeb(percentage):
    dataAttack = open('attacksDataAll/BruteForceWeb.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 362
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignBruteForceWeb.txt','r')
    sizeBenign = 2096222
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------Brute Force Web-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def BruteForceXSS(percentage):
    dataAttack = open('attacksDataAll/BruteForceXSS.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 151
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignBruteForceXSS.txt','r')
    sizeBenign = 2096222
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------Brute Force XSS-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def SQLinjection(percentage):
    dataAttack = open('attacksDataAll/SQLinjection.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 53
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    if attackPercentage < 1:
        attackPercentage = 1
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignSQLinjection.txt','r')
    sizeBenign = 2096222
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------SQL injection-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def Infiltration(percentage):
    dataAttack = open('attacksDataAll/Infiltration.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 93063
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignInfiltration.txt','r')
    sizeBenign = 782237
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------Infiltration-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def Bot(percentage):
    dataAttack = open('attacksDataAll/Bot.txt','r')
    dataFinal = open('DATASET.txt','a')
    sizeAttack = 286191
    percent = float(percentage)
    attackPercentage = int(round(sizeAttack * percent / 100))
    counter = 0
    for data in dataAttack:
        if counter <= attackPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataAttack.close()
    dataBenign = open('BenignDataAll/BenignBot.txt','r')
    sizeBenign = 762384
    benignPercentage = int(round(sizeBenign * percent / 100))
    counter = 0
    for data in dataBenign:
        if counter <= benignPercentage:
            dataFinal.writelines(data)
            counter = counter + 1
        
    dataBenign.close()
    dataFinal.close()
    print("------Bot-----")
    print(attackPercentage)
    print(benignPercentage)
    return attackPercentage,benignPercentage

def startComposer(percentage):
    (attack1,benign1) = FTPbruteForce(percentage)
    (attack2,benign2) = SSHbruteForce(percentage)
    (attack3,benign3) = DoSGoldenEye(percentage)
    (attack4,benign4) = DoSslowLoris(percentage)
    (attack5,benign5) = DoSslowHTTPTest(percentage)
    (attack6,benign6) = DoSHulk(percentage)
    (attack7,benign7) = DDoSLOICHTTP(percentage)
    (attack8,benign8) = DDoSLOICUDP(percentage)
    (attack9,benign9) = DDoSHOIC(percentage)
    (attack10,benign10) = BruteForceWeb(percentage)
    (attack11,benign11) = BruteForceXSS(percentage)
    (attack12,benign12) = SQLinjection(percentage)
    (attack13,benign13) = Infiltration(percentage)
    (attack14,benign14) = Bot(percentage)
    print("--------------------------------------")
    attacks = attack1+attack2+attack3+attack4+attack5+attack6+attack7+attack8+attack9+attack10+attack11+attack12+attack13+attack14
    benign = benign1+benign2+benign3+benign4+benign5+benign6+benign7+benign8+benign9+benign10+benign11+benign12+benign13+benign14
    print("TOTAL ATTACKS: ")
    print(attacks)
    print("-------------------------------")
    print("TOTAL BENIGN: ")
    print(benign)
    print("---------------------------------")
    print("TOTAL DATASET: ")
    print(attacks+benign)
    print("--------------------------------")
    print("RATIO BENIGN / ATTACK: ")
    benign = benign + 0.0
    print(benign/attacks)
startComposer(1)
def howManysamplesAre():
    data = open('DATASET.txt','r')
    cont = 0
    for sample in data:
        cont = cont + 1
    print("TOTAL COUNTER SAMPLES ON DATASET: ")
    print(cont)
    data.close()

howManysamplesAre()








