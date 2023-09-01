# Student Grades

Write a program that reads a list of students and their grades from a file and outputs to a JSON file. 

## Focus on

- Read / Write files
- Standard collections (List, Dictionary)
- Common data tasks (Order, Average, Find Max and Min)

## Instructions

Write a program that reads a list of students and their grades from a file. 

The file should be formatted as follows:

```
student_name, grade
```

For example, the following file would contain the grades for three students:

```
John Doe, 80
Jane Doe, 90
Peter Smith, 75
```

The program should then do the following:

1. Create a dictionary where the keys are the student names and the values are the grades.
2. Sort the students by their grades in decreasing order.
3. Find the highest and lowest grades.
4. Calculate the class average.
5. Create a dictionary with the following keys and corresponding values:
- `high_score`: Highest Score
- `low_score`: Lowest Score
- `total_students`: Total Number of Students
- `avg_score`: Average Score
- `students`: List of students and scores ordered by score.
6. Serialize the dictionary to JSON format in a file called `output.json`.

Example Output:

```json
{
  "high_score": 90,
  "low_score": 75,
  "total_students": 3,
  "avg_score": 81.6,
  "students": [
    ["Jane Doe", 90],
    ["John Doe", 80],
    ["Peter Smith", 75]
  ]
}
```
