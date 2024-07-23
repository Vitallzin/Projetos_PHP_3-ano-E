<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      h1{
        color:blueviolet
      }
      p{
        color: red
      }
    </style>
</head>
<body>
    <h1>Sport filho do Santa</h1>

    <?php

      echo "Aqui aparece que o Santa é o pai do sport para nto usuário";// vai aparecer alguma frase par usuário
      echo"<h1> Balão</h1>";// echo/print serve para poder colocar as tags dentro de um PHP

      //Variáveis em PHP
      // Para criar, basta atribuir um valor a ela  
      $nome = "Grafite"; // Variáveis sempre começam em PHP com "$" e não é necessário indetificar o tipo do dado
      $idade = 45;
      $altura = 1.89;
      echo "$nome tem $altura m e $idade anos de idade"; 



      //Aritmética Básica
      echo "<p> Operadores Aritméticos.<p>";
      echo "<p> a = 10 e b = 5<br>  ";
      $a = 10;
      $b = 5;
      $c = $a + $b;
      echo $c;
      echo "<br>"; // para quebrar a linha
      $c = $a - $b;
      echo $c;
      echo "<br>";
      $c = $a * $b;
      echo $c;
      echo "<br>";
      $c = $a / $b;
      echo $c;
      echo "<br>";
      $c = $a % $b;
      echo $c;
      echo "<br>"; // para quebrar a linha


      
      
    
    ?>

    
</body>
</html>