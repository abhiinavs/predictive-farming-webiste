/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - farmers_app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmers_app` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `farmers_app`;

/*Table structure for table `app_complaint_table` */

DROP TABLE IF EXISTS `app_complaint_table`;

CREATE TABLE `app_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_complaint_table_user_id_id_787938c1_fk_app_login_table_id` (`user_id_id`),
  CONSTRAINT `app_complaint_table_user_id_id_787938c1_fk_app_login_table_id` FOREIGN KEY (`user_id_id`) REFERENCES `app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_complaint_table` */

insert  into `app_complaint_table`(`id`,`complaint`,`date`,`reply`,`user_id_id`) values 
(1,'ufjd rerni d','2024-09-22','pending',3),
(2,'fdxcjk','2024-09-22','pending',3),
(3,'hdrftghujh','2024-09-22','pending',3),
(4,'gfgkuyug','2024-09-22','pending',3),
(5,'yyyy','2024-09-22','pending',3),
(6,'mmmmmmmmmmm','2024-09-22','pending',3),
(7,'Farmer','2024-09-23','pending',8),
(8,'','2024-09-23','pending',8),
(9,'','2024-09-23','pending',8),
(10,'','2024-09-23','pending',8),
(11,'','2024-09-23','pending',8),
(12,'','2024-09-23','pending',8),
(13,'  e','2024-09-23','pending',8),
(14,'admin','2024-09-23','pending',3),
(15,'aaaa','2024-09-23','pending',8),
(16,'admin','2024-09-23','pending',8);

/*Table structure for table `app_complaints` */

DROP TABLE IF EXISTS `app_complaints`;

CREATE TABLE `app_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_complaints_user_id_id_ab3c7f48_fk_app_login_table_id` (`user_id_id`),
  CONSTRAINT `app_complaints_user_id_id_ab3c7f48_fk_app_login_table_id` FOREIGN KEY (`user_id_id`) REFERENCES `app_login_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_complaints` */

/*Table structure for table `app_crop_table` */

DROP TABLE IF EXISTS `app_crop_table`;

CREATE TABLE `app_crop_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `stock` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_crop_table` */

insert  into `app_crop_table`(`id`,`name`,`details`,`price`,`stock`) values 
(11,'admin','ghehb','admin','hgh');

/*Table structure for table `app_doubt_table` */

DROP TABLE IF EXISTS `app_doubt_table`;

CREATE TABLE `app_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `FARMER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_doubt_table_EXPERT_id_9608a3fc_fk_app_expert_table_id` (`EXPERT_id`),
  KEY `app_doubt_table_FARMER_id_41a27c75_fk_app_farmer_table_id` (`FARMER_id`),
  CONSTRAINT `app_doubt_table_EXPERT_id_9608a3fc_fk_app_expert_table_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `app_expert_table` (`id`),
  CONSTRAINT `app_doubt_table_FARMER_id_41a27c75_fk_app_farmer_table_id` FOREIGN KEY (`FARMER_id`) REFERENCES `app_farmer_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_doubt_table` */

insert  into `app_doubt_table`(`id`,`doubt`,`date`,`reply`,`EXPERT_id`,`FARMER_id`) values 
(1,'hello','2024-09-10','iuhda',1,1),
(2,'Farmer','2024-09-23','pending',2,1),
(3,'Farmer','2024-09-23','pending',2,1),
(4,'Farmer','2024-09-23','pending',2,1),
(5,'hello','2024-09-23','pending',2,1),
(6,'wxwx','2024-09-23','pending',2,1),
(7,'wxwx','2024-09-23','pending',2,1),
(8,'eded','2024-09-23','pending',2,1),
(9,'eded','2024-09-23','pending',2,1),
(10,'sdvsd','2024-09-23','pending',2,1),
(11,'fvfd','2024-09-23','pending',2,1),
(12,'fvfd','2024-09-23','cccc',1,1),
(13,'etyreyer','2024-09-23','pending',2,1),
(14,'sdcsdcsda','2024-09-23','pending',1,1),
(15,'sdcsdcsda','2024-09-23','pending',2,1),
(16,'admin','2024-09-23','pending',2,1),
(17,'admin','2024-09-23','pending',1,1),
(18,'aDaADa','2024-09-23','pending',2,1),
(19,'aaaa','2024-09-23','pending',2,1),
(20,'bb','2024-09-23','pending',2,1),
(21,'bgkf','2024-09-23','pending',2,1),
(22,'admin','2024-09-23','pending',2,1),
(23,'admin','2024-09-23','pending',2,1),
(24,'hvhgvjbj','2024-09-23','pending',2,1),
(25,'Farmer','2024-09-23','pending',2,1),
(26,'Farmer','2024-09-23','pending',2,1),
(27,'admin','2024-09-23','pending',2,1);

/*Table structure for table `app_expert_table` */

DROP TABLE IF EXISTS `app_expert_table`;

CREATE TABLE `app_expert_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_expert_table_LOGIN_id_7416376a_fk_app_login_table_id` (`LOGIN_id`),
  CONSTRAINT `app_expert_table_LOGIN_id_7416376a_fk_app_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_expert_table` */

insert  into `app_expert_table`(`id`,`FirstName`,`LastName`,`Place`,`qualification`,`Phone`,`Email`,`Image`,`LOGIN_id`) values 
(1,'ddd','2','hgh','hh','09778291129','sidharthramachandran27@gmail.com','/2024-09-20-11-22-17.jpg',6),
(2,'sds','sds','ds','ds','sd','fgg','/2024-09-20-15-01-34.jpg',7);

/*Table structure for table `app_farmer_table` */

DROP TABLE IF EXISTS `app_farmer_table`;

CREATE TABLE `app_farmer_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `Post` varchar(100) NOT NULL,
  `Pin` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_farmer_table_LOGIN_id_ff0e1729_fk_app_login_table_id` (`LOGIN_id`),
  CONSTRAINT `app_farmer_table_LOGIN_id_ff0e1729_fk_app_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_farmer_table` */

insert  into `app_farmer_table`(`id`,`FirstName`,`LastName`,`Place`,`Post`,`Pin`,`Phone`,`Email`,`Image`,`LOGIN_id`) values 
(1,'farm','xx','plvv','west','897665','8888888','a@g.c','aaa',8),
(2,'farmer','famer','pulpally','east','21819','12019028','asnja','jnas',3),
(3,'Farmer','2','AFADD','FA','F32`','','sidharthramachandran27@gmail.com','2024-09-24-09-53-36.jpg',11),
(4,'Farmer','2','AFADD','FA','F32`','','','2024-09-24-09-54-29.jpg',12),
(5,'Farmer','2','AFADD','FA','F32`','','','2024-09-24-09-55-50.jpg',13),
(6,'Farmer','2','AFADD','FA','F32`','','','2024-09-24-10-12-23.jpg',14);

