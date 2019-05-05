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

def bayesClassifierMultinomial(X_entreno, y_entreno, X_testeo, y_testeo,name):
    model = MultinomialNB()
    model.fit(X_entreno,y_entreno)
    predicted_labels = model.predict(X_testeo)
    accuracy = accuracy_score(y_testeo, predicted_labels)
    listPredicted = predicted_labels.tolist()
    listGivenTest = y_testeo.tolist()
    print("\n*** ACCURACY MULTINOMIAL BAYES **************")
    print(accuracy)
    print("\n ***** RESULTS BAYES MULTINOMIAL "+str(name)+" ********\n")
    print(confusion_matrix(y_testeo,predicted_labels))  
    print(classification_report(y_testeo,predicted_labels))
    y_pred_prob = model.predict_proba(X_testeo)[:,1]
    fpr, tpr, thresholds = roc_curve(y_testeo, y_pred_prob)
    auc = roc_auc_score(y_testeo, y_pred_prob)
    print("****** AUC BAYES MULTINOMIAL "+str(name)+" *********")
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


def plottingROC(fpr):
    fig, ax = plt.subplots()
    ax.plot(fpr[0][0], fpr[0][1], 'purple', label='NB-Gaussian')
    ax.plot(fpr[1][0], fpr[1][1], 'blue', label='LogReg')
    ax.plot(fpr[2][0], fpr[2][1], 'green', label='RandForest')
    #ax.plot(fpr[3][0], fpr[3][1], 'orange', label='NB-Multinomial')
    leg = ax.legend()
    ax.legend(loc='lower right', frameon=True)
    plt.title('ROC curve ML classifier')
    plt.xlabel('False Positive Rate (1 - Specificity)')
    plt.ylabel('True Positive Rate (Sensitivity)')
    plt.grid(True)
    plt.savefig('ROCnoSVMnoMulti.png')


def startClassifier(X_entreno, y_entreno, X_testeo, y_testeo, name):
    ROC = open('ROC.txt','w')
    bayGauss = ThreadWithReturnValue(target=bayesClassifierGaussian, args=(X_train,y_train,X_test,y_test, "bayesGauss"))
    logreg = ThreadWithReturnValue(target=logisticReg, args=(X_train,y_train,X_test,y_test, "LogReg"))
    ranfor = ThreadWithReturnValue(target=randomForest, args=(X_train,y_train,X_test,y_test, "RandForest"))
    #bayMilti = ThreadWithReturnValue(target=bayesClassifierMultinomial, args=(X_train,y_train,X_test,y_test, "bayesMultinomial"))

    bayGauss.start()
    #bayMilti.start()
    logreg.start()
    ranfor.start()
  
    outBayes = bayGauss.join()
    #outMulti = bayMilti.join()
    outlogreg = logreg.join()
    outrandfor = ranfor.join()
    
    ROC.writelines(str(outBayes[0].tolist())+'#'+str(outBayes[1].tolist())+'\n')
    ROC.writelines(str(outlogreg[0].tolist())+'#'+str(outlogreg[1].tolist())+'\n')
    ROC.writelines(str(outrandfor[0].tolist())+'#'+str(outrandfor[1].tolist())+'\n')
    #ROC.writelines(str(outMulti[0].tolist())+'#'+str(outMulti[1].tolist())+'\n')

    ROC.close()
    ROC = open('ROC.txt','r')
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











