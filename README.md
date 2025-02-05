# SchedulerAI
----------------------------------------------------------------------------------------------------------------------------
### An intelligent timetable generator that generates University timetable using `Genetic Algorithm`.

## Overview
The **Timetable Management System** is a web-based application designed to manage the creation, editing, and viewing of academic timetables for institutions. It allows administrators to:
- Add and manage courses, instructors, rooms, and meeting times.
- Generate and view timetables for different sections.
- Download the generated timetables in Excel format.
- Filter timetables by date for easier navigation.

The system is built using Django, with an intuitive front-end interface for interacting with the timetable and backend.

## Features
- **Date Selection**: Users can select a specific date to filter the timetable by the corresponding day of the week.
- **Timetable Display**: A dynamic timetable that shows the course schedule for each section based on time slots and meeting days.
- **Excel Export**: Users can download the generated timetable in `.xlsx` format.
- **CRUD Operations**: Admin users can perform Create, Read, Update, and Delete operations for:
  - Courses
  - Instructors
  - Rooms
  - Meeting Times
  - Sections
  - Departments

 #### About the project:
Project uses genetic algorithm to satisfy the constraints related to Timetable scheduling. The program satisfies the following constraints:-

| Hard Constraints                                  | Soft Constraints                                     |
| --------------------------------------------------|:----------------------------------------------------:|
| Unique class timing                               | classes are alloted according to section requirements|
| Course.students <= room.seating capacity          | All courses are according to their department        |
| Two classes dont have same room to avoid clash    | Even distribution of course in a section per week    |
| Class timing for each teacher is unique           |
| Teachers are allocated to their course accordingly|


## Requirements
- **Python 3.x**: The backend is built using Django, a Python web framework.
- **Django**: The web framework used to manage routing, views, models, and admin functionality.
- **JavaScript**: Used for interactivity on the frontend (e.g., handling the date picker and downloading the timetable).
- **HTML/CSS**: Used for building and styling the frontend pages.
- **MySQL or SQLite**: The database to store timetable data and other entities.

## Installation Instructions

### Prerequisites
1. **Python**: Ensure Python 3.x is installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. **Django**: Install Django using pip.
   ```bash
   pip install django
   pip install -r requirements.txt

## Technologies Used
**Django**: Backend framework for managing routes, views, and database.

**HTML/CSS**: Frontend design and styling.

**JavaScript**: For date selection and handling the download action.

**SQLite3**: Used for storing timetable and related data.

**AJAX**: For generating and downloading the timetable without refreshing the page.