/*Table structure for table `app_feedback_table` */

DROP TABLE IF EXISTS `app_feedback_table`;

CREATE TABLE `app_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `rating` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `USER_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_feedback_table_USER_ID_id_829ddd5b_fk_app_login_table_id` (`USER_ID_id`),
  CONSTRAINT `app_feedback_table_USER_ID_id_829ddd5b_fk_app_login_table_id` FOREIGN KEY (`USER_ID_id`) REFERENCES `app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_feedback_table` */

insert  into `app_feedback_table`(`id`,`feedback`,`rating`,`date`,`USER_ID_id`) values 
(1,'uwgf','alskdn','2024-09-12',5);

/*Table structure for table `app_fertilizer_table` */

DROP TABLE IF EXISTS `app_fertilizer_table`;

CREATE TABLE `app_fertilizer_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_fertilizer_table` */

insert  into `app_fertilizer_table`(`id`,`name`,`image`,`details`,`price`) values 
(6,'wdcx','2024-09-21-16-56-20.jpg','tgrw',32),
(16,'wdcx','2024-09-21-16-51-54.jpg','tgrw',32),
(17,'FFXYJ','2024-09-21-16-52-05.jpg','FTHXDF',32235),
(18,'wdcx','2024-09-21-16-56-10.jpg','tgrw',32);

/*Table structure for table `app_login_table` */

DROP TABLE IF EXISTS `app_login_table`;

CREATE TABLE `app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_login_table` */

insert  into `app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'Expert','Expert','Expert'),
(3,'Farmer','Farmer','Farmer'),
(5,'aaaawqwq','11111','expert'),
(6,'aaaa','11111','reject'),
(7,'gf','fgfd','reject'),
(8,'far','far','Farmer'),
(9,'gf','fgfd','expert'),
(10,'ADMIN','323`12','farmer'),
(11,'ADMIN','323`12','farmer'),
(12,'ADMIN','323`12','farmer'),
(13,'ADMIN','323`12','farmer'),
(14,'ADMIN','323`12','farmer');

