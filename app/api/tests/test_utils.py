from django.test import TestCase

from api.utils import skill_cleaner, skill_compare


class SkillCleanerTests(TestCase):

    def test_skill_cleaner_functionality(self):
        """Test functionality of skill_cleaner"""
        data = "Agile Methodologies, Analytical Skills"
        skills_cleaned = skill_cleaner(data)
        self.assertEqual(skills_cleaned, ['Agile', 'Analytics'])


class SkillCompareTests(TestCase):

    def test_skill_compare_functionality(self):
        """Test functionality of skill_compare"""
        skills = ['Agile', 'Analytics']
        results_dictionary, missing_dictionary = skill_compare(skills)
        self.assertEqual(results_dictionary, {'Analytics': 44, 'Agile': 7})
