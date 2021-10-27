/*
 Navicat Premium Data Transfer

 Source Server         : Localhost
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : localhost:3306
 Source Schema         : asistencia

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : 65001

 Date: 21/09/2019 19:14:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cb_operaciones_bitacora
-- ----------------------------
DROP TABLE IF EXISTS `cb_operaciones_bitacora`;
CREATE TABLE `cb_operaciones_bitacora`  (
  `cb_bitacora_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cb_bitacora_fkusuario` int(11) NULL DEFAULT NULL,
  `cb_bitacora_ip` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cb_bitacora_accion` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cb_bitacora_fecha` datetime(0) NOT NULL,
  `cb_bitacora_tabla` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cb_bitacora_identificador` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`cb_bitacora_id`) USING BTREE,
  INDEX `cb_bitacora_fkusuario`(`cb_bitacora_fkusuario`) USING BTREE,
  CONSTRAINT `cb_operaciones_bitacora_ibfk_1` FOREIGN KEY (`cb_bitacora_fkusuario`) REFERENCES `cb_usuarios_usuario` (`cb_usuario_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cb_operaciones_bitacora
-- ----------------------------
INSERT INTO `cb_operaciones_bitacora` VALUES (1, 1, '127.0.0.1', 'Registro Centro_costo.', '2019-09-21 18:22:31', 'rrhh_gerencia', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (2, 1, '127.0.0.1', 'Registro Empresa.', '2019-09-21 18:22:39', 'rrhh_empresa', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (3, 1, '127.0.0.1', 'Registro Gerencia.', '2019-09-21 18:22:47', 'rrhh_gerencia', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (4, 1, '127.0.0.1', 'Registro Cargo.', '2019-09-21 18:22:59', 'rrhh_gerencia', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (5, 1, '127.0.0.1', 'Registro Pais.', '2019-09-21 18:23:13', 'rrhh_pais', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (6, 1, '127.0.0.1', 'Registro Departamento.', '2019-09-21 18:23:27', 'rrhh_departamento', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (7, 1, '127.0.0.1', 'Registro Ciudad.', '2019-09-21 18:23:43', 'rrhh_ciudad', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (8, 1, '127.0.0.1', 'Registro Sucursal.', '2019-09-21 18:23:54', 'rrhh_sucursal', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (9, 1, '127.0.0.1', 'Registro Oficina.', '2019-09-21 18:24:05', 'rrhh_gerencia', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (10, 1, '127.0.0.1', 'Registro Persona.', '2019-09-21 18:24:32', 'rrhh_persona', 1);
INSERT INTO `cb_operaciones_bitacora` VALUES (11, 1, '127.0.0.1', 'Registro Gerencia.', '2019-09-21 19:04:39', 'rrhh_gerencia', 2);
INSERT INTO `cb_operaciones_bitacora` VALUES (12, 1, '127.0.0.1', 'Registro Gerencia.', '2019-09-21 19:04:47', 'rrhh_gerencia', 3);
INSERT INTO `cb_operaciones_bitacora` VALUES (13, 1, '127.0.0.1', 'Registro Cargo.', '2019-09-21 19:05:02', 'rrhh_gerencia', 2);
INSERT INTO `cb_operaciones_bitacora` VALUES (14, 1, '127.0.0.1', 'Registro Departamento.', '2019-09-21 19:05:17', 'rrhh_departamento', 2);
INSERT INTO `cb_operaciones_bitacora` VALUES (15, 1, '127.0.0.1', 'Registro Departamento.', '2019-09-21 19:05:31', 'rrhh_departamento', 3);
INSERT INTO `cb_operaciones_bitacora` VALUES (16, 1, '127.0.0.1', 'Registro Ciudad.', '2019-09-21 19:05:48', 'rrhh_ciudad', 2);
INSERT INTO `cb_operaciones_bitacora` VALUES (17, 1, '127.0.0.1', 'Registro Ciudad.', '2019-09-21 19:06:00', 'rrhh_ciudad', 3);
INSERT INTO `cb_operaciones_bitacora` VALUES (18, 1, '127.0.0.1', 'Registro Ciudad.', '2019-09-21 19:06:09', 'rrhh_ciudad', 4);
INSERT INTO `cb_operaciones_bitacora` VALUES (19, 1, '127.0.0.1', 'Registro Sucursal.', '2019-09-21 19:06:24', 'rrhh_sucursal', 2);
INSERT INTO `cb_operaciones_bitacora` VALUES (20, 1, '127.0.0.1', 'Registro Sucursal.', '2019-09-21 19:06:35', 'rrhh_sucursal', 3);
INSERT INTO `cb_operaciones_bitacora` VALUES (21, 1, '127.0.0.1', 'Registro Oficina.', '2019-09-21 19:06:52', 'rrhh_gerencia', 2);
INSERT INTO `cb_operaciones_bitacora` VALUES (22, 1, '127.0.0.1', 'Registro Oficina.', '2019-09-21 19:07:06', 'rrhh_gerencia', 3);
INSERT INTO `cb_operaciones_bitacora` VALUES (23, 1, '127.0.0.1', 'Registro Persona.', '2019-09-21 19:13:46', 'rrhh_persona', 2);

-- ----------------------------
-- Table structure for cb_usuarios_acceso
-- ----------------------------
DROP TABLE IF EXISTS `cb_usuarios_acceso`;
CREATE TABLE `cb_usuarios_acceso`  (
  `cb_acceso_id` int(11) NOT NULL AUTO_INCREMENT,
  `cb_acceso_fkrol` int(11) NULL DEFAULT NULL,
  `cb_acceso_fkmodulo` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`cb_acceso_id`) USING BTREE,
  INDEX `cb_acceso_fkrol`(`cb_acceso_fkrol`) USING BTREE,
  INDEX `cb_acceso_fkmodulo`(`cb_acceso_fkmodulo`) USING BTREE,
  CONSTRAINT `cb_usuarios_acceso_ibfk_1` FOREIGN KEY (`cb_acceso_fkrol`) REFERENCES `cb_usuarios_rol` (`cb_rol_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cb_usuarios_acceso_ibfk_2` FOREIGN KEY (`cb_acceso_fkmodulo`) REFERENCES `cb_usuarios_modulo` (`cb_modulo_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 85 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cb_usuarios_acceso
-- ----------------------------
INSERT INTO `cb_usuarios_acceso` VALUES (1, 1, 1);
INSERT INTO `cb_usuarios_acceso` VALUES (2, 1, 2);
INSERT INTO `cb_usuarios_acceso` VALUES (3, 1, 3);
INSERT INTO `cb_usuarios_acceso` VALUES (4, 1, 4);
INSERT INTO `cb_usuarios_acceso` VALUES (5, 1, 5);
INSERT INTO `cb_usuarios_acceso` VALUES (6, 1, 6);
INSERT INTO `cb_usuarios_acceso` VALUES (7, 1, 7);
INSERT INTO `cb_usuarios_acceso` VALUES (8, 1, 8);
INSERT INTO `cb_usuarios_acceso` VALUES (9, 1, 9);
INSERT INTO `cb_usuarios_acceso` VALUES (10, 1, 10);
INSERT INTO `cb_usuarios_acceso` VALUES (11, 1, 11);
INSERT INTO `cb_usuarios_acceso` VALUES (12, 1, 12);
INSERT INTO `cb_usuarios_acceso` VALUES (13, 1, 13);
INSERT INTO `cb_usuarios_acceso` VALUES (14, 1, 14);
INSERT INTO `cb_usuarios_acceso` VALUES (15, 1, 15);
INSERT INTO `cb_usuarios_acceso` VALUES (16, 1, 16);
INSERT INTO `cb_usuarios_acceso` VALUES (17, 1, 17);
INSERT INTO `cb_usuarios_acceso` VALUES (18, 1, 18);
INSERT INTO `cb_usuarios_acceso` VALUES (19, 1, 19);
INSERT INTO `cb_usuarios_acceso` VALUES (20, 1, 20);
INSERT INTO `cb_usuarios_acceso` VALUES (21, 1, 21);
INSERT INTO `cb_usuarios_acceso` VALUES (22, 1, 22);
INSERT INTO `cb_usuarios_acceso` VALUES (23, 1, 23);
INSERT INTO `cb_usuarios_acceso` VALUES (24, 1, 24);
INSERT INTO `cb_usuarios_acceso` VALUES (25, 1, 25);
INSERT INTO `cb_usuarios_acceso` VALUES (26, 1, 26);
INSERT INTO `cb_usuarios_acceso` VALUES (27, 1, 27);
INSERT INTO `cb_usuarios_acceso` VALUES (28, 1, 28);
INSERT INTO `cb_usuarios_acceso` VALUES (29, 1, 29);
INSERT INTO `cb_usuarios_acceso` VALUES (30, 1, 30);
INSERT INTO `cb_usuarios_acceso` VALUES (31, 1, 31);
INSERT INTO `cb_usuarios_acceso` VALUES (32, 1, 32);
INSERT INTO `cb_usuarios_acceso` VALUES (33, 1, 33);
INSERT INTO `cb_usuarios_acceso` VALUES (34, 1, 34);
INSERT INTO `cb_usuarios_acceso` VALUES (35, 1, 55);
INSERT INTO `cb_usuarios_acceso` VALUES (36, 1, 56);
INSERT INTO `cb_usuarios_acceso` VALUES (37, 1, 57);
INSERT INTO `cb_usuarios_acceso` VALUES (38, 1, 58);
INSERT INTO `cb_usuarios_acceso` VALUES (39, 1, 59);
INSERT INTO `cb_usuarios_acceso` VALUES (40, 1, 35);
INSERT INTO `cb_usuarios_acceso` VALUES (41, 1, 36);
INSERT INTO `cb_usuarios_acceso` VALUES (42, 1, 37);
INSERT INTO `cb_usuarios_acceso` VALUES (43, 1, 38);
INSERT INTO `cb_usuarios_acceso` VALUES (44, 1, 39);
INSERT INTO `cb_usuarios_acceso` VALUES (45, 1, 40);
INSERT INTO `cb_usuarios_acceso` VALUES (46, 1, 41);
INSERT INTO `cb_usuarios_acceso` VALUES (47, 1, 42);
INSERT INTO `cb_usuarios_acceso` VALUES (48, 1, 43);
INSERT INTO `cb_usuarios_acceso` VALUES (49, 1, 44);
INSERT INTO `cb_usuarios_acceso` VALUES (50, 1, 45);
INSERT INTO `cb_usuarios_acceso` VALUES (51, 1, 46);
INSERT INTO `cb_usuarios_acceso` VALUES (52, 1, 47);
INSERT INTO `cb_usuarios_acceso` VALUES (53, 1, 48);
INSERT INTO `cb_usuarios_acceso` VALUES (54, 1, 49);
INSERT INTO `cb_usuarios_acceso` VALUES (55, 1, 50);
INSERT INTO `cb_usuarios_acceso` VALUES (56, 1, 51);
INSERT INTO `cb_usuarios_acceso` VALUES (57, 1, 52);
INSERT INTO `cb_usuarios_acceso` VALUES (58, 1, 53);
INSERT INTO `cb_usuarios_acceso` VALUES (59, 1, 54);
INSERT INTO `cb_usuarios_acceso` VALUES (60, 1, 60);
INSERT INTO `cb_usuarios_acceso` VALUES (61, 1, 61);
INSERT INTO `cb_usuarios_acceso` VALUES (62, 1, 62);
INSERT INTO `cb_usuarios_acceso` VALUES (63, 1, 63);
INSERT INTO `cb_usuarios_acceso` VALUES (64, 1, 64);
INSERT INTO `cb_usuarios_acceso` VALUES (65, 1, 65);
INSERT INTO `cb_usuarios_acceso` VALUES (66, 1, 66);
INSERT INTO `cb_usuarios_acceso` VALUES (67, 1, 67);
INSERT INTO `cb_usuarios_acceso` VALUES (68, 1, 68);
INSERT INTO `cb_usuarios_acceso` VALUES (69, 1, 69);
INSERT INTO `cb_usuarios_acceso` VALUES (70, 1, 70);
INSERT INTO `cb_usuarios_acceso` VALUES (71, 1, 71);
INSERT INTO `cb_usuarios_acceso` VALUES (72, 1, 72);
INSERT INTO `cb_usuarios_acceso` VALUES (73, 1, 73);
INSERT INTO `cb_usuarios_acceso` VALUES (74, 1, 74);
INSERT INTO `cb_usuarios_acceso` VALUES (75, 1, 75);
INSERT INTO `cb_usuarios_acceso` VALUES (76, 1, 76);
INSERT INTO `cb_usuarios_acceso` VALUES (77, 1, 77);
INSERT INTO `cb_usuarios_acceso` VALUES (78, 1, 78);
INSERT INTO `cb_usuarios_acceso` VALUES (79, 1, 79);
INSERT INTO `cb_usuarios_acceso` VALUES (80, 1, 80);
INSERT INTO `cb_usuarios_acceso` VALUES (81, 1, 81);
INSERT INTO `cb_usuarios_acceso` VALUES (82, 1, 82);
INSERT INTO `cb_usuarios_acceso` VALUES (83, 1, 83);
INSERT INTO `cb_usuarios_acceso` VALUES (84, 1, 84);

-- ----------------------------
-- Table structure for cb_usuarios_modulo
-- ----------------------------
DROP TABLE IF EXISTS `cb_usuarios_modulo`;
CREATE TABLE `cb_usuarios_modulo`  (
  `cb_modulo_id` int(11) NOT NULL AUTO_INCREMENT,
  `cb_modulo_route` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cb_modulo_title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_modulo_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_modulo_icon` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_modulo_menu` tinyint(1) NOT NULL,
  `cb_modulo_fkmodulo` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`cb_modulo_id`) USING BTREE,
  UNIQUE INDEX `cb_modulo_name`(`cb_modulo_name`) USING BTREE,
  INDEX `cb_modulo_fkmodulo`(`cb_modulo_fkmodulo`) USING BTREE,
  CONSTRAINT `cb_usuarios_modulo_ibfk_1` FOREIGN KEY (`cb_modulo_fkmodulo`) REFERENCES `cb_usuarios_modulo` (`cb_modulo_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 85 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cb_usuarios_modulo
-- ----------------------------
INSERT INTO `cb_usuarios_modulo` VALUES (1, NULL, 'Usuarios', 'user_Modulo', 'person', 1, NULL);
INSERT INTO `cb_usuarios_modulo` VALUES (2, '/rol', 'Rol', 'roles', 'dashboard', 1, 1);
INSERT INTO `cb_usuarios_modulo` VALUES (3, '/usuario', 'Usuario', 'usuario', 'account_box', 1, 1);
INSERT INTO `cb_usuarios_modulo` VALUES (4, '/usuario_profile', 'Perfil Usuario', 'perfil', 'dvr', 1, 1);
INSERT INTO `cb_usuarios_modulo` VALUES (5, '/track', 'track', 'track', 'dvr', 1, 1);
INSERT INTO `cb_usuarios_modulo` VALUES (6, '', 'Consultar', 'usuario_query', 'home', 0, 3);
INSERT INTO `cb_usuarios_modulo` VALUES (7, '/usuario_insert', 'Adicionar', 'usuario_insert', 'home', 0, 3);
INSERT INTO `cb_usuarios_modulo` VALUES (8, '/usuario_update', 'Actualizar', 'usuario_update', 'home', 0, 3);
INSERT INTO `cb_usuarios_modulo` VALUES (9, '/usuario_delete', 'Dar de Baja', 'usuario_delete', 'home', 0, 3);
INSERT INTO `cb_usuarios_modulo` VALUES (10, '', 'Consultar', 'rol_query', 'home', 0, 2);
INSERT INTO `cb_usuarios_modulo` VALUES (11, '/rol_insert', 'Adicionar', 'rol_insert', 'home', 0, 2);
INSERT INTO `cb_usuarios_modulo` VALUES (12, '/rol_update', 'Actualizar', 'rol_update', 'home', 0, 2);
INSERT INTO `cb_usuarios_modulo` VALUES (13, '/rol_delete', 'Dar de Baja', 'rol_delete', 'home', 0, 2);
INSERT INTO `cb_usuarios_modulo` VALUES (14, '', 'Consultar', 'bitacora_query', 'home', 0, 5);
INSERT INTO `cb_usuarios_modulo` VALUES (15, NULL, 'Monitoreo de Registros', 'monitoreo', 'book', 1, NULL);
INSERT INTO `cb_usuarios_modulo` VALUES (16, '/registros', 'Marcaciones', 'registros', 'portrait', 1, 15);
INSERT INTO `cb_usuarios_modulo` VALUES (17, '', 'Consultar', 'registros_query', 'home', 0, 16);
INSERT INTO `cb_usuarios_modulo` VALUES (18, '/registros_imprimirpdf', 'Imprimir Pdf', 'registros_imprimirpdf', 'home', 0, 16);
INSERT INTO `cb_usuarios_modulo` VALUES (19, '/registros_imprimirxls', 'Imprimir Xls', 'registros_imprimirxls', 'home', 0, 16);
INSERT INTO `cb_usuarios_modulo` VALUES (20, '/registros_enviar', 'Enviar Registros', 'registros_enviar', 'home', 0, 16);
INSERT INTO `cb_usuarios_modulo` VALUES (21, '/registros_filtrar', 'Filtrar Registros', 'registros_filtrar', 'home', 0, 16);
INSERT INTO `cb_usuarios_modulo` VALUES (22, NULL, 'Personal', 'personal', 'book', 1, NULL);
INSERT INTO `cb_usuarios_modulo` VALUES (23, '/persona', 'personas', 'persona', 'portrait', 1, 22);
INSERT INTO `cb_usuarios_modulo` VALUES (24, '', 'Consultar', 'persona_query', 'home', 0, 23);
INSERT INTO `cb_usuarios_modulo` VALUES (25, '/persona_insert', 'Adicionar', 'persona_insert', 'home', 0, 23);
INSERT INTO `cb_usuarios_modulo` VALUES (26, '/persona_update', 'Actualizar', 'persona_update', 'home', 0, 23);
INSERT INTO `cb_usuarios_modulo` VALUES (27, '/persona_delete', 'Dar de Baja', 'persona_delete', 'home', 0, 23);
INSERT INTO `cb_usuarios_modulo` VALUES (28, '/persona_imprimir', 'Imprimir', 'persona_imprimir', 'home', 0, 23);
INSERT INTO `cb_usuarios_modulo` VALUES (29, NULL, 'Configuraciones', 'configuraciones', 'book', 1, NULL);
INSERT INTO `cb_usuarios_modulo` VALUES (30, '/centro_costo', 'centro_costos', 'centro_costo', 'portrait', 1, 29);
INSERT INTO `cb_usuarios_modulo` VALUES (31, '/empresa', 'Empresa', 'empresa', 'portrait', 1, 29);
INSERT INTO `cb_usuarios_modulo` VALUES (32, '/gerencia', 'Gerencias', 'gerencia', 'portrait', 1, 29);
INSERT INTO `cb_usuarios_modulo` VALUES (33, '/cargo', 'Cargos', 'cargo', 'portrait', 1, 29);
INSERT INTO `cb_usuarios_modulo` VALUES (34, NULL, 'Localizacion', 'localizacion', 'book', 1, 29);
INSERT INTO `cb_usuarios_modulo` VALUES (35, '', 'Consultar', 'centro_costo_query', 'home', 0, 30);
INSERT INTO `cb_usuarios_modulo` VALUES (36, '/centro_costo_insert', 'Adicionar', 'centro_costo_insert', 'home', 0, 30);
INSERT INTO `cb_usuarios_modulo` VALUES (37, '/centro_costo_update', 'Actualizar', 'centro_costo_update', 'home', 0, 30);
INSERT INTO `cb_usuarios_modulo` VALUES (38, '/centro_costo_delete', 'Dar de Baja', 'centro_costo_delete', 'home', 0, 30);
INSERT INTO `cb_usuarios_modulo` VALUES (39, '/centro_costo_imprimir', 'Imprimir', 'centro_costo_imprimir', 'home', 0, 30);
INSERT INTO `cb_usuarios_modulo` VALUES (40, '', 'Consultar', 'empresa_query', 'home', 0, 31);
INSERT INTO `cb_usuarios_modulo` VALUES (41, '/empresa_insert', 'Adicionar', 'empresa_insert', 'home', 0, 31);
INSERT INTO `cb_usuarios_modulo` VALUES (42, '/empresa_update', 'Actualizar', 'empresa_update', 'home', 0, 31);
INSERT INTO `cb_usuarios_modulo` VALUES (43, '/empresa_delete', 'Dar de Baja', 'empresa_delete', 'home', 0, 31);
INSERT INTO `cb_usuarios_modulo` VALUES (44, '/empresa_imprimir', 'Imprimir', 'empresa_imprimir', 'home', 0, 31);
INSERT INTO `cb_usuarios_modulo` VALUES (45, '', 'Consultar', 'gerencia_query', 'home', 0, 32);
INSERT INTO `cb_usuarios_modulo` VALUES (46, '/gerencia_insert', 'Adicionar', 'gerencia_insert', 'home', 0, 32);
INSERT INTO `cb_usuarios_modulo` VALUES (47, '/gerencia_update', 'Actualizar', 'gerencia_update', 'home', 0, 32);
INSERT INTO `cb_usuarios_modulo` VALUES (48, '/gerencia_delete', 'Dar de Baja', 'gerencia_delete', 'home', 0, 32);
INSERT INTO `cb_usuarios_modulo` VALUES (49, '/gerencia_imprimir', 'Imprimir', 'gerencia_imprimir', 'home', 0, 32);
INSERT INTO `cb_usuarios_modulo` VALUES (50, '', 'Consultar', 'cargo_query', 'home', 0, 33);
INSERT INTO `cb_usuarios_modulo` VALUES (51, '/cargo_insert', 'Adicionar', 'cargo_insert', 'home', 0, 33);
INSERT INTO `cb_usuarios_modulo` VALUES (52, '/cargo_update', 'Actualizar', 'cargo_update', 'home', 0, 33);
INSERT INTO `cb_usuarios_modulo` VALUES (53, '/cargo_delete', 'Dar de Baja', 'cargo_delete', 'home', 0, 33);
INSERT INTO `cb_usuarios_modulo` VALUES (54, '/cargo_imprimir', 'Imprimir', 'cargo_imprimir', 'home', 0, 33);
INSERT INTO `cb_usuarios_modulo` VALUES (55, '/pais', 'paiss', 'pais', 'portrait', 1, 34);
INSERT INTO `cb_usuarios_modulo` VALUES (56, '/departamento', 'departamentos', 'departamento', 'portrait', 1, 34);
INSERT INTO `cb_usuarios_modulo` VALUES (57, '/ciudad', 'ciudads', 'ciudad', 'portrait', 1, 34);
INSERT INTO `cb_usuarios_modulo` VALUES (58, '/sucursal', 'sucursals', 'sucursal', 'portrait', 1, 34);
INSERT INTO `cb_usuarios_modulo` VALUES (59, '/oficina', 'oficinas', 'oficina', 'portrait', 1, 34);
INSERT INTO `cb_usuarios_modulo` VALUES (60, '', 'Consultar', 'pais_query', 'home', 0, 55);
INSERT INTO `cb_usuarios_modulo` VALUES (61, '/pais_insert', 'Adicionar', 'pais_insert', 'home', 0, 55);
INSERT INTO `cb_usuarios_modulo` VALUES (62, '/pais_update', 'Actualizar', 'pais_update', 'home', 0, 55);
INSERT INTO `cb_usuarios_modulo` VALUES (63, '/pais_delete', 'Dar de Baja', 'pais_delete', 'home', 0, 55);
INSERT INTO `cb_usuarios_modulo` VALUES (64, '/pais_imprimir', 'Imprimir', 'pais_imprimir', 'home', 0, 55);
INSERT INTO `cb_usuarios_modulo` VALUES (65, '', 'Consultar', 'departamento_query', 'home', 0, 56);
INSERT INTO `cb_usuarios_modulo` VALUES (66, '/departamento_insert', 'Adicionar', 'departamento_insert', 'home', 0, 56);
INSERT INTO `cb_usuarios_modulo` VALUES (67, '/departamento_update', 'Actualizar', 'departamento_update', 'home', 0, 56);
INSERT INTO `cb_usuarios_modulo` VALUES (68, '/departamento_delete', 'Dar de Baja', 'departamento_delete', 'home', 0, 56);
INSERT INTO `cb_usuarios_modulo` VALUES (69, '/departamento_imprimir', 'Imprimir', 'departamento_imprimir', 'home', 0, 56);
INSERT INTO `cb_usuarios_modulo` VALUES (70, '', 'Consultar', 'ciudad_query', 'home', 0, 57);
INSERT INTO `cb_usuarios_modulo` VALUES (71, '/ciudad_insert', 'Adicionar', 'ciudad_insert', 'home', 0, 57);
INSERT INTO `cb_usuarios_modulo` VALUES (72, '/ciudad_update', 'Actualizar', 'ciudad_update', 'home', 0, 57);
INSERT INTO `cb_usuarios_modulo` VALUES (73, '/ciudad_delete', 'Dar de Baja', 'ciudad_delete', 'home', 0, 57);
INSERT INTO `cb_usuarios_modulo` VALUES (74, '/ciudad_imprimir', 'Imprimir', 'ciudad_imprimir', 'home', 0, 57);
INSERT INTO `cb_usuarios_modulo` VALUES (75, '', 'Consultar', 'sucursal_query', 'home', 0, 58);
INSERT INTO `cb_usuarios_modulo` VALUES (76, '/sucursal_insert', 'Adicionar', 'sucursal_insert', 'home', 0, 58);
INSERT INTO `cb_usuarios_modulo` VALUES (77, '/sucursal_update', 'Actualizar', 'sucursal_update', 'home', 0, 58);
INSERT INTO `cb_usuarios_modulo` VALUES (78, '/sucursal_delete', 'Dar de Baja', 'sucursal_delete', 'home', 0, 58);
INSERT INTO `cb_usuarios_modulo` VALUES (79, '/sucursal_imprimir', 'Imprimir', 'sucursal_imprimir', 'home', 0, 58);
INSERT INTO `cb_usuarios_modulo` VALUES (80, '', 'Consultar', 'oficina_query', 'home', 0, 59);
INSERT INTO `cb_usuarios_modulo` VALUES (81, '/oficina_insert', 'Adicionar', 'oficina_insert', 'home', 0, 59);
INSERT INTO `cb_usuarios_modulo` VALUES (82, '/oficina_update', 'Actualizar', 'oficina_update', 'home', 0, 59);
INSERT INTO `cb_usuarios_modulo` VALUES (83, '/oficina_delete', 'Dar de Baja', 'oficina_delete', 'home', 0, 59);
INSERT INTO `cb_usuarios_modulo` VALUES (84, '/oficina_imprimir', 'Imprimir', 'oficina_imprimir', 'home', 0, 59);

-- ----------------------------
-- Table structure for cb_usuarios_rol
-- ----------------------------
DROP TABLE IF EXISTS `cb_usuarios_rol`;
CREATE TABLE `cb_usuarios_rol`  (
  `cb_rol_id` int(11) NOT NULL AUTO_INCREMENT,
  `cb_rol_nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_rol_descripcion` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_rol_enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`cb_rol_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cb_usuarios_rol
-- ----------------------------
INSERT INTO `cb_usuarios_rol` VALUES (1, 'ADMINISTRADOR', 'Todos los permisos', 1);

-- ----------------------------
-- Table structure for cb_usuarios_usuario
-- ----------------------------
DROP TABLE IF EXISTS `cb_usuarios_usuario`;
CREATE TABLE `cb_usuarios_usuario`  (
  `cb_usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `cb_usuario_nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_usuario_apellido` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_usuario_correo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_usuario_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_usuario_password` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cb_usuario_fkrol` int(11) NOT NULL,
  `cb_usuario_activo` int(11) NULL DEFAULT NULL,
  `cb_usuario_token2` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cb_usuario_token` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cb_usuario_fkpersona` int(11) NULL DEFAULT NULL,
  `cb_usuario_enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`cb_usuario_id`) USING BTREE,
  UNIQUE INDEX `cb_usuario_username`(`cb_usuario_username`) USING BTREE,
  INDEX `cb_usuario_fkrol`(`cb_usuario_fkrol`) USING BTREE,
  CONSTRAINT `cb_usuarios_usuario_ibfk_1` FOREIGN KEY (`cb_usuario_fkrol`) REFERENCES `cb_usuarios_rol` (`cb_rol_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cb_usuarios_usuario
-- ----------------------------
INSERT INTO `cb_usuarios_usuario` VALUES (1, 'Administrador', 'principal', 'admin@host.com', 'admin', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', 1, 0, 'Sin Token2', 'Sin Token', NULL, 1);

-- ----------------------------
-- Table structure for dispositivos
-- ----------------------------
DROP TABLE IF EXISTS `dispositivos`;
CREATE TABLE `dispositivos`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `puerto` int(11) NULL DEFAULT NULL,
  `descripcion` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for eventos
-- ----------------------------
DROP TABLE IF EXISTS `eventos`;
CREATE TABLE `eventos`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `card` int(11) NULL DEFAULT NULL,
  `codigo` int(11) NULL DEFAULT NULL,
  `verificado` int(11) NULL DEFAULT NULL,
  `puerta` int(11) NULL DEFAULT NULL,
  `evento` int(11) NULL DEFAULT NULL,
  `estado` int(11) NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL,
  `iddispositivo` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for puertas
-- ----------------------------
DROP TABLE IF EXISTS `puertas`;
CREATE TABLE `puertas`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NULL DEFAULT NULL,
  `descripcion` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `fkdispositivo` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fkdispositivo`(`fkdispositivo`) USING BTREE,
  CONSTRAINT `puertas_ibfk_1` FOREIGN KEY (`fkdispositivo`) REFERENCES `dispositivos` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for rrhh_cargo
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_cargo`;
CREATE TABLE `rrhh_cargo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fkresponsable` int(11) NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fkresponsable`(`fkresponsable`) USING BTREE,
  CONSTRAINT `rrhh_cargo_ibfk_1` FOREIGN KEY (`fkresponsable`) REFERENCES `rrhh_cargo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_cargo
-- ----------------------------
INSERT INTO `rrhh_cargo` VALUES (1, 'Ing de Desarrollo', NULL, 1);
INSERT INTO `rrhh_cargo` VALUES (2, 'Gerente', NULL, 1);

-- ----------------------------
-- Table structure for rrhh_centro_costo
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_centro_costo`;
CREATE TABLE `rrhh_centro_costo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `nombre`(`nombre`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_centro_costo
-- ----------------------------
INSERT INTO `rrhh_centro_costo` VALUES (1, 'ce1', 'centro de costos 1', 1);

-- ----------------------------
-- Table structure for rrhh_ciudad
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_ciudad`;
CREATE TABLE `rrhh_ciudad`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  `fkdepartamento` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `nombre`(`nombre`) USING BTREE,
  INDEX `fkdepartamento`(`fkdepartamento`) USING BTREE,
  CONSTRAINT `rrhh_ciudad_ibfk_1` FOREIGN KEY (`fkdepartamento`) REFERENCES `rrhh_departamento` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_ciudad
-- ----------------------------
INSERT INTO `rrhh_ciudad` VALUES (1, 'Montero', 1, 1);
INSERT INTO `rrhh_ciudad` VALUES (2, 'Warnes', 1, 1);
INSERT INTO `rrhh_ciudad` VALUES (3, 'Quillacollo', 1, 2);
INSERT INTO `rrhh_ciudad` VALUES (4, 'Sacaba', 1, 2);

-- ----------------------------
-- Table structure for rrhh_departamento
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_departamento`;
CREATE TABLE `rrhh_departamento`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fkpais` int(11) NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `nombre`(`nombre`) USING BTREE,
  INDEX `fkpais`(`fkpais`) USING BTREE,
  CONSTRAINT `rrhh_departamento_ibfk_1` FOREIGN KEY (`fkpais`) REFERENCES `rrhh_pais` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_departamento
-- ----------------------------
INSERT INTO `rrhh_departamento` VALUES (1, 'Santa Cruz', 1, 1);
INSERT INTO `rrhh_departamento` VALUES (2, 'Cochabamba', 1, 1);
INSERT INTO `rrhh_departamento` VALUES (3, 'La paz', 1, 1);

-- ----------------------------
-- Table structure for rrhh_empleado
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_empleado`;
CREATE TABLE `rrhh_empleado`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fkpersona` int(11) NULL DEFAULT NULL,
  `codigo` int(11) NOT NULL,
  `foto` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `fkgerencia` int(11) NULL DEFAULT NULL,
  `fkcargo` int(11) NULL DEFAULT NULL,
  `fksucursal` int(11) NULL DEFAULT NULL,
  `fkcentro` int(11) NULL DEFAULT NULL,
  `fkoficina` int(11) NULL DEFAULT NULL,
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `afp` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `profesion` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nroseguro` int(11) NULL DEFAULT NULL,
  `afiliado` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nroapf` int(11) NULL DEFAULT NULL,
  `tipo` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `haberbasico` float NULL DEFAULT NULL,
  `nrocuenta` int(11) NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `codigo`(`codigo`) USING BTREE,
  INDEX `fkpersona`(`fkpersona`) USING BTREE,
  INDEX `fkgerencia`(`fkgerencia`) USING BTREE,
  INDEX `fkcargo`(`fkcargo`) USING BTREE,
  INDEX `fksucursal`(`fksucursal`) USING BTREE,
  INDEX `fkcentro`(`fkcentro`) USING BTREE,
  INDEX `fkoficina`(`fkoficina`) USING BTREE,
  CONSTRAINT `rrhh_empleado_ibfk_1` FOREIGN KEY (`fkpersona`) REFERENCES `rrhh_persona` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rrhh_empleado_ibfk_2` FOREIGN KEY (`fkgerencia`) REFERENCES `rrhh_gerencia` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rrhh_empleado_ibfk_3` FOREIGN KEY (`fkcargo`) REFERENCES `rrhh_cargo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rrhh_empleado_ibfk_4` FOREIGN KEY (`fksucursal`) REFERENCES `rrhh_sucursal` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rrhh_empleado_ibfk_5` FOREIGN KEY (`fkcentro`) REFERENCES `rrhh_centro_costo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rrhh_empleado_ibfk_6` FOREIGN KEY (`fkoficina`) REFERENCES `rrhh_oficina` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_empleado
-- ----------------------------
INSERT INTO `rrhh_empleado` VALUES (1, 1, 123, NULL, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `rrhh_empleado` VALUES (2, 2, 22233, NULL, 3, 2, 3, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);

-- ----------------------------
-- Table structure for rrhh_empresa
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_empresa`;
CREATE TABLE `rrhh_empresa`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `foto` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `nombre`(`nombre`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_empresa
-- ----------------------------
INSERT INTO `rrhh_empresa` VALUES (1, 'Cloudbit Srl', NULL, 1);

-- ----------------------------
-- Table structure for rrhh_gerencia
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_gerencia`;
CREATE TABLE `rrhh_gerencia`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  `fkempresa` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fkempresa`(`fkempresa`) USING BTREE,
  CONSTRAINT `rrhh_gerencia_ibfk_1` FOREIGN KEY (`fkempresa`) REFERENCES `rrhh_empresa` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_gerencia
-- ----------------------------
INSERT INTO `rrhh_gerencia` VALUES (1, 'Gerencia Operaciones', 1, 1);
INSERT INTO `rrhh_gerencia` VALUES (2, 'Gerencia Tecnica', 1, 1);
INSERT INTO `rrhh_gerencia` VALUES (3, 'Gerencia Comercial', 1, 1);

-- ----------------------------
-- Table structure for rrhh_oficina
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_oficina`;
CREATE TABLE `rrhh_oficina`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fksucursal` int(11) NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fksucursal`(`fksucursal`) USING BTREE,
  CONSTRAINT `rrhh_oficina_ibfk_1` FOREIGN KEY (`fksucursal`) REFERENCES `rrhh_sucursal` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_oficina
-- ----------------------------
INSERT INTO `rrhh_oficina` VALUES (1, 'Oficina 1', 1, 1);
INSERT INTO `rrhh_oficina` VALUES (2, 'Oficina 2', 1, 1);
INSERT INTO `rrhh_oficina` VALUES (3, 'Oficina Colla 1', 3, 1);

-- ----------------------------
-- Table structure for rrhh_pais
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_pais`;
CREATE TABLE `rrhh_pais`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `nombre`(`nombre`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_pais
-- ----------------------------
INSERT INTO `rrhh_pais` VALUES (1, 'Bolivia', 1);

-- ----------------------------
-- Table structure for rrhh_persona
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_persona`;
CREATE TABLE `rrhh_persona`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apellidopaterno` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `apellidomaterno` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nombres` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sexo` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ci` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fechanacimiento` date NULL DEFAULT NULL,
  `domicilio` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `telefono` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_persona
-- ----------------------------
INSERT INTO `rrhh_persona` VALUES (1, 'VILLAZON', 'VILLCA', ' UBALDO FRANCISCO', 'M', '5190630   CB', '2019-09-21', NULL, NULL, 1);
INSERT INTO `rrhh_persona` VALUES (2, 'AGUILAR', 'MONTAÑO', ' BORIS MARCELO', 'M', '528833 CB', '2019-09-21', NULL, NULL, 1);

-- ----------------------------
-- Table structure for rrhh_sucursal
-- ----------------------------
DROP TABLE IF EXISTS `rrhh_sucursal`;
CREATE TABLE `rrhh_sucursal`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fkciudad` int(11) NULL DEFAULT NULL,
  `enabled` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `nombre`(`nombre`) USING BTREE,
  INDEX `fkciudad`(`fkciudad`) USING BTREE,
  CONSTRAINT `rrhh_sucursal_ibfk_1` FOREIGN KEY (`fkciudad`) REFERENCES `rrhh_ciudad` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rrhh_sucursal
-- ----------------------------
INSERT INTO `rrhh_sucursal` VALUES (1, 'Sucursal A', 1, 1);
INSERT INTO `rrhh_sucursal` VALUES (2, 'Sucursal B', 1, 1);
INSERT INTO `rrhh_sucursal` VALUES (3, 'Sucursal Colla 1', 3, 1);

SET FOREIGN_KEY_CHECKS = 1;
