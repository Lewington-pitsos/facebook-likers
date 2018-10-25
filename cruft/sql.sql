CREATE TABLE likes(
    id SERIAL,
    user_id INTEGER,
    supplier_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers (id),
    UNIQUE(user_id, supplier_id),
    PRIMARY KEY(id)
);

CREATE TABLE links_encountered (
    id Serial,
    link_type VARCHAR(10),
    outer_html VARCHAR(500),
    bad INTEGER,
    good INTEGER,
    UNIQUE(link_type, outer_html),
    PRIMARY KEY(id)
);


INSERT INTO links_encountered (link_type, outer_html, good, bad)
        VALUES('nav', 'window', 0, 1)
        ON CONFLICT (link_type, outer_html) DO UPDATE SET good = links_encountered.good + 1, bad = links_encountered.bad + 0
        RETURNING id;