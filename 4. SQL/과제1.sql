USE HW1;
-- 2.     tCity의 모든 값들을 확인하세요
select * from tCity;
-- 3.     tStaff의 모든 값들을 확인하세요.
select * from tStaff;
-- 4.     tCity의 도시 이름과 인구에 대한 정보를 확인하세요.
select name, popu from tCity;

show columns from tCity where field in ("name", "popu");
-- 5.     tCity의 도시이름, 지역, 면적에 대한 정보를 확인하세요.
select name, region, area from tCity;
-- 6.     tStaff의 이름과 월급에 대한 정보를 확인하세요.
select name, salary from tStaff;
-- 7.     직원테이블에서 이름, 부서, 직급만 출력하세요.
select name, depart, grade from tStaff;
-- 8.     도시테이블에서 도시명, 면접(제곱km) 인구(만명)으로 이름이 보이도록 출력하세요.
select name as '도시명', area as '면적(제곱km)', popu as '인구(만명)' from tCity;
-- 9.     도시테이블에서 name, popu 값에 10000을 곱해서 인구(명)으로 이름이 보이도록 출력하세요.
select name, popu*10000 as '인구(명)' from tCity;
-- 10.  도시테이블에서 이름, 면적, 인구와 인구밀도라는 이름으로 (기존의 popu * 10000 / area 로 계산이 되는)것을 보고 나타내도록 하세요.
select name as '이름', area as '면적', popu as '인구', popu * 10000 / area as '인구밀도' from tCity;
-- 11.  도시테이블에서 면적이 1000제곱키로미터 이상인 도시만 출력하세요
select * from tCity where area >= 1000;
-- 12.  도시테이블에서 면적이 1000재곱키로미터 이상인 도시의 이름과 면적을 출력하세요.
select name, area from tCity where area >= 1000;
-- 13.  인구가 10만명 미만의 도시의 이름을 출력하세요.
select name from tCity where popu < 10;
-- 14.  전라도에 있는 도시의 정보를 출력하세요
select * from tCity where region = '전라';
-- 15.  월급이 400만원 이상인 직원의 이름을 출력하세요
select name from tStaff where salary >= 400;
-- 16.  스탭의 테이블에서 SCORE의 값이 NULL인 정보를 출력하세요
select * from tStaff where score is null;
-- 17.  스탭의 테이블에서 SCORE의 값이 있는 사람들의 정보를 출력하세요.
select * from tStaff where score is not null;
-- 18.  도시테이블에서 인구가 100만이상이면서, 면적이 700제곱키로 이상인 도시를 찾아보세요
select * from tCity where popu >= 100 and area >=700;
-- 19.  도시테이블에서 경기권 도시 중에서 인구가 50만명 이상이거나 또는 경기원이 아니고 인구가 50만보다 적더라도 면적이 500이상인 도시를 찾아보세요.
select * from tCity where (region = '경기' and popu >=50) | (region != '경기' and area>=500);
-- 20.  직원 목록에서 월급이 300미만이면서 성취도는 60 이상인 직원이 누구인지 찾아보세요
select * from tStaff where salary<300 and score>=60;
-- 21.  영업무의 여직원 분들의 이름을 찾아보세요
select name from tStaff where depart='영업부' and gender='여';
-- 22.  도시 이름에 ‘천’이 들어가는 도시들을 찾아보세요.
select * from tCity where name like '%천%';
-- 23.  직원 목록에서 성이 “정”씨인 사람들을 찾아보세요
select * from tStaff where name like '정%';
-- 24.  이름에 “신”자가 포함된 직원을 찾아보세요.
select * from tStaff where name like '%신%';
-- 25.  인구가 50~100만 사이인 도시를 찾아보세요.
select * from tCity where popu between 50 and 100;
-- 26.  직원들 중에서 입사일이 2015년부터 2018년 사이의 분들을 찾아보세요
select * from tStaff where joindate between '2015-01-01' and '2018-12-31';
-- 27.  면적인 50~1000사이의 도시의 목록을 조사하세요
select * from tCity where area between 50 and 1000;
-- 28.  월급이 200만원대의 직원들을 조사하세요.
select * from tStaff where salary between 200 and 299;
-- 29.  지역이 경상/전라인 모든 도시를 찾아보세요.
select * from tCity where region regexp '경상|전라';
-- 30.  인구가 적은 도시부터 출력하세요.
select * from tCity order by popu;
-- 31.  지역, 도시이름, 면적, 인구에 대한 것을 지역과 도시 이름에 대해서 정렬해보세요.
select region, name, area, popu from tCity order by region, name;
-- 32.  면적에 의해서 도시들의 정보들을 정렬해보세요.
select * from tCity order by area;
-- 33.  도시이름을 인구수에 따라서 도시의 이름만 출력해보세요.
select name from tCity order by popu;
-- 34.  경기도에 있는 도시만 골라서 면적별로 그 도시의 정보들을 출력해보세요.
select * from tCity where region like '경기' order by area;
-- 35.  직원 목록을 월급이 적은 사람부터 순서대로 출력하되, 월급이 같다면 성취도가 높은 사람을 먼저 출력하세요.
select * from tStaff order by salary, score desc;
-- 36.  영업부 직원을 먼저 입사한 순서대로 정렬하세요.
select * from tStaff where depart like '영업부' order by joindate;