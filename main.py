#!/usr/bin/env python3
"""A program that reads grades from a file and writes them to a JSON file."""


import sys
import json

def read_input(filename):
    """Reads grades from a file.
    
    Args:
        filename: The name of the file.

    Returns:
        A dictionary mapping student names to grades.
    """
    grades = {}
    with open(filename, "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            student_name, grade = line.split(",")
            grades[student_name] = int(grade)
    return grades

def write_output(grades):
    """Writes grades to a file.

    Args:
        filename: The name of the file.
        grades: A dictionary mapping student names to grades.
    """

    with open("output.json", "w", encoding="utf8") as file:
        json.dump(grades, file, indent=4)

def main():
    """The main function."""

    try:
        file = sys.argv[1]
    except IndexError:
        print("Usage: main.py <file>")
        sys.exit(1)

    grades = read_input(file)

    # Sort the students by their grades in decreasing order.
    sorted_grades = sorted(grades.items(), key=lambda x: x[1], reverse=True)

    # Find the highest and lowest grades.
    highest_grade = max(grades.values())
    lowest_grade = min(grades.values())

    # Calculate the class average.
    class_average = sum(grades.values()) / len(grades)

    # Create a dictionary with the required keys.
    output_dict = {
    "high_score": highest_grade,
    "low_score": lowest_grade,
    "total_students": len(grades),
    "avg_score": class_average,
    "students": sorted_grades
    }

    # Write the dictionary as JSON to a file.
    write_output(output_dict)


if __name__ == "__main__":
    main()
