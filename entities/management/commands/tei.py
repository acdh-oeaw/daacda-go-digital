import os
from django.core.management.base import BaseCommand
from django.conf import settings
from entities.models import Bomber
from tei.tei_utils import MakeTeiDoc


class Command(BaseCommand):
    help = "Serialize Bombers as TEI/XML"

    def handle(self, *args, **options):
        tei_folder = os.path.join(settings.MEDIA_ROOT, "tei")
        os.makedirs(tei_folder, exist_ok=True)

        for x in Bomber.objects.all():
            file_name = f"a-{x.id:0>5}"
            save_path = f"{os.path.join(tei_folder, file_name)}.xml"
            doc = MakeTeiDoc(x)
            doc.export_full_doc_str(save_path)
            print(f"{save_path}")
    print("done")
