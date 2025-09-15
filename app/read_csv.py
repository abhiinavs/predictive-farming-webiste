import csv

from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
x=[]
y=[]
dlabels=[]

with open('C:\\Users\\sidha\\OneDrive\\Desktop\\predictive_farming (2)\\predictive_farming\\app\\Crop_recommendation.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    i=0
    for lines in csvFile:
        # print(lines)

        if i!=0:
            r=[]
            for j in range(7):
                r.append(float(lines[j]))
            x.append(r)
            if lines[7] not in dlabels:
                dlabels.append(lines[7])

            y.append(dlabels.index(lines[7]))
        i=i+1
print(x)
print(dlabels)
print(y)


# def predict_crop():
#     from sklearn.model_selection import train_test_split
#     X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#
#     # neigh =linear_model.LogisticRegression()
#     # neigh = KNeighborsClassifier(n_neighbors=3)
#     # print(neigh)
#     # f=neigh.fit(X_train, y_train)
#     # print(f)
#     # from sklearn.tree import DecisionTreeClassifier
#     # dtree = DecisionTreeClassifier()
#     # dtree = dtree.fit(X_train, y_train)
#     # y_pred=dtree.predict(X_test)
#     from sklearn.ensemble import RandomForestClassifier
#
#     clf = RandomForestClassifier(n_estimators=100)
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)

def random_forest(t1,t2,t3,t4,t5,t6,t7):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    lst=[[t1,t2,t3,t4,t5,t6,t7]]
    lst=np.array(lst)
    lst.reshape(-1,1)

    rfc_predict = rfc.predict(lst)
    print(dlabels)
    print("----------------------------------")
    print(dlabels[rfc_predict[0]])
    ab = rfc.score(X_test, y_test)
    return str(dlabels[rfc_predict[0]])