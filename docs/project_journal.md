# IAM-SOC-Analytics-Lab Project Journal

## Project Goal

Build a portfolio project that combines:

* Identity and Access Management (IAM)
* Security Operations Center (SOC) Analytics
* Data Analytics and Reporting

The project simulates an enterprise environment where users, groups, login events, help desk tickets, and security incidents can be analyzed using SQL, Python, SQLite, and Power BI.

---

# Phase 1 - Environment Setup

## Step 1 - Repository Creation

Created GitHub repository:

IAM-SOC-Analytics-Lab

Repository initialized with:

* README.md
* MIT License
* Python .gitignore

### Purpose

Establish version control and project documentation.

### Concepts Learned

* GitHub Repository Management
* Version Control
* Open Source Licensing
* Project Documentation

---

## Step 2 - Development Environment

Installed:

* Git
* Python
* DBeaver
* Visual Studio Code

### VS Code Extensions

* Python
* GitHub Copilot
* GitLens
* SQLite Viewer
* SQLTools
* PowerShell

### Purpose

Create a professional development environment for cybersecurity, IAM, and data analytics projects.

### Concepts Learned

* Development Environment Setup
* Dependency Management
* IDE Configuration
* Database Management Tools

---

## Step 3 - Project Structure

Created folders:

* data
* database
* sql
* dashboards
* reports
* docs
* scripts

### Purpose

Organize datasets, SQL queries, reports, scripts, and documentation.

### Folder Functions

| Folder     | Purpose                           |
| ---------- | --------------------------------- |
| data       | CSV datasets                      |
| database   | SQLite database files             |
| sql        | SQL queries                       |
| dashboards | Power BI screenshots              |
| reports    | Security findings and analysis    |
| docs       | Documentation and project journal |
| scripts    | Python automation                 |

### Concepts Learned

* Project Organization
* Documentation Standards
* Enterprise Project Structure

---

# Phase 2 - Dataset Creation

## Step 4 - Users Dataset

Created:

data/users.csv

### Fields

* user_id
* first_name
* last_name
* department
* job_title
* status
* hire_date

### Concepts Learned

* User Identity
* User Lifecycle Management
* Active vs Inactive Accounts
* Department Ownership
* Primary Keys

### IAM Relevance

Used to simulate:

* User Provisioning
* Access Reviews
* Account Lifecycle Management

### Cybersecurity Relevance

Used to identify:

* Inactive Accounts
* Privileged Users
* Security Risks

### Data Analytics Relevance

Used for:

* Workforce Reporting
* Department Metrics
* User Analysis

---

## Step 5 - Groups Dataset

Created:

data/groups.csv

### Fields

* group_id
* group_name
* group_type
* privilege_level

### Concepts Learned

* Security Groups
* Role-Based Access Control (RBAC)
* Least Privilege
* Privileged Access

### IAM Relevance

Used to assign permissions through groups instead of directly to users.

---

## Step 6 - User Group Mapping

Created:

data/user_groups.csv

### Fields

* user_id
* group_id

### Concepts Learned

* Many-to-Many Relationships
* Group Membership
* Access Assignment
* Identity Governance

### IAM Relevance

Maps users to groups and simulates Active Directory group membership.

---

## Step 7 - Security Monitoring Datasets

Created:

* data/login_events.csv
* data/helpdesk_tickets.csv
* data/security_incidents.csv

### Purpose

Provide security and operational data for investigation and analysis.

### Concepts Learned

* Authentication Monitoring
* Security Incident Tracking
* Help Desk Correlation
* Event Analysis

---

# Phase 3 - Database Creation

## Step 8 - SQLite Database Creation

Created:

database/create_database.py

Generated:

database/iam_soc_analytics.db

### Process

CSV Files
→ Pandas DataFrames
→ SQLite Database Tables

### Tables Created

* users
* groups
* user_groups
* login_events
* helpdesk_tickets
* security_incidents

