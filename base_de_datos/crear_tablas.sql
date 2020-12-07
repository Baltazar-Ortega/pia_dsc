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

-- CASO 3

CREATE TABLE "ProductosCaso3" (
    "Producto" varchar(6) NOT NULL UNIQUE PRIMARY KEY,
    "Descripcion" varchar(20) NOT NULL,
    "CostoUnitario" integer NOT NULL CHECK ("CostoUnitario" between 1 and 99)
);

DELETE FROM "ProductosCaso3" WHERE "Producto" = 'P00073';

-- insert valido
INSERT INTO "ProductosCaso3"("Producto", "Descripcion", "CostoUnitario") VALUES 
('P00001', 'Pluma 1', 15),
 ('P00002', 'Pluma 2', 5),
 ('P00003', 'Pluma 3', 35),
('P00004', 'Pluma 1', 15),
 ('P00005', 'Pluma 2', 5),
 ('P00006', 'Pluma 3', 35),
 ('P00007', 'Pluma 1', 15),
 ('P00008', 'Pluma 2', 5),
 ('P00009', 'Pluma 3', 35),
 ('P00010', 'Pluma 1', 15),
 ('P00011', 'Pluma 2', 5),
 ('P00012', 'Pluma 3', 35),
 ('P00013', 'Pluma 1', 15),
 ('P00014', 'Pluma 2', 5),
 ('P00015', 'Pluma 3', 35),
 ('P00016', 'Pluma 1', 15),
 ('P00017', 'Pluma 2', 5),
 ('P00018', 'Pluma 3', 35),
 ('P00019', 'Pluma 1', 15),
 ('P00020', 'Pluma 2', 5),
 ('P00021', 'Pluma 3', 35),
 ('P00022', 'Pluma 1', 15),
 ('P00023', 'Pluma 2', 5),
 ('P00024', 'Pluma 3', 35),
 ('P00025', 'Pluma 1', 15),
 ('P00026', 'Pluma 2', 5),
 ('P00027', 'Pluma 3', 35),
 ('P00028', 'Pluma 1', 15),
 ('P00029', 'Pluma 2', 5),
 ('P00030', 'Pluma 3', 35),
 ('P00031', 'Pluma 1', 15),
 ('P00032', 'Pluma 2', 5),
 ('P00033', 'Pluma 3', 35),
 ('P00034', 'Pluma 1', 15),
 ('P00035', 'Pluma 2', 5),
 ('P00036', 'Pluma 3', 35),
 ('P00037', 'Pluma 1', 15),
 ('P00038', 'Pluma 2', 5),
 ('P00039', 'Pluma 3', 35),
 ('P00040', 'Pluma 1', 15),
 ('P00041', 'Pluma 2', 5),
 ('P00042', 'Pluma 3', 35),
 ('P00043', 'Pluma 1', 15),
 ('P00044', 'Pluma 2', 5),
 ('P00045', 'Pluma 3', 35),
 ('P00046', 'Pluma 1', 15),
 ('P00047', 'Pluma 2', 5),
 ('P00048', 'Pluma 3', 35),
 ('P00049', 'Pluma 1', 15),
 ('P00050', 'Pluma 2', 5),
 ('P00051', 'Pluma 3', 35),
 ('P00052', 'Pluma 1', 15),
 ('P00053', 'Pluma 2', 5),
 ('P00054', 'Pluma 3', 35),
 ('P00055', 'Pluma 1', 15),
 ('P00056', 'Pluma 2', 5),
 ('P00057', 'Pluma 3', 35),
 ('P00058', 'Pluma 1', 15),
 ('P00059', 'Pluma 2', 5),
 ('P00060', 'Pluma 3', 35),
 ('P00061', 'Pluma 1', 15),
 ('P00062', 'Pluma 2', 5),
 ('P00063', 'Pluma 3', 35),
 ('P00064', 'Pluma 1', 15),
 ('P00065', 'Pluma 2', 5),
 ('P00066', 'Pluma 3', 35),
 ('P00067', 'Pluma 1', 15),
 ('P00068', 'Pluma 2', 5),
 ('P00069', 'Pluma 3', 35),
 ('P00070', 'Pluma 1', 15),
 ('P00071', 'Pluma 2', 5),
 ('P00072', 'Pluma 3', 35)
;



