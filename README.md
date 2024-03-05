# more_sql_types

# SECTION 1

## Description

In this exercise, we will practice the definition and basic usage of advanced data types.

##

## Tasks

###

### Task 1

Create a table named `site_user` with the following fields:

- **id**: a `PRIMARY KEY` of type `serial`.
- **name**: a `varchar` of length 100.

Now add these fields and decide what is the best type to use on each case:

- **uuid**: It will store a universal identifier to allow us to identify this resource uniquely across tables and applications.
- **avatar**: It will store a small image representing the user.
- **role**: It will store the role of the user. Possible roles are: *Anonymous, Guest, User, Moderator* and *Admin*. The permissions of these roles are unknown but we know they are incremental: Anonymous < Guest < User < ...
- **birthdate**: It will store the date the user was born.
- **siblings**: It will store the names of the user siblings. We don't know how many children a user may have.
- **availability**: It will store the time windows available for contact during the day. Each window is comprised of two values indicating the starting and ending time of each window. There may be an indefinite number of windows during the day, but we will not make distinction between days of the week.
- **site_settings**: It will store a variety of configuration options of our web site. These options are still unknown and they may be changing in nature, but we know they will consist of a series of keys and values.
- **created_on**: It will store the date and time the user profile was created.
- **active_for**: It will store the number of days the user has been registered for.

> Compare with the solution before advancing to the next task.

###

### Task 2

Create the following users:

| name          | Miriam Valira                         | Johann Müller                         | Louise Clark                         |
|---------------|---------------------------------------|--------------------------------------|--------------------------------------|
| uuid          | e41e1291-33b8-4316-8a86-28a618d5c338  | d81331bf-a4f6-4ecd-8883-51dee509309e | e6168ec9-7306-44a5-9875-2c659e15740e |
| role          | Admin                                 | User                                 | Moderator                            |
| birthdate     | Aug. 29th, 1995                       | May 9th, 2002                        | May 3th, 1992                        |
| siblings      | Dani & Louis                          |                                      | Monique                              |
| availabilty   | From 12 to 15h                        | From 9 to 14 and from 18 to 20h      | From 9 to 12 and from 13 to 17h      |
| site_settings | Background = red, notifications = off | notifications=on                     | notifications=on                     |
| created_on    | Sep. 23rd, 2015 at 08:56 am           | May 01, 2017 at 13:03                | Mar 21, 2007 at 10:31                |

The fields `avatar` and `active_for` will be ignored for now.

- By doing a basic `SELECT` you should see the following table:

| id | name          | uuid                                 | role      | birthdate  | siblings     | availability                              | site_settings                                 | created_on        |
|----|---------------|--------------------------------------|-----------|------------|--------------|-------------------------------------------|-----------------------------------------------|-------------------|
| 1  | Miriam Valira | e41e1291-33b8-4316-8a86-28a618d5c338 | Admin     | 1995-08-29 | {Dani,Louis} | {{12:00:00,15:00:00}}                     | {"background": "red", "notifications": false} | 09/23/15 08:56 AM |
| 2  | Johann Müller  | d81331bf-a4f6-4ecd-8883-51dee509309e | User      | 2002-05-09 |              | {{09:00:00,14:00:00},{18:00:00,20:00:00}} | {"notifications": true}                       | 05/01/17 01:03 PM |
| 3  | Louise Clark  | e6168ec9-7306-44a5-9875-2c659e15740e | Moderator | 1992-05-03 | {Monique}    | {{09:00:00,12:00:00},{13:00:00,17:00:00}} | {"notifications": true}                       | 03/21/07 10:31 AM |

# Task 3

Now update the `active_for` field by calculating the interval between the `CURRENT_TIMESTAMP` and the `created_on` value for each user.

- Then, execute `SELECT name, active_for FROM site_user;` and you should see something similar to the following result:

| name          | active_for |
|---------------|------------|
| Miriam Valira | 2150 days  |
| Johann Müller | 1564 days  |
| Louise Clark  | 5258 days  |

# Task 4

Complete the following list of SQL queries:

1. Find those born before 2000. Answer: Miriam & Louise.
2. Find those with siblings. Answer: Miriam & Louise.
3. Find those who have notifications set to true. Answer: Johann & Louise.
4. Find those with more than one availability time window. Answer: Johann & Louise.


# SECTION II

## Description

In this exercise, we will practice extensively with the more complex and versatile types.

## Data

This exercise uses data from the previous section (SECTION I). You can use your own data from that exercise or you can create a new database and load the [initial content](src/data/initial.sql).

The initial content for this exercise includes:

- Table **site_user**
  - Field **id**: `integer`, `PRIMARY KEY`
  - Field **name**: `varchar(25)`
  - Field **uuid**: `uuid`
  - Field **avatar**: `bytea`
  - Field **role**: `role_type` AS `ENUM`
  - Field **birthdate**: `date`
  - Field **siblings**: `text[]`
  - Field **availability**: `time[][]`
  - Field **site_settings**: `json`
  - Field **created_on**: `timestamp`
  - Field **active_for**: `interval`

##

## Tasks

###

### Task 1

Produce a list of users who have more than one child.

Your query should return only one user: Miriam.

### Task 2

Good news! Luoise Clark just gave birth to Jordi, so you've been tasked with adding him to her siblings field.

Then, execute again the statement of the previous task to confirm it works and now returns Miriam and Louise.

### Task 3

Louise will be on a temporary leave, but between 9 and 10 in the morning she can check emails and be contacted at home if something urgent arises, so you've been tasked with setting her availability accordingly.

> You may replace the availability array with a new one.

### Task 4

Louise's site notifications should be turned off as well.

> You may **not** replace the site_settings field this time.

### Task 5

Also, the system is left without moderator for a while, so it has been decided to promote someone to the role moderator.

First, write an SQL statement to find everyone who has a role below moderator, so that it can be decided who to promote.

You will find out there is only one, Johann, so your task now will be to promote him to moderator.

### Task 6

Produce a list showing which users have their notifications turned off.

The answer should be: Miriam & Louise.

### Task 7

Produce a list showing which users don't have any custom background color for the site.

The answer should be: Louise and Johann.
