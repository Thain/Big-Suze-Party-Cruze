import pandas as pd

df = pd.read_csv("./NYC-vehicle-collisions.csv")

def getBoro(boro):
	maxZip = getMax('BOROUGH', boro)
	maxNH = getNeighborhood(maxZip)
	maxCas = getCasualties(maxZip)
	max_str1 = 'and the most accident prone zip code is ' + str(maxZip) + ' with ' + maxCas + ' casualties.'
	max_str2 = 'The most accident prone neighborhood in your borough is ' + str(maxNH)
	
	minZip = getMin('BOROUGH', boro)
	minNH = getNeighborhood(minZip)
	minCas = getCasualties(minZip)
	min_str1 = 'and the least accident prone zip code is ' + str(minZip) + ' with ' + minCas + ' casualties.'
	min_str2 = 'The least accident prone neighborhood in your borough is ' + str(minNH)
	
	whole = max_str2 + '\n' + max_str1 + '\n' + min_str2 + '\n' + min_str1
	return whole

def getVehi(veh):
	maxZip = getMax('VEHICLE', veh)
	maxNH = getNeighborhood(maxZip)
	maxCas = getCasualties(maxZip)
	max_str1 = 'and the most accident prone zip code is ' + str(maxZip) + ' with ' + maxCas + ' casualties.'
	max_str2 = 'The most accident prone neighborhood for your vehicle is ' + str(maxNH)
	
	minZip = getMin('VEHICLE', veh)
	minNH = getNeighborhood(minZip)	
	minCas = getCasualties(maxZip)
	min_str1 = 'and the least accident prone zip code  is ' + str(minZip) + ' with ' + minCas + ' casualties.'
	min_str2 = 'The least accident prone neighborhood for your vehicle is ' + str(minNH)
	
	whole = max_str2 + '\n' + max_str1 + '\n' + min_str2 + '\n' + min_str1
	return whole

def getMax(intype, inthing):
	myIn = df.loc[(df[intype] == inthing)]
	maxZip = int(myIn['ZIP CODE'].value_counts().idxmax())
	return maxZip

def getMin(intype, inthing):
	myIn = df.loc[(df[intype] == inthing)]
	minZip = int(myIn['ZIP CODE'].value_counts().idxmin())
	return minZip	
		
def getNeighborhood(zc):
	zipdf = pd.read_csv("./NYC-ZIP-NEIGHBORHOODS.csv")
	zipdict = zipdf.set_index('ZIP CODES')['NEIGHBORHOOD'].to_dict()
	try:
		deadNH = zipdict[zc]
	except KeyError:
		deadNH = 'not found in our dictionary'
	return deadNH

def getCasualties(zc):
	zipcas = df.loc[(df['ZIP CODE'] == zc)]
	casualties = zipcas['PERSONS INJURED'].sum()
	casualties += zipcas['PERSONS KILLED'].sum()
	if casualties != 0:
		return str(casualties)
	else:
		return 'undocumented'
	
