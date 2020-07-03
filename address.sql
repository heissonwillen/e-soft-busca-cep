-- CREATE TABLE "address_address" (
--   "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
--   "cep" varchar(9) NOT NULL,
--   "street" text NOT NULL,
--   "number" varchar(10) NOT NULL,
--   "neighborhood" text NOT NULL,
--   "city" text NOT NULL,
--   "uf" varchar(2) NOT NULL,
--   "description" text NOT NULL,
--   "complement" text NOT NULL
-- );
-- COMMIT;

CREATE TABLE "address_address" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cep" varchar(9) NOT NULL, "street" varchar(100) NOT NULL, "number" varchar(10) NOT NULL, "neighborhood" varchar(100) NOT NULL, "city" varchar(100) NOT NULL, "uf" varchar(100) NOT NULL, "description" text NOT NULL, "complement" varchar(100) NOT NULL);
COMMIT;
