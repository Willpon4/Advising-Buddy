"""Unit tests for catalog_utils.

Author: Will Ponczak
Version:
"""

import catalog_utils as cu


def test_parse_credits():
    assert cu.parse_credits('1-4') == (1, 2, 3, 4)
    assert cu.parse_credits('4') == (4,)

def test_json_to_catalog():
    json_dict = {
    "JAPN 101": {
        "name": "Elementary Japanese I",
        "credits": '4',
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing.",
        "prerequisites": []
    },
    "JAPN 102": {
        "name": "Elementary Japanese II",
        "credits": '4',
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.",
        "prerequisites": [
            "JAPN 101"
        ]
    },
    "JAPN 231": {
        "name": "Intermediate Japanese I",
        "credits": '3-4',
        "description": "A thorough review of grammar, vocabulary building, conversation, composition, and reading.",
        "prerequisites": [
            "JAPN 102"
        ]
    },
    "CS 488": {
        "name": "Computer Graphics Applications",
        "credits": "3",
        "description": "This course develops a computer graphics application package based on standard graphics functions as well as attributes of a graphical user interface. It includes experience in applying interactive computer graphics techniques to industrial problems.",
        "prerequisites": [
            "CS 240",
            "CS 261"
        ]
    },
    "ALGEBRA": {
        "name": "College Algebra",
        "credits": "0-3",
        "description": "This is a stand-in course representing MATH 255, MATH 256, or a sufficient score on the ALEKS exam.",
        "prerequisites": []
    }
    }
    
    assert cu.json_to_catalog(json_dict) == {
    "JAPN 101": {
        "name": "Elementary Japanese I",
        "credits": (4,),
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing.",
        "prerequisites": set()
    },
    "JAPN 102": {
        "name": "Elementary Japanese II",
        "credits": (4,),
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.",
        "prerequisites": {
            "JAPN 101"
        }
    },
    "JAPN 231": {
        "name": "Intermediate Japanese I",
        "credits": (3, 4,),
        "description": "A thorough review of grammar, vocabulary building, conversation, composition, and reading.",
        "prerequisites": {
            "JAPN 102"
        }   
    },
    "CS 488": {
        "name": "Computer Graphics Applications",
        "credits": (3,),
        "description": "This course develops a computer graphics application package based on standard graphics functions as well as attributes of a graphical user interface. It includes experience in applying interactive computer graphics techniques to industrial problems.",
        "prerequisites": {
            "CS 240",
            "CS 261"
        }
    },
    "ALGEBRA": {
        "name": "College Algebra",
        "credits": (0, 1, 2, 3,),
        "description": "This is a stand-in course representing MATH 255, MATH 256, or a sufficient score on the ALEKS exam.",
        "prerequisites": set()
    }
    }
    assert len(cu.json_to_catalog(json_dict)) == 5



def test_load_catalog():
    assert cu.load_catalog("japn_catalog.json") == {
        'JAPN 101': {
              'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()
              },
         'JAPN 102': {
              'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}
              },
         'JAPN 231': {
            'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}
            }
        }
    
    assert len(cu.load_catalog("japn_catalog.json")) == 3
    

def test_get_dependencies():
    catalog = {
        "JAPN 101": {
            "name": "Elementary Japanese I",
            "credits": (4,),
            "description": "The fundamentals of Japanese through listening, speaking, reading, and writing.",
            "prerequisites": set()
        },
        "JAPN 102": {
            "name": "Elementary Japanese II",
            "credits": (4,),
            "description": "The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.",
            "prerequisites": {
                "JAPN 101"
            }
        },
        "JAPN 231": {
            "name": "Intermediate Japanese I",
            "credits": (3, 4),
            "description": "A thorough review of grammar, vocabulary building, conversation, composition, and reading.",
            "prerequisites": {
                "JAPN 102"
            }
        }
    }
    assert cu.get_dependencies('JAPN 102', catalog) == {'JAPN 101'}
    assert cu.get_dependencies('JAPN 231', catalog) == {'JAPN 102', 'JAPN 101'}


