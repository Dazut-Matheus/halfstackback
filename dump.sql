DROP SCHEMA asa;

CREATE SCHEMA asa;

use asa;

CREATE TABLE
    IF NOT EXISTS `django_content_type` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `app_label` varchar(100) NOT NULL,
        `model` varchar(100) NOT NULL
    );

INSERT INTO django_content_type VALUES (1, 'admin', 'logentry');

INSERT INTO django_content_type VALUES (2, 'auth', 'permission');

INSERT INTO django_content_type VALUES(3, 'auth', 'group');

INSERT INTO
    django_content_type
VALUES (
        4,
        'contenttypes',
        'contenttype'
    );

INSERT INTO django_content_type VALUES (5, 'sessions', 'session');

INSERT INTO django_content_type VALUES (6, 'empresa', 'empresa');

INSERT INTO django_content_type VALUES (7, 'pedido', 'pedido');

INSERT INTO django_content_type VALUES (8, 'produto', 'produto');

INSERT INTO django_content_type VALUES (9, 'cliente', 'cliente');

INSERT INTO
    django_content_type
VALUES (
        10,
        'cliente',
        'passwordresets'
    );

INSERT INTO django_content_type VALUES (11, 'cliente', 'tokens');

INSERT INTO django_content_type VALUES(12, 'itens', 'itens');

CREATE TABLE
    IF NOT EXISTS `django_migrations` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `app` varchar(255) NOT NULL,
        `name` varchar(255) NOT NULL,
        `applied` datetime NOT NULL
    );

INSERT INTO django_migrations
VALUES (
        1,
        'contenttypes',
        '0001_initial',
        '2023-01-18 14:27:11.551056'
    );

INSERT INTO django_migrations
VALUES (
        2,
        'empresa',
        '0001_initial',
        '2023-01-18 14:27:11.561451'
    );

INSERT INTO django_migrations
VALUES (
        3,
        'empresa',
        '0002_alter_empresa_cnpj_alter_empresa_complemento_and_more',
        '2023-01-18 14:27:11.586781'
    );

INSERT INTO django_migrations
VALUES (
        4,
        'empresa',
        '0003_remove_empresa_foto',
        '2023-01-18 14:27:11.596057'
    );

INSERT INTO django_migrations
VALUES (
        5,
        'cliente',
        '0001_initial',
        '2023-01-18 14:27:11.606053'
    );

INSERT INTO django_migrations
VALUES (
        6,
        'admin',
        '0001_initial',
        '2023-01-18 14:27:11.618646'
    );

INSERT INTO django_migrations
VALUES (
        7,
        'admin',
        '0002_logentry_remove_auto_add',
        '2023-01-18 14:27:11.632867'
    );

INSERT INTO django_migrations
VALUES (
        8,
        'admin',
        '0003_logentry_add_action_flag_choices',
        '2023-01-18 14:27:11.646976'
    );

INSERT INTO django_migrations
VALUES (
        9,
        'contenttypes',
        '0002_remove_content_type_name',
        '2023-01-18 14:27:11.668210'
    );

INSERT INTO django_migrations
VALUES (
        10,
        'auth',
        '0001_initial',
        '2023-01-18 14:27:11.695805'
    );

INSERT INTO django_migrations
VALUES (
        11,
        'auth',
        '0002_alter_permission_name_max_length',
        '2023-01-18 14:27:11.707916'
    );

INSERT INTO django_migrations
VALUES (
        12,
        'auth',
        '0003_alter_user_email_max_length',
        '2023-01-18 14:27:11.717684'
    );

INSERT INTO django_migrations
VALUES (
        13,
        'auth',
        '0004_alter_user_username_opts',
        '2023-01-18 14:27:11.727160'
    );

INSERT INTO django_migrations
VALUES (
        14,
        'auth',
        '0005_alter_user_last_login_null',
        '2023-01-18 14:27:11.734692'
    );

INSERT INTO django_migrations
VALUES (
        15,
        'auth',
        '0006_require_contenttypes_0002',
        '2023-01-18 14:27:11.737797'
    );

INSERT INTO django_migrations
VALUES (
        16,
        'auth',
        '0007_alter_validators_add_error_messages',
        '2023-01-18 14:27:11.747309'
    );

INSERT INTO django_migrations
VALUES (
        17,
        'auth',
        '0008_alter_user_username_max_length',
        '2023-01-18 14:27:11.757924'
    );

