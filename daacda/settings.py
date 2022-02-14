import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, '../'))))

ACDH_IMPRINT_URL = "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="
REDMINE_ID = 11260
BOMB_GROUP_LABEL = "bomb group"
AIR_FORCE_LABEL = "airforce division"
SQUAD_LABEL = "squadroon"

DEBUG = os.environ.get('DEBUG', True)
ADD_ALLOWED_HOST = os.environ.get('ALLOWED_HOST', '*')
SECRET_KEY = os.environ.get('SECRET_KEY', 'TZRHHwasdfsadfdsafkljlxö7639827249324GV')

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]


INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_filters',
    'django_tables2',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'leaflet',
    'idprovider',
    'webpage',
    'vocabs',
    'entities',
    'stats',
    'archeutils',
    'charts',
    'detentions',
    'news',
    'browsing',
    'materials',
    'tei',
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'daacda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'webpage.webpage_content_processors.installed_apps',
                'webpage.webpage_content_processors.is_dev_version',
                'webpage.webpage_content_processors.get_db_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'daacda.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('POSTGRES_DB', 'daacda'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTEGRES_PORT', '5432')
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
    },
}

ARCHE_SETTINGS = {
    'project_name': ROOT_URLCONF.split('.')[0],
    'base_url': "https://id.acdh.oeaw.ac.at/{}".format(ROOT_URLCONF.split('.')[0])
}

VOCABS_DEFAULT_PEFIX = os.path.basename(BASE_DIR)

VOCABS_SETTINGS = {
    'default_prefix': VOCABS_DEFAULT_PEFIX,
    'default_ns': "http://www.vocabs/{}/".format(VOCABS_DEFAULT_PEFIX),
    'default_lang': "eng"
}


LEAFLET_CONFIG = {
    'MAX_ZOOM': 18,
    'DEFAULT_CENTER': (47, 16),
    'DEFAULT_ZOOM': 4,
    'TILES': [
        (
            'BASIC',
            'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            {
                'attribution':
                    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>\
                    contributors',
                'maxZoom': 18,
            }
        )
    ],
}


NETVIS_TYPES = {
    'nodes': [
        {'id': 'CurrentPerson', 'label': 'Person', 'color': '#20c997'},
        {'id': 'Person', 'label': 'Person', 'color': '#006699'},
        {'id': 'PrisonStation', 'label': 'Prisonstation', 'color': '#28a745'},
        {'id': 'Location', 'label': 'Location', 'color': '#669900'},
        {'id': 'Place', 'label': 'Location', 'color': '#669900'},
        {'id': 'Bomber', 'label': 'Bomber', 'color': '#ffc107'},
    ]
}


ARCHE_SETTINGS = {
    'project_name': ROOT_URLCONF.split('.')[0],
    'base_url': "https://id.acdh.oeaw.ac.at/daacda".format(ROOT_URLCONF.split('.')[0])
}

ARCHE_BASE_URL = "https://id.acdh.oeaw.ac.at/daacda"
ARCHE_LANG = 'en'

ARCHE_CONST_MAPPINGS = [
    ('hasOwner', "https://d-nb.info/gnd/143373765",),  # Hoffmann
    ('hasContact', "https://d-nb.info/gnd/143373765",),
    ('hasRightsHolder', "https://d-nb.info/gnd/143373765",),
    ('hasPrincipalInvestigator', "https://d-nb.info/gnd/143373765",),
    ('hasLicensor', 'https://d-nb.info/gnd/143373765',),
    ('hasCreator', 'https://d-nb.info/gnd/143373765',),
    ('hasCreator', 'https://d-nb.info/gnd/143174754',),  # Goll
    ('hasContributor', 'https://orcid.org/0000-0001-7081-2280',),  # Kirnbauer
    ('hasContributor', 'https://d-nb.info/gnd/1043833846',),  # Andorfer
    ('hasLicense', 'https://vocabs.acdh.oeaw.ac.at/archelicenses/cc-by-4-0',),
    ('hasLanguage', 'https://vocabs.acdh.oeaw.ac.at/iso6393/eng',),
    ('hasLanguage', 'https://vocabs.acdh.oeaw.ac.at/iso6393/deu',),
    ('hasRelatedDiscipline', 'https://vocabs.acdh.oeaw.ac.at/oefosdisciplines/601',),
    ('hasSubject', 'Second world war',),
    ('hasSubject', 'aerial warfare',),
    ('hasMetadataCreator', 'https://d-nb.info/gnd/1043833846',),  # Andorfer
    ('hasDepositor', 'https://d-nb.info/gnd/1043833846',),  # Andorfer
]


