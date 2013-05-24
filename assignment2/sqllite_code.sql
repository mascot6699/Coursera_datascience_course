select count(*) from frequency where docid = "10398_txt_earn";

select count(term) from frequency where docid ="10398_txt_earn" and count =1;

select count(*) from (select term from frequency where docid = "10398_txt_earn" and count = 1 union select term from frequency where docid = "925_txt_trade" and count = 1);

select count(*) from frequency where term = "parliament";

select count(*) from (select docid , sum(count) from frequency group by docid having sum(count) > 300);

create view v2 as select * from frequency where term = "transactions";
create view v1 as select * from frequency where term = "world";
select count(*) from (select * from v1 intersect select * from v2);

create view multab as select A.row_num , B.col_num , sum(A.value*B.value) as val from A , B where A.col_num = B.row_num group by A.row_num , B.col_num;
select val from multab where row_num =2 and col_num =3;

create view v11 as select * from frequency where docid="10080_txt_crude" or docid="17035_txt_earn";
create view v11t as select docid as term, term as docid,count from v11;
create view simtab as select v11.docid , v11t.term , sum(v11.count*v11t.count) as val from v11 , v11t where v11.term = v11t.docid group by v11.docid , v11t.term;

create view ans1 as select docid , sum(count) as oo from frequency where term ="washington" or term = "taxes" or term ="treasury" group by docid order by sum(count);
select max(oo) from ans1;