INSERT INTO django_migrations
VALUES (
        18,
        'auth',
        '0009_alter_user_last_name_max_length',
        '2023-01-18 14:27:11.765915'
    );

INSERT INTO django_migrations
VALUES (
        19,
        'auth',
        '0010_alter_group_name_max_length',
        '2023-01-18 14:27:11.778739'
    );

INSERT INTO django_migrations
VALUES (
        20,
        'auth',
        '0011_update_proxy_permissions',
        '2023-01-18 14:27:11.789977'
    );

INSERT INTO django_migrations
VALUES (
        21,
        'auth',
        '0012_alter_user_first_name_max_length',
        '2023-01-18 14:27:11.799789'
    );

INSERT INTO django_migrations
VALUES (
        22,
        'cliente',
        '0002_passwordresets_tokens',
        '2023-01-18 14:27:11.817903'
    );

INSERT INTO django_migrations
VALUES (
        23,
        'pedido',
        '0001_initial',
        '2023-01-18 14:27:11.833595'
    );

INSERT INTO django_migrations
VALUES (
        24,
        'pedido',
        '0002_remove_pedido_cliente_endereco_pedido_bairro_and_more',
        '2023-01-18 14:27:11.878077'
    );

INSERT INTO django_migrations
VALUES (
        25,
        'itens',
        '0001_initial',
        '2023-01-18 14:27:11.896162'
    );

INSERT INTO django_migrations
VALUES (
        26,
        'produto',
        '0001_initial',
        '2023-01-18 14:27:11.901116'
    );

INSERT INTO django_migrations
VALUES (
        27,
        'produto',
        '0002_produto_empresa',
        '2023-01-18 14:27:11.919954'
    );

INSERT INTO django_migrations
VALUES (
        28,
        'sessions',
        '0001_initial',
        '2023-01-18 14:27:11.928089'
    );

INSERT INTO django_migrations
VALUES (
        29,
        'cliente',
        '0003_rename_user_tokens_cliente',
        '2023-01-18 15:01:57.813893'
    );

INSERT INTO django_migrations
VALUES (
        30,
        'cliente',
        '0004_remove_cliente_empresa',
        '2023-01-18 15:32:22.707241'
    );

INSERT INTO django_migrations
VALUES (
        31,
        'itens',
        '0002_itens_produto',
        '2023-01-18 16:10:42.002068'
    );

INSERT INTO django_migrations
VALUES (
        32,
        'itens',
        '0003_itens_quantidade',
        '2023-01-18 16:15:34.996328'
    );

INSERT INTO django_migrations
VALUES (
        33,
        'cliente',
        '0005_auto_20230201_2157',
        '2023-02-01 21:57:29.768613'
    );

INSERT INTO django_migrations
VALUES (
        34,
        'itens',
        '0004_auto_20230201_2157',
        '2023-02-01 21:57:29.842823'
    );

INSERT INTO django_migrations
VALUES (
        35,
        'pedido',
        '0003_alter_pedido_empresa',
        '2023-02-01 21:57:29.854126'
    );

INSERT INTO django_migrations
VALUES (
        36,
        'produto',
        '0003_alter_produto_empresa',
        '2023-02-01 21:57:29.864298'
    );

CREATE TABLE
    IF NOT EXISTS `empresa` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `nome` varchar(48) NOT NULL,
        `cnpj` varchar(48) NULL,
        `telefone` varchar(48) NOT NULL,
        `cidade` varchar(50) NOT NULL,
        `rua` varchar(50) NOT NULL,
        `bairro` varchar(50) NOT NULL,
        `numero` varchar(10) NOT NULL,
        `complemento` varchar(50) NULL
    );

INSERT INTO empresa
VALUES (
        2,
        'Pastelaria',
        '999999999',
        '+34 99999-9999',
        'Uberlandia',
        'bo',
        'pl',
        '123',
        '1'
    );

INSERT INTO empresa
VALUES (
        5,
        'Pizzaria',
        '8888888888',
        '+34 99999-9999',
        'Uberlandia',
        'av. 5',
        'santa',
        '111',
        ''
    );

INSERT INTO empresa
VALUES (
        6,
        'Espetaria',
        '7777777',
        '+34 99999-9999',
        'Uberlandia',
        'av. 2',
        'santa',
        '222',
        'em frente a ufu'
    );

