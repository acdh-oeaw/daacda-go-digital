import datetime
import lxml.etree as ET

from tei.partials import TEI_NSMAP, TEI_STUMP, custom_escape


class TeiPerson():
    def __init__(self, res):
        self.nsmap = TEI_NSMAP
        self.stump = TEI_STUMP
        self.res = res

    def get_el(self):
        item = ET.Element("{http://www.tei-c.org/ns/1.0}person")
        item.attrib[
            "{http://www.w3.org/XML/1998/namespace}id"
        ] = f"person__{self.res.id}"
        name = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
        item.append(name)

        f_name = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
        if self.res.forename:
            f_name.text = f"{self.res.forename}"
        else:
            f_name.text = 'N.'
        name.append(f_name)

        f_name = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
        if self.res.name:
            f_name.text = f"{self.res.name}"
        else:
            f_name.text = 'N.'
        name.append(f_name)

        return item
