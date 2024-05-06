CREATE TABLE Clientes(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(200) NOT null
)

INSERT INTO public.clientes(nombre)
VALUES ('John')

UPDATE public.clientes
SET nombre ='John Doe'
Where id = 1

DELETE FROM public.clientes
WHERE id = 1;

SELECT * FROM public.clientes

CREATE TABLE pedidos(
	id SERIAL PRIMARY KEY,
	cliente_id INT NOT null
)

INSERT INTO public.pedidos(cliente_id)
VALUES (1)

UPDATE public.pedidos
SET cliente_id = 2
Where id = 1

DELETE FROM public.pedidos
WHERE id = 1;

SELECT * FROM public.pedidos

CREATE TABLE Productos(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(200) NOT null
)

INSERT INTO public.productos(nombre)
VALUES ('camisa')

UPDATE public.productos
SET nombre = 'Pantalón'
Where id = 1

DELETE FROM public.productos
WHERE id = 1;

SELECT * FROM public.productos

CREATE TABLE detallespedido(
	id SERIAL PRIMARY KEY,
	producto_id INT NOT null
)

INSERT INTO public.detallespedido(producto_id)
VALUES (1)

UPDATE public.detallespedido
SET producto_id = 2
Where id = 1

DELETE FROM public.detallespedido
WHERE id = 1;

SELECT * FROM public.detallespedido

SELECT *FROM public.clientes c
INNER JOIN public.pedidos p
ON c.id = p.cliente_id

SELECT *FROM public.clientes c
LEFT JOIN public.pedidos p
ON c.id = p.cliente_id

SELECT *FROM public.productos c
INNER JOIN public.detallespedido p
ON c.id = p.producto_id

SELECT *FROM public.productos c
LEFT JOIN public.detallespedido p
ON c.id = p.producto_id

ALTER TABLE public.clientes
add column telefono VARCHAR(15);

ALTER TABLE public.clientes
ALTER COLUMN telefono TYPE INT

ALTER table public.clientes
Drop column telefono;

alter table public.clientes rename to usuarios

ALTER table public.usuarios
	rename column nombre to nombre_completo

ALTER table public.usuarios
  add primary key (id);