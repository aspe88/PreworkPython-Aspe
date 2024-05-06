CREATE TABLE Pedidos(
	id SERIAL PRIMARY KEY,
	id_usuario INT NOT null,
	CONSTRAINT FK_id_usuario FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
	id_producto INT NOT null,
	CONSTRAINT FK_id_producto FOREIGN KEY (id_producto) REFERENCES productos(id)	
)

INSERT INTO public.usuarios (nombre, edad, ciudades_id)
VALUES ('Juan', 20, 1)

INSERT INTO public.pedidos(id_usuario, id_producto)
VALUES (2,1)

INSERT INTO public.pedidos(id_usuario, id_producto)
VALUES (2,2)

INSERT INTO public.pedidos(id_usuario, id_producto)
VALUES (2,4)

SELECT * FROM public.usuarios u
left JOIN public.pedidos p
ON u.id = p.id_usuario
left JOIN public.productos x
ON x.id = p.id_producto

SELECT * FROM public.usuarios u
left JOIN public.pedidos p
ON u.id = p.id_usuario

ALTER table public.pedidos
	add column cantidad INT

UPDATE public.pedidos
SET cantidad = 2
Where id = 1

UPDATE public.pedidos
SET cantidad = 4
Where id = 2

UPDATE public.pedidos
SET cantidad = 6
Where id = 3