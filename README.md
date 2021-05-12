# dc2solr
Indexing DublinCore metadata with Apache Solr
### Intro
DublinCore is, conversely speaking, a set of fields for describing document items. It has, as well, some specifications or rules applying to each field. Fields and their associated values can be in several formats; one of these is an XML spec, coming from de Open Archives Initiative.
This XML is particularly handly, as the OAI-ProtocolMetadataHarvest is a common way to access to records in open digital repositories.
### Data Source example
an DublinCore record in such XML format looks like:

<pre>

&lt;oai_dc:dc xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xsi="http://
www.w3.org/2001/XMLSchema-instance" xmlns="http://www.openarchives.org/OAI/2.0/" xsi:schemaLocation="http://www.openarchives.org/OAI
/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd"&gt;
        &lt;dc:relation&gt;http://eprints.rclis.org/9989/&lt;/dc:relation&gt;
        &lt;dc:title&gt;Avalia&#231;&#227;o da cole&#231;&#227;o de livros que atende ao Curso de Com&#233;rcio Exterior da Universidade d
o Vale do Itaja&#237;&lt;/dc:title&gt;
        &lt;dc:creator&gt;Borinelli, Christiane Aparecida&lt;/dc:creator&gt;
        &lt;dc:creator&gt;Nascimento, Maria de Jesus&lt;/dc:creator&gt;
        &lt;dc:subject&gt;J. Technical services in libraries, archives, museum.&lt;/dc:subject&gt;
        &lt;dc:description&gt;It presents the results of the evaluation of the collection of workmanships of the Course of Foreign commerc
e of the Communitarian Central Library of the University of the Valley of the Itaja&#237;. 175 workmanships cited in basic bibliogra
phies of the programs of education of the related course had been analyzed, and verified the number of units that consist in the qua
ntity of the BCC, as well as the average life, obsolescence and use of this quantity. The library possesss 89% of the cited headings
, however, only 69% of the collection are brought up to date editions. The average life of the cited workmanships is between that th
ey have between five and six years of publication&lt;/dc:description&gt;
        &lt;dc:date&gt;2006&lt;/dc:date&gt;
        &lt;dc:type&gt;Journal article (Unpaginated)&lt;/dc:type&gt;
        &lt;dc:type&gt;PeerReviewed&lt;/dc:type&gt;
        &lt;dc:format&gt;application/pdf&lt;/dc:format&gt;
        &lt;dc:language&gt;en&lt;/dc:language&gt;
        &lt;dc:identifier&gt;http://eprints.rclis.org/9989/1/Avalia%C3%A7%C3%A3o_de_cole%C3%A7%C3%A3o.pdf&lt;/dc:identifier&gt;
        &lt;dc:identifier&gt;  Borinelli, Christiane Aparecida and Nascimento, Maria de Jesus Avalia&#231;&#227;o da cole&#231;&#227;o de 
livros que atende ao Curso de Com&#233;rcio Exterior da Universidade do Vale do Itaja&#237;. Biblionline, 2006, vol. 2, n. 1 ano .  
     [Journal article (Unpaginated)] &lt;/dc:identifier&gt;&lt;/oai_dc:dc&gt;

</pre>

We can see fields, which are optional and also can have several values in the same record.

### Solr Schema
Solr looks for field features (data type, required or not, etc.) in a file called **schema.xml** or, in more recent Solr versions, **managed-schema**.
For enabling Solr to index DublinCore records, we must to define fields in our **schema** file. A managed-schema file is provided as an example. Although it is a minimal schema file, it works; note that
- real use of Dublin Core fields varies, following diverse interpretations
- some fields are defined as text (general or english text), but you can specify another kind of text (spanish, french, ...)
- some fields are defined as *string* (that is, they can't be tokenized, stemmed, etc.); this can be good for normalized values as URLs, doctypes (example: "application/pdf") or even for subject headings, if they are controlled ones
- choose your data types carefully, acording the specific use of Dublin Core on your records


### Reading records, identifying fields

### Producing XML ready to be ingested by Solr
