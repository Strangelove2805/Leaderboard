import pytest
from process_json import twin_sort


@pytest.fixture
def example_score_data():
    return [105, 82, 16, 20, 65, 167, 1, 19, 35, 211, 78, 119]


@pytest.fixture
def example_year_data():
    return ["04/09/2008", "01/04/2019", "08/12/2005", "10/08/2001", 
            "12/03/2018", "22/08/2008", "19/01/2002", "12/01/2019", 
            "22/10/2023", "13/08/2002", "23/03/2023", "15/03/2000"]


def test_twin_sort(example_score_data, example_year_data):
    assert twin_sort(example_score_data, example_year_data) == (
        [211, 167, 119, 105, 82, 78, 65, 35, 20, 19, 16, 1], 
        ['13/08/2002', '22/08/2008', '15/03/2000', '04/09/2008', 
         '01/04/2019', '23/03/2023', '12/03/2018', '22/10/2023', 
         '10/08/2001', '12/01/2019', '08/12/2005', '19/01/2002']
    )
