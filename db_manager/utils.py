import csv
import os

from django.conf import settings

from core.models import DataSkill

data_skills_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/data_science/skills_count.csv")


def database_upload():
    data_skills = DataSkill.objects.all()
    data_skills.delete()
    with open(data_skills_path) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                _, created = DataSkill.objects.get_or_create(dataskill=row[0], percentage=row[1])
            except:
                pass
