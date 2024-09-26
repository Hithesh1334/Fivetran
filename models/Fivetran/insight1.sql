select "Age Years","Sex",
Sum("Total deaths") as total_deaths
from {{source("source_2","TRANSFORMRAW")}}
group by 
"Age Years","Sex"