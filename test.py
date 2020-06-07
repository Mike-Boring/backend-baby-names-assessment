"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    sorting_names = []
    with open(filename) as f:
        text = f.read().split()
        for text_section in text:
            if text_section.endswith('</h3>'):
                sorting_names.append(text_section.replace('</h3>', ''))
            if text_section.startswith('align="right"><td>'):
                sorting_names.append(text_section.replace(
                    'align="right"><td>', '').replace('</td><td>', ' ').replace('</td>', ''))
    final_list = []
    for single_name in sorting_names:
        if single_name == sorting_names[0]:
            final_list.append(single_name)
        else:
            split_single_name = single_name.split()
            if len(split_single_name) == 3:
                if split_single_name[1] in ' '.join(final_list):
                    continue
                if split_single_name[2] in ' '.join(final_list):
                    continue
                final_list.append(
                    split_single_name[1] + ' ' + split_single_name[0])
                final_list.append(
                    split_single_name[2] + ' ' + split_single_name[0])
    final_sorted_list = sorted(final_list)
    return final_sorted_list


extract_names('./baby1990.html')
