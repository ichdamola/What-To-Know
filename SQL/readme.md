##How do I find duplicates across multiple columns?

```
select h.id, t.* 
from hr_employee h
join (
    select name_related, employee_no, count(*) as numer_of_occurences
    from hr_employee
    group by name_related, employee_no 
    having count(*) > 1
) t on h.name_related = t.name_related and h.employee_no = t.employee_no
```