from xml.sax.saxutils import escape, unescape


TEI_NSMAP = {
    'tei': "http://www.tei-c.org/ns/1.0",
    'xml': "http://www.w3.org/XML/1998/namespace",
}

TEI_STUMP = """
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main"></title>
            <title type="sub"></title>
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
      </fileDesc>
     <encodingDesc>
        <ab>Der vorliegende Datensatz wurde von Georg Hoffmann, Nicole-Melanie Goll sowie Martin Kirnbauer erhoben und mittels einer von Peter Andorfer entwickelten Python/Django Web-Applikation in das vorliegende TEI Dokument transformiert</ab>
     </encodingDesc>
  </teiHeader>
   <facsimile/>
  <text>
      <body/>
      <back/>
  </text>
</TEI>
"""


def custom_escape(somestring):
    un_escaped = unescape(somestring)
    return escape(un_escaped)
