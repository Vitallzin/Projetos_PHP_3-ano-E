<!DOCTYPE html>
<html>
<head>
    <title>Agenda de Contatos</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        
            
            <h1 class="text-center">Leitores Cadastrados</h1>
       
    </header>
   <main>
   <div class="container">
       <div class="box">
            <?php
                include "config.php";

                $sql = "SELECT * FROM leitores";
                $result = mysqli_query($conn, $sql);

                if ($result->num_rows > 0) {
                    while ($linha = mysqli_fetch_assoc($result)) {
                        echo $linha['CodLeitor']. " - ". $linha['Nome']. "<br>";
                    }
                } else {
                    echo "0 resultados";
                }
            ?>
    
                <form method="post" action="form-altera-leitores.php">
                    <table border="0">
                        <tr>
                            <td bgcolor="#cccccc" class="myinputstyle" size="3">Código:</td>
                            <td bgcolor="#EBEBEB">
                                <input type="text" name="codleitor" size="3" class="myinputstyle"
                                    title="Digite código do contato" required onchange="this.value = this.value.trim()"> &nbsp;
                                <button type="submit" name="alterar_contato">Alterar Contato</button>
                            </td>
                        </tr>
                    </table>
                </form>
        </div>    
   </div>            <a href="index.html"><button title="Voltar ao início">Voltar</button></a>
   </main>
</body>
</html>