

## SQLite basics
| Command | Meaning |
|---|---|
| `sqlite3 shop.db` | Open (or create) the database |
| `.tables` | Show all tables |
| `.quit` | Leave SQLite |
| `;` | Ends every SQL command |

If you see `...>`, the command isn't finished yet (missing `;` or `)`). Press **Ctrl + C** to cancel.

## The commands

**CREATE TABLE** makes a new table (sheet):
```sql
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
```
`PRIMARY KEY` is a unique ID per row. `INTEGER` is a whole number, `TEXT` is text, `REAL` is a decimal number.

**INSERT** adds a row:
```sql
INSERT INTO customers (name, city) VALUES ('Anna', 'Berlin');
```

**SELECT** reads data:
```sql
SELECT * FROM orders;
SELECT * FROM orders WHERE price > 100;
```
`*` means all columns. `WHERE` filters rows.

**UPDATE** changes a row:
```sql
UPDATE customers SET city = 'Berlin' WHERE id = 1;
```

**DELETE** removes a row:
```sql
DELETE FROM orders WHERE product = 'Mouse';
```

**Important:** `UPDATE` and `DELETE` without `WHERE` change or delete **all rows**.

## JOIN: combine two tables
```sql
SELECT customers.name, orders.product, orders.price
FROM customers
JOIN orders ON customers.id = orders.customer_id;
```
`ON` says how the tables are linked: the `customer_id` in orders points to the `id` in customers (that's the **foreign key** idea).

**LEFT JOIN** keeps all rows from the left table, even without a match:
```sql
SELECT customers.name
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
WHERE orders.id IS NULL;
```
This finds customers **without** orders (Mia).

## INDEX: faster searching
```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);
```
Like the index of a book. It makes no difference with 3 rows, but a big one with millions.

## Key ideas
- **Primary key:** unique ID of a row
- **Foreign key:** an ID that points to a row in another table
- **Orphan:** an order whose customer was deleted (foreign keys help prevent this)
- **Normalization:** store each piece of info only once (customer data in one table, not repeated in every order)