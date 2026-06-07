import sqlite3
import pandas as pd

# Create database connection
conn = sqlite3.connect("database/iam_soc_analytics.db")

# Import CSV files
users = pd.read_csv("data/users.csv")
groups = pd.read_csv("data/groups.csv")
user_groups = pd.read_csv("data/user_groups.csv")
login_events = pd.read_csv("data/login_events.csv")
helpdesk_tickets = pd.read_csv("data/helpdesk_tickets.csv")
security_incidents = pd.read_csv("data/security_incidents.csv")

# Create tables
users.to_sql("users", conn, if_exists="replace", index=False)
groups.to_sql("groups", conn, if_exists="replace", index=False)
user_groups.to_sql("user_groups", conn, if_exists="replace", index=False)
login_events.to_sql("login_events", conn, if_exists="replace", index=False)
helpdesk_tickets.to_sql("helpdesk_tickets", conn, if_exists="replace", index=False)
security_incidents.to_sql("security_incidents", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()