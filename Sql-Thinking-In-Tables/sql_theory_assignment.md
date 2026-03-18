QUESTION 1-Explain why databases are important in real-world AI systems. Mention examples of the types of data typically stored in databases and why structured storage is necessary.
ANSWER- Databases are the backbone of real‑world AI systems because they store, organize, and serve the data that models train on and use in production. Without databases, AI would lack reliable, up‑to‑date, and structured information, making deployment at scale almost impossible.Databases routinely store many different kinds of data, but they are especially good at handling structured information, which is essential for reliable queries, efficient training, and consistent AI behavior. Structured storage means each piece of data has a fixed place in a schema (like rows and columns), so machines can quickly read, filter, join, and update it.


QUESTION 2-Describe the relational database mental model? Explain what tables, rows, and columns represent, and why each table   should represent a single entity.
ANSWER -  The relational database mental model is essentially: think in tables, rows, and columns, linked by keys. Instead of one big unstructured dump, you mentally break the world into cleanly separated “entities” (like users, orders, products) and model each as a table where rows are individual records and columns are attributes.
Table represents a single kind of thing or entity (for example, users, orders, or products).
Row (also called a record or tuple) represents one specific instance of that entity, such as one particular user or one specific order.
Column (also called an attribute or field) represents one property or aspect of the entity, such as name, email, price, or order_date.


QUESTION 3-Explain the concept of a primary key? Describe why primary keys must be unique and non-null, and how they help identify records in a table.
ANSWER -A primary key is a special column (or a small group of columns) that gives each row in a table its own unique ID.
No two rows can have the same primary‑key value, and it can never be empty.It helps you find one specific row quickly and lets other tables link to this row (using “foreign keys”) so everything stays connected and organized.
Why it must be unique ;
- If two rows had the same primary‑key value, the database could not tell them apart, so you might update or delete the wrong record.
- Uniqueness stops duplicate rows from sneaking in and keeps the data clean and trustworthy.
Why it must be non‑null ;
- If a key could be empty (null), some rows would have no ID at all, so you could never safely refer to them.
- Requiring a value in every row enforces that every record is identifiable, which is called entity integrity. 


QUESTION 4- Explain what a database schema is. Describe what information a schema defines and why schemas are important for maintaining consistent data structure.
ANSWER -A database schema is the blueprint or structure of a database: it defines how the data is organized, not the actual data itself. Think of it as a plan that says what tables exist, what columns they have, and how everything is connected.  It specifies which tables exist, their columns, data types, constraints (like primary keys, foreign keys, and uniqueness), and sometimes indexes and default values. Schemas are important because they enforce consistent shapes and rules for data, preventing invalid or incomplete records and making sure that applications, ETL jobs, and AI pipelines can all rely on the same data structure over time.They make sure everyone uses the same structure (same table and column names), so data stays organized. Rules in the schema prevent wrong or missing data, so the database stays clean and reliable. Because the schema is fixed, queries, apps, and AI systems can depend on stable tables and columns, making development easier and safer.


QUESTION 5- Explain how relationships between tables work in relational databases? Describe the role of foreign keys and how tables such as users and orders can be connected.
ANSWER - In relational databases, tables are connected through relationships, which let you link data from one table to another (for example, users to their orders). These relationships are usually built using keys, especially foreign keys, so the database knows how rows in different tables.
==== Role of foreign keys
A foreign key is a column in one table that holds the primary key value of another table. 
-It creates the link: the foreign key says “this row belongs to that row over there.”
-The database can also enforce a foreign‑key constraint, so you can’t insert an order that points to a user that doesn’t exist (no “orphaned” records).
   Example: users and orders tables
            users table:
                Columns: user_id (primary key), name, email.
            orders table:
                Columns: order_id, user_id (foreign key), total, order_date.
             Each order has a user_id that matches the user_id of one particular user.







