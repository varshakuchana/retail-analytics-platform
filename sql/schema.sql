CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    title VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100),
    price NUMERIC(10,2),
    rating NUMERIC(3,2),
    stock INT
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    segment VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount NUMERIC(10,2),
    order_status VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    unit_price NUMERIC(10,2),
    total_price NUMERIC(10,2)
);
