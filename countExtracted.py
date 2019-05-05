def count():
    counter = 0
    attack = 0
    benign = 0
    data = open('attacksDataAll/FTP-BruteForce.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("FTP-BruteForce.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignFTPBrute.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignFTPBrute.txt")
    print(auxCount)
    print("--------------------")
    
    data = open('attacksDataAll/SSH-BruteForce.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("SSH-BruteForce.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignSSHBrute.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignSSHBrute.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DoS-GoldenEye.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DoS-GoldenEye.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDos-GoldenEye.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDos-GoldenEye.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DoS-SlowLoris.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DoS-SlowLoris.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDosSlowLoris.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDosSlowLoris.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DoS-SlowHTTPTest.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DoS-SlowHTTPTest.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDosSlowHTTPtest.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDosSlowHTTPtest.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DoS-Hulk.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DoS-Hulk.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDosHulk.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDosHulk.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DDoS-LOICHTTP.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DDoS-LOICHTTP.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDDos-LOICHTTP.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDDos-LOICHTTP.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DDoS-LOICUDP.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DDoS-LOICUDP.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDDoS-LOICUDP.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDDoS-LOICUDP.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/DDoS-HOIC.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("DDoS-HOIC.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignDDoS-HOIC.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignDDoS-HOIC.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/BruteForceWeb.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("BruteForceWeb.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignBruteForceWeb.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignBruteForceWeb.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/BruteForceXSS.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("BruteForceXSS.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignBruteForceXSS.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignBruteForceXSS.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/SQLinjection.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("SQLinjection.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignSQLinjection.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignSQLinjection.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/Infiltration.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("Infiltration.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignInfiltration.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignInfiltration.txt")
    print(auxCount)
    print("--------------------")

    data = open('attacksDataAll/Bot.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        attack = attack + 1
    data.close()
    counter = counter + auxCount
    print("Bot.txt")
    print(auxCount)
    print("--------------------")

    data = open('BenignDataAll/BenignBot.txt','r')
    auxCount = 0
    for row in data:
        auxCount = auxCount + 1
        benign = benign + 1
    data.close()
    counter = counter + auxCount
    print("BenignBot.txt")
    print(auxCount)
    print("--------------------")
    print("TOTAL BENIGN: ")
    print(benign)
    print("---------------------")
    print("TOTAL ATTACKS: ")
    print(attack)
    print("--------------------")
    print("TOTAL SAMPLES: ")
    print(counter)
    
count()












