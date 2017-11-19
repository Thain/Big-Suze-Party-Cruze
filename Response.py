import pandas as pd

def getResponse(boro):
	pt1 = getZip(boro)
	str1 = 'and the most accident prone zip code in your borough is ' + str(pt1)
	pt2 = getNeighborhood(pt1)
	str2 = 'the most accident prone neighborhood in your borough is ' + str(pt2)
	whole = str2 + '\n' + str1
	return whole

def getZip(boro):
	df = pd.read_csv("./NYC-vehicle-collisions.csv")
	myBoro = df.loc[(df["BOROUGH"] == boro)]
	deadZip = int(myBoro["ZIP CODE"].value_counts().idxmax())
	return deadZip
	
def getNeighborhood(zc):
	zipdf = pd.read_csv("./NYC-ZIP-NEIGHBORHOODS.csv")
	zipdict = zipdf.set_index('ZIP CODES')['NEIGHBORHOOD'].to_dict()
	try:
		deadNH = zipdict[zc]
	except KeyError:
		deadNH = 'not found in our dictionary'
	return deadNH