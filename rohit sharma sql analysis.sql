create database rohit;
use rohit;



-- 1. execute below statements to know all the details of 48 century;
select * from century;



 -- CLIENT ASK 1."NO OF century by format";
 
 SELECT `century`.`Type of Match`,
 COUNT(`century`.`S.No.`)
 FROM CENTURY
 GROUP BY `century`.`Type of Match` 
 ORDER BY  COUNT(`century`.`S.No.`) ASC ;
 
 
 
 -- CLIENT ASK 2."NO OF century by  BATTING POSITION";
 
  SELECT `Position`,
 COUNT(`century`.`S.No.`)
 FROM CENTURY
 GROUP BY `Position` 
 ORDER BY  COUNT(`century`.`S.No.`) DESC ;
 


  -- CLIENT ASK 3."NO OF century by  MATCH RESULT";
 
  SELECT `Result`,
 COUNT(`century`.`S.No.`)
 FROM CENTURY
 GROUP BY `Result` 
 ORDER BY  COUNT(`century`.`S.No.`) DESC ;
 
 
 
 
  -- CLIENT ASK 4."NO OF century by  OPPONENT TEAM";
 
  SELECT `Against`,
 COUNT(`S.No.`)
 FROM CENTURY
 GROUP BY `Against` 
 ORDER BY  COUNT(`S.No.`) DESC ;


-- CLIENT ASK 5."NO OF century by CAPTAINCY";
 
  SELECT `Captain`,
 COUNT(`S.No.`)
 FROM CENTURY
 GROUP BY `Captain`
 ORDER BY  COUNT(`S.No.`) DESC ;
 
 
 -- CLIENT ASK 6."NO OF century by VENUE";
 
  SELECT `Venue` ,
 COUNT(`S.No.`)
 FROM CENTURY
 GROUP BY `Venue`
 ORDER BY  COUNT(`S.No.`) DESC ;
 
  SELECT `H/A/N`, 
 COUNT(`S.No.`)
 FROM CENTURY
 GROUP BY `H/A/N`
 ORDER BY  COUNT(`S.No.`) DESC ;
 
  -- CLIENT ASK 7."NO OF 199+ SCORES BY FORMAT";
 
  SELECT  `Type of Match`,
 COUNT(`S.No.`)
 FROM CENTURY 
 WHERE `Score`>199
 GROUP BY  `Type of Match`
 ORDER BY COUNT(`S.No.`) DESC ;
 SELECT SCORE ,VENUE, DATE,`Against` FROM CENTURY where SCORE>199; 
  
  
  
  
  -- CLIENT ASK 8."CENTURY BY STRIKE RATE BY FORMAT";
  
  
   SELECT  `Type of Match`, AVG(`Strike Rate`)
   FROM CENTURY 
   WHERE `Score`>99
   GROUP BY  `Type of Match`
   ORDER BY  AVG(`Strike Rate`);
   
   
-- CLIENT ASK 8. "CENTURY BY YEAR";
  
    select `year` , count(`S.No.`)
    from century
    group by year
    order by count(`S.No.`) desc;

    
-- client ask 9. "century by month";

   select `month` , count(`S.No.`)
    from century
    group by `month`
    order by count(`S.No.`) desc;
    
     -- client ask 10. max score against teams
    
     SELECT  `Against`,  max(SCORE)
     FROM CENTURY 
     group by `Against`
     order by max(score) desc;
    
     
     
   
    
	
   
   
   
  
  
