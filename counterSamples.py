def counter():
    benignSamples = 0
    attackSamples = 0
    finalAttacks = 0
    finalBenign = 0
    day = open('originalData/Wednesday-14-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'FTP-BruteForce\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'SSH-Bruteforce\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in wed14: "+str(benignSamples))
    print("attack samples in wed14: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Thursday-15-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DoS attacks-GoldenEye\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'DoS attacks-Slowloris\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in thu15: "+str(benignSamples))
    print("attack samples in thu15: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Friday-16-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DoS attacks-SlowHTTPTest\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'DoS attacks-Hulk\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in fri16: "+str(benignSamples))
    print("attack samples in fri16: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Thuesday-20-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if len(auxRow[len(auxRow)-1]) == 24:
            attackSamples = attackSamples + 1
        else:
        #elif len(auxRow[len(auxRow)-1]) == 7:
            benignSamples = benignSamples + 1
    print("benign samples in thu20: "+str(benignSamples))
    print("attack samples in thu20: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Wednesday-21-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DDOS attack-LOIC-UDP\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'DDOS attack-HOIC\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in wed21: "+str(benignSamples))
    print("attack samples in wed21: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Thursday-22-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Brute Force -Web\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Brute Force -XSS\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'SQL Injection\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in thu22: "+str(benignSamples))
    print("attack samples in thu22: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Friday-23-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Brute Force -Web\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Brute Force -XSS\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'SQL Injection\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in fri23: "+str(benignSamples))
    print("attack samples in fri23: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Wednesday-28-02-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Infilteration\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in wed28: "+str(benignSamples))
    print("attack samples in wed28: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Thursday-01-03-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Infilteration\n':
            attackSamples = attackSamples + 1
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            benignSamples = benignSamples + 1
    print("benign samples in thu01: "+str(benignSamples))
    print("attack samples in thu01: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    benignSamples = 0
    attackSamples = 0
    day = open('originalData/Friday-02-03-2018_TrafficForML_CICFlowMeter.txt','r')
    for row in day:
        auxRow = row.split(',')
        if len(auxRow[len(auxRow)-1]) == 5:
            attackSamples = attackSamples + 1
        else:
            benignSamples =  benignSamples + 1
    print("benign samples in fri02: "+str(benignSamples))
    print("attack samples in fri02: "+ str(attackSamples))
    finalAttacks = finalAttacks + attackSamples
    finalBenign = finalBenign + benignSamples
    day.close()
    print("----------------------------------------------------------")
    print("TOTAL BENIGN SAMPLES = "+str(finalBenign))
    print("TOTAL ATTACK SAMPLES = "+str(finalAttacks))
    print("TOTAL SAMPLES DATASETS = "+str(finalAttacks+finalBenign))
    finalAttacks = float(finalAttacks + 0.0)
    print("RATIO BENIGN/ATTACK SAMPLES = "+str(float(finalBenign/finalAttacks)))


counter()









