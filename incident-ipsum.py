#Incident Ipsum 
# An adaptation of the tutorial: https://www.youtube.com/watch?v=iLS4Hk-kJXE

from random import randint

incident_jargon = [ "redeploying", "API", "intgration", "cloudwatch", "expired certificate", "baseline", "availability zones", "security group", "failure", "monitoring", "alert", "AWS","Azure","terraform","cloud formation script","postgres","load balancer", "endpoint", "threads", "application", "fatal", "roll back", "maintenance page", "devops", "404 error", "403 error", "500 error", "docker","container", "microservice", "object durability", "Lambda","versioning","firewall","credentials","isolating","root cause","iterating","cluster","mount","logs","feature toggle","database"]

def incidentize (word):
	translate_or_not = randint(0,4)
	if translate_or_not > 1:
		return word
	else:
		index = randint(0,len(incident_jargon) -1)
		replacement = incident_jargon[index]
		if word.istitle() == True and replacement.istitle() == False:
			return replacement.capitalize()
		return replacement

paragraphs = int(input("How many paragraphs of incident text do you need:"))

with open('cicero.txt') as original:
	elements = original.read().split()

	for x in range(paragraphs):
		incident_text = list( map(incidentize,elements))
		print(" ".join(incident_text) + '\n\n')
