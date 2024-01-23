"""Utility functions for working with course schedules.

A course schedule is a list of sets where each entry in the list
represents an academic term, and the entries in the sets are strings
representing the course ids of courses taken during that term.

Author:
Version: 
"""

import json


def schedule_to_json(schedule):
    """Convert a course schedule to a format suitable for saving as JSON.

    The provided schedule will not be modified.

    Args:
        schedule (list): A list of sets.

    Returns:
        list: A list of lists.
    """
    
    total_list = []
    for sets in schedule:
        lists = list(sets)
        total_list.append(lists)
    return total_list
#Monday
#done

def json_to_schedule(schedule_list):
    """Convert a list of lists to a list of sets.

    The elements in each list will be stored in alphabetical order.
    The provided list will not be modified.

    Args:
        schedule_list (list): A list of lists.

    Returns:
        list: A list of sets.

    """
    lst_of_sets = []
    for lsts in schedule_list:
        lst_of_sets.append(set(lsts))
    return lst_of_sets

#Monday
#Done

def save_schedule(schedule, filename):
    """Save a course schedule to a JSON file.

    The course schedule is represented as a list of sets, where each
    set contains the course ids (strings) for the corresponding
    semester.

    Within each semester, the course ids will be stored in alphabetical
    order in the resulting JSON file.

    Args:
        schedule (list): The course schedule.
        filename (str): The filename for the JSON file.

    """
    json.dump(schedule, filename)
#wednesday
#done?
    #ask TAs

def load_schedule(filename):
    """Load a course schedule from an JSON file.

    The return value will be a list of sets, where each set contains
    the course ids (strings) for the corresponding semester.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        list: A list of sets representing the course schedule.

    """
    with open(filename) as f:
        total = json.load(f)
    return total
#Wednesday
#done?
#ask TAs

def get_duplicates(schedule):
    """Get duplicate courses in a schedule.

    The resulting set will be empty if there are no duplicates.

    Args:
        schedule (list): The course schedule.

    Returns:
        set: A set of duplicate courses.
    """
    dup_list = []
    dup_set = set()
    for sets in schedule:
        for courses in sets:
            dup_list.append(courses)
            if dup_list.count(courses) > 1:
                dup_set.add(courses)
    return dup_set
    
    
    
#wednesday
#done?
