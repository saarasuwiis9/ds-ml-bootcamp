import os
import re

def track_assignments(base_dir):
    submissions_dir = os.path.join(base_dir, "submissions")
    if not os.path.exists(submissions_dir):
        print(f"Error: Submissions directory not found at {submissions_dir}")
        return

    students = {}
    
    # Stricter regex patterns: 
    # - Assignment/Assigment/Asigment followed by 1, 2, or 3
    # - Standalone folder/file named "A1", "A2", "A3"
    # - "Research" or "Project" followed by assignment number
    a1_regex = re.compile(r"^(assig[n]*m[er]*nt|asig[n]*ment|a1|research|lesson[-_ ]*one)[-_ ]*(1|one|one\.md)?$", re.IGNORECASE)
    a2_regex = re.compile(r"^(assig[n]*m[er]*nt|asig[n]*ment|a2|project|lesson[-_ ]*two)[-_ ]*(2|two)?$", re.IGNORECASE)
    a3_regex = re.compile(r"^(assig[n]*m[er]*nt|asig[n]*ment|a3|lesson[-_ ]*three)[-_ ]*(3|three)?$", re.IGNORECASE)

    # Secondary patterns for nested files (must be more specific to avoid false positives like data1.csv)
    sub_a1_regex = re.compile(r"(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(1|one)", re.IGNORECASE)
    sub_a2_regex = re.compile(r"(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(2|two)", re.IGNORECASE)
    sub_a3_regex = re.compile(r"(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(3|three)", re.IGNORECASE)

    exclude_folders = {"000.example", ".git", "assignment-1", "assignment-2", "assignment-3"}

    for item in os.listdir(submissions_dir):
        item_path = os.path.join(submissions_dir, item)
        
        if os.path.isdir(item_path):
            student_name = item
            if student_name.lower() in exclude_folders:
                continue
                
            students[student_name] = {
                "A1": {"status": False, "evidence": ""}, 
                "A2": {"status": False, "evidence": ""}, 
                "A3": {"status": False, "evidence": ""}
            }
            
            # Recursive check (up to 3 levels deep)
            for root, dirs, files in os.walk(item_path):
                depth = root[len(item_path):].count(os.sep)
                if depth > 2:
                    continue
                
                # Check directory names first (higher priority evidence)
                for d in dirs:
                    if a1_regex.match(d) or sub_a1_regex.search(d):
                        if not students[student_name]["A1"]["status"]:
                            students[student_name]["A1"] = {"status": True, "evidence": d}
                    if a2_regex.match(d) or sub_a2_regex.search(d):
                        if not students[student_name]["A2"]["status"]:
                            students[student_name]["A2"] = {"status": True, "evidence": d}
                    if a3_regex.match(d) or sub_a3_regex.search(d):
                        if not students[student_name]["A3"]["status"]:
                            students[student_name]["A3"] = {"status": True, "evidence": d}
                
                # Check filenames
                for f in files:
                    # Skip README if it's the only match or if we have better evidence
                    cleanup_name = f.lower()
                    if "readme" in cleanup_name or cleanup_name.startswith("."):
                        continue
                        
                    if sub_a1_regex.search(f):
                        if not students[student_name]["A1"]["status"]:
                            students[student_name]["A1"] = {"status": True, "evidence": f}
                    if sub_a2_regex.search(f):
                        if not students[student_name]["A2"]["status"]:
                            students[student_name]["A2"] = {"status": True, "evidence": f}
                    if sub_a3_regex.search(f):
                        if not students[student_name]["A3"]["status"]:
                            students[student_name]["A3"] = {"status": True, "evidence": f}
    
    generate_report(base_dir, students)

def generate_report(base_dir, students):
    # Filter out students who have NO assignments detected (noise folders)
    valid_students = {k: v for k, v in students.items() if any(a["status"] for a in v.values())}
    
    total_students = len(valid_students)
    count_a1 = sum(1 for s in valid_students.values() if s["A1"]["status"])
    count_a2 = sum(1 for s in valid_students.values() if s["A2"]["status"])
    count_a3 = sum(1 for s in valid_students.values() if s["A3"]["status"])
    
    report_path = os.path.join(base_dir, "TRACKER.md")
    
    with open(report_path, "w") as f:
        f.write("# Student Assignment Tracker Report (Evidence-Based)\n\n")
        f.write(f"**Total Valid Students (with at least 1 submission):** {total_students}\n\n")
        f.write("| Assignment | Submissions |\n")
        f.write("| --- | --- |\n")
        f.write(f"| Assignment 1 | {count_a1} |\n")
        f.write(f"| Assignment 2 | {count_a2} |\n")
        f.write(f"| Assignment 3 | {count_a3} |\n\n")
        
        f.write("## Detailed Submission List with Evidence\n\n")
        f.write("| Student Name | A1 Submission | A2 Submission | A3 Submission |\n")
        f.write("| --- | --- | --- | --- |\n")
        
        for student in sorted(valid_students.keys()):
            a1 = f"✅ ({valid_students[student]['A1']['evidence']})" if valid_students[student]["A1"]["status"] else "❌"
            a2 = f"✅ ({valid_students[student]['A2']['evidence']})" if valid_students[student]["A2"]["status"] else "❌"
            a3 = f"✅ ({valid_students[student]['A3']['evidence']})" if valid_students[student]["A3"]["status"] else "❌"
            f.write(f"| {student} | {a1} | {a2} | {a3} |\n")
            
    print(f"Report generated successfully at {report_path}")
    print(f"Total Students: {total_students}")
    print(f"A1: {count_a1}, A2: {count_a2}, A3: {count_a3}")

if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    track_assignments(current_dir)
