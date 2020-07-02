CREATE TABLE "address_address" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "cep" varchar(8) NOT NULL, "street" text NOT NULL,
  "number" varchar(10) NOT NULL,
  "neighborhood" text NOT NULL,
  "city" text NOT NULL,
  "uf" varchar(2) NOT NULL,
  "description" text NOT NULL,
  "complement" text NOT NULL
);
COMMIT;
