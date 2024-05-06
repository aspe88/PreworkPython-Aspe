CREATE TABLE Clientes(
	id SERIAL PRIMARY KEY,
	name VARCHAR(200) NOT null,
	email VARCHAR(200) NOT null
)

INSERT INTO public.clientes(name, email)
VALUES ('Juan', 'juan@example.com')

UPDATE public.clientes
SET email ='juan@gmail.com'
Where id = 1

DELETE FROM public.clientes
WHERE id = 1;

CREATE TABLE Pedidos(
	id SERIAL PRIMARY KEY,
	cliente_id INT NOT null,
	CONSTRAINT FK_cliente_id FOREIGN KEY (cliente_id) REFERENCES clientes(id),
	producto VARCHAR(200) NOT null,
	cantidad INT NOT null
)

INSERT INTO public.pedidos(cliente_id, producto, cantidad)
VALUES (1, 'camiseta', 2)

UPDATE public.pedidos
SET cantidad = 3
Where id = 3

DELETE FROM public.pedidos
WHERE id = 3;

CREATE TABLE Productos(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(200) NOT null,
	precio DECIMAL NOT null
)

INSERT INTO public.productos(nombre, precio)
VALUES ('gorra', 18.49)

SELECT * FROM public.clientes

SELECT *FROM public.pedidos p
INNER JOIN public.clientes c
ON c.id = p.cliente_id

SELECT *FROM public.productos p
Where precio > 50

SELECT * FROM public.pedidos p
Where cantidad >= 5

SELECT * FROM public.clientes c
Where name LIKE 'A%'

SELECT * FROM public.clientes c
left JOIN public.pedidos p
ON c.id = p.cliente_id

SELECT * FROM public.productos c
INNer join public.pedidos p
on c.nombre = p.producto

ALTER TABLE public.pedidos
add column fecha date;

ALTER table public.pedidos
	add column producto_id INT

SELECT * FROM public.clientes
INNer join public.pedidos
on public.clientes.name = public.pedidos.producto