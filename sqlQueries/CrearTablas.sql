CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(255) NOT NULL
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    overview TEXT,
    descripcion TEXT,
    datos_adicionales TEXT,
    categorias INTEGER REFERENCES categorias(id),
    link_imagen1 VARCHAR(255),
    link_imagen2 VARCHAR(255),
    link_imagen3 VARCHAR(255),
    precio_antes_descuento DECIMAL(10, 2),
    precio_despues_descuento DECIMAL(10, 2),
    stock_disponible INTEGER
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    address TEXT,
    addInfo TEXT,  -- Información adicional
    phone_number VARCHAR(20)
);

CREATE TABLE ordenes (
    id SERIAL PRIMARY KEY,
    email_usuario VARCHAR(255) REFERENCES usuarios(email),
    codigo_trackeo VARCHAR(100),
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    producto INTEGER REFERENCES productos(id),
    nombre VARCHAR(255),
    cantidad INTEGER
);
