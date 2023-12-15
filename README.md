# IVDM_A3

### Aufgabenstellung ###

Praktikumsaufgabe IVDA


a) Lesen Sie den Datensatz „titanic.csv“ ein und untersuchen Sie den Zweck der Daten sowie die
Datenqualität. Identifizieren Sie mögliche Probleme in den Daten und beheben Sie die Fehler, falls
möglich. Dokumentieren Sie Ihr Vorgehen.

b) Traininieren Sie die folgende Klassifizierer mit den Daten, erstellen Sie hierfür Trainings- und
Testdatensätze mit den Methoden Crossvalidation mit 10 folds und Bootstraping 0.632:
- Logistische Regression
- Decision Tree
- K-nearest neighbor mit k=3
- 
c) Evaluieren Sie die Performance der Klassifizierer. Berechnen Sie hierfür die notwendigen
statistischen Werte und stellen Sie diese visuell für die Klassfizierer dar. Visualisieren Sie außerdem
die confusion Matrix. Beim Verfahren Decision Tree soll zudem der generierte Baum visuell
dargestellt werden.

### Beschreibung Dataset ###

PassengerId : ID um die Passagiere an Board der Titanic eindeutig zu identifizieren

Survived: 0 für Verunglückt 1 für Überlebt

Name: Name der Passagier:innen

PClass : Es gab 3 Passagierklassen an Board der Titanic , die 1. war die luxuriöseste

Sex: In dem Datensatz gibt es 2 Geschlechter codiert mit male, female

Age: Alter der Passagier:innen

SibSp: Anzahl der Geschwister und Ehepartner an Board 

Parch: Anzahl an Eltern/Kindern dan Board

Cabin: Kabinenbezeichnung

Fare: Wie viel bezahlt für das Ticket

Embarked: Wo sind die Passagiere eingestiegen S = Southhampton Q = Queenstown C= Cherbourg





### Probleme ###

Age: Was machen wir mit denen, die kein Alter haben / Was machen wir mit den Float Werten

Embarked: ID 62, 830 haben kein Value

Cabin: Manche haben mehrere Bezeichnungen Bsp.: ID 873 , ganz viele haben gar keine Kabine

Fare: Manche haben keine Values bzw. 0 Values (ca.20), Integer und Float Werte, welche Einheit , stimmen die Preise kommt mir billig vor


### Carlos notizen ###

Heatmap der numerischen Spalten zur erkennung von ausreißern:  
<img width="397" alt="image" src="https://github.com/lynx5001/IVDM_A3/assets/105308348/fc945123-7951-4521-be1e-fe8fe6f9d955">

Heatmap der boolean Matrix von df.isnull() zur erkennung von ausreißern in nicht numerischen Spalten:  
<img width="378" alt="image" src="https://github.com/lynx5001/IVDM_A3/assets/105308348/8e53036d-857b-4295-9c09-314943317113">

**PassengerId** vollständig  
**Survied** vollständig  
**Pclass** vollständig
**Name**
**Sex**
**Age** unvollständig, float müsste aber int sein
**SibSp** vollständig
**Parch** vollständig
**Ticket** 
**Fare** vollständig
**Cabin** 
**Embarked** enthält zwei "außreißer" (Null values) in Zeile 61 und 


