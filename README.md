# News Database Logs Analysis

### Database code for analyzing log data using queries.
This program displays the plain text results for queries regarding:
most popular articles, authors ranked by popularity, and date(s) on which more than 1% of requests returned an error.

This program utilizes:
* Python DB-API
* PostgreSQL

The `logs_analysis.py` file contains the code to perform the queries. The `newsdata.sql` file has the database information. The `Vagrantfile` has the data needed for Vagrant to run properly.

#### Documentation
1. Install [Git Bash](https://git-scm.com/downloads).
2. Install the appropriate platform package of [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2).
3. Install the [Vagrant](https://www.vagrantup.com/downloads.html) software.
4. Run `pip3 install psycopg2-binary --user` in Git Bash.
5. Start the virtual machine by running `vagrant up` in Git Bash.
6. Log in to the virtual machine by running `vagrant ssh` in Git Bash.
7. Fork the GitHub [repository](https://github.com/mejeter/logs-analysis.git).
8. Change to desired directory in Git Bash and type `git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.
9. After you have `cd` into the directory, run `psql -d news -f newsdata.sql` in the terminal to load the data into the database.
10. Type `psql -d news` to connect to the database.
11. Run the following create view commands in the terminal:
    ```PostgreSQL
    create view errors_by_day as
    select to_char(time, 'Mon DD, YYYY') as date, count(*) as errors
    from log
    group by status, date
    having status = '404 NOT FOUND'
    ```

    ```PostgreSQL
    create view requests_by_day as
    select to_char(time, 'Mon DD, YYYY') as date, count(*) as requests
    from log
    group by date
    ```
11. Type `\q` in the terminal to close psql or open another terminal window.
12. Run `python logs_analysis.py` in the terminal.


#### Acknowledgements
The news database was provided by Udacity. The functionality for the server code came from the forum.py code provided by Udacity.
