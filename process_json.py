"""Transforming raw .json file data to a usable Python list format"""

BEST_SUB_LIMIT = 24


def parse_data(data: list[dict]) -> tuple[list[str], list[int]]:
    """Grabs the name and their submissions scores from a dictionary
       in the input .json file

    Input Parameters:
    -----------------
    data            Type:   list[dict]
                    Use:    Dict containing a candidate's name and data
                            for submission attempts

    Output Parameters:
    -----------------

    candidate       Type:   list[str]
                    Use:    The list for storing the name, and later total 
                            score and top-N scores for a candidate

    scores          Type:   list[int]
                    Use:    List of all numeric scores for a given candidate

    dates           Type:   list[str]
                    Use:    List of all dates that coincide with scores
    """
    candidate = []
    scores = []
    dates = []

    candidate.append(data['name'])

    for attempt in data['submissions']:

        scores.append(attempt['score'])
        dates.append(attempt['date'])

    return (candidate, scores, dates)


def twin_sort(scores, dates) -> tuple[list[int], list[str]]:
    """Sort the candidate's scores from highest-to-lowest and sort
       the corresponding list of dates to coincide
       
    Input Parameters:
    -----------------
    scores          Type:   list[int]
                    Use:    Unordered list of scores for candidate

    dates           Type:   list[str]
                    Use:    Unordered dates that correspond to scores

    Output Parameters:
    -----------------

    scores          Type:   list[int]
                    Use:    Sorted scores for a given candidate

    dates           Type:   list[str]
                    Use:    Sorted date list
    """
    sorted_lists = sorted(zip(scores, dates), reverse=True)

    scores, dates = zip(*sorted_lists)

    return (list(scores), list(dates))


def limit_best_sumbissions(scores: list[int],
                           dates: list[int],
                           limit=BEST_SUB_LIMIT) -> tuple[list[int], list[str]]:
    """Cut down the list of numerical scores and their dates to just 
       the top-N best submissions

    Input Parameters:
    -----------------
    scores          Type:   list[int]
                    Use:    Unordered list of scores for candidate

    dates           Type:   list[str]
                    Use:    Unordered dates that correspond to scores

    Output Parameters:
    -----------------

    scores          Type:   list[int]
                    Use:    Top-N scores for a given candidate

    dates           Type:   list[str]
                    Use:    Top-N list of dates
    """
    scores, dates = twin_sort(scores, dates)

    if len(scores) > limit:

        scores = scores[:limit]
        dates = dates[:limit]

    return (scores, dates)


def process(data: list[dict]) -> list[str,int,list,list]:
    """Take the raw .json file and convert it to an easily
       workable format:

       [ candidate name, total score, [scores], [dates] ]

    Input Parameters:
    -----------------
    data            Type:   list[dict]
                    Use:    Unprocessed json file data containing
                            submission info (name, scores etc.)

    Output Parameters:
    -----------------

    people          Type:   list[str,int,list,list]
                    Use:    Each candidate's name, total score, list of
                            top-N scores and list or top-N dates - all
                            sorted by the total score column
    """
    people = []

    for person in data:

        candidate, scores, dates = parse_data(person)
        scores, dates = limit_best_sumbissions(scores, dates)

        total = sum(scores)

        candidate.append(total)
        candidate.append(scores)
        candidate.append(dates)

        people.append(candidate)

    # Sort by total-scores row
    people.sort(key=lambda row: row[1], reverse=True)

    return people
