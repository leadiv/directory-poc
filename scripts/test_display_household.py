import unittest

from mock_household import single_household
from display_household import display_household

''',
            'The Kocher Household<br />',
            '<img src="https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg" alt="Rob Kocher" /> <span data-primary data-membership="Participant (CBC)" data-status="active">Rob Kocher</span>,',
            '<img src=""https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg alt="Tammy Kocher" /> <span data-membership="Participant (CBC)" data-status="active">Tammy Kocher</span>,',
            '<img src="https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png" alt="Charisa Kocher" /> <span data-membership="Participant (CBC)" data-status="active">Charisa Kocher</span>,',
            '<img src="https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png" alt="Kupo Kocher" /> <span data-membership="Friend of CBC" data-status="active">Kupo Kocher</span>'
'''
class TestHousehold(unittest.TestCase):
    def test_display_household(self):
        expected = '<img src=""https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg" alt="Kocher Household"/>'
        actual = display_household(single_household)

        self.assertIn(expected, actual, 'it should be able to display the family image')

if __name__ == '__main__':
    unittest.main()