import pandas as pd

df = pd.read_csv("./NYC-vehicle-collisions.csv")

def getBoro(boro):
	maxZip = getMax('BOROUGH', boro)
	maxNH = getNeighborhood(maxZip)
	max_str1 = 'and the most accident prone zip code in your borough is ' + str(maxZip)
	max_str2 = 'The most accident prone neighborhood in your borough is ' + str(maxNH)
	
	minZip = getMin('BOROUGH', boro)
	minNH = getNeighborhood(minZip)
	min_str1 = 'and the least accident prone zip code in your borough is ' + str(minZip)
	min_str2 = 'The least accident prone neighborhood in your borough is ' + str(minNH)
	
	whole = max_str2 + '\n' + max_str1 + '\n' + min_str2 + '\n' + min_str1
	return whole

def getMax(intype, inthing):
	myBoro = df.loc[(df[intype] == inthing)]
	maxZip = int(myBoro["ZIP CODE"].value_counts().idxmax())
	return maxZip

def getMin(intype, inthing):
	myBoro = df.loc[(df[intype] == inthing)]
	minZip = int(myBoro["ZIP CODE"].value_counts().idxmin())
	return minZip	
		
def getNeighborhood(zc):
	zipdf = pd.read_csv("./NYC-ZIP-NEIGHBORHOODS.csv")
	zipdict = zipdf.set_index('ZIP CODES')['NEIGHBORHOOD'].to_dict()
	try:
		deadNH = zipdict[zc]
	except KeyError:
		deadNH = 'not found in our dictionary'
	return deadNH
