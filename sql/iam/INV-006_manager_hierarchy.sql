/*
============================================================
Investigation 08
Manager Hierarchy Report

Business Question:
How many direct reports does each manager have?

Purpose:
Identify team sizes by manager.

Concepts Demonstrated:
- Self Join
- COUNT()
- GROUP BY
- LEFT JOIN
- ORDER BY

Expected Result:
A list of managers, their departments, and the number of employees who report to them.
============================================================
*/

SELECT
    m.first_name AS manager_first_name,
    m.last_name AS manager_last_name,
    m.department AS manager_department,
    COUNT(u.user_id) AS direct_reports
FROM users u
LEFT JOIN users m
    ON u.manager_id = m.user_id
WHERE m.user_id IS NOT NULL
GROUP BY
    m.user_id,
    m.first_name,
    m.last_name,
    m.department
ORDER BY
    direct_reports DESC,
    m.last_name;