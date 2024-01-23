"""Unit tests for schedule_utils.

Author: Will Ponczak
Version:
"""

import schedule_utils as su

def test_schedule_to_json():
    assert su.schedule_to_json([{'ALGEBRA', 'CS 159'}, {'CS 149'}, {'CS 227'}]) == [['ALGEBRA', 'CS 159'], ['CS 149'], ['CS 227']]
    assert su.schedule_to_json([{'CS 497'}, {'CS 482'}]) == [['CS 497'], ['CS 482']]

def test_json_to_schedule():
    assert su.json_to_schedule([['ALGEBRA', 'CS 159'], ['CS 149'], ['CS 227']]) == [{'ALGEBRA', 'CS 159'}, {'CS 149'}, {'CS 227'}]
    assert su.json_to_schedule([['CS 497'], ['CS 482']]) == [{'CS 497'}, {'CS 482'}]


def test_save_load_schedule():
    schedule = [{'JAPN 101'}, {'JAPN 102'}, set()]
    saved_data =  su.save_schedule(schedule, "sample.json")
    assert su.load_schedule("sample.json") == schedule
    
    schedule_2 = [{'JAPN 101'}, {'JAPN 102'}, {'JAPN 231'}]
    saved_data_2 = su.save_schedule(schedule_2, 'sample1.json')
    assert su.load_schedule('sample1.json') == schedule_2
    #assert saved_data == loaded_data
    
    # One strategy for testing save and load is to:
    #
    # * Create a schedule by hand.
    # * Use save_schedule() to save that schedule.
    # * Use load_schedule() to load the resulting file.
    # * Assert that the loaded data matches the saved data.
    #
    # This strategy has the disadvantage of not testing the two methods
    # in isolation, which is generally the goal of unit testing. But it
    # is easier to implement, because no additional files are required.
    


def test_get_duplicates():
    assert su.get_duplicates([{'ALGEBRA', 'CS 149'},
         {'CS 149'},
         {'CS 227', 'CS 159', 'CS 149'},
         {'CS 240', 'CS 261', 'ALGEBRA'}
         ]) == {'ALGEBRA', 'CS 149'}
    assert su.get_duplicates([{'ALGEBRA', 'CS 149'},
         {'CS 159'},
         {'CS 227', 'CS 159', 'CS 149'},
         {'CS 240', 'CS 261', 'ALGEBRA'}
         ]) == {'ALGEBRA', 'CS 159', 'CS 149'}