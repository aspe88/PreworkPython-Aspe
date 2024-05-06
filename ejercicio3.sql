CREATE TABLE Productos(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(200) NOT null,
	precio DECIMAL NOT null
)

INSERT INTO public.productos(nombre, precio)
VALUES ('gorra', 18.49)

INSERT INTO public.productos(nombre, precio)
VALUES ('camiseta', 8.49)

INSERT INTO public.productos(nombre, precio)
VALUES ('pantalon', 28.49)

INSERT INTO public.productos(nombre, precio)
VALUES ('chaqueta', 48.49)

INSERT INTO public.productos(nombre, precio)
VALUES ('calcetines', 1.49)

INSERT INTO public.productos(nombre, precio)
VALUES ('albornoz', 11.49)

UPDATE public.productos
SET precio = 15
Where id = 1

DELETE FROM public.productos
WHERE id = 5;

No se puede relacionar productos con usuarios sin una Foreign key. no tiene sentido relacionar productos con clientes de forma directa.