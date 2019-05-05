#Dst Port,Protocol,Timestamp,Flow Duration,Tot Fwd Pkts,Tot Bwd Pkts,TotLen Fwd Pkts,TotLen Bwd Pkts,Fwd Pkt Len Max,Fwd Pkt Len Min,Fwd Pkt Len Mean,Fwd Pkt Len Std,Bwd Pkt Len Max,Bwd Pkt Len Min,Bwd Pkt Len Mean,Bwd Pkt Len Std,Flow Byts/s,Flow Pkts/s,Flow IAT Mean,Flow IAT Std,Flow IAT Max,Flow IAT Min,Fwd IAT Tot,Fwd IAT Mean,Fwd IAT Std,Fwd IAT Max,Fwd IAT Min,Bwd IAT Tot,Bwd IAT Mean,Bwd IAT Std,Bwd IAT Max,Bwd IAT Min,Fwd PSH Flags,Bwd PSH Flags,Fwd URG Flags,Bwd URG Flags,Fwd Header Len,Bwd Header Len,Fwd Pkts/s,Bwd Pkts/s,Pkt Len Min,Pkt Len Max,Pkt Len Mean,Pkt Len Std,Pkt Len Var,FIN Flag Cnt,SYN Flag Cnt,RST Flag Cnt,PSH Flag Cnt,ACK Flag Cnt,URG Flag Cnt,CWE Flag Count,ECE Flag Cnt,Down/Up Ratio,Pkt Size Avg,Fwd Seg Size Avg,Bwd Seg Size Avg,Fwd Byts/b Avg,Fwd Pkts/b Avg,Fwd Blk Rate Avg,Bwd Byts/b Avg,Bwd Pkts/b Avg,Bwd Blk Rate Avg,Subflow Fwd Pkts,Subflow Fwd Byts,Subflow Bwd Pkts,Subflow Bwd Byts,Init Fwd Win Byts,Init Bwd Win Byts,Fwd Act Data Pkts,Fwd Seg Size Min,Active Mean,Active Std,Active Max,Active Min,Idle Mean,Idle Std,Idle Max,Idle Min,Label
import numpy as np
import threading
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.manifold import Isomap
from mpl_toolkits.mplot3d import Axes3D



#importing the dataset
dataset = pd.read_csv('DATASET.csv')
X = dataset.iloc[:,3:-1].values
Y = dataset.iloc[:,79]

#missing data treatment
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X)
X = imputer.transform(X)

#feature scaling
scaler_X = StandardScaler()
X = scaler_X.fit_transform(X)

#making PCA visualization

def makePCA(X,Y):
    pca = PCA(n_components = 2)
    X_pca = pca.fit_transform(X)
    explained_variance = pca.explained_variance_ratio_
    count = 0
    attackX,attackY,benignX,benignY = [],[],[],[]
    for case in Y:
        if str(case) == '1':
            attackX.append(X_pca[count][0])
            attackY.append(X_pca[count][1])
        elif str(case) == '0':
            benignX.append(X_pca[count][0])
            benignY.append(X_pca[count][1])
        count = count + 1

    plt.figure()
    plt.scatter(x=benignX,y=benignY,c='red',marker='o',label='Benign')
    plt.scatter(x=attackX,y=attackY,c='blue',marker='o',label='Attack')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.title('2-PCA')
    plt.grid()
    plt.savefig('images/PCA.png')

def makeTSNE(X,Y):
    #making t-SNE visualization
    tsne = TSNE(n_components=3, random_state=0)
    x_tsne = tsne.fit_transform(X)
    count = 0
    attackX,attackY,attackZ, benignX,benignY, benignZ = [],[],[],[],[],[]
    for case in Y:
        if str(case) == '1':
            attackX.append(x_tsne[count][0])
            attackY.append(x_tsne[count][1])
            attackZ.append(x_tsne[count][2])
        elif str(case) == '0':
            benignX.append(x_tsne[count][0])
            benignY.append(x_tsne[count][1])
            benignZ.append(x_tsne[count][2])
        count = count + 1

    plt.figure()
    plt.scatter(x=benignX,y=benignY,c='blue',marker='o',label='Benign')
    plt.scatter(x=attackX,y=attackY,c='red',marker='o',label='Attack')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.title('t-SNE')
    plt.grid()
    plt.savefig('images/TSNE.png')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(attackX,attackY,attackZ, c='red',marker ='o',label='Attack')
    ax.scatter(benignX,benignY,benignZ, c='blue',marker ='o',label='Benign')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.title('t-SNE 3D')
    plt.savefig('images/TSNE3D.png')


def makeISOMAP(X,Y):
    X_std = X
    y = Y
    iso = Isomap(n_neighbors=3, n_components=2)
    x_iso = iso.fit_transform(X_std)
    count = 0
    anomalousX,anomalousY,normalX,normalY = [],[],[],[]
    for tipo in y:
        if str(tipo) == '1':
            anomalousX.append(x_iso[count][0])
            anomalousY.append(x_iso[count][1])
        elif str(tipo) == '0':
            normalX.append(x_iso[count][0])
            normalY.append(x_iso[count][1])
        count += 1

    markers=('o', 'o')
    color_map = {0:'red', 1:'blue'}
    plt.figure()
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=x_iso[y==cl,0], y=x_iso[y==cl,1], c=color_map[idx], marker=markers[idx], label=cl)
    plt.xlabel('X in Isomap')
    plt.ylabel('Y in Isomap')
    plt.legend(loc='upper left')
    plt.title('Isomap visualization')
    plt.savefig('images/ISOMAP.png')


def startVisual(X,Y):
    pca = threading.Thread(target=makePCA,args=(X,Y))
    tsne = threading.Thread(target=makeTSNE,args=(X,Y))
    #isomap = threading.Thread(target=makeISOMAP,args=(X,Y))
    pca.start()
    tsne.start()
    #isomap.start()

makePCA(X,Y)
makeTSNE(X,Y)

