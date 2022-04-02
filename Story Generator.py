from __future__ import with_statement
import random

from numpy import who
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Maryam', 'Daniel', 'Ahmad', 'Bilal']
residence = ['Islamabad', 'Lahore', 'Karachi', 'Peshawer'] 
went = ['school', 'college', 'university', 'seminar', 'office', 'ground']
happened = ['made a lot of friends', 'eat a burger', 'found a secret', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) +', went to the ' + random.choice(went) + ', and ' + random.choice(happened))