#!/usr/bin/env python

import psycopg2
import psycopg2.extras
import functools
import operator


def popular_articles():
    """Print the three most popular articles of all time from the database."""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select articles.title, count(*) as num
        from log join articles
        on right(log.path, -9) = articles.slug
        group by title, status
        having status = '200 OK'
        order by num desc
        limit 3;
        """)
    results = c.fetchall()
    c.close()
    db.close()

    string = functools.reduce(operator.add, (results))
    answer = '\n'.join([str(s) for s in string])
    return answer


def popular_authors():
    """Print the most popular authors from the database, most popular first."""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select authors.name, count(*) as num
        from log inner join articles
        on right(log.path, -9) = articles.slug
        inner join authors
        on authors.id = articles.author
        group by name
        order by num desc;
        """)
    results = c.fetchall()
    c.close()
    db.close()

    string = functools.reduce(operator.add, (results))
    answer = '\n'.join([str(s) for s in string])
    return answer


def errors_requests_per_day():
    """Print date(s) that more than 1% of requests lead to errors."""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select date, percent from
        (select requests_by_day.date,
        round(errors * 100.00 / requests, 2) as percent
        from requests_by_day, errors_by_day
        where requests_by_day.date = errors_by_day.date
        and requests > errors)
        as percentage
        where percent > 1.00;
        """)
    results = c.fetchall()
    c.close()
    db.close()

    string = functools.reduce(operator.add, (results))
    answer = '\n'.join([str(s) for s in string])
    return answer


if __name__ == "__main__":
    print "What are the most popular three articles of all time?"
    print popular_articles()
    print "\n"
    print "Who are the most popular article authors of all time?"
    print popular_authors()
    print "\n"
    print "On which days did more than 1% of requests lead to errors?"
    print errors_requests_per_day()
