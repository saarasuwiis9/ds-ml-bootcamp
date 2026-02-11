import os
import re

def track_assignments(base_dir):
    submissions_dir = os.path.join(base_dir, "submissions")
    if not os.path.exists(submissions_dir):
        print(f"Error: Submissions directory not found at {submissions_dir}")
        return

    students = {}
    
    # regex patterns for assignments (handles typos, word numbers, and common naming conventions)
    # Using \b for short forms a1, a2, a3 to avoid matching data1.csv etc.
    a1_pattern = re.compile(r"(assig[n]*m[e]*nt|assig[n]*m[er]nt|asig[n]*ment)[-_ ]*(1|one)|\ba1\b", re.IGNORECASE)
    a2_pattern = re.compile(r"(assig[n]*m[e]*nt|assig[n]*m[er]nt|asig[n]*ment)[-_ ]*(2|two)|\ba2\b", re.IGNORECASE)
    a3_pattern = re.compile(r"(assig[n]*m[e]*nt|assig[n]*m[er]nt|asig[n]*ment)[-_ ]*(3|three)|\ba3\b", re.IGNORECASE)

    # Folders that are definitely NOT students
    exclude_folders = {"000.example", ".git", "assignment-1", "assignment-2", "assignment-3"}

    for item in os.listdir(submissions_dir):
        item_path = os.path.join(submissions_dir, item)
        
        if os.path.isdir(item_path):
            student_name = item
            if student_name.lower() in exclude_folders:
                continue
                
            students[student_name] = {"A1": False, "A2": False, "A3": False}
            
            # Recursive check (up to 3 levels deep) inside student folder
            for root, dirs, files in os.walk(item_path):
                depth = root[len(item_path):].count(os.sep)
                if depth > 2:
                    continue
                    
                all_items = dirs + files
                for sub_item in all_items:
                    if a1_pattern.search(sub_item):
                        students[student_name]["A1"] = True
                    if a2_pattern.search(sub_item):
                        students[student_name]["A2"] = True
                    if a3_pattern.search(sub_item):
                        students[student_name]["A3"] = True
    
    generate_report(base_dir, students)

def generate_report(base_dir, students):
    total_students = len(students)
    count_a1 = sum(1 for s in students.values() if s["A1"])
    count_a2 = sum(1 for s in students.values() if s["A2"])
    count_a3 = sum(1 for s in students.values() if s["A3"])
    
    report_path = os.path.join(base_dir, "TRACKER.md")
    
    with open(report_path, "w") as f:
        f.write("# Student Assignment Tracker Report\n\n")
        f.write(f"**Total Students:** {total_students}\n\n")
        f.write("| Assignment | Submissions |\n")
        f.write("| --- | --- |\n")
        f.write(f"| Assignment 1 | {count_a1} |\n")
        f.write(f"| Assignment 2 | {count_a2} |\n")
        f.write(f"| Assignment 3 | {count_a3} |\n\n")
        
        f.write("## Detailed Submission List\n\n")
        f.write("| Student Name | A1 | A2 | A3 |\n")
        f.write("| --- | --- | --- | --- |\n")
        
        for student in sorted(students.keys()):
            a1 = "✅" if students[student]["A1"] else "❌"
            a2 = "✅" if students[student]["A2"] else "❌"
            a3 = "✅" if students[student]["A3"] else "❌"
            f.write(f"| {student} | {a1} | {a2} | {a3} |\n")
            
    print(f"Report generated successfully at {report_path}")
    print(f"Total Students: {total_students}")
    print(f"A1: {count_a1}, A2: {count_a2}, A3: {count_a3}")

if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    track_assignments(current_dir)
