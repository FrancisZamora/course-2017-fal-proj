import urllib.request
import json
import dml
import prov.model
import datetime
import uuid
import requests
import geojson
from tqdm import tqdm
import pdb
import scipy.stats

class BudgetCalculator(dml.Algorithm):
    contributor = 'francisz_jrashaan'
    
    reads = ['francisz_jrashaan.neighborhoodScores']
    
    writes = ['francisz_jrashaan.optimalScore']
    
    def takeFirst(elem):
        return elem[0]
    
    @staticmethod
    def execute(trial = False):
        startTime = datetime.datetime.now()
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('francisz_jrashaan','francisz_jrashaan')

        data = [('North End', [0, 3, 236, 240]), ('Bay Village', [0, 0, 24, 42]), ('East Boston', [0, 19, 222, 3544]), ('Leather District', [8, 8, 34, 43]), ('Allston', [0, 1, 1888, 1994]), ('Hyde Park', [0, 0, 569, 1163]), ('Roslindale', [0, 0, 450, 608]), ('Charlestown', [0, 7, 189, 455]), ('Back Bay', [4, 17, 432, 817]), ('South End', [0, 0, 116, 150]), ('Downtown', [4, 33, 160, 420]), ('Dorchester', [0, 7, 1382, 3710]), ('South Boston Waterfront', [15, 7, 102, 222]), ('West Roxbury', [0, 0, 559, 708]), ('Longwood Medical Area', [0, 11, 136, 154]), ('Mission Hill', [0, 11, 135, 161]), ('Roxbury', [0, 7, 315, 525]), ('Beacon Hill', [1, 16, 149, 391]), ('Mattapan', [0, 0, 348, 627]), ('Harbor Islands', [0, 0, 0, 155]), ('Brighton', [0, 0, 983, 1466]), ('South Boston', [0, 1, 410, 1061]), ('West End', [0, 5, 387, 549]), ('Fenway', [4, 21, 893, 1034]), ('Chinatown', [11, 21, 74, 112]), ('Jamaica Plain', [0, 0, 356, 919])]
        scores = []
        newdata = []
        for i in data:
            temp = i[1]
            score += temp[0] * 7 + temp[1] * 3 + temp[2] * 5
            scores += [(score, i[0], i[1])]
        
        
        scores.sort(key=takeFirst)
        average = 0
        count = 0
        for i in scores:
            average += i[0]
            count += 1
        average = average / count
        budget = 1000000
        Cstation = 7000
        Hstation = 3000
        Bnetwork = 10000
        flag = True
        while(flag):
            lowest = scores[0]

    


    @staticmethod
    def provenance(doc = prov.model.ProvDocument(), startTime = None, endTime = None):
        '''
            Create the provenance document describing everything happening
            in this script. Each run of the script will generate a new
            document describing that invocation event.
        '''
        
        # Set up the database connection.
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('francisz_jrashaan', 'francisz_jrashaan')
        doc.add_namespace('alg', 'http://datamechanics.io/algorithm/') # The scripts are in <folder>#<filename> format.
        doc.add_namespace('dat', 'http://datamechanics.io/data/') # The data sets are in <user>#<collection> format.
        doc.add_namespace('ont', 'http://datamechanics.io/ontology#') # 'Extension', 'DataResource', 'DataSet', 'Retrieval', 'Query', or 'Computation'.
        doc.add_namespace('log', 'http://datamechanics.io/log/') # The event log.
        doc.add_namespace('bdp', 'http://bostonopendata-boston.opendata.arcgis.com/')
        
        
        this_script = doc.agent('alg:francisz_jrashaan#Correlation', {prov.model.PROV_TYPE:prov.model.PROV['SoftwareAgent'], 'ont:Extension':'py'})
        resource_neighborhoodscores = doc.entity('dat:francisz_jrashaan#NeighborhoodScores', {'prov:label':'Neighborhood Scores', prov.model.PROV_TYPE:'ont:DataResource', 'ont:Extension':'BSON'})
        
        compute_budget = doc.activity('log:uuid'+str(uuid.uuid4()), startTime, endTime)
        

        doc.wasAssociatedWith(compute_budget, this_script)
       
        doc.usage(compute_correlation, resource_neighborhood, startTime, None, {prov.model.PROV_TYPE:'ont:Used for Computation'})
     
                  
        optimalscore = doc.entity('dat:francisz_jrashaan#optimalScore', {prov.model.PROV_LABEL:'Correlation Score', prov.model.PROV_TYPE:'ont:DataSet'})
        doc.wasAttributedTo(optimalscore, this_script)
        doc.wasGeneratedBy(optimalscore, compute_budget, endTime)
        doc.wasDerivedFrom(optimalscore, resource_neighborhood, compute_budget, compute_budget, compute_budgets)
                  
        repo.logout()
                  
        return doc
BudgetCalculator.execute()
doc = constraint.provenance()
#print(doc.get_provn())
#print(json.dumps(json.loads(doc.serialize()), indent=4))

## eof

