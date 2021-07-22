'''
reads in XML files with DublinCore records and prepares them
to be ingested by Solr retrieval system

XML files are one per record, and they follows the OAI-PMH spec

'''
from glob import glob
from lxml import etree
from sys import argv, exit

def help():
	# just print some info about the use of the script
	# end exit
	print('''
	usage: python3 dc2solr.py  -i input_folder -o output folder
	input_folder is the path to the folder with XML records
	ouput_folder es the path for saving recoreds ready for Solr
	if not -o output_folder is provided, output is done trough the screen,
	just for check pourposes
	''')
	exit(88)

# namespaces for parsing XML DC
namespaces = {'dc':'http://purl.org/dc/elements/1.1/', 'rdf':'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
fields=['dc:title','dc:creator','dc:subject','dc:description',
	'dc:publisher', 'dc:contributor', 'dc:date', 'dc:type', 'dc:format', 'dc:identifier',
	'dc:source','dc:language', 'dc:relation', 'dc:coverage', 'dc:rights']

# catching arguments
pathin=''
pathout=''
if len(argv) < 2:
	help()
try:
	for e in range(1, len(argv)):
		if argv[e]=='-i':
			pathin=argv[e+1]
		elif argv[e]=='-o':
			pathout=argv[e+1]
except:
	print('bad arguments...')
	help()

if pathin=='':
	print('need an input as argument...')
	help()
# if pathout == '' assume output in the script for visual check


for filepath in glob(pathin+'/*'):
	r=etree.parse(filepath)
	# getting fields, note that they could be multivalued
	thisrecord={}
	for field in fields:
		values=[v.text for v in r.findall('.//'+field, namespaces)]
		thisrecord[field]=values
	'''
	WARN:
	depending on the specific use of DublinCore in every specific set of records,
	perhaps check and transformation of some fields should be done before output.
	This is just a crude translation from DC
	'''
	# output thisrecord in a suitable format for Solr
	record=''
	for field in sorted(thisrecord.keys()):
		for value in thisrecord[field]:
			record=record+'<field name="'+field+'">'+value+'</field>\n'
	record='<add>\n<doc>\n'+record+'</doc>\n</add>\n'
	
	# preparing new filename, if we wanted output to a file for every record
	if pathout !='':
		filename=filepath.split('/')[-1]
		filename=filename+'_2solr.xml'
		filename=pathout+'/'+filename
		F=open(filename,'w')
		F.write(record)
		F.close()
	else: # instead, output to the screen
		print(record)


