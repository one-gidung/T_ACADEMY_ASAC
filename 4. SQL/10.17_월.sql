
# DB 종류들 확인
show databases;

# 지금 Database 내의 테이블에 대한 정보
use employees;
show table status;

# 간단하게 내가 사용하는 DB의 테이블이 뭐가 있냐 볼 때..
show tables;
# 주의!!) 자세히 볼때는 단순, 간단히가 복수!!

# 
select first_name as 이름, gender as 성별, hire_date "입사일" from employees.employees


# sqldb 생성시작 #
# 1. Database 생성 -> 기존에 DB가 있는지 없는지 체크
drop database if exists sqldb;
create database sqldb;

# 2. Table 만들기
use sqldb;
CREATE TABLE usertbl (
	userID CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디 PK
    name VARCHAR(10) NOT NULL, -- 이름
    birthYear INT NOT NULL,
    addr CHAR(2) NOT NULL, -- 지역(경기, 서울, 경남 이렇게 2글자만)
    mobile1 CHAR(3), -- 휴대폰 번호 국번(011, 016, 018, 010 etc)
    mobile2 CHAR(8), -- 휴대폰 뒤 8자리 번호(-제외)
    height SMALLINT, -- 키에 대한 정보
	mDate DATE -- 회원 가입일
);
SELECT * FROM usertbl;
# buy tbl 생성
-- CREATE TABLE buttbl (
-- 	num INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- PK
--     userID CHAR(8) NOT NULL, -- FK
--     prodName CHAR(6) NOT NULL,
--     price INT NOT NULL,
--     amount SMALLINT NOT NULL,
--     FOREIGN KEY
--     -- userID HCAR-- 
-- );


use employees;