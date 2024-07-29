<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        h1{
            
            text-align: center;

        }
        h4{
            color: blueviolet;
            text-align: center;
            
        }
        table{
            border-collapse: collapse;
            font-size: 150%;
            
        }
        td{
            border: 1px solid black;
            font-size: 150%;
            
            
        }
        img{
            width: 300px;
            height: 250px;
        }
        tr{
            text-align: center;
        }

    </style>
</head>
<body>
    <?php
        echo"<h1>Top 10 Jogadores do Século XI</h1>";
        echo"<h4>(na minha humilde opnião)</h4>";
        echo"<table><tr>";
    
         for ($x = 1 ; $x <= 5; $x++ ){
            echo "<td> <img src='img/$x.jpg'></td>"; 
       
         }
        echo"</table></tr>";
        echo"<table><tr>";

        
        for ($x = 6 ; $x <= 10; $x++ ){
            echo "<td> <img src='img/$x.jpg'></td> ";  
        }
        echo"</tr></table>";
        
        

    ?>

    
</body>
</html>