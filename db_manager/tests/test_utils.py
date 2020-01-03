# from django.test import TestCase
#
# from core.models import DataSkill
# from db_manager.utils import database_upload
#
#
# class DatabaseUploadTests(TestCase):
#
#     def setUp(self):
#         self.dataskill = DataSkill.objects.create(
#                             dataskill="test skill",
#                             percentage=0.12
#                         )
#         self.empty_dataskill = DataSkill.objects.create()
#
#     def tearDown(self):
#         self.dataskill.delete()
#         self.empty_dataskill.delete()
#
#     def test_function_deletes_previous_dataskills(self):
#         """Test that db is cleaned before the upload"""
#         database_upload()
#         self.assertEqual(len(DataSkill.objects.filter(dataskill="test skill")), 0)
#         self.assertEqual(len(DataSkill.objects.filter(name="")), 0)













