> # SQL query Security Filters
>
> ## Purpose
>
> This project provides a simple Python tool for analyzing login attempts and related security log data using SQLite and plain SQL files. It helps cybersecurity students, SOC analysts, and incident responders quickly filter and inspect activity such as:
>
> - Unauthorized or failed login attempts
> - Logins on specific dates or during certain hours
> - Activity by country, office, or department
>
> By combining Python and SQL, it enables rapid, scriptable, and repeatable filtering of log data — useful for building automation skills and incident investigation playbooks.
>
> ## What `main.py` Does
>
> 1.  Creates and populates a default SQLite database (`db/security.db`) from `schema.sql` if it does not already exist.
> 2.  Connects to the database (default or user-provided).
> 3.  Executes a SQL query file (default or user-provided) and prints the results to the console.
>
> ## How to Use
>
> ### Run with defaults
>
> python main.py
>
> - Database: `db/security.db` (created and populated from `schema.sql` on first run)
> - Query: `queries/login_by_date.sql`
>
> ## Run with a custom database
>
> python main.py path/to/custom.db
>
> If `path/to/custom.db` does not exist, `main.py` will create it and initialize it with `schema.sql`.
>
> ## Run with a custom query
>
> python main.py queries/your_query.sql
>
> This uses the default database (`db/security.db`) and runs the specified SQL file.
>
> ## Run with both custom database and custom query
>
> python main.py path/to/custom.db queries/your_query.sql
>
> `main.py` detects arguments by file extension:
>
> - `*.db` is treated as the database path.
> - `*.sql` is treated as the query file.
>
> If only one argument is provided, it may be either a `.db` or a `.sql` file.
>
> ## Project Structure
>
> .
> ├── db/
> │ └── security.db # Default SQLite database (auto-created on firstrun)
> ├── queries/
> │ ├── login_by_date.sql # Example/default query
> │ └── ... # Add your own .sql files here
> ├── schema.sql # Schema and seed data (used to initialize DB)
> └── main.py # Entry point: creates DB (if missing) and runs a query
>
> ## Why This Matters for Security Professionals
>
> Security teams frequently need to:
>
> - Identify brute-force or unauthorized login attempts
> - Trace activity by user, time, or source location
> - Audit historical login patterns
> - Triage alerts without relying solely on a SIEM
>
> This project teaches practical log filtering with SQL for scenarios where:
>
> - You are analyzing exported logs during incident response
> - You need quick, reproducible queries
> - You want lightweight tooling that does not depend on large platforms
>
> ## Example Output
>
> [+] Using existing database at 'db/security.db'
> [+] Running query from 'queries/login_by_date.sql'
> (1, '2022-05-08', '19:30', 0, 'USA')
> (2, '2022-05-08', '21:00', 1, 'MEXICO')
> (3, '2022-05-09', '20:15', 0, 'CANADA')
>
> Note: Output format depends on the SQL you run.
>
> ## Requirements
>
> - Python 3.6+
> - No external packages required (uses the standard library `sqlite3`)
>
> ## Tips
>
> - Write new queries as separate `.sql` files in `queries/`.
> - Edit `schema.sql` to simulate additional scenarios or tables.
> - If a query returns no results, verify that:
>
> - The database contains the expected data.
> - The date/time formats in your query match the stored values.
>
> - To reset the default database during development, delete `db/security.db` and run `python main.py` again to recreate it from `schema.sql`.
>
> ## Contributing
>
> Contributions are welcome. Feel free to submit pull requests for new queries, improved documentation, or additional features.
>
> If you want, I can also add a “Troubleshooting” section (e.g., common errors, Windows path tips) or a few example queries to include under `queries/`.
