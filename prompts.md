You have access to my workspace and to the existing database access code in this project.

Do the following using the existing database connection and models already defined here:

1. Use the existing ORM / data access layer to connect to the database. Do NOT create a new connection or new config.

2. Query the Courses table (or equivalent model in this project) and find ONE course that has no description (NULL, empty string, or missing). Do NOT fetch all courses. If no such course exists, tell me that and stop.

3. If you find a course with no description:
   - Open and read the file `course_description_template.txt` from the repository.
   - Use that template to create a description for this specific course, filling in any placeholders using the course’s existing fields (e.g. name, subject, level).
   - Update ONLY this one course in the database with the generated description, using the existing ORM / data access patterns.

4. After you’ve done this, show me exactly what you changed (queries or code you executed) and confirm which course was updated.
