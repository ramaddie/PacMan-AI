from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def Q5():
    print "\nStarting Q5 Test Part 1: Car Data"
    print "Will run NN for 5 iterations with Random restarts \n"
    i = 0
    testAcc = []
    while i < 5:
        print "Starting iteration: ", i
        NN, testAccuracy = testCarData()
        print "Test accuracy is:", testAccuracy
        testAcc.append(testAccuracy)
        i += 1
    print "Average Test Accuracy of the 5 NNs for Car Data is: ", average(testAcc)  
    print "St.Dev of the 5 NNs for Car Data is: ", stDeviation(testAcc)
    print "Max Test Accuracy of the 5 NNs for Car Data is: ", max(testAcc)

    print "=========================================================================="
    print "\nStarting Q5 Test Part 2: Pen Data"
    print "Will run NN for 5 iterations with Random restarts \n"
    i = 0
    testAcc = []
    while i < 5:
        print "Starting iteration: ", i
        NN, testAccuracy = testPenData()
        print "Test accuracy is:", testAccuracy
        testAcc.append(testAccuracy)
        i += 1
    print "Average Test Accuracy of the 5 NNs for Pen Data is: ", average(testAcc)  
    print "St.Dev of the 5 NNs for Pen Data: ", stDeviation(testAcc)
    print "Max Test Accuracy of the 5 NNs for Pen Data is: ", max(testAcc)

    print "FINISHED!\n"

def Q6():
    print "\nStarting Q6 Test Part 1: Car Data"
    print "Will run NN for 5 iterations with increasing Num of Perceptrons from 0 - 40\n"

    numPerc = 0
    while numPerc <= 40:
        print "Have set number of perceptrons to: ", numPerc
        i = 0
        testAcc = []
        while i < 5:
            print "Starting iteration: ", i
            NN, testAccuracy = testCarData(hiddenLayers = [numPerc])
            print "Test accuracy for this iteration is:", testAccuracy
            testAcc.append(testAccuracy)
            i += 1
        print "All 5 iteration have been run with number of perceptrons equal to", numPerc
        print "\nAverage Test Accuracy of the 5 NNs for Car Data is: ", average(testAcc)  
        print "St.Dev of the 5 NNs for Car Data is: ", stDeviation(testAcc)
        print "Max Test Accuracy of the 5 NNs for Car Data is: ", max(testAcc)
        numPerc += 5
        
    print "=========================================================================="
    print "\nStarting Q6 Test Part 2: Pen Data"
    print "Will run NN for 5 iterations with increasing Num of Perceptrons from 0 - 40\n"
    
    numPerc = 0
    while numPerc <= 40:
        print "Have set number of perceptrons to: ", numPerc
        i = 0
        testAcc = []
        while i < 5:
            print "Starting iteration: ", i
            NN, testAccuracy = testPenData(hiddenLayers = [numPerc])
            print "Test accuracy for this iteration is:", testAccuracy
            testAcc.append(testAccuracy)
            i += 1
        print "All 5 iteration have been run with number of perceptrons equal to", numPerc
        print "\nAverage Test Accuracy of the 5 NNs for Pen Data is: ", average(testAcc)  
        print "St.Dev of the 5 NNs for Pen Data is: ", stDeviation(testAcc)
        print "Max Test Accuracy of the 5 NNs for Pen Data is: ", max(testAcc)
        numPerc += 5

    print "FINISHED!\n"


