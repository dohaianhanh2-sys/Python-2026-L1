import gzip
import os
import pickle
import threading
from input import get_courses, get_marks, get_students
from output import display_results

# If using the Extra tasks
try:
    from extra import export_csv, query_data
except ImportError:
    pass


def _save_data_worker(students, courses):
    """Worker function executed in the background thread to pickle and compress data."""
    print("\n[Background Thread] Starting serialization and compression...")
    data = {"students": students, "courses": courses}
    with gzip.open("students.dat", "wb") as f:
        pickle.dump(data, f)
    print("\n[Background Thread] Data saved to students.dat successfully!")


def save_pickled_data_background(students, courses):
    """Instantiate and start a background thread to handle data persistence."""
    save_thread = threading.Thread(
        target=_save_data_worker,
        args=(students, courses),
        name="SaveDataThread"
    )
    save_thread.start()
    return save_thread


def load_pickled_data():
    """Decompress and unpack the saved objects from students.dat."""
    with gzip.open("students.dat", "rb") as f:
        data = pickle.load(f)
    return data["students"], data["courses"]


def main():
    if os.path.exists("students.dat"):
        print("Found existing students.dat. Decompressing and loading data...")
        students, courses = load_pickled_data()
    else:
        print("No existing data found. Please enter fresh data.")
        students = get_students()
        courses = get_courses()
        get_marks(students, courses)

    for s in students:
        s.calculate_gpa(courses)

    students.sort(key=lambda x: x.gpa, reverse=True)

    # Display results using the curses interface
    display_results(students, courses)

    # PW8 Requirement: Trigger persistence in a background thread
    save_thread = save_pickled_data_background(students, courses)

    # --- EXTRA SECTION (CSV & PANDAS QUERY) ---
    run_extra = input("\nDo you want to run Extra task (CSV & Query)? (y/n): ")
    if run_extra.strip().lower() == "y":
        try:
            export_csv(students, courses)
            query_data()
        except Exception as e:
            print(f"Extra task error: {e}")

    # Ensure the background thread finishes writing to disk before exiting the main process
    if save_thread.is_alive():
        print("Waiting for background saving process to complete...")
        save_thread.join()

    print("Program exited.")


if __name__ == "__main__":
    main()