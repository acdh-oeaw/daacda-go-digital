from xml.sax.saxutils import escape, unescape


TEI_NSMAP = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace",
}

TEI_METHOD = """
Der vorliegende Datensatz wurde von Georg Hoffmann, Nicole-Melanie Goll sowie Martin Kirnbauer erhoben und mittels einer von Peter Andorfer entwickelten Python/Django Web-Applikation in das vorliegende TEI Dokument transformiert. Die in diesem TEI Dokument präsentierten Daten basieren vornehmlich aus dem Archivbestand National Archives and Records Administration College Park NARA, Record Group 92 und wurden ergänzt mit Quellen aus dem Bestand NARA, Record Groups 18, 153, 242, 498, 549 sowie The National Archives Kew TNA, AIR 10, 20, 23, 49 sowie WO 204, 219
"""

TEI_STUMP = f"""
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main"></title>
            <title type="sub">Downed Allied Air Crew Database Austria</title>
            <funder>
                <orgName key="https://d-nb.info/gnd/1090414722">
                    Österreichische Akademie der Wissenschaften
                </orgName>
            </funder>
            <respStmt>
               <resp>Projektleitung, Datenerhebung</resp>
               <persName key="https://d-nb.info/gnd/143373765">
                  <forename>Georg</forename>
                  <surname>Hoffmann</surname>
               </persName>
            </respStmt>
            <respStmt>
               <resp>Datenerhebung</resp>
               <persName key="https://d-nb.info/gnd/143174754">
                  <forename>Nicole-Melanie</forename>
                  <surname>Goll</surname>
               </persName>
            </respStmt>
            <respStmt>
               <resp>Datenkuratierung</resp>
               <persName key="https://orcid.org/0000-0001-7081-2280">
                  <forename>Martin</forename>
                  <surname>Kirnbauer</surname>
               </persName>
            </respStmt>
            <respStmt>
               <resp>Datenmodellierung, Aufsetzen einer Datenbankapplikation zur Datenerhebung und Datenkonvertierung nach TEI</resp>
               <persName key="https://d-nb.info/gnd/1043833846">
                  <forename>Peter</forename>
                  <surname>Andorfer</surname>
               </persName>
            </respStmt>
         </titleStmt>
         <publicationStmt>
            <authority>
               <persName key="https://d-nb.info/gnd/143373765">
                  <forename>Georg</forename>
                  <surname>Hoffmann</surname>
               </persName>
            </authority>
            <availability>
               <licence target="https://vocabs.acdh.oeaw.ac.at/archelicenses/cc-by-4-0/">CC-BY 4.0</licence>
            </availability>
         </publicationStmt>
         <sourceDesc>
            <msDesc>
              <msIdentifier>
                <institution>
                  <orgName>National Archives and Records Administration</orgName>
                  <idno type="VIAF">162565459</idno>
                </institution>
                <collection>Record Group 92</collection>
              </msIdentifier>
            </msDesc>
         </sourceDesc>
      </fileDesc>
     <encodingDesc>
       <ab>{TEI_METHOD}</ab>
     </encodingDesc>
  </teiHeader>
  <text>
      <body/>
      <back/>
  </text>
</TEI>
"""


def custom_escape(somestring):
    un_escaped = unescape(somestring)
    return escape(un_escaped)
