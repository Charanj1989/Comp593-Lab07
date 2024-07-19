"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
import sqlite3
from create_db import main
import pandas as pd
def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Getting People Data from the Database"
    con = sqlite3.connect("social_network.db")
    cur = con.cursor()
    cur.execute("select name,age from people where age > 50 OR age = 50")
    all_people = cur.fetchall()
    con.commit()
    con.close()
    return all_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # TODO: Create function body
    # Hint: Use a for loop to iterate the list of tuples to print a sentence for each old person
    for o in name_and_age_list:
        print(f"{o[0]} is {o[1]} years")
    return

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # TODO: Create function body
    # Hint: In Lab 3, we converted a list of tuples into a pandas DataFrame and saved it to a CSV file
    Ne = []
    Ae = []
    for c in name_and_age_list:
        Ne.append(c[0])
        Ae.append(c[1])
    df = pd.DataFrame({"Name": Ne,"Age":Ae})
    fname = os.path.basename(csv_path)
    df.to_csv(fname, index=False)
        
if __name__ == '__main__':
   main()