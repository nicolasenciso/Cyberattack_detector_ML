import  pandas as  pd
import  numpy  as  np
import matplotlib.pyplot as plt
from threading import Thread
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#from StackOverflow to get return values from a thread
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return

#importing the dataset
dataset = pd.read_csv('DATASET.csv')
X = dataset.iloc[:,3:-1].values
y = dataset.iloc[:,79]

#missing data treatment
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X)
X = imputer.transform(X)

#feature scaling
scaler_X = StandardScaler()
X = scaler_X.fit_transform(X)

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


def bayesClassifierGaussian(X_entreno, y_entreno, X_testeo, y_testeo, name):
    model = GaussianNB()
    model.fit(X_entreno,y_entreno)
    predicted_labels = model.predict(X_testeo)
    listPredicted = predicted_labels.tolist()
    listGivenTest = y_testeo.tolist()
    accuracy = accuracy_score(y_testeo, predicted_labels)
    """print("****** PREDICTED MODEL ********")
    print(predicted_labels)
    print("********* TEST MODEL ************")
    print(y_testeo)"""
    print("\n*** ACCURACY GAUSSIAN BAYES **************")
    print(accuracy)
    print("\n ***** RESULTS BAYES GAUSSIAN "+str(name)+"********\n")
    print(confusion_matrix(y_testeo,predicted_labels))  
    print(classification_report(y_testeo,predicted_labels))
    #y_pred_prob = model.predict_proba(X_testeo)[:,0] PARA COMPROBAR RESULTADOS
    #print(y_pred_prob)
    y_pred_prob = model.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC BAYES GAUSSIAN "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)


def logisticReg(X_entreno,y_entreno,X_testeo, y_testeo,name):
    logreg = LogisticRegression()
    logreg.fit(X_entreno, y_entreno)
    y_pred_class = logreg.predict(X_testeo)
    print("\n ***** RESULTS LOGISTIC REGRESSION "+str(name)+"********\n")
    print(confusion_matrix(y_testeo,y_pred_class)) 
    print(classification_report(y_testeo,y_pred_class))
    print("\n*** ACCURACY **************")
    accuracy = accuracy_score(y_testeo, y_pred_class)
    print(accuracy)
    y_pred_prob = logreg.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC LOGISCTIC REGRESSION "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)

def randomForest(X_entreno,y_entreno,X_testeo, y_testeo,name):
    classifier=RandomForestClassifier(n_estimators=100)
    classifier=classifier.fit(X_entreno,y_entreno)
    predictions=classifier.predict(X_testeo)
    print("\n ***** RESULTS RANDOM FOREST "+str(name)+"********\n")
    print(confusion_matrix(y_testeo,predictions)) 
    print(classification_report(y_testeo,predictions))
    print("\n*** ACCURACY **************")
    accuracy = accuracy_score(y_testeo, predictions)
    print(accuracy)
    y_pred_prob = classifier.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC RANDOM FOREST "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)

def SVMgaussian(X_entreno,y_entreno,X_testeo, y_testeo, name):
    c = 1.11
    gamma = 0.09
    svclassifier = SVC(kernel='rbf', C=c, gamma=gamma, probability=True)
    svclassifier.fit(X_entreno,y_entreno)
    y_pred = svclassifier.predict(X_testeo)
    print("\n ***** RESULTS SVM GAUSSIAN C="+str(c)+" gamma="+str(gamma)+"*****"+str(name)+"***\n")
    print(confusion_matrix(y_testeo,y_pred))  
    print(classification_report(y_testeo,y_pred))
    print("\n*** ACCURACY **************")
    accuracy = accuracy_score(y_testeo, y_pred)
    print(accuracy)
    y_pred_prob = svclassifier.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC SVM GAUSSIAN "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)

def SVMlineal(X_entreno,y_entreno,X_testeo, y_testeo,name):
    svclassifier = SVC(kernel='linear', probability=True)
    svclassifier.fit(X_entreno,y_entreno)
    y_pred = svclassifier.predict(X_testeo)
    print("\n ***** RESULTS SVM LINEAR "+str(name)+"********\n")
    print(confusion_matrix(y_testeo,y_pred))  
    print(classification_report(y_testeo,y_pred)) 
    print("\n*** ACCURACY **************")
    accuracy = accuracy_score(y_testeo, y_pred)
    print(accuracy)
    y_pred_prob = svclassifier.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC SVM LINEAR "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)

def SVMpolynomial(X_entreno,y_entreno,X_testeo, y_testeo, name):
    svclassifier = SVC(kernel='poly', probability=True)
    svclassifier.fit(X_entreno,y_entreno)
    y_pred = svclassifier.predict(X_testeo)
    print("\n ***** RESULTS SVM POLYNOMIAL "+str(name)+"********\n")
    print(confusion_matrix(y_testeo,y_pred))  
    print(classification_report(y_testeo,y_pred))
    print("\n*** ACCURACY **************")
    accuracy = accuracy_score(y_testeo, y_pred)
    print(accuracy)
    y_pred_prob = svclassifier.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC SVM POLYNOMIAL "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)

def SVMsigmoid(X_entreno,y_entreno,X_testeo, y_testeo,name):
    svclassifier = SVC(kernel='sigmoid', probability=True)
    svclassifier.fit(X_entreno,y_entreno)
    y_pred = svclassifier.predict(X_testeo)
    print(y_pred)
    print(y_testeo)
    print("\n ***** RESULTS SVM SIGMOID "+str(name)+"********\n")
    print(confusion_matrix(y_testeo,y_pred)) 
    print(classification_report(y_testeo,y_pred))
    print("\n*** ACCURACY **************")
    accuracy = accuracy_score(y_testeo, y_pred)
    print(accuracy)
    y_pred_prob = svclassifier.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC SVM SIGMOID "+str(name)+" *********")
    print(auc)
    return (fpr,tpr)