/*Table structure for table `app_notification_table` */

DROP TABLE IF EXISTS `app_notification_table`;

CREATE TABLE `app_notification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `notification` varchar(100) NOT NULL,
  `time` time(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_notification_table` */

insert  into `app_notification_table`(`id`,`date`,`notification`,`time`) values 
(6,'2024-09-23','bghjk','22:36:28.490811'),
(7,'2024-09-24','dthrrsegfsfd','09:03:44.878144'),
(8,'2024-09-24','sddsfs','14:53:40.614495');

/*Table structure for table `app_order_details` */

DROP TABLE IF EXISTS `app_order_details`;

CREATE TABLE `app_order_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_order_details_ORDER_id_f3f3a40f_fk_app_order_product_id` (`ORDER_id`),
  KEY `app_order_details_PRODUCT_id_27601dbc_fk_app_product_table_id` (`PRODUCT_id`),
  CONSTRAINT `app_order_details_ORDER_id_f3f3a40f_fk_app_order_product_id` FOREIGN KEY (`ORDER_id`) REFERENCES `app_order_product` (`id`),
  CONSTRAINT `app_order_details_PRODUCT_id_27601dbc_fk_app_product_table_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `app_product_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_order_details` */

insert  into `app_order_details`(`id`,`quantity`,`ORDER_id`,`PRODUCT_id`) values 
(1,5,1,5);

/*Table structure for table `app_order_product` */

DROP TABLE IF EXISTS `app_order_product`;

CREATE TABLE `app_order_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total_amount` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_order_product_user_id_id_df1b2089_fk_app_user_table_id` (`user_id_id`),
  CONSTRAINT `app_order_product_user_id_id_df1b2089_fk_app_user_table_id` FOREIGN KEY (`user_id_id`) REFERENCES `app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_order_product` */

insert  into `app_order_product`(`id`,`total_amount`,`date`,`status`,`user_id_id`) values 
(1,'500','2024-09-23','approved',1);

/*Table structure for table `app_product_table` */

DROP TABLE IF EXISTS `app_product_table`;

CREATE TABLE `app_product_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `FARMER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_product_table_FARMER_id_9bc88eb9_fk_app_farmer_table_id` (`FARMER_id`),
  CONSTRAINT `app_product_table_FARMER_id_9bc88eb9_fk_app_farmer_table_id` FOREIGN KEY (`FARMER_id`) REFERENCES `app_farmer_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_product_table` */

insert  into `app_product_table`(`id`,`name`,`image`,`stock`,`price`,`details`,`FARMER_id`) values 
(5,'jnty','kk.png','40','400','nuty',1),
(6,'wqrq','Screenshot 2024-07-08 203631_VeTiDFZ.png','qew3414','14','4121',1);

/*Table structure for table `app_soil_table` */

DROP TABLE IF EXISTS `app_soil_table`;

CREATE TABLE `app_soil_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `soil_type` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `EXPERT_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_soil_table_EXPERT_ID_id_a5bced30_fk_app_expert_table_id` (`EXPERT_ID_id`),
  CONSTRAINT `app_soil_table_EXPERT_ID_id_a5bced30_fk_app_expert_table_id` FOREIGN KEY (`EXPERT_ID_id`) REFERENCES `app_expert_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_soil_table` */

insert  into `app_soil_table`(`id`,`soil_type`,`details`,`EXPERT_ID_id`) values 
(7,'soil','soil type',1),
(8,'admin','admin',1),
(9,'','',1);

/*Table structure for table `app_tips_table` */

DROP TABLE IF EXISTS `app_tips_table`;

