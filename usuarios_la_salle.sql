-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-12-2022 a las 08:05:45
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `usuarios_la_salle`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `data_users`
--

CREATE TABLE `data_users` (
  `nombres` varchar(40) NOT NULL COMMENT 'Los nombres de cada usuario, separados por espacios.',
  `apellidos` varchar(40) DEFAULT NULL COMMENT 'Los apellidos de los usuarios, separados por espacios.',
  `dni` int(10) DEFAULT NULL COMMENT 'El DNI de los usuarios, no debe de tener espacios ni caracteres especiales, simplemente datos de tipo INT.',
  `cargo` varchar(30) DEFAULT NULL COMMENT 'El tipo de cargo de cada usuario, por ejemplo, estudiante, profesor, director, etc.',
  `fecha_nacimiento` date NOT NULL DEFAULT '2000-01-01',
  `asistencias` int(6) NOT NULL DEFAULT 0,
  `inasistencias` int(6) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `data_users`
--

INSERT INTO `data_users` (`nombres`, `apellidos`, `dni`, `cargo`, `fecha_nacimiento`, `asistencias`, `inasistencias`) VALUES
('Giovanny Andree', 'Jimenez Deza', 00000000, 'Estudiante', '2006-01-01', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_asistencia`
--

CREATE TABLE `registro_asistencia` (
  `dni` int(8) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT curdate(),
  `hora_registro` time NOT NULL DEFAULT curtime()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registro_asistencia`
--

INSERT INTO `registro_asistencia` (`dni`, `fecha_registro`, `hora_registro`) VALUES
(00000000, '2022-12-08', '12:58:57'),
(123456, '2022-12-08', '12:59:07'),
(00000000, '2022-12-09', '14:42:47'),
(123456, '2022-12-09', '17:13:45'),
(00000000, '2022-12-10', '10:49:06'),
(123456, '2022-12-10', '10:59:23'),
(00000000, '2022-12-12', '11:45:30'),
(123456, '2022-12-12', '11:46:23'),
(00000000, '2022-12-20', '17:35:23'),
(00000000, '2022-12-27', '16:42:03');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `data_users`
--
ALTER TABLE `data_users`
  ADD PRIMARY KEY (`nombres`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