def plottingROC(fpr):
    fig, ax = plt.subplots()
    ax.plot(fpr[0][0], fpr[0][1], 'purple', label='NB-Gaussian')
    ax.plot(fpr[1][0], fpr[1][1], 'blue', label='LogReg')
    ax.plot(fpr[2][0], fpr[2][1], 'green', label='RandForest')
    ax.plot(fpr[3][0], fpr[3][1], 'red', label='SVM-Gauss')
    ax.plot(fpr[4][0], fpr[4][1], 'brown', label='SVM-lineal')
    ax.plot(fpr[5][0], fpr[5][1], 'grey', label='SVM-poly')
    ax.plot(fpr[6][0], fpr[6][1], 'darkgreen', label='SVM-sigmoid')
    leg = ax.legend()
    ax.legend(loc='lower right', frameon=True)
    plt.title('ROC curve ML classifier')
    plt.xlabel('False Positive Rate (1 - Specificity)')
    plt.ylabel('True Positive Rate (Sensitivity)')
    plt.grid(True)
    plt.savefig('ROC.png')


def startClassifier(X_entreno, y_entreno, X_testeo, y_testeo, name):
    ROC = open('ROCnoMulti.txt','w')
    bayGauss = ThreadWithReturnValue(target=bayesClassifierGaussian, args=(X_train,y_train,X_test,y_test, "bayesGauss"))
    logreg = ThreadWithReturnValue(target=logisticReg, args=(X_train,y_train,X_test,y_test, "LogReg"))
    ranfor = ThreadWithReturnValue(target=randomForest, args=(X_train,y_train,X_test,y_test, "RandForest"))
    svmGauss = ThreadWithReturnValue(target=SVMgaussian, args=(X_train,y_train,X_test,y_test, "svmGauss"))
    svmLineal = ThreadWithReturnValue(target=SVMlineal, args=(X_train,y_train,X_test,y_test, "svmLineal"))
    svmPoly = ThreadWithReturnValue(target=SVMpolynomial, args=(X_train,y_train,X_test,y_test, "svmPoly"))
    svmSig = ThreadWithReturnValue(target=SVMsigmoid, args=(X_train,y_train,X_test,y_test, "svmSig"))

    bayGauss.start()
    logreg.start()
    ranfor.start()
    svmGauss.start()
    svmLineal.start()
    svmPoly.start()
    svmSig.start()

    outBayes = bayGauss.join()
    outlogreg = logreg.join()
    outrandfor = ranfor.join()
    outsvm = svmGauss.join()
    outSVMlineal = svmLineal.join()
    outSVMpoly = svmPoly.join()
    outSVMsig = svmSig.join()
    """
    outBayes = bayesClassifierGaussian(X_train,y_train,X_test,y_test, "bayesGauss")
    outlogreg = logisticReg(X_train,y_train,X_test,y_test, "LogReg")
    outrandfor = randomForest(X_train,y_train,X_test,y_test, "RandForest")
    outsvm = SVMgaussian(X_train,y_train,X_test,y_test, "svmGauss")
    outSVMlineal = SVMlineal(X_train,y_train,X_test,y_test, "svmLineal")
    outSVMpoly = SVMpolynomial(X_train,y_train,X_test,y_test, "svmPoly")
    outSVMsig = SVMsigmoid(X_train,y_train,X_test,y_test, "svmSig")
    """
    ROC.writelines(str(outBayes[0].tolist())+'#'+str(outBayes[1].tolist())+'\n')
    ROC.writelines(str(outlogreg[0].tolist())+'#'+str(outlogreg[1].tolist())+'\n')
    ROC.writelines(str(outrandfor[0].tolist())+'#'+str(outrandfor[1].tolist())+'\n')
    ROC.writelines(str(outsvm[0].tolist())+'#'+str(outsvm[1].tolist())+'\n')
    ROC.writelines(str(outSVMlineal[0].tolist())+'#'+str(outSVMlineal[1].tolist())+'\n')
    ROC.writelines(str(outSVMpoly[0].tolist())+'#'+str(outSVMpoly[1].tolist())+'\n')
    ROC.writelines(str(outSVMsig[0].tolist())+'#'+str(outSVMsig[1].tolist())+'\n')

    ROC.close()
    ROC = open('ROCnoMultiGauss.txt','r')
    fprs = []
    for line in ROC:
        newLine = line.split('#') #to get points from txt and put it in fprs array
        fpr = newLine[0]
        tpr = newLine[1]
        fpr = fpr.split('[')
        tpr = tpr.split('[')
        fpr = str(fpr[1])
        tpr = str(tpr[1])
        fpr = fpr.split(']')
        tpr = tpr.split(']')
        fpr = str(fpr[0])
        tpr = str(tpr[0])
        fpr = fpr.split(',')
        tpr = tpr.split(',')
        newTpr = []
        newFpr = []
        for point in tpr:
            newTpr.append(float(point))
        for point in fpr:
            newFpr.append(float(point))
        fprs.append((newFpr,newTpr))
    ROC.close()
    plottingROC(fprs)


startClassifier(X_train, X_test, y_train, y_test, "IDS Dataset")