TOP_COL_RDF = """
    <rdf:RDF xmlns:acdh="https://vocabs.acdh.oeaw.ac.at/schema#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <acdh:Place>
            <acdh:hasIdentifier rdf:resource="https://www.geonames.org/2782113"/>
            <acdh:hasTitle xml:lang="de">Österreich</acdh:hasTitle>
        </acdh:Place>
        <acdh:Person>
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/none"/>
            <acdh:hasTitle xml:lang="de">Niemand</acdh:hasTitle>
        </acdh:Person>
        <rdf:Description rdf:about="https://id.acdh.oeaw.ac.at/daacda">
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/daacda"/>
            <acdh:hasTitle xml:lang="en">Downed Allied Air Crew Database Austria</acdh:hasTitle>
            <rdf:type rdf:resource="https://vocabs.acdh.oeaw.ac.at/schema#TopCollection"/>
            <acdh:hasOaiSet rdf:resource="https://vocabs.acdh.oeaw.ac.at/archeoaisets/kulturpool"/>
            <acdh:hasLifeCycleStatus rdf:resource="https://vocabs.acdh.oeaw.ac.at/archelifecyclestatus/active"/>
            <acdh:hasAppliedMethodDescription xml:lang="de">Die hier archivierten Datensätze wurden von Georg Hoffmann, Nicole-Melanie Goll sowie Martin Kirnbauer erhoben und mithilfe einer von Peter Andorfer entwickelten Python/Django Web-Applikation in TEI Dokumente überführt. Die in diesen Dokumenten präsentierten Daten basieren vornehmlich auf dem Archivbestand National Archives and Records Administration College Park NARA, Record Group 92 und wurden mit Quellen aus folgenden Beständen ergänzt: NARA, Record Groups 18, 153, 242, 498, 549, The National Archives Kew TNA, AIR 10, 20, 23, 49 sowie WO 204, 219.</acdh:hasAppliedMethodDescription>
            <acdh:hasAppliedMethodDescription xml:lang="en">The archived data sets were compiled by Georg Hoffmann, Nicole-Melanie Goll, and Martin Kirnbauer and converted into TEI documents with the help of a Python / Django web application developed by Peter Andorfer. The data in these documents are primarily based on files from National Archives and Records Administration College Park NARA, Record Group 92 and have been supplemented with sources from the following holdings: NARA, Record Groups 18, 153, 242, 498, 549, The National Archives Kew TNA, AIR 10, 20, 23, 49 and WO 204, 219.</acdh:hasAppliedMethodDescription>
            <acdh:hasDescription xml:lang="de">DAACDA umfasst vernetzte Daten zu britischen und US-amerikanischen Flugzeugen sowie deren Besatzungen, die zwischen 1939 und 1945 über dem heutigen Österreich und Ungarn abstürzten. Informationen zu jedem abgestürzten Flugzeug und seiner Besatzung sind im XML/TEI-Format archiviert. Die Datensätze zu den einzelnen Flugzeugen und Crews sind nach den jeweiligen militärischen Einheiten, sogenannten „Squadrons“, gruppiert und den entsprechenden Orten (Absturz, Aufgriff, Ort des Todes, Gefangenschaft) zugeordnet.</acdh:hasDescription>
            <acdh:hasDescription xml:lang="en">DAACDA contains interconnected data on U.S. and British planes and air crews downed over today’s Austria and Hungary between 1939 and 1945. Information on each crashed plane as well as on the related air crew is stored in XML/TEI-format. The data sets for each aircraft and crew are grouped according to the respective military units, the so-called "squadrons", and assigned to corresponding locations (crash, apprehension, place of death, imprisonment).</acdh:hasDescription>
            <acdh:hasPid>http://hdl.handle.net/21.11115/0000-000D-CA69-A</acdh:hasPid>
            <acdh:hasSpatialCoverage rdf:resource="https://www.geonames.org/2782113"/>
            <acdh:hasCurator rdf:resource="https://d-nb.info/gnd/1043833846"/>
            <acdh:hasCoverageStartDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1943-08-13</acdh:hasCoverageStartDate>
            <acdh:hasCoverageEndDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1945-05-01</acdh:hasCoverageEndDate>
            <acdh:hasCreatedStartDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2017-01-01</acdh:hasCreatedStartDate>
            <acdh:hasCreatedEndDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-12-31</acdh:hasCreatedEndDate>
            <acdh:hasRelatedProject rdf:resource="https://id.acdh.oeaw.ac.at/daacda/project"/>
            <acdh:hasSubject xml:lang="de">Zweiter Weltkrieg</acdh:hasSubject>
            <acdh:hasSubject xml:lang="de">Luftkrieg</acdh:hasSubject>
        </rdf:Description>
        <acdh:Project rdf:about="https://id.acdh.oeaw.ac.at/daacda/project">
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/daacda/project"/>
            <acdh:hasTitle xml:lang="en">Downed Allied Air Crew Database Austria</acdh:hasTitle>
            <rdf:type rdf:resource="https://vocabs.acdh.oeaw.ac.at/schema#Project"/>
            <acdh:hasPrincipalInvestigator rdf:resource="https://d-nb.info/gnd/143373765"/>
            <acdh:hasStartDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2017-01-01</acdh:hasStartDate>
            <acdh:hasEndDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-11-30</acdh:hasEndDate>
            <acdh:hasLifeCycleStatus rdf:resource="https://vocabs.acdh.oeaw.ac.at/archelifecyclestatus/completed"/>
            <acdh:hasRelatedCollection rdf:resource="https://id.acdh.oeaw.ac.at/daacda"/>
            <acdh:hasRelatedDiscipline rdf:resource="https://vocabs.acdh.oeaw.ac.at/oefosdisciplines/601"/>
            <acdh:hasMetadataCreator rdf:resource="https://d-nb.info/gnd/1043833846"/>
            <acdh:hasContact rdf:resource="https://d-nb.info/gnd/143373765"/>
            <acdh:hasFunder rdf:resource="https://viaf.org/viaf/141440509"/>
            <acdh:hasFunder rdf:resource="https://viaf.org/viaf/130145003282161301677"/>
            <acdh:hasDescription xml:lang="en">DAACDA (Downed Allied Air Crew Database Austria) is a project carried out by Dr. Georg Hoffmann (head of project) and Dr. Nicole-Melanie Goll, conducted at the ACDH-CH and the Austrian National Library between 2017 and 2020. The project was funded by the Austrian Academy of Sciences (GoDigital 2.0-program) as well as the Future Fund of the Republic of Austria. The project merges research results dedicated to examinations on violence against downed Allied air crews (“mob law against airmen") and so-called "Missing-in-Action" cases (MIA) and provides them for the first time in a cross-linked manner. The project is concerned with the collection, evaluation and visualization of data and information on downed planes of the US Army Air Force as well as the Royal Air Force, and their crews who were arrested, became victims of war crimes and/or died in the area of present-day Austria and Hungary between 1939 and 1945. A networked approach to different sources – among them from archives in the US, the UK, Germany and Austria – allows, for the first time, a complete overview of a so far scarcely investigated aspect of the Allied Air War. The web application developed in the course of the project captures and visualizes more than 1,000 plane crashes and traces and depicts the fate of more than 10,000 American and British airmen. The collected data is thereby connected and provided to the public as well as to researchers, ultimately allowing for further investigations and research.</acdh:hasDescription>
            <acdh:hasDescription xml:lang="de">Das Projekt DAACDA (Downed Allied Air Crew Database Austria) wurde von Dr. Georg Hoffmann (Projektleitung) und Dr.in Nicole-Melanie Goll zwischen 2017 und 2020 am ACDH-CH und der Österreichischen Nationalbibliothek durchgeführt.</acdh:hasDescription>
            <acdh:hasSubject xml:lang="de">Zweiter Weltkrieg</acdh:hasSubject>
            <acdh:hasSubject xml:lang="de">Luftkrieg</acdh:hasSubject>
            <acdh:hasSubject xml:lang="en">Second world war</acdh:hasSubject>
            <acdh:hasSubject xml:lang="en">aerial warfare</acdh:hasSubject>
        </acdh:Project>
        <acdh:Resource rdf:about="https://id.acdh.oeaw.ac.at/daacda/title-image.jpg">
            <acdh:hasTitle xml:lang="en">DAACDA Title Image</acdh:hasTitle>
            <acdh:isPartOf rdf:resource="https://id.acdh.oeaw.ac.at/daacda"/>
            <acdh:hasRightsHolder rdf:resource="https://id.acdh.oeaw.ac.at/none"/>
            <acdh:hasOwner rdf:resource="https://viaf.org/viaf/162565459"/>
            <acdh:hasLicensor rdf:resource="https://id.acdh.oeaw.ac.at/none"/>
            <acdh:hasLicense rdf:resource="https://vocabs.acdh.oeaw.ac.at/archelicenses/cc0-1-0"/>
            <acdh:hasCategory rdf:resource="https://vocabs.acdh.oeaw.ac.at/archecategory/image"/>
            <acdh:isTitleImageOf rdf:resource="https://id.acdh.oeaw.ac.at/daacda"/>
            <acdh:hasMetadataCreator rdf:resource="https://d-nb.info/gnd/1043833846"/>
            <acdh:hasDepositor rdf:resource="https://d-nb.info/gnd/1043833846"/>
        </acdh:Resource>
        <acdh:Person rdf:about="https://d-nb.info/gnd/143373765">
            <acdh:hasTitle xml:lang="und">Georg Hoffmann</acdh:hasTitle>
            <acdh:hasLastName xml:lang="und">Hoffmann</acdh:hasLastName>
            <acdh:hasFirstName xml:lang="und">Georg</acdh:hasFirstName>
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/ghoffmann"/>
            <acdh:hasPersonalTitle>Mag. Dr.</acdh:hasPersonalTitle>
        </acdh:Person>
        <acdh:Person rdf:about="https://d-nb.info/gnd/143174754">
            <acdh:hasTitle xml:lang="und">Nicole-Melanie Goll</acdh:hasTitle>
            <acdh:hasLastName xml:lang="und">Goll</acdh:hasLastName>
            <acdh:hasFirstName xml:lang="und">Nicole-Melanie</acdh:hasFirstName>
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/ngoll"/>
            <acdh:hasPersonalTitle>Mag. Dr.</acdh:hasPersonalTitle>
        </acdh:Person>
        <acdh:Person rdf:about="https://orcid.org/0000-0001-7081-2280">
            <acdh:hasLastName xml:lang="de">Kirnbauer</acdh:hasLastName>
            <acdh:hasFirstName xml:lang="de">Martin</acdh:hasFirstName>
        </acdh:Person>
        <acdh:Organisation rdf:about="https://viaf.org/viaf/162565459">
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/usnationalarchivesrecordsadmin"/>
            <acdh:hasTitle xml:lang="en">United States. National Archives and Records Administration</acdh:hasTitle>
        </acdh:Organisation>
        <acdh:Organisation rdf:about="https://viaf.org/viaf/130145003282161301677">
            <acdh:hasIdentifier rdf:resource="https://id.acdh.oeaw.ac.at/zukunftsfondsoesterreich"/>
            <acdh:hasTitle xml:lang="de">Zukunftsfonds der Republik Österreich</acdh:hasTitle>
        </acdh:Organisation>
    </rdf:RDF>
"""
