import pickle
import os
import re


from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from django.db.models.query import QuerySet

from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF

from browsing.browsing_utils import model_to_dict
from webpage.metadata import PROJECT_METADATA

ARCHE_CONST_MAPPINGS = getattr(settings, 'ARCHE_CONST_MAPPINGS', False)

ARCHE_LANG = getattr(settings, 'ARCHE_LANG', 'en')
ARCHE_BASE_URL = getattr(settings, 'ARCHE_BASE_URL', 'https://id.acdh.oeaw.ac.at/MYPROJECT')

TOP_COL_RDF = getattr(
    settings,
    'TOP_COL_RDF',
    None
)
repo_schema = "https://raw.githubusercontent.com/acdh-oeaw/repo-schema/master/acdh-schema.owl"
acdh_ns = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
owl_ns = Namespace("http://www.w3.org/2002/07/owl#")
rdfs_ns = Namespace("http://www.w3.org/2000/01/rdf-schema#")


def get_prop_types(repo_schema_url=repo_schema):
    g = Graph()
    g.parse(repo_schema, format='xml')
    prop_types = {}
    for s in g.subjects(RDF.type, None):
        if s.startswith('https://vocabs.acdh'):
            prop_name = s.split('#')[-1]
            for range_prop in g.objects(s, rdfs_ns.range):
                prop_types[prop_name] = range_prop.split('#')[-1]
    return prop_types


ARCHE_PROPS_LOOKUP = get_prop_types()


def get_root_col():
    g = Graph()
    g.parse(data=TOP_COL_RDF)
    sub = URIRef(ARCHE_BASE_URL)
    for const in ARCHE_CONST_MAPPINGS:
        arche_prop_domain = ARCHE_PROPS_LOOKUP.get(const[0], 'No Match')
        # print(f"property: {const[0]}, value: {const[1]}, range: {arche_prop_domain}")
        if arche_prop_domain == 'string':
            g.add((sub, acdh_ns[const[0]], Literal(const[1], lang=ARCHE_LANG)))
        elif arche_prop_domain == 'date':
            g.add((sub, acdh_ns[const[0]], Literal(const[1], datatype=XSD.date)))
        else:
            g.add((sub, acdh_ns[const[0]], URIRef(const[1])))
    return g


def get_arche_id(res, id_prop="pk", arche_uri=ARCHE_BASE_URL):
    """ function to generate generic ARCHE-IDs
        :param res: A model object
        :param id_prop: The object's primary key property
        :param arche_uri: A base url; should be configued in the projects settings file
        :return: An ARCHE-ID (URI)
    """
    if isinstance(res, str):
        return res
    else:
        app_name = res.__class__._meta.app_label.lower()
        class_name = res.__class__.__name__.lower()
        return "/".join(
            [arche_uri, app_name, class_name, f"{getattr(res, id_prop)}"]
        )


def as_arche_graph(res):
    g = Graph()
    sub = URIRef(get_arche_id(res))
    g.add(
        (sub, acdh_ns.hasTitle, Literal(
            f"{res}",
            lang=ARCHE_LANG)
        )
    )
    g.add(
        (
            sub,
            acdh_ns.hasCategory,
            URIRef("https://vocabs.acdh.oeaw.ac.at/archecategory/dataset/xml"))
    )
    for x in ['target_place', 'crash_place']:
        pl = getattr(res, x)
        pl_g = Graph()
        pl_uri = URIRef(f"{ARCHE_BASE_URL}/places/{pl.id}")
        pl_g.add(
            (
                pl_uri, acdh_ns.hasTitle,
                Literal(f"{pl}", lang='und')
            )
        )
        if pl.geonames_id:
            pl_g.add(
                (
                    pl_uri, acdh_ns.hasIdentifier,
                    URIRef(f"{pl.geonames_id}")
                )
            )
        if pl.geonames_id:
            pl_g.add(
                (
                    pl_uri, acdh_ns.hasIdentifier,
                    URIRef(f"{pl.geonames_id}")
                )
            )
        g.add(
            (
                sub,
                RDF.type,
                acdh_ns.Place
            )
        )
        g = g + pl_g
    g.add((sub, RDF.type, acdh_ns.Resource))
    col = Graph()
    col_sub = URIRef(f"{ARCHE_BASE_URL}/squads/{res.squadron.id}")
    g.add((col_sub, RDF.type, acdh_ns.Collection))
    col.add(
        (col_sub, acdh_ns.isPartOf, URIRef(f"{ARCHE_BASE_URL}"))
    )
    col.add(
        (
            col_sub,
            acdh_ns.hasTitle,
            Literal(
                f"{res.squadron}",
                lang=ARCHE_LANG)
            )
    )

    for const in ARCHE_CONST_MAPPINGS:
        arche_prop_domain = ARCHE_PROPS_LOOKUP.get(const[0], 'No Match')
        if arche_prop_domain == 'date':
            col.add()
            g.add((sub, acdh_ns[const[0]], Literal(const[1], datatype=XSD.date)))
            col.add((col_sub, acdh_ns[const[0]], Literal(const[1], datatype=XSD.date)))
        if arche_prop_domain == 'string':
            g.add((sub, acdh_ns[const[0]], Literal(const[1], lang=ARCHE_LANG)))
            col.add((col_sub, acdh_ns[const[0]], Literal(const[1], lang=ARCHE_LANG)))
        else:
            g.add((sub, acdh_ns[const[0]], URIRef(const[1])))
            col.add((col_sub, acdh_ns[const[0]], URIRef(const[1])))
    g = g + col
    return g