### Concepts Learned

* ETL (Extract, Transform, Load)
* Pandas DataFrames
* SQLite Databases
* Data Import Automation

### Cybersecurity Relevance

Centralized security and identity data for analysis.

### Data Analytics Relevance

Prepared structured datasets for SQL reporting and dashboard development.

---

# Phase 4 - SQL Analytics Investigations

## Investigation 00 - Workforce Distribution Analysis

### Objective

Determine workforce distribution across departments.

### Query

SELECT department,
COUNT(*) AS total_users
FROM users
GROUP BY department
ORDER BY total_users DESC;

### Results

| Department | Total Users |
| ---------- | ----------- |
| IT         | 3           |
| Sales      | 2           |
| HR         | 2           |
| Finance    | 2           |
| Operations | 1           |

### Analysis

The IT department contains the highest number of users in the environment.

### Business Use Case

Department staffing analysis and workforce reporting.

### IAM Use Case

Determine the number of identities managed within each department.

### Cybersecurity Use Case

Understand user distribution when evaluating access management and risk exposure.

### Concepts Demonstrated

* SELECT
* COUNT()
* GROUP BY
* ORDER BY

---

## Investigation 01 - Group Membership Review

### Objective

Identify user-to-group relationships and understand privilege assignments within the environment.

### Query

SELECT
u.first_name,
u.last_name,
g.group_name,
g.privilege_level
FROM users u
JOIN user_groups ug
ON u.user_id = ug.user_id
JOIN groups g
ON ug.group_id = g.group_id
ORDER BY g.privilege_level DESC;

### Results

Users were mapped to their assigned groups and privilege levels.

Examples:

* Chris Giggleman → Helpdesk_Team → Medium
* Chris Giggleman → Security_Analysts → High
* Angela Brown → IT_Admins → High
* Angela Brown → Security_Analysts → High

### Analysis

Several users belong to multiple groups. Group membership determines privilege assignment through Role-Based Access Control (RBAC).

### Risk Assessment

Users assigned to multiple privileged groups should be reviewed to ensure access aligns with business requirements.

### Recommendation

Perform periodic group membership reviews and validate access assignments.

### IAM Concepts Demonstrated

* Role-Based Access Control (RBAC)
* Group-Based Access Control
* Identity Governance
* Access Reviews

---

## Investigation 02 - High Privilege Access Review

### Objective

Identify users assigned to High-Privilege security groups.

### Query

SELECT
u.first_name,
u.last_name,
u.department,
g.group_name,
g.privilege_level
FROM users u
JOIN user_groups ug
ON u.user_id = ug.user_id
JOIN groups g
ON ug.group_id = g.group_id
WHERE g.privilege_level = 'High'
ORDER BY u.last_name;

### Results

| First Name | Last Name | Department | Group Name        | Privilege Level |
| ---------- | --------- | ---------- | ----------------- | --------------- |
| Angela     | Brown     | IT         | IT_Admins         | High            |
| Angela     | Brown     | IT         | Security_Analysts | High            |
| Emily      | Davis     | Finance    | Finance_Admins    | High            |
| Chris      | Giggleman | IT         | Security_Analysts | High            |
| Daniel     | Moore     | IT         | Security_Analysts | High            |

### Analysis

Four users possess High-Privilege access within the environment.

Angela Brown is assigned to two separate High-Privilege groups.

### Risk Assessment

Multiple privileged group memberships may indicate privilege creep and increase the attack surface if an account becomes compromised.

### Recommendation

Perform periodic access reviews and validate business justification for privileged access assignments.

### IAM Concepts Demonstrated

* Role-Based Access Control (RBAC)
* Least Privilege
* Access Reviews
* Privileged Access Management

### Security Finding

Finding ID: IAM-001

Issue:
Angela Brown is assigned to multiple High-Privilege groups.

Risk:
Potential privilege creep.

Recommendation:
Review access assignments and validate business requirements.

Status:
Open