def test_total_credits():
    catalog = {"CS 488": {
        "name": "Computer Graphics Applications",
        "credits": (3,),
        "description": "This course develops a computer graphics application package based on standard graphics functions as well as attributes of a graphical user interface. It includes experience in applying interactive computer graphics techniques to industrial problems.",
        "prerequisites": {
            "CS 240",
            "CS 261"
        }
        },
    "CS 497": {
        "name": "Independent Study",
        "credits": (1, 2, 3,),
        "description": "An advanced course to give independent study experience under faculty supervision. May be taken multiple times for credit, but no more than three credits may be used in the computer science program graduation requirements.",
        "prerequisites": {
            "CS 159"
        }
    },
    "CS 482": {
        "name": "Selected Topics in Information Security",
        "credits": (1, 2, 3,),
        "description": "Topics in information security. Offered only with the approval of the department head; may be repeated for credit when course content changes",
        "prerequisites": {
            "CS 240",
            "CS 261"
        }
    },
    "ALGEBRA": {
        "name": "College Algebra",
        "credits": (0, 1, 2, 3,),
        "description": "This is a stand-in course representing MATH 255, MATH 256, or a sufficient score on the ALEKS exam.",
        "prerequisites": set()
    },
    "JAPN 101": {
        "name": "Elementary Japanese I",
        "credits": (4,),
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing.",
        "prerequisites": set()
    }
               
               }
    assert cu.total_credits([{"CS 497", 'CS 488'}], catalog) == (4, 6,)
    assert cu.total_credits([{'JAPN 101', 'CS 488'}], catalog) == (7, 7)


def test_available_classes():
    catalog = {
        "JAPN 101": {
            "name": "Elementary Japanese I",
            "credits": (4,),
            "description": "The fundamentals of Japanese through listening, speaking, reading, and writing.",
            "prerequisites": set()
        },
        "JAPN 102": {
            "name": "Elementary Japanese II",
            "credits": (4,),
            "description": "The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.",
            "prerequisites": {
                "JAPN 101"
            }
        },
        "JAPN 231": {
            "name": "Intermediate Japanese I",
            "credits": (3, 4,),
            "description": "A thorough review of grammar, vocabulary building, conversation, composition, and reading.",
            "prerequisites": {
                "JAPN 102"
            }
        }
    }
    assert cu.available_classes([{'JAPN 101'}, set(), set()], 1, catalog) == {'JAPN 102'}
    assert cu.available_classes([{'JAPN 101'}, {'JAPN 102'}, set()], 2, catalog) == {'JAPN 231'}


def test_check_prerequisites():
    catalog = {
    "JAPN 101": {
        "name": "Elementary Japanese I",
        "credits": (4,),
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing.",
        "prerequisites": set()
    },
    "JAPN 102": {
        "name": "Elementary Japanese II",
        "credits": (3,),
        "description": "The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.",
        "prerequisites": {
            "JAPN 101"
        }
    },
    "JAPN 231": {
        "name": "Intermediate Japanese I",
        "credits": (3, 4),
        "description": "A thorough review of grammar, vocabulary building, conversation, composition, and reading.",
        "prerequisites": {
            "JAPN 102"
        }
    }
        }
    assert cu.check_prerequisites([{'JAPN 101'}, set(), {'JAPN 231'}], catalog) == {'JAPN 231'}
    assert cu.check_prerequisites([set(), {'JAPN 102'}, {'JAPN 231'}], catalog) == {'JAPN 102'}
    


# We're providing tests for format_course_info() because these
# kinds of tests are particularly annoying to write.

def test_format_course_info():
    catalog = cu.load_catalog("japn_catalog.json")

    # Test the default width...
    actual = cu.format_course_info("JAPN 231", catalog)
    expect = """Name: Intermediate Japanese I

Description: A thorough review of
grammar, vocabulary building,
conversation, composition, and reading.

Credits: 3-4

Prerequisites: JAPN 102

Dependencies: JAPN 101, JAPN 102"""
    assert actual == expect

    #  Test an alternate width...
    actual = cu.format_course_info("JAPN 231", catalog, width=80)
    expect = """Name: Intermediate Japanese I

Description: A thorough review of grammar, vocabulary building, conversation,
composition, and reading.

Credits: 3-4

Prerequisites: JAPN 102

Dependencies: JAPN 101, JAPN 102"""
    assert actual == expect

    #  Test a different course and a different width...
    actual = cu.format_course_info("JAPN 101", catalog, width=50)
    expect = """Name: Elementary Japanese I

Description: The fundamentals of Japanese through
listening, speaking, reading, and writing.

Credits: 4

Prerequisites:

Dependencies:"""
    assert actual == expect