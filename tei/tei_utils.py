import datetime
import lxml.etree as ET

from django.conf import settings
from django.template.loader import get_template

from tei.partials import TEI_NSMAP, TEI_STUMP, custom_escape
from tei.places import TeiPlace

ARCHE_BASE_URL = settings.ARCHE_BASE_URL


class MakeTeiDoc:
    def __init__(self, res):
        self.nsmap = TEI_NSMAP
        self.stump = TEI_STUMP
        self.res = res
        self.title = f"{self.res}"
        self.tree = self.populate_header()

    def get_node_from_template(self, template_path, other_object=False):
        template = get_template(template_path)
        if other_object:
            context = {"object": other_object}
        else:
            context = {"object": self.res}
        temp_str = f"{template.render(context=context)}"
        node = ET.fromstring(temp_str)
        return node

    def populate_header(self):
        doc = ET.fromstring(self.stump)

        root_el = doc
        root_el.attrib["{http://www.w3.org/XML/1998/namespace}base"] = (
            f"{ARCHE_BASE_URL}"
        )
        root_el.attrib["{http://www.w3.org/XML/1998/namespace}id"] = (
            f"bomber__{self.res.id}.xml"
        )
        prev_obj = self.res.get_prev()
        if prev_obj:
            root_el.attrib["prev"] = f"{ARCHE_BASE_URL}/data/bomber__{prev_obj}.xml"
        next_obj = self.res.get_next()
        if next_obj:
            root_el.attrib["next"] = f"{ARCHE_BASE_URL}/data/bomber__{next_obj}.xml"

        title_el = doc.xpath('.//tei:title[@type="main"]', namespaces=self.nsmap)[0]
        title_el.text = f"{self.res}"
        if "[internal-id]" not in self.res.macr_nr:
            ms_identifier_el = doc.xpath(".//tei:msIdentifier", namespaces=self.nsmap)[
                0
            ]
            ms_idno_el = listperson_el = ET.Element("{http://www.tei-c.org/ns/1.0}idno")
            ms_idno_el.text = f"Missing Air Crew Reports No.: {self.res.macr_nr}"
            ms_identifier_el.append(ms_idno_el)

        # idno_el = doc.xpath('.//tei:msIdentifier/tei:idno', namespaces=self.nsmap)[0]
        # idno_el.text = self.res.get_idno

        back_el = doc.xpath(".//tei:back", namespaces=self.nsmap)[0]
        listperson_el = ET.Element("{http://www.tei-c.org/ns/1.0}listPerson")
        listplace_el = ET.Element("{http://www.tei-c.org/ns/1.0}listPlace")
        listorg_el = ET.Element("{http://www.tei-c.org/ns/1.0}listOrg")
        back_el.append(listperson_el)
        back_el.append(listplace_el)
        back_el.append(listorg_el)

        for x in self.res.has_crew.all():
            p_el = self.get_node_from_template("tei/person_tei.xml", x)
            listperson_el.append(p_el)

        for x in self.res.get_prisons.all():
            item_node = self.get_node_from_template("tei/institution_tei.xml", x)
            listorg_el.append(item_node)

        for x in self.res.get_orgs.all():
            item_node = self.get_node_from_template("tei/institution_tei.xml", x)
            listorg_el.append(item_node)

        for x in self.res.get_places:
            item_node = self.get_node_from_template("tei/place_tei.xml", x)
            listplace_el.append(item_node)

        xeno = doc.xpath(".//tei:teiHeader", namespaces=self.nsmap)[0]
        for x in self.res.get_concepts:
            xeno.append(self.get_node_from_template("tei/skosify_concepts.xml", x))

        return doc

    def pop_body(self):
        doc = self.tree
        body_el = doc.xpath(".//tei:body", namespaces=self.nsmap)[0]
        div_el = ET.Element("{http://www.tei-c.org/ns/1.0}div")
        div_el.attrib["type"] = "main"
        div_head_el = ET.Element("{http://www.tei-c.org/ns/1.0}head")
        div_head_el.text = self.title
        div_el.append(div_head_el)
        div_el.append(self.get_node_from_template("tei/bomber_tei.xml"))
        div_el.append(self.get_node_from_template("tei/crew_tei.xml"))
        body_el.append(div_el)
        return doc

    def export_full_doc(self):
        return self.pop_body()

    def export_full_doc_str(self, file="temp.xml"):
        with open(file, "wb") as f:
            f.write(ET.tostring(self.pop_body(), pretty_print=True, encoding="UTF-8"))
        return file

    def as_tei_node(self):
        return self.pop_body()

    def as_tei_str(self):
        return ET.tostring(self.as_tei_node(), pretty_print=True, encoding="UTF-8")