CREATE TABLE `app_tips_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tips` varchar(100) NOT NULL,
  `EXPERT_ID_id` bigint NOT NULL,
  `Details` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_tips_table_EXPERT_ID_id_b034cd10_fk_app_expert_table_id` (`EXPERT_ID_id`),
  CONSTRAINT `app_tips_table_EXPERT_ID_id_b034cd10_fk_app_expert_table_id` FOREIGN KEY (`EXPERT_ID_id`) REFERENCES `app_expert_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_tips_table` */

insert  into `app_tips_table`(`id`,`tips`,`EXPERT_ID_id`,`Details`) values 
(16,'wqe',1,'ewq'),
(17,'wqe',1,'ewq'),
(18,'wqe',1,'ewq');

/*Table structure for table `app_user_table` */

DROP TABLE IF EXISTS `app_user_table`;

CREATE TABLE `app_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `Post` varchar(100) NOT NULL,
  `Pin` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_user_table_LOGIN_id_717a8485_fk_app_login_table_id` (`LOGIN_id`),
  CONSTRAINT `app_user_table_LOGIN_id_717a8485_fk_app_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `app_user_table` */

insert  into `app_user_table`(`id`,`FirstName`,`LastName`,`Place`,`Post`,`Pin`,`Phone`,`Email`,`Image`,`LOGIN_id`) values 
(1,'fas','ahsa','yuya','823y','8293','6vw','hdbc','11',6);

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add fertilizer_table',7,'add_fertilizer_table'),
(26,'Can change fertilizer_table',7,'change_fertilizer_table'),
(27,'Can delete fertilizer_table',7,'delete_fertilizer_table'),
(28,'Can view fertilizer_table',7,'view_fertilizer_table'),
(29,'Can add login_table',8,'add_login_table'),
(30,'Can change login_table',8,'change_login_table'),
(31,'Can delete login_table',8,'delete_login_table'),
(32,'Can view login_table',8,'view_login_table'),
(33,'Can add notification_table',9,'add_notification_table'),
(34,'Can change notification_table',9,'change_notification_table'),
(35,'Can delete notification_table',9,'delete_notification_table'),
(36,'Can view notification_table',9,'view_notification_table'),
(37,'Can add soil_tabel',10,'add_soil_tabel'),
(38,'Can change soil_tabel',10,'change_soil_tabel'),
(39,'Can delete soil_tabel',10,'delete_soil_tabel'),
(40,'Can view soil_tabel',10,'view_soil_tabel'),
(41,'Can add feedback_table',11,'add_feedback_table'),
(42,'Can change feedback_table',11,'change_feedback_table'),
(43,'Can delete feedback_table',11,'delete_feedback_table'),
(44,'Can view feedback_table',11,'view_feedback_table'),
(45,'Can add farmer_table',12,'add_farmer_table'),
(46,'Can change farmer_table',12,'change_farmer_table'),
(47,'Can delete farmer_table',12,'delete_farmer_table'),
(48,'Can view farmer_table',12,'view_farmer_table'),
(49,'Can add expert_table',13,'add_expert_table'),
(50,'Can change expert_table',13,'change_expert_table'),
(51,'Can delete expert_table',13,'delete_expert_table'),
(52,'Can view expert_table',13,'view_expert_table'),
(53,'Can add complaint_table',14,'add_complaint_table'),
(54,'Can change complaint_table',14,'change_complaint_table'),
(55,'Can delete complaint_table',14,'delete_complaint_table'),
(56,'Can view complaint_table',14,'view_complaint_table'),
(57,'Can add order_product',15,'add_order_product'),
(58,'Can change order_product',15,'change_order_product'),
(59,'Can delete order_product',15,'delete_order_product'),
(60,'Can view order_product',15,'view_order_product'),
(61,'Can add product_table',16,'add_product_table'),
(62,'Can change product_table',16,'change_product_table'),
(63,'Can delete product_table',16,'delete_product_table'),
(64,'Can view product_table',16,'view_product_table'),
(65,'Can add order_details',17,'add_order_details'),
(66,'Can change order_details',17,'change_order_details'),
(67,'Can delete order_details',17,'delete_order_details'),
(68,'Can view order_details',17,'view_order_details'),
(69,'Can add tips_table',18,'add_tips_table'),
(70,'Can change tips_table',18,'change_tips_table'),
(71,'Can delete tips_table',18,'delete_tips_table'),
(72,'Can view tips_table',18,'view_tips_table'),
(73,'Can add user_table',19,'add_user_table'),
(74,'Can change user_table',19,'change_user_table'),
(75,'Can delete user_table',19,'delete_user_table'),
(76,'Can view user_table',19,'view_user_table'),
(77,'Can add doubt_table',20,'add_doubt_table'),
(78,'Can change doubt_table',20,'change_doubt_table'),
(79,'Can delete doubt_table',20,'delete_doubt_table'),
(80,'Can view doubt_table',20,'view_doubt_table'),
(81,'Can add crop_table',21,'add_crop_table'),
(82,'Can change crop_table',21,'change_crop_table'),
(83,'Can delete crop_table',21,'delete_crop_table'),
(84,'Can view crop_table',21,'view_crop_table'),
(85,'Can add soil_table',10,'add_soil_table'),
(86,'Can change soil_table',10,'change_soil_table'),
(87,'Can delete soil_table',10,'delete_soil_table'),
(88,'Can view soil_table',10,'view_soil_table'),
(89,'Can add complaints',22,'add_complaints'),
(90,'Can change complaints',22,'change_complaints'),
(91,'Can delete complaints',22,'delete_complaints'),
(92,'Can view complaints',22,'view_complaints');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(14,'app','complaint_table'),
(22,'app','complaints'),
(21,'app','crop_table'),
(20,'app','doubt_table'),
(13,'app','expert_table'),
(12,'app','farmer_table'),
(11,'app','feedback_table'),
(7,'app','fertilizer_table'),
(8,'app','login_table'),
(9,'app','notification_table'),
(17,'app','order_details'),
(15,'app','order_product'),
(16,'app','product_table'),
(10,'app','soil_table'),
(18,'app','tips_table'),
(19,'app','user_table'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-08-17 06:45:44.532806'),
(2,'auth','0001_initial','2024-08-17 06:45:44.807360'),
(3,'admin','0001_initial','2024-08-17 06:45:44.870451'),
(4,'admin','0002_logentry_remove_auto_add','2024-08-17 06:45:44.886082'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-08-17 06:45:44.886082'),
(6,'app','0001_initial','2024-08-17 06:45:45.445590'),
(7,'contenttypes','0002_remove_content_type_name','2024-08-17 06:45:45.508488'),
(8,'auth','0002_alter_permission_name_max_length','2024-08-17 06:45:45.539736'),
(9,'auth','0003_alter_user_email_max_length','2024-08-17 06:45:45.555358'),
(10,'auth','0004_alter_user_username_opts','2024-08-17 06:45:45.570984'),
(11,'auth','0005_alter_user_last_login_null','2024-08-17 06:45:45.602225'),
(12,'auth','0006_require_contenttypes_0002','2024-08-17 06:45:45.602225'),
(13,'auth','0007_alter_validators_add_error_messages','2024-08-17 06:45:45.602225'),
(14,'auth','0008_alter_user_username_max_length','2024-08-17 06:45:45.633535'),
(15,'auth','0009_alter_user_last_name_max_length','2024-08-17 06:45:45.682816'),
(16,'auth','0010_alter_group_name_max_length','2024-08-17 06:45:45.697096'),
(17,'auth','0011_update_proxy_permissions','2024-08-17 06:45:45.697096'),
(18,'auth','0012_alter_user_first_name_max_length','2024-08-17 06:45:45.743965'),
(19,'sessions','0001_initial','2024-08-17 06:45:45.759590'),
(20,'app','0002_remove_expert_table_gender','2024-09-20 05:51:58.301705'),
(21,'app','0003_crop_table','2024-09-20 06:11:29.078582'),
(22,'app','0004_crop_table_price_crop_table_stock','2024-09-20 06:15:23.477086'),
(23,'app','0005_tips_table_details','2024-09-20 12:03:27.905834'),
(24,'app','0006_rename_soil_tabel_soil_table','2024-09-22 04:13:11.451084'),
(25,'app','0007_soil_table_expert_id','2024-09-22 04:20:19.263560'),
(26,'app','0008_complaints','2024-09-22 07:19:58.436574'),
(27,'app','0009_rename_login_complaints_user_id_and_more','2024-09-23 06:38:53.842207'),
(28,'app','0010_remove_order_product_farmer_id','2024-09-23 08:12:29.396976');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('cgv416ksab76hx4h0wx5khvkrgiff48s','eyJsaWQiOjEsImZpZCI6NX0:1st1lB:iGdCgl2QSPq_NtgbfvG8FO8hMCSsBzxfnwBApk_IFCM','2024-10-08 09:23:05.244636'),
('e6b10ist2c15gvk2e5sjquy7nuiibimv','eyJsaWQiOjF9:1ssgwH:0bs9h2iA_o19JQz-oOIMTVABx_Jzm34gMZl9P5ebfGU','2024-10-07 11:09:09.625491');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
