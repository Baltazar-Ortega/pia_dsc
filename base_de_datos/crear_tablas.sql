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


DELETE FROM "Productos" WHERE "Producto" = 'P00073';

-- insert valido
INSERT INTO "Productos"("Producto", "Descripcion", "CostoUnitario") VALUES 
('P00001', 'Foco 1', 15),
 ('P00002', 'Foco 2', 5),
 ('P00003', 'Foco 3', 35),
('P00004', 'Foco 4', 15),
 ('P00005', 'Foco 5', 5),
 ('P00006', 'Foco 6', 35),
 ('P00007', 'Foco 7', 15),
 ('P00008', 'Foco 8', 5),
 ('P00009', 'Foco 9', 35),
 ('P00010', 'Foco 10', 15),
 ('P00011', 'Foco 11', 5),
 ('P00012', 'Foco 12', 35),
 ('P00013', 'Foco 13', 15),
 ('P00014', 'Foco 14', 5),
 ('P00015', 'Foco 15', 35),
 ('P00016', 'Foco 16', 15),
 ('P00017', 'Foco 17', 5),
 ('P00018', 'Foco 18', 35),
 ('P00019', 'Foco 19', 15),
 ('P00020', 'Foco 20', 5),
 ('P00021', 'Foco 21', 35),
 ('P00022', 'Foco 22', 15),
 ('P00023', 'Foco 23', 5),
 ('P00024', 'Foco 24', 35),
 ('P00025', 'Foco 25', 15),
 ('P00026', 'Foco 26', 5),
 ('P00027', 'Foco 27', 35),
 ('P00028', 'Foco 28', 15),
 ('P00029', 'Foco 29', 5),
 ('P00030', 'Foco 30', 35),
 ('P00031', 'Foco 31', 15),
 ('P00032', 'Foco 32', 5),
 ('P00033', 'Foco 33', 35),
 ('P00034', 'Foco 34', 15),
 ('P00035', 'Foco 35', 5),
 ('P00036', 'Foco 36', 35),
 ('P00037', 'Foco 37', 15),
 ('P00038', 'Foco 38', 5),
 ('P00039', 'Foco 39', 35),
 ('P00040', 'Foco 40', 15),
 ('P00041', 'Foco 41', 5),
 ('P00042', 'Foco 42', 35),
 ('P00043', 'Foco 43', 15),
 ('P00044', 'Foco 44', 5),
 ('P00045', 'Foco 45', 35),
 ('P00046', 'Foco 46', 15),
 ('P00047', 'Foco 47', 5),
 ('P00048', 'Foco 48', 35),
 ('P00049', 'Foco 49', 15),
 ('P00050', 'Foco 50', 5),
 ('P00051', 'Foco 51', 35),
 ('P00052', 'Foco 52', 15),
 ('P00053', 'Foco 53', 5),
 ('P00054', 'Foco 54', 35),
 ('P00055', 'Foco 55', 15),
 ('P00056', 'Foco 56', 5),
 ('P00057', 'Foco 57', 35),
 ('P00058', 'Foco 58', 15),
 ('P00059', 'Foco 59', 5),
 ('P00060', 'Foco 60', 35),
 ('P00061', 'Foco 61', 15),
 ('P00062', 'Foco 62', 5),
 ('P00063', 'Foco 63', 35),
 ('P00064', 'Foco 64', 15),
 ('P00065', 'Foco 65', 5),
 ('P00066', 'Foco 66', 35),
 ('P00067', 'Foco 67', 15),
 ('P00068', 'Foco 68', 5),
 ('P00069', 'Foco 69', 35),
 ('P00070', 'Foco 70', 15),
 ('P00071', 'Foco 71', 5),
 ('P00072', 'Foco 72', 35),
 ('P00073', 'Foco 73', 5),
 ('P00074', 'Foco 74', 35),
 ('P00075', 'Foco 75', 15),
 ('P00076', 'Foco 76', 5),
 ('P00077', 'Foco 77', 35),
 ('P00078', 'Foco 78', 35),
 ('P00079', 'Foco 79', 35)
;


--  ('P00072', 'Foco 72', 35),
('P00073', 'Foco 73', 5),
 ('P00074', 'Foco 74', 35),
 ('P00075', 'Foco 75', 15),
 ('P00076', 'Foco 76', 5),
 ('P00077', 'Foco 77', 35),
 ('P00078', 'Foco 78', 35),
 ('P00079', 'Foco 79', 35)
