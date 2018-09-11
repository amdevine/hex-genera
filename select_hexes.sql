SELECT *

FROM taxon

WHERE 
    length(replace(canonicalName, ' ', '')) in (3, 6)
    AND substr(canonicalName, 1, 1) in ('A', 'B', 'C', 'D', 'E', 'F')
