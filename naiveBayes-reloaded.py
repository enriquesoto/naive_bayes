from __future__ import division
import collections
import math
 
class Model: 
        def __init__(self, dataFile):
                self.trainingFile = dataFile
                self.features = {}      #all feature names and their possible values (including the class label)
                self.featureNameList =[]      #this is to maintain the order of features as in the arff
                self.featureCounts = collections.defaultdict(lambda: 1)#contains tuples of the form (label, feature_name, feature_value)
                self.featureVectors = []        #contains all the values and the label as the last entry
                self.labelCounts = collections.defaultdict(lambda: 0)   #these will be smoothed later
                self.numeroClasses =  {}
                self.matrix = []

        def TrainClassifier(self):
                #print "hello"
                #print self.featureNameList
                self.numeroClases = len(self.features['class'])
                #print self.features[self.featureNameList[0]]
                
                for i in range(len(self.featureNameList)-1):
                        valoresPorAtributo = len(self.features[self.featureNameList[i]])
                        self.matrix.append ([[0 for x in xrange(self.numeroClases)] for x in xrange(valoresPorAtributo)])  #columnas x fila

                # for row in self.featureVectors:
                #         #indexClass = len(row)-1
                #         for item in row:
                #                 print item 
                
                                
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
        model = Model("tennis.arff")
        model.GetValues()
        model.TrainClassifier()
        #print model.features['outlook'].index('rain')
        #print model.featureNameList.index('temperature')
        print model.matrix
        # model.TrainClassifier()
        # model.TestClassifier("tennis.arff")