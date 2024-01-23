"""Utility functions for working with catalog information.

Author: Will Ponczak
Version:
"""

import json
import textwrap


def parse_credits(credits):
    """Return a tuple of ints representing the possible credit values.

    Examples:
    >>> parse_credits("3")
    (3,)
    >>> parse_credits("1-4")
    (1, 2, 3, 4)

    Args:
        credits (str): The credits string.

    Returns:
        tuple: An ordered tuple of all possible credit values.
    """
    if '-' in credits:
        credits.replace('-', ',')
        int_credit = int(credits)
    print(credits)
    num_list = []
    '''if len(credits) == 1:
        num = int(credits)
        tup = (num,)
        return tup
    else:
        start_num = int(credits[0])
        if len(credits) == 3:
            end_num = int(credits[-1])
        elif len(credits) == 4:
            end_num = int(credits[-2:-1])
        elif len(credits) == 5:
            end_num = int(credits[-3])
            
        for num in range(start_num, end_num + 1): 
            num_list.append(num)
    return tuple(num_list)
        '''
#Done

def json_to_catalog(json_dict):
    """Convert from the json catalog format to the correct internal format.

    This will return an exact copy of the provided dictionary except for the
    following:

    * The lists of prerequisite course ids will be converted to sets.
    * The credit strings will be converted to integer tuples (using
    the parse_credits function)

    Args:
        json_dict (dict): A catalog dictionary as ready by the json module.

    Returns:
        dict: A catalog dictionary in the correct internal format.

    """
    new_dict = json_dict.copy()
    for index, course in new_dict.items():
        new_cred = parse_credits(course["credits"])
        new_prereq = set(course["prerequisites"]) 
        course['credits'] = new_cred
        course['prerequisites'] = new_prereq
    return new_dict
#Done

def load_catalog(filename):
    """Read course information from an JSON file and return a dictionary.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        dict: A dictionary containing course information.
    """
    
    with open(filename) as file:
        total = json.load(file)
    return total
#how could I test this?
#arent the contents of the file already a dictionary?
#ask teacher



def get_dependencies(course_id, catalog):
    """Get the all dependencies for a course.

    This function will return the prerequisites for the course, plus
    all prerequisites for those prerequisites, and so on.

    Args:
        course_id (str): The ID of the course.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of course dependencies.

    """
    dependencies = set()
    for course in catalog: #needed for course_id check
        if course_id == course: #checks for if the couirse_id matches the catalog
            pre_set = catalog[course]['prerequisites']
            dependencies = dependencies.union(pre_set)
            
    for name in dependencies:
        dependencies = dependencies.union(get_dependencies(name, catalog))
    return dependencies
#Monday
#Done

def format_course_info(course_id, catalog, width=40):
    """Format course information for display.

    The resulting string will have five fields: Name, Description,
    Credits, Prerequisites, and Dependencies.  Each field will be
    separated by a blank line and each will be wrapped to the maximum
    allowable number of characters. The string will not end in a newline.

    Args:
        course_id (str): The ID of the course.
        catalog (dict): The dictionary containing course information.
        width (int, optional): The width for text wrapping. Defaults to 40.

    Returns:
        str: Formatted course information.

    """
    
# Tuesday

def total_credits(schedule, catalog):
    """Calculate the range of total credits in a schedule.

    Args:
        schedule (list): The course schedule.
        catalog (dict): The dictionary containing course information.

    Returns:
        tuple: A two entry tuple where the first entry is the minimum
            total credits for the schedule and the second is the maximum total
            credits.
    """ 
    num_list = []
    max_cred_list = []
    min_cred_list = []
    for list_classes in schedule:
        for classes in list_classes:
            for course in catalog:
                if classes == course:
                    num_list.append(catalog[course]['credits'])
    for max_tup in num_list:
        new_max_tup = max(max_tup)
        max_cred_list.append(new_max_tup)
            
    for min_tup in num_list:
        new_min_tup = min(min_tup)
        min_cred_list.append(new_min_tup)
    
    min_cred = sum(min_cred_list)
    max_cred = sum(max_cred_list)
    
    total_list = (min_cred, max_cred)
    
    return tuple(total_list)
    
    
                
        
#Monday
#Work on at night//Office Hours
#Done? Tests are working, but seems too simple...

def available_classes(schedule, semester, catalog):
    """Get the available classes for a semester based on the current schedule.

    A course is available for the indicated semester if it is not
    already present somewhere in the schedule, and all of the
    prerequisites have been fulfilled in some previous semester.

    Args:
        schedule (list): The current course schedule.
        semester (int): The semester for which to find available classes.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of available classes for the specified semester.

    """
    completed_prereq = set()
    available = set()
    schedule_total_set = set()
    new_semester = set()
    
    #This is the classes except for the classes in the given semester
    sub_list = (schedule[0:semester-1])
    for set_1 in sub_list:
        new_semester.update(set_1)
    
    #get the classes into a set
    for sem_set in new_semester:
        completed_prereq.add(sem_set)#adds the classes in the schedule into a set
            
    #Get the available classes into a set
    for course in catalog:
        pre_req_set = catalog[course]['prerequisites']
        for prereq_str in pre_req_set:
            if prereq_str in completed_prereq:
                available.add(course)
        
    for course in available.copy():
        if course in new_semester:
            available.difference_update(new_semester)
        
    
    return available
            
#Tuesday
#done?

def check_prerequisites(schedule, catalog):
    """Check for courses in a schedule with unmet prerequisites.

    Args:
        schedule (list): The course schedule.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of courses with unmet prerequisites.
    """  
    pre_req_set = set()
    for sets in schedule:
        for classes in sets:
            for course in catalog:
                if classes == course:
                    if catalog[course]['prerequisites'] not in schedule: #good here
                        pre_req_set.add(course)
    return pre_req_set                       
#tuesday
#done?
if __name__ == '__main__':
    print(parse_credits('3-8'))


