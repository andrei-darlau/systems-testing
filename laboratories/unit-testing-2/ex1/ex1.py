import datetime
from faker import Faker
from unittest.mock import patch, MagicMock
from calendar import isleap

fake = Faker()

def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)

def test_leap_year():
    with patch('__main__.datetime.datetime') as mock_datetime:
        for i in range(100):
            random_year = int(fake.year())
            
            mock_today = MagicMock()
            mock_today.year = random_year
            mock_datetime.today.return_value = mock_today
            
            assert is_leap_year() == isleap(random_year)
        print("Passed")

if __name__ == "__main__":
    test_leap_year()
