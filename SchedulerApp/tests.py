import unittest
from django.test import TestCase
from .models import Room, MeetingTime, Instructor, Course, Department, Section
from .views import Schedule, Data

class TimetableGenerationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = Data()

    def setUp(self):
        self.schedule = Schedule().initialize()

    def test_timetable_generation(self):
        # Check if the schedule is generated
        self.assertIsNotNone(self.schedule)

    def test_class_capacity(self):
        # Check if the maximum capacity of a class is not exceeded
        classes = self.schedule.getClasses()
        for cls in classes:
            self.assertTrue(cls.room.seating_capacity <= 50)

    def test_teacher_schedule_conflicts(self):
        # Check if teachers do not teach at the same time slot
        classes = self.schedule.getClasses()
        instructor_schedule = {}
        for cls in classes:
            instructor_id = cls.instructor.id
            if instructor_id in instructor_schedule:
                for time_slot in instructor_schedule[instructor_id]:
                    self.assertNotEqual(cls.meeting_time, time_slot)
            else:
                instructor_schedule[instructor_id] = [cls.meeting_time]

    def test_unique_class_timing(self):
        # Check if each class has a unique timing
        classes = self.schedule.getClasses()
        timings = set()
        for cls in classes:
            self.assertNotIn(cls.meeting_time, timings)
            timings.add(cls.meeting_time)

    def test_section_requirements(self):
        # Check if classes are allotted according to section requirements
        sections = self.data.get_sections()
        for section in sections:
            section_courses = [cls.course for cls in self.schedule.getClasses() if cls.section == section]
            self.assertTrue(section.checkRequirements(section_courses))

    def test_course_students_capacity(self):
        # Check if course students <= room seating capacity
        classes = self.schedule.getClasses()
        for cls in classes:
            self.assertTrue(cls.course.students <= cls.room.seating_capacity)

    def test_unique_room_assignment(self):
        # Check if two classes don't have the same room
        classes = self.schedule.getClasses()
        room_assignments = {}
        for cls in classes:
            self.assertNotIn(cls.room.id, room_assignments.get(cls.meeting_time, []))
            room_assignments.setdefault(cls.meeting_time, []).append(cls.room.id)

    def test_even_course_distribution(self):
        # Check if there is an even distribution of courses in a section per week
        sections = self.data.get_sections()
        for section in sections:
            section_courses = [cls for cls in self.schedule.getClasses() if cls.section == section]
            days_count = {}
            for cls in section_courses:
                days_count[cls.meeting_time.day] = days_count.get(cls.meeting_time.day, 0) + 1
            max_count = max(days_count.values())
            min_count = min(days_count.values())
            self.assertTrue(max_count - min_count <= 1)

    def test_unique_teacher_timing(self):
        # Check if class timing for each teacher is unique
        classes = self.schedule.getClasses()
        teacher_timings = {}
        for cls in classes:
            teacher_id = cls.instructor.id
            self.assertNotIn(cls.meeting_time, teacher_timings.get(teacher_id, []))
            teacher_timings.setdefault(teacher_id, []).append(cls.meeting_time)

    def test_teacher_allocation(self):
        # Check if teachers are allocated to their course accordingly
        classes = self.schedule.getClasses()
        for cls in classes:
            self.assertEqual(cls.instructor.id, cls.course.instructor.id)

if __name__ == '__main__':
    unittest.main()
