import unittest
from unittest.mock import MagicMock

from mock_household import single_household
from mock_household import households_people

from display_household import display_household
from display_household import get_people_links
from display_household import get_allowed_people_list 


class TestHousehold(unittest.TestCase):

    def test_single_display_household(self):
        self.maxDiff = None

        expected = ''.join((
            '<img src="https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg" alt="Kocher Household"/>',
            '<h2>The Kocher Household</h2>',
            '<ul>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg" alt="Rob Kocher"/><span>Rob Kocher</span></li>',
            '</ul>'
        ))
        actual = display_household(single_household, ['36729400'])

        self.assertEqual(expected, actual, 'it should be able to display one family member as HTML')

    def test_multiple_display_household(self):
        self.maxDiff = None

        expected = ''.join((
            '<img src="https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg" alt="Kocher Household"/>',
            '<h2>The Kocher Household</h2>',
            '<ul>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg" alt="Rob Kocher"/><span>Rob Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg" alt="Tammy Kocher"/><span>Tammy Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png" alt="Charisa Kocher"/><span>Charisa Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png" alt="Kupo Kocher"/><span>Kupo Kocher</span></li>',
            '</ul>'
        ))
        actual = display_household(single_household, ['36729400', '49166778', '49657796', '76460632'])

        self.assertEqual(expected, actual, 'it should be able to display multiple amily members as HTML')

class TestPeopleLinks(unittest.TestCase):

    def test_get_people_links(self):
        self.maxDiff = None

        expected = ['https://api.planningcenteronline.com/people/v2/households/6759685/people?include=field_data']
        actual = get_people_links(single_household)

        self.assertEqual(expected, actual, 'it should return the API links for the people related to the household')

class TestAllowedPeopleList(unittest.TestCase):

    def test_get_allowed_people_list(self):
        self.maxDiff = None

        mock_api_call = MagicMock(side_effect=[households_people])

        expected = ['36729400']
        actual = get_allowed_people_list(['https://api.planningcenteronline.com/people/v2/households/6759685/people?include=field_data'], mock_api_call)

        self.assertEqual(expected, actual, 'it should return a list of all peopel IDs that are allowed to be shown on the online directory from the list of API calls')


if __name__ == '__main__':
    unittest.main()
