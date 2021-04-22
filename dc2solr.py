'''
reads in XML files with DublinCore records and prepares them
to be ingested by Solr retrieval system

XML files are one per record, and the follows the OAI-PMH spec

'''
from glob import glob
from lxml import etree
import requests

# namespaces for parsing XML DC
namespaces = {'dc':'http://purl.org/dc/elements/1.1/', 'rdf':'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
fields=['dc:title','dc:creator','dc:subject','dc:description',
	'dc:publisher', 'dc:contributor', 'dc:date', 'dc:type', 'dc:format', 'dc:identifier',
	'dc:source','dc:language', 'dc:relation', 'dc:coverage', 'dc:rights']

pathin='/home/figue/e-lis/xml'
for filepath in glob(pathin+'/*'):
	r=etree.parse(filepath)
	# getting fields, note that they could be multivalued
	thisrecord={}
	for field in fields:
		values=[v.text for v in r.findall('.//'+field, namespaces)]
		thisrecord[field]=values

	#---- print just to make visual checks ---
	print(filepath)
	for field in sorted(thisrecord.keys()):
		print(field,':', thisrecord[field])
	print('==============================')
	#-----
	# translate to Solr fields and save in files
