#!/usr/bin/python

import cPickle as pickle
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import sys

sys.stderr.write("Started mapper.\n");

def word_feats(words):
    # Turn a string into a list of feature words
    return dict([(word, True) for word in words])

def main(argv):
    # Classifier trained with example from:
    # http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
    classifier = pickle.load(open("movclass.p", "r"))
    
    for line in sys.stdin:
        # split line into words and test with classifier
        tolk_posset = word_tokenize(line.rstrip())
        d = word_feats(tolk_posset)
        subjgen = line.lower()
        if (subjgen.find("hilary")!= -1 or subjgen.find("clinton")!= -1):
            print "LongValueSum:" + " Hilary Clinton" + ": " + classifier.classify(d) + "\t" + "1"
        if (subjgen.find("donald")!= -1 or subjgen.find("trump")!= -1):
            print "LongValueSum:" + " Donald Trump" + ": " + classifier.classify(d) + "\t" + "1"
        if (subjgen.find("ben")!= -1 or subjgen.find("carson")!= -1):
            print "LongValueSum:" + " Ben Carson" + ": " + classifier.classify(d) + "\t" + "1"
        if (subjgen.find("bernie")!= -1 or subjgen.find("sanders")!= -1):
            print "LongValueSum:" + " Bernie Sanders" + ": " + classifier.classify(d) + "\t" + "1"

if __name__ == "__main__":
    main(sys.argv)




