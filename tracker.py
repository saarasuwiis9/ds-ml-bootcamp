import os
import re

def track_assignments(base_dir):
    submissions_dir = os.path.join(base_dir, "submissions")
    if not os.path.exists(submissions_dir):
        print(f"Error: Submissions directory not found at {submissions_dir}")
        return

    students = {}
    
    # regex patterns for assignments (handles typos and common naming conventions)
    a1_pattern = re.compile(r"assig[n]*ment[-_ ]*1|a1", re.IGNORECASE)
    a2_pattern = re.compile(r"assig[n]*ment[-_ ]*2|a2", re.IGNORECASE)
    a3_pattern = re.compile(r"assig[n]*ment[-_ ]*3|a3", re.IGNORECASE)

    # Walk through the submissions directory
    for item in os.listdir(submissions_dir):
        item_path = os.path.join(submissions_dir, item)
        
        if os.path.isdir(item_path):
            # It's likely a student folder
            student_name = item
            if student_name == "000.example" or student_name == ".git":
                continue
                
            students[student_name] = {"A1": False, "A2": False, "A3": False}
            
            # Check for assignment folders or files inside student folder
            for sub_item in os.listdir(item_path):
                if a1_pattern.search(sub_item):
                    students[student_name]["A1"] = True
                elif a2_pattern.search(sub_item):
                    students[student_name]["A2"] = True
                elif a3_pattern.search(sub_item):
                    students[student_name]["A3"] = True
        elif os.path.isfile(item_path):
            # Check if an assignment file is directly in submissions (e.g. "Assignment 1.md")
            # We skip READMEs and system files
            if item.lower().startswith("readme") or item.startswith("."):
                continue
                
            # If it's a file like "Assignment 1.md", we try to extract a name or just count it?
            # Actually, the user asked for student tracker.
            pass
    
    # Generate the report
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
        
        # Sort students alphabetically
        for student in sorted(students.keys()):
            a1 = "✅" if students[student]["A1"] else "❌"
            a2 = "✅" if students[student]["A2"] else "❌"
            a3 = "✅" if students[student]["A3"] else "❌"
            f.write(f"| {student} | {a1} | {a2} | {a3} |\n")
            
    print(f"Report generated successfully at {report_path}")

if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    track_assignments(current_dir)
