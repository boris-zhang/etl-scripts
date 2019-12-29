
CREATE TABLE `core`.`question_baseinfo_crawler` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '题目标识',
  `question_stem` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '题干',
  `question_options` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '选',
  `answer` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '答案',
  `analysis` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '解析',
  `difficulty` decimal(5,4) DEFAULT NULL COMMENT '难度',
  `image_filename` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图片目录',
  `question_type_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,

  `textbook_id` int(11) NOT NULL COMMENT '教材标识',
  `textbook_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '目录名称',
  `textbook_version_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '教材版本名称',
  `grade_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '年级名称',
  `volume_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '版本号',

  `unit_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '单元标识',
  `unit_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '单元名称',
  `knowledge_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '知识点标识',
  `knowledge_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '知识点名称',
  `super_knowledge_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '上级知识点标识',
  `super_knowledge_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '上级知识点名称',
  `subject_type` varchar(20) DEFAULT NULL COMMENT '科目类型',

  `file_id` int(11) NOT NULL COMMENT '文件标识',
  `file_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '文件名称',
  `row_no` int(11) NOT NULL COMMENT '行号',
  `path_image_loaded` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图像文件路径',
  `source_type` varchar(255) DEFAULT NULL COMMENT '来源类型',
  `url` varchar(255) DEFAULT NULL COMMENT 'url地址',
  `load_time` timestamp NULL DEFAULT NULL COMMENT '加载时间',
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into core.question_baseinfo_crawler(
  question_stem
  ,question_options
  ,answer
  ,analysis
  ,difficulty
  ,image_filename
  ,question_type_name
  ,textbook_id
  ,textbook_name
  ,textbook_version_name
  ,grade_name
  ,volume_name
  ,unit_id
  ,unit_name
  ,knowledge_id
  ,knowledge_name
  ,super_knowledge_id
  ,super_knowledge_name
  ,subject_type
  ,file_id
  ,file_name
  ,row_no
  ,path_image_loaded
  ,source_type
  ,url
  ,load_time
)
select
  t1.question_stem
  ,t1.question_options
  ,t1.answer
  ,t1.analysis
  ,t1.difficulty
  ,t1.image_filename
  ,t2.question_type_name
  ,t3.textbook_id
  ,t3.textbook_name
  ,t3.textbook_version_name
  ,t3.grade_name
  ,t3.volume_name
  ,t2.unit_id
  ,t2.unit_name
  ,t2.knowledge_id
  ,t2.knowledge_name
  ,t2.super_knowledge_id
  ,t2.super_knowledge_name
  ,t3.subject_type
  ,t1.file_id
  ,t2.file_name
  ,t1.row_no
  ,t3.path_image_loaded
  ,'website网'
  ,t1.url
  ,current_time
from staging.question_stem t1
inner join staging.question_unit_klpoint_type t2 on t1.file_id=t2.file_id
inner join staging.question_textbook t3 on t3.textbook_id=t2.textbook_id
where t3.textbook_id>=43
order by t1.file_id,t1.row_no
;

select textbook_name,count(*)
from core.question_baseinfo_crawler
group by textbook_name
order by textbook_name