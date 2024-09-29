"""Organising the .json score information by a specified year-range"""


def pop_misfits(candidate: list[str,int,list,list],
               cutoff_year: int) -> list[str,int,list,list]:
    """Grabs the name and their submissions scores from a dictionary
       in the input .json file

    Input Parameters:
    -----------------
    candidate       Type:   list[str,int,list,list]
                    Use:    List with a candidate's name, total score, list
                            of top scores and dates for those scores

    cutoff_year     Type:   int
                    Use:    The year before-which all submissions should be cropped

    Output Parameters:
    -----------------

    candidate       Type:   list[str,int,list,list]
                    Use:    Cut-down version of the input list with the lists
                            of scores and dates sorted above a given year
    """

    # Count backwards so that popping doesn't affect 'i'
    for i in range(len(candidate[2]) - 1, -1, -1):

        date = int(candidate[3][i][-4:])

        if date < cutoff_year:

            candidate[2].pop(i)
            candidate[3].pop(i)

    return candidate


def crop_dates(json_data: list[list], cutoff_year: int) -> list[list]:
    """Grabs the name and their submissions scores from a dictionary
       in the input .json file

    Input Parameters:
    -----------------
    json_data       Type:   list[list]
                    Use:    Compiled json data containing lists that correspond
                            to each candidate's compiled submissions

    cutoff_year     Type:   int
                    Use:    The year before-which all submissions should be cropped

    Output Parameters:
    -----------------

    json_data       Type:   list[list]
                    Use:    Compiled candidate submission data sorted by total score
    """
    for candidate in json_data:

        candidate = pop_misfits(candidate, cutoff_year)
        candidate[1] = sum(candidate[2])

    json_data.sort(key=lambda row: row[1], reverse=True)

    return json_data
