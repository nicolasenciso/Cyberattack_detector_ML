from threading import Thread

#from StackOverflow to get return values from a thread
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        #print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def startExtractor():
    ftp = ThreadWithReturnValue(target=ftpBruteForce, args=())
    ssh = ThreadWithReturnValue(target=sshBruteForce, args=())
    golden = ThreadWithReturnValue(target=dosGoldenEye, args=())
    loris = ThreadWithReturnValue(target=dosSlowLoris, args=())

    #start every 4 threads, due to my pc has 4 cores
    ftp.start()
    ssh.start()
    golden.start()
    loris.start()

    outftp = ftp.join()
    outssh = ssh.join()
    outgolden = golden.join()
    outloris = loris.join()

    chunk1 = outftp + outssh + outgolden + outloris

    slow = ThreadWithReturnValue(target=dosSlowHTTP, args=())
    hulk = ThreadWithReturnValue(target=dosHulk, args=())
    http = ThreadWithReturnValue(target=ddosLOICHTTP, args=())
    udp = ThreadWithReturnValue(target=ddosLOICUDP, args=())

    slow.start()
    hulk.start()
    http.start()
    udp.start()

    outslow = slow.join()
    outhulk = hulk.join()
    outhttp = http.join()
    outudp = udp.join()

    chunk2 = outslow + outhulk + outhttp + outudp

    hoic = ThreadWithReturnValue(target=ddosHOIC, args=())
    web = ThreadWithReturnValue(target=bruteForceWeb, args=())
    xss = ThreadWithReturnValue(target=bruteForceXSS, args=())
    sql = ThreadWithReturnValue(target=SQLinjection, args=())
    
    hoic.start()
    web.start()
    xss.start()
    sql.start()

    outhoic = hoic.join()
    outweb = web.join()
    outxss = xss.join()
    outsql = sql.join()

    chunk3 = outhoic + outweb + outxss + outsql

    infil = ThreadWithReturnValue(target=Infiltration, args=())
    bot = ThreadWithReturnValue(target=Bot, args=())

    infil.start()
    bot.start()

    outinfil = infil.join()
    outbot = bot.join()

    chunk4 = outinfil + outbot

    print(chunk1 + chunk2 + chunk3 + chunk4)    


def ftpBruteForce():
    count = 0
    dataset = open('originalData/Wednesday-14-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/FTP-BruteForce.txt','w')
    benignData = open('BenignDataAll/BenignFTPBrute.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'FTP-BruteForce\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def sshBruteForce():
    count = 0
    dataset = open('originalData/Wednesday-14-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/SSH-BruteForce.txt','w')
    benignData = open('BenignDataAll/BenignSSHBrute.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'SSH-Bruteforce\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def dosGoldenEye():
    count = 0
    dataset = open('originalData/Thursday-15-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DoS-GoldenEye.txt','w')
    benignData = open('BenignDataAll/BenignDos-GoldenEye.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DoS attacks-GoldenEye\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def dosSlowLoris():
    count = 0
    dataset = open('originalData/Thursday-15-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DoS-SlowLoris.txt','w')
    benignData = open('BenignDataAll/BenignDosSlowLoris.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DoS attacks-Slowloris\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count


def dosSlowHTTP():
    count = 0
    dataset = open('originalData/Friday-16-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DoS-SlowHTTPTest.txt','w')
    benignData = open('BenignDataAll/BenignDosSlowHTTPtest.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DoS attacks-SlowHTTPTest\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def dosHulk():
    count = 0
    dataset = open('originalData/Friday-16-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DoS-Hulk.txt','w')
    benignData = open('BenignDataAll/BenignDosHulk.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DoS attacks-Hulk\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def ddosLOICHTTP():
    count = 0
    dataset = open('originalData/Thuesday-20-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DDoS-LOICHTTP.txt','w')
    benignData = open('BenignDataAll/BenignDDos-LOICHTTP.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        #print(len(auxRow[len(auxRow)-1]))
        if len(auxRow[len(auxRow)-1]) == 24:
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif len(auxRow[len(auxRow)-1]) == 7:
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def ddosLOICUDP():
    count = 0
    dataset = open('originalData/Wednesday-21-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DDoS-LOICUDP.txt','w')
    benignData = open('BenignDataAll/BenignDDoS-LOICUDP.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DDOS attack-LOIC-UDP\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def ddosHOIC():
    count = 0
    dataset = open('originalData/Wednesday-21-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/DDoS-HOIC.txt','w')
    benignData = open('BenignDataAll/BenignDDoS-HOIC.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'DDOS attack-HOIC\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def bruteForceWeb():
    count = 0
    dataset = open('originalData/Thursday-22-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/BruteForceWeb.txt','w')
    benignData = open('BenignDataAll/BenignBruteForceWeb.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Brute Force -Web\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    dataset = open('originalData/Friday-23-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/BruteForceWeb.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Brute Force -Web\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count


def bruteForceXSS():
    count = 0
    dataset = open('originalData/Thursday-22-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/BruteForceXSS.txt','w')
    benignData = open('BenignDataAll/BenignBruteForceXSS.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Brute Force -XSS\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    dataset = open('originalData/Friday-23-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/BruteForceXSS.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Brute Force -XSS\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def SQLinjection():
    count = 0
    dataset = open('originalData/Thursday-22-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/SQLinjection.txt','w')
    benignData = open('BenignDataAll/BenignSQLinjection.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'SQL Injection\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    dataset = open('originalData/Friday-23-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/SQLinjection.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'SQL Injection\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def Infiltration():
    count = 0
    dataset = open('originalData/Wednesday-28-02-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/Infiltration.txt','w')
    benignData = open('BenignDataAll/BenignInfiltration.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Infilteration\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    dataset = open('originalData/Thursday-01-03-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/Infiltration.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        if str(auxRow[len(auxRow)-1]) == 'Infilteration\n':
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        elif str(auxRow[len(auxRow)-1]) == 'Benign\n':
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

def Bot():
    count = 0
    dataset = open('originalData/Friday-02-03-2018_TrafficForML_CICFlowMeter.txt','r')
    outdata = open('attacksDataAll/Bot.txt','w')
    benignData = open('BenignDataAll/BenignBot.txt','w')
    for row in dataset:
        auxRow = row.split(',')
        #print(len(auxRow[len(auxRow)-1]))
        if len(auxRow[len(auxRow)-1]) == 5:
            auxRow[len(auxRow)-1] = '1'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            outdata.writelines(finalRow+'\n')
        else:
            auxRow[len(auxRow)-1] = '0'
            finalRow = ''
            index = 1
            for i in auxRow:
                if index <= len(auxRow)-1:
                    finalRow = finalRow + i + ','
                    index = index + 1
                else:
                    finalRow = finalRow + i
            benignData.writelines(finalRow+'\n')
            count = count + 1
    dataset.close()
    outdata.close()
    benignData.close()
    return count

startExtractor()



