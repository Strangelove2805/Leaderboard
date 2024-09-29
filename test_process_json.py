"""Unit tests for json data processing functions"""

import pytest
import process_json as pj


@pytest.fixture
def example_score_data():
    """Create test data for the scores row of processed json files"""
    return [105, 82, 16, 20, 65, 167, 1, 19, 35, 211, 78, 119,
            83, 6, 76, 145, 248, 216, 32, 56, 112, 90, 129, 101,
            34, 73, 109, 24, 46, 205, 83, 13, 23, 192, 10, 47]


@pytest.fixture
def example_year_data():
    """Create test data for the dates row of processed json files"""
    return ["04/09/2008", "01/04/2019", "08/12/2005", "10/08/2001", 
            "12/03/2018", "22/08/2008", "19/01/2002", "12/01/2019", 
            "22/10/2023", "13/08/2002", "23/03/2023", "15/03/2000",
            '01/06/2016', '27/02/2010', '26/12/2006', '27/06/2019', 
            '14/03/2012', '30/09/2004', '04/06/2022', '23/03/2009', 
            '12/08/2013', '07/03/2003', '07/12/2006', '28/12/2002',
            '12/10/2000', '03/09/2002', '16/02/2005', '04/06/2012', 
            '16/03/2004', '23/12/2004', '17/04/2007', '02/02/2021', 
            '18/08/2018', '22/02/2023', '21/05/2014', '26/08/2011']


def test_twin_sort(example_score_data, example_year_data):
    """Ensure both scores and dates are zipped and sorted together"""
    assert pj.twin_sort(example_score_data, example_year_data) == (
        [248, 216, 211, 205, 192, 167, 145, 129, 119, 112, 109, 105,
         101, 90, 83, 83, 82, 78, 76, 73, 65, 56, 47, 46,
         35, 34, 32, 24, 23, 20, 19, 16, 13, 10, 6, 1], 
         ['14/03/2012', '30/09/2004', '13/08/2002', '23/12/2004',
          '22/02/2023', '22/08/2008', '27/06/2019', '07/12/2006',
          '15/03/2000', '12/08/2013', '16/02/2005', '04/09/2008',
          '28/12/2002', '07/03/2003', '17/04/2007', '01/06/2016',
          '01/04/2019', '23/03/2023', '26/12/2006', '03/09/2002',
          '12/03/2018', '23/03/2009', '26/08/2011', '16/03/2004',
          '22/10/2023', '12/10/2000', '04/06/2022', '04/06/2012',
          '18/08/2018', '10/08/2001', '12/01/2019', '08/12/2005',
          '02/02/2021', '21/05/2014', '27/02/2010', '19/01/2002']
    )


def test_limit_best_sumbissions(example_score_data, example_year_data):
    """Test that the submissions per person are limited to a specified length"""
    assert pj.limit_best_sumbissions(example_score_data, example_year_data) == (
        [248, 216, 211, 205, 192, 167, 145, 129, 119, 112, 109, 105,
         101, 90, 83, 83, 82, 78, 76, 73, 65, 56, 47, 46],
         ['14/03/2012', '30/09/2004', '13/08/2002', '23/12/2004',
          '22/02/2023', '22/08/2008', '27/06/2019', '07/12/2006',
          '15/03/2000', '12/08/2013', '16/02/2005', '04/09/2008',
          '28/12/2002', '07/03/2003', '17/04/2007', '01/06/2016',
          '01/04/2019', '23/03/2023', '26/12/2006', '03/09/2002',
          '12/03/2018', '23/03/2009', '26/08/2011', '16/03/2004']
    )


def test_process():
    """Ensure processing is in order and can handle an overflow
       of submission scores"""
    data = [{"name": "Astarion Ancunin", "submissions": 
             [{"name": "A", "date": "05/12/2021", "score": 105},
              {"name": "B", "date": "09/04/2004", "score": 82}, 
              {"name": "C", "date": "17/10/2010", "score": 16}, 
              {"name": "D", "date": "15/02/2014", "score": 54}]}, 
            {"name": "Jenevelle Hallowleaf", "submissions": 
             [{"name": "E", "date": "24/11/2016", "score": 20}, 
              {"name": "F", "date": "29/03/2006", "score": 167}, 
              {"name": "G", "date": "15/02/2013", "score": 1}, 
              {"name": "H", "date": "31/10/2000", "score": 211}, 
              {"name": "I", "date": "09/06/2009", "score": 78}, 
              {"name": "J", "date": "28/09/2017", "score": 47}, 
              {"name": "K", "date": "23/05/2000", "score": 2}, 
              {"name": "L", "date": "21/09/2014", "score": 205}, 
              {"name": "M", "date": "16/12/2001", "score": 208}, 
              {"name": "N", "date": "22/04/2014", "score": 83}, 
              {"name": "O", "date": "20/04/2007", "score": 13}, 
              {"name": "P", "date": "29/11/2018", "score": 83}, 
              {"name": "Q", "date": "29/09/2010", "score": 132}, 
              {"name": "R", "date": "13/10/2007", "score": 244},
              {"name": "S", "date": "13/10/2007", "score": 101},
              {"name": "T", "date": "13/10/2007", "score": 129},
              {"name": "U", "date": "13/10/2007", "score": 248},
              {"name": "V", "date": "13/10/2007", "score": 62},
              {"name": "W", "date": "13/10/2007", "score": 29},
              {"name": "X", "date": "13/10/2007", "score": 192},
              {"name": "Y", "date": "13/10/2007", "score": 23},
              {"name": "Z", "date": "13/10/2007", "score": 20},
              {"name": "0", "date": "13/10/2007", "score": 88},
              {"name": "1", "date": "13/10/2007", "score": 97},
              {"name": "2", "date": "13/10/2007", "score": 6},
              {"name": "3", "date": "13/10/2007", "score": 201},
              {"name": "4", "date": "13/10/2007", "score": 4}]},
            {"name": "Gale Dekarios", "submissions": 
             [{"name": "5", "date": "24/11/2016", "score": 210}, 
              {"name": "6", "date": "29/03/2006", "score": 240}, 
              {"name": "7", "date": "15/02/2013", "score": 178}, 
              {"name": "8", "date": "31/10/2000", "score": 112}, 
              {"name": "9", "date": "09/06/2009", "score": 219}]}]

    assert pj.process(data) == [
        ['Jenevelle Hallowleaf', 
         2687, 
         [248, 244, 211, 208, 205, 201, 192, 167, 132, 129, 101, 
          97, 88, 83, 83, 78, 62, 47, 29, 23, 20, 20, 13, 6], 
         ['13/10/2007', '13/10/2007', '31/10/2000', '16/12/2001', '21/09/2014', 
          '13/10/2007', '13/10/2007', '29/03/2006', '29/09/2010', '13/10/2007', 
          '13/10/2007', '13/10/2007', '13/10/2007', '29/11/2018', '22/04/2014', 
          '09/06/2009', '13/10/2007', '28/09/2017', '13/10/2007', '13/10/2007', 
          '24/11/2016', '13/10/2007', '20/04/2007', '13/10/2007']], 
        ['Gale Dekarios', 
         959, 
         [240, 219, 210, 178, 112], 
         ['29/03/2006', '09/06/2009', '24/11/2016', '15/02/2013', '31/10/2000']], 
        ['Astarion Ancunin', 
         257, 
         [105, 82, 54, 16], 
         ['05/12/2021', '09/04/2004', '15/02/2014', '17/10/2010']]
        ]
