# ************************************************************
# Sequel Pro SQL dump
# Version 5446
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 8.0.18)
# Database: staging
# Generation Time: 2019-12-22 03:44:56 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table question_stem
# ------------------------------------------------------------



DROP TABLE IF EXISTS `question_stem`;

CREATE TABLE `question_stem` (
  `file_id` int(11) NOT NULL COMMENT '文件标识',
  `row_no` int(11) NOT NULL COMMENT '行号',
  `question_stem` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '题干',
  `question_options` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '选项',
  `answer` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '答案',
  `analysis` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '解析',
  `difficulty` decimal(5,4) DEFAULT NULL COMMENT '难度',
  `image_filename` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图片目录',
  `url` varchar(255) DEFAULT NULL COMMENT 'url地址',
  `load_time` timestamp NULL DEFAULT NULL COMMENT '加载时间',
  PRIMARY KEY (`file_id`,`row_no`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table question_textbook
# ------------------------------------------------------------

DROP TABLE IF EXISTS `question_textbook`;

CREATE TABLE `question_textbook` (
  `path_image_loaded` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '目录路径',
  `textbook_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '目录名称',
  `textbook_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '教材标识',
  `textbook_version_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '教材版本名称',
  `grade_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '年级名称',
  `volume_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '版本号',
  `load_time` timestamp NULL DEFAULT NULL COMMENT '加载时间',
  PRIMARY KEY (`textbook_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table question_unit_klpoint_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `question_unit_klpoint_type`;

CREATE TABLE `question_unit_klpoint_type` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '文件名称标识',
  `file_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '文件名称',
  `textbook_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `unit_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '单元标识',
  `unit_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '单元名称',
  `knowledge_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '知识点标识',
  `knowledge_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '知识点名称',
  `super_knowledge_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '上级知识点标识',
  `super_knowledge_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '上级知识点名称',
  `question_type_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `load_time` timestamp NULL DEFAULT NULL COMMENT '加载时间',
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
