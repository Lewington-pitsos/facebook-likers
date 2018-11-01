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

CREATE TABLE fake_users (
    id SERIAL,
    profile_pic_path VARCHAR(100),
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    birth_day INTEGER NOT NULL,
    birth_month CHAR(3) NOT NULL,
    birth_year INTEGER NOT NULL,
    pass VARCHAR(20) NOT NULL,
    temp_mail VARCHAR(30) NOT NULL,
    PRIMARY KEY (id),
);

INSERT INTO links_encountered (link_type, outer_html, good, bad)
        VALUES('nav', 'window', 0, 1)
        ON CONFLICT (link_type, outer_html) DO UPDATE SET good = links_encountered.good + 1, bad = links_encountered.bad + 0
        RETURNING id;