INSERT INTO empresa
VALUES (
        7,
        'Bar',
        '7777777',
        '+34 99999-9999',
        'Uberlandia',
        'av. 2',
        'osvaldo',
        '222',
        'do lado da ufu'
    );

CREATE TABLE
    IF NOT EXISTS `cliente` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `nome` varchar(255) NOT NULL,
        `data_de_nascimento` date NOT NULL,
        `email` varchar(255) NOT NULL UNIQUE,
        `email_verified_at` bool NOT NULL,
        `password` varchar(255) NOT NULL,
        `cidade` varchar(50) NOT NULL,
        `rua` varchar(50) NOT NULL,
        `bairro` varchar(50) NOT NULL,
        `numero` varchar(10) NOT NULL,
        `complemento` varchar(50) NULL
    );

INSERT INTO cliente
VALUES (
        5,
        'Matheus Ferreira Gomes',
        '1998-01-01',
        'matheusferreiragomes1998@gmail.com',
        0,
        'pbkdf2_sha256$260000$9bo2pv4C2HA0NVOmf50HvM$mxlaHL/+dwQcCzT6DpPqXMMdQONjrDgXRqkfresjMg4=',
        'Uberlandia',
        'bo',
        'pl',
        '123',
        NULL
    );

CREATE TABLE
    IF NOT EXISTS `auth_group` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(150) NOT NULL UNIQUE
    );

CREATE TABLE
    IF NOT EXISTS `auth_permission` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `content_type_id` INT NOT NULL,
        `codename` varchar(100) NOT NULL,
        `name` varchar(255) NOT NULL,
        FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
    );

INSERT INTO auth_permission
VALUES (
        1,
        1,
        'add_logentry',
        'Can add log entry'
    );

INSERT INTO auth_permission
VALUES (
        2,
        1,
        'change_logentry',
        'Can change log entry'
    );

INSERT INTO auth_permission
VALUES (
        3,
        1,
        'delete_logentry',
        'Can delete log entry'
    );

INSERT INTO auth_permission
VALUES (
        4,
        1,
        'view_logentry',
        'Can view log entry'
    );

INSERT INTO auth_permission
VALUES (
        5,
        2,
        'add_permission',
        'Can add permission'
    );

INSERT INTO auth_permission
VALUES (
        6,
        2,
        'change_permission',
        'Can change permission'
    );

INSERT INTO auth_permission
VALUES (
        7,
        2,
        'delete_permission',
        'Can delete permission'
    );

INSERT INTO auth_permission
VALUES (
        8,
        2,
        'view_permission',
        'Can view permission'
    );

INSERT INTO auth_permission
VALUES (
        9,
        3,
        'add_group',
        'Can add group'
    );

INSERT INTO auth_permission
VALUES (
        10,
        3,
        'change_group',
        'Can change group'
    );

INSERT INTO auth_permission
VALUES (
        11,
        3,
        'delete_group',
        'Can delete group'
    );

INSERT INTO auth_permission
VALUES (
        12,
        3,
        'view_group',
        'Can view group'
    );

INSERT INTO auth_permission
VALUES (
        13,
        4,
        'add_contenttype',
        'Can add content type'
    );

INSERT INTO auth_permission
VALUES (
        14,
        4,
        'change_contenttype',
        'Can change content type'
    );

INSERT INTO auth_permission
VALUES (
        15,
        4,
        'delete_contenttype',
        'Can delete content type'
    );

INSERT INTO auth_permission
VALUES (
        16,
        4,
        'view_contenttype',
        'Can view content type'
    );

INSERT INTO auth_permission
VALUES (
        17,
        5,
        'add_session',
        'Can add session'
    );

INSERT INTO auth_permission
VALUES (
        18,
        5,
        'change_session',
        'Can change session'
    );

INSERT INTO auth_permission
VALUES (
        19,
        5,
        'delete_session',
        'Can delete session'
    );

INSERT INTO auth_permission
VALUES (
        20,
        5,
        'view_session',
        'Can view session'
    );

INSERT INTO auth_permission
VALUES (
        21,
        6,
        'add_empresa',
        'Can add empresa'
    );

INSERT INTO auth_permission
VALUES (
        22,
        6,
        'change_empresa',
        'Can change empresa'
    );

INSERT INTO auth_permission
VALUES (
        23,
        6,
        'delete_empresa',
        'Can delete empresa'
    );

INSERT INTO auth_permission
VALUES (
        24,
        6,
        'view_empresa',
        'Can view empresa'
    );

INSERT INTO auth_permission
VALUES (
        25,
        7,
        'add_pedido',
        'Can add pedido'
    );

INSERT INTO auth_permission
VALUES (
        26,
        7,
        'change_pedido',
        'Can change pedido'
    );

INSERT INTO auth_permission
VALUES (
        27,
        7,
        'delete_pedido',
        'Can delete pedido'
    );

INSERT INTO auth_permission
VALUES (
        28,
        7,
        'view_pedido',
        'Can view pedido'
    );

INSERT INTO auth_permission
VALUES (
        29,
        8,
        'add_produto',
        'Can add produto'
    );

INSERT INTO auth_permission
VALUES (
        30,
        8,
        'change_produto',
        'Can change produto'
    );

INSERT INTO auth_permission
VALUES (
        31,
        8,
        'delete_produto',
        'Can delete produto'
    );

INSERT INTO auth_permission
VALUES (
        32,
        8,
        'view_produto',
        'Can view produto'
    );

INSERT INTO auth_permission
VALUES (
        33,
        9,
        'add_cliente',
        'Can add cliente'
    );

INSERT INTO auth_permission
VALUES (
        34,
        9,
        'change_cliente',
        'Can change cliente'
    );

INSERT INTO auth_permission
VALUES (
        35,
        9,
        'delete_cliente',
        'Can delete cliente'
    );

INSERT INTO auth_permission
VALUES (
        36,
        9,
        'view_cliente',
        'Can view cliente'
    );

INSERT INTO auth_permission
VALUES (
        37,
        10,
        'add_passwordresets',
        'Can add password resets'
    );

INSERT INTO auth_permission
VALUES (
        38,
        10,
        'change_passwordresets',
        'Can change password resets'
    );

INSERT INTO auth_permission
VALUES (
        39,
        10,
        'delete_passwordresets',
        'Can delete password resets'
    );

INSERT INTO auth_permission
VALUES (
        40,
        10,
        'view_passwordresets',
        'Can view password resets'
    );

INSERT INTO auth_permission
VALUES (
        41,
        11,
        'add_tokens',
        'Can add tokens'
    );

INSERT INTO auth_permission
VALUES (
        42,
        11,
        'change_tokens',
        'Can change tokens'
    );

INSERT INTO auth_permission
VALUES (
        43,
        11,
        'delete_tokens',
        'Can delete tokens'
    );

INSERT INTO auth_permission
VALUES (
        44,
        11,
        'view_tokens',
        'Can view tokens'
    );

INSERT INTO auth_permission
VALUES (
        45,
        12,
        'add_itens',
        'Can add itens'
    );

INSERT INTO auth_permission
VALUES (
        46,
        12,
        'change_itens',
        'Can change itens'
    );

INSERT INTO auth_permission
VALUES (
        47,
        12,
        'delete_itens',
        'Can delete itens'
    );

INSERT INTO auth_permission
VALUES (
        48,
        12,
        'view_itens',
        'Can view itens'
    );

CREATE TABLE
    IF NOT EXISTS `auth_group_permissions` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `group_id` INT NOT NULL,
        `permission_id` INT NOT NULL,
        FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
        FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
    );

CREATE TABLE
    IF NOT EXISTS `password_resets` (
        `email` varchar(255) NOT NULL PRIMARY KEY,
        `token` varchar(255) NOT NULL,
        `created_at` datetime NULL
    );

INSERT INTO password_resets
VALUES (
        'matheusferreiragomes1998@gmail.com',
        '853499',
        '2023-02-01 21:41:57.545354'
    );

CREATE TABLE
    IF NOT EXISTS `pedido` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `cliente_nome` varchar(100) NOT NULL,
        `empresa_id` INT NOT NULL,
        `bairro` varchar(50) NOT NULL,
        `cidade` varchar(50) NOT NULL,
        `complemento` varchar(50) DEFAULT NULL,
        `numero` varchar(10) NOT NULL,
        `rua` varchar(50) NOT NULL,
        FOREIGN KEY (`empresa_id`) REFERENCES `empresa` (`id`)
    );

INSERT INTO pedido
VALUES (
        1,
        'Matheus',
        2,
        'pl',
        'Uberlandia',
        NULL,
        '66',
        'bo'
    );

CREATE TABLE
    IF NOT EXISTS `produto` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `nome` varchar(48) NOT NULL,
        `descricao` varchar(250) DEFAULT NULL,
        `valor` DECIMAL(10, 2) NOT NULL,
        `empresa_id` INT NOT NULL,
        FOREIGN KEY (`empresa_id`) REFERENCES `empresa` (`id`)
    );

INSERT INTO produto
VALUES (
        2,
        'Pastal de Queijo',
        'Pastal sabor (queijo Serve uma pessoa)',
        8.0,
        2
    );

INSERT INTO produto
VALUES (
        3,
        'Pastal de Carne',
        'Pastal sabor carne (Serve uma pessoa)',
        10.0,
        2
    );

INSERT INTO produto
VALUES (
        5,
        'Pizza calabresa G',
        'Serve quatro pessoas',
        40.0,
        5
    );

INSERT INTO produto
VALUES (
        6,
        'Pizza Frango com captupry M',
        'Serve duas pessoas',
        30.0,
        5
    );

INSERT INTO produto
VALUES (
        7,
        'Espeto franbacon',
        'Serve uma pessoas',
        12.0,
        6
    );

INSERT INTO produto
VALUES (
        8,
        'Espeto cupim',
        'Serve uma pessoas',
        15.0,
        6
    );

INSERT INTO produto
VALUES (
        9,
        'Refrigerante Coca',
        '200ml',
        4.0,
        7
    );

INSERT INTO produto VALUES ( 10, 'Cerveja Bhama', '355ml', 4.0, 7 );

CREATE TABLE
    IF NOT EXISTS `django_session` (
        `session_key` varchar(40) NOT NULL PRIMARY KEY,
        `session_data` text NOT NULL,
        `expire_date` datetime NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS `auth_tokens` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `token` varchar(500) NOT NULL,
        `flag` tinyint(1) NOT NULL,
        `cliente_id` INT NOT NULL,
        FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`)
    );

INSERT INTO auth_tokens
VALUES (
        16,
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6Im1hdGhldXNmZXJyZWlyYWdvbWVzMTk5OEBnbWFpbC5jb20iLCJleHAiOjE2NzU0NDU4MTMsImVtYWlsIjoibWF0aGV1c2ZlcnJlaXJhZ29tZXMxOTk4QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjc1NDI3ODEzfQ.s3ny5gzoZ6Vj5XKywASVPkpDIE-IP5d_fZ8YBNC_VkQ',
        1,
        5
    );

CREATE TABLE
    IF NOT EXISTS `itens` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `cliente_id` INT NOT NULL,
        `empresa_id` INT NOT NULL,
        `pedido_id` INT NOT NULL,
        `produto_id` INT NOT NULL,
        `quantidade` INT NOT NULL,
        FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
        FOREIGN KEY (`empresa_id`) REFERENCES `empresa` (`id`),
        FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id`),
        FOREIGN KEY (`produto_id`) REFERENCES `produto` (`id`)
    );

CREATE UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` ON `django_content_type` (`app_label`, `model`);

CREATE UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` ON `auth_group_permissions` (`group_id`, `permission_id`);

CREATE INDEX
    `auth_group_permissions_group_id_b120cbf9` ON `auth_group_permissions` (`group_id`);

CREATE INDEX
    `auth_group_permissions_permission_id_84c5c92e` ON `auth_group_permissions` (`permission_id`);

CREATE UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` ON `auth_permission` (`content_type_id`, `codename`);

CREATE INDEX
    `auth_permission_content_type_id_2f476e4b` ON `auth_permission` (`content_type_id`);

CREATE INDEX `pedido_empresa_id_9d0d25e0` ON `pedido` (`empresa_id`);

CREATE INDEX
    `produto_empresa_id_02a6fdf9` ON `produto` (`empresa_id`);

CREATE INDEX
    `django_session_expire_date_a5c62663` ON `django_session` (`expire_date`);

CREATE INDEX
    `auth_tokens_cliente_id_f270c2b3` ON `auth_tokens` (`cliente_id`);

CREATE INDEX `itens_cliente_id_1ff7d8e1` ON `itens` (`cliente_id`);

CREATE INDEX `itens_empresa_id_5268203d` ON `itens` (`empresa_id`);

CREATE INDEX `itens_pedido_id_3caff943` ON `itens` (`pedido_id`);

CREATE INDEX `itens_produto_id_c08e3ed1` ON `itens` (`produto_id`);

COMMIT;