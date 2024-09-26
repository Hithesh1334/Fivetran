select 
"Sex",
"Age Years",
Count(*) as record_count,
SUM("Total deaths") as total_deaths,
Min("Start Date") as first_record_date,
Max("End Date") as last_recorde_date
from 
{{source("source_2","TRANSFORMRAW")}}
group by
"Sex","Age Years"
order by 
"Sex",
"Age Years"
