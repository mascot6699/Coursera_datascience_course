select count(*) from frequency where docid = "10398_txt_earn";

select count(term) from frequency where docid ="10398_txt_earn" and count =1;

select count(*) from (select term from frequency where docid = "10398_txt_earn" and count = 1 union select term from frequency where docid = "925_txt_trade" and count = 1);

select count(*) from frequency where term = "parliament";

select count(*) from (select docid , sum(count) from frequency group by docid having sum(count) > 300);

create view v2 as select * from frequency where term = "transactions";
create view v1 as select * from frequency where term = "world";
select count(*) from (select * from v1 intersect select * from v2);

