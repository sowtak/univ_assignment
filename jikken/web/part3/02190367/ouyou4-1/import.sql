CREATE TABLE accounts(
        name text PRIMARY KEY,
        password text);

CREATE TABLE messages(
        id integer PRIMARY KEY,
        date text, 
        name text,
        message text);

.separator ,

.import accounts.csv accounts