CREATE TABLE likes(
    id SERIAL,
    user_id INTEGER,
    supplier_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers (id),
    UNIQUE(user_id, supplier_id),
    PRIMARY KEY(id)
);