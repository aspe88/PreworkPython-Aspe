CREATE TABLE Usuarios(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(200) NOT null,
	edad INT NOT null
)

INSERT INTO public.usuarios(nombre, edad)
VALUES ('Juan', 25)

INSERT INTO public.usuarios(nombre, edad)
VALUES ('Vic', 30)

UPDATE public.usuarios
SET edad = 22
Where id = 1

DELETE FROM public.usuarios
WHERE id = 1;

CREATE TABLE Ciudades(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(200) NOT null,
	pais VARCHAR(200) NOT null
)

INSERT INTO public.ciudades(nombre, pais)
VALUES ('Vigo', 'Spain')

INSERT INTO public.ciudades(nombre, pais)
VALUES ('Roma', 'Italy')

INSERT INTO public.ciudades(nombre, pais)
VALUES ('Paris', 'France')

ALTER table public.usuarios
	add column ciudades_id INT


Alter table public.usuarios
	add CONSTRAINT FK_ciudades_id FOREIGN KEY (ciudades_id) REFERENCES ciudades(id)


SELECT * FROM public.usuarios u
left JOIN public.ciudades c
ON u.ciudades_id = c.id

SELECT * FROM public.usuarios u
inner JOIN public.ciudades c
ON u.ciudades_id = c.id