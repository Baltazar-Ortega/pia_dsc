CREATE TABLE "Productos" (
    "Producto" varchar(6) NOT NULL UNIQUE PRIMARY KEY,
    "Descripcion" varchar(20) NOT NULL,
    "CostoUnitario" integer NOT NULL CHECK ("CostoUnitario" between 1 and 99)
);

-- insert valido
INSERT INTO "Productos"("Producto", "Descripcion", "CostoUnitario") VALUES 
('P00001', 'Pluma azul', 15),
 ('P00002', 'Tornillo', 5),
 ('P00003', 'Vaso de vidrio', 35);

CREATE TABLE "Tablas" (
    "ClaveTabla" varchar(3) NOT NULL CHECK ("ClaveTabla" IN ('T04', 'T05', 'F01')),
    "LlaveTabla" varchar(19),
    "Informacion" varchar(58) NOT NULL,
    PRIMARY KEY("ClaveTabla", "LlaveTabla")
);

-- Inserts validos
INSERT INTO "Tablas"("ClaveTabla", "LlaveTabla", "Informacion") VALUES 
    ('T04', 'PT1', 'Queretaro'),
  ('T04', 'PT2', 'Monterrey'),
  ('T05', 'PT1DPT001', 'Articulos generales'),
  ('T05', 'PT1DPT002', 'Articulos de construcción'),
  ('T05', 'PT2DPT001', 'Articulos escolares'),
  ('F01', '', '20201201') ;