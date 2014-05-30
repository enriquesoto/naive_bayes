from __future__ import division
import collections
import math
import numpy as np
 
class Model: 
        def __init__(self, TrainingDataFile):
                self.trainingFile = TrainingDataFile
                self.features = {}      #all feature names and their possible values (including the class label)
                self.featureNameList =[]      #this is to maintain the order of features as in the arff
                self.featureCounts = collections.defaultdict(lambda: 1)#contains tuples of the form (label, feature_name, feature_value)
                self.featureVectors = []        #contains all the values and the label as the last entry
                self.labelCounts = collections.defaultdict(lambda: 0)   #these will be smoothed later
                self.lookuptable = []
                self.lookuptableClasses = []
                self.testVector = []  #contains all testing data
                




        def TrainClassifier(self):
                #print "hello"
                #print self.featureNameList
                self.numeroClases = len(self.features['class'])
                self.lookuptableClasses = [ 0 for i in range(self.numeroClases)]
                #print self.features[self.featureNameList[0]]
                
                for i in range(len(self.featureNameList)-1):
                        valoresPorAtributo = len(self.features[self.featureNameList[i]])
                        self.lookuptable.append ([[0 for x in xrange(self.numeroClases)] for x in xrange(valoresPorAtributo)])  #column x row of zeros

                for row in self.featureVectors:
                        indexOfColumClass = row[len(row)-1] #getting value of this record's class i.e "yes" "no" classes
                        indexOfrowClass = self.features['class'].index(indexOfColumClass) # getting index of this record class to add up into look-up table
                        self.lookuptableClasses[indexOfrowClass] = self.lookuptableClasses[indexOfrowClass] + 1 # counting occurrences of the classes
                        # print rowClass
                        for i in range(len(row)-1):
                                attributeIndex=self.features[self.featureNameList[i]].index(row[i])
                                self.lookuptable[i][attributeIndex][indexOfrowClass] =  self.lookuptable[i][attributeIndex][indexOfrowClass] +1 # making look-up table
        
        def Testing(self,TestingDataFile):

                file = open(TestingDataFile, 'r')

                for line in file:
                        self.testVector.append(line.strip().lower().split(','))

                file.close()
                #prediction algorithm


                for row in self.testVector:
                        
                        probabilityMatrixClass =np.matrix([ 1 for i in range(self.numeroClases)])
                        evidenceValue = 1
                        for i in range(len(row)):
                                attributeIndex=self.features[self.featureNameList[i]].index(row[i])
                                evidenceValue=np.sum(self.lookuptable[i][attributeIndex])/np.sum(self.lookuptableClasses)*evidenceValue
                                
                                #print attributeIndex
                                currentVector= np.divide(self.lookuptable[i][attributeIndex],np.matrix(self.lookuptableClasses)+0.)
                                probabilityMatrixClass = np.multiply(probabilityMatrixClass,currentVector)
                                #print probabilityMatrixClass
                        probabilityMatrixClass = np.multiply(self.lookuptableClasses,probabilityMatrixClass)
                        
                        probabilityMatrixClass = np.divide(probabilityMatrixClass,np.sum(self.lookuptableClasses))
                        print np.divide(probabilityMatrixClass,evidenceValue)


                                

                     
        
        def GetValues(self):
                file = open(self.trainingFile, 'r')
                for line in file:
                        if line[0] != '@':  #start of actual data
                                self.featureVectors.append(line.strip().lower().split(','))
                        else:   #feature definitions
                                if line.strip().lower().find('@data') == -1 and (not line.lower().startswith('@relation')):
                                        self.featureNameList.append(line.strip().split()[1])
                                        self.features[self.featureNameList[len(self.featureNameList) - 1]] = line[line.find('{')+1: line.find('}')].strip().split(',')

                file.close()
 
        # def TestClassifier(self, arffFile):
        #         file = open(arffFile, 'r')
        #         for line in file:
        #                 if line[0] != '@':
        #                         vector = line.strip().lower().split(',')
        #                         print "classifier: " + self.Classify(vector) + " given " + vector[len(vector) - 1]                                
		
if __name__ == "__main__":
        model = Model("car.data")
        model.GetValues()
        model.TrainClassifier()
        #print model.features['outlook'].index('rain')
        #print model.featureNameList.index('temperature')
        #print model.lookuptable
        #print model.featureVectors
        model.Testing("car-prueba.data")
        #print model.lookuptableClasses

        # model.TrainClassifier()
        # model.TestClassifier("tennis.arff")