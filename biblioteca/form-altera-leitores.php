<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alterar/Excluir Cadastro de Leitores</title>
  <link rel="stylesheet" href="style-altera.css">
</head>
<body>
  <header>
            <h1>Cadastro Dos Leitores</h1>
     
       
  </header>
  <h3>Alterar/Excluir</h3>
  <div class="container">
    
    
    <?php
include "config.php";

$codleitor = isset($_POST['codleitor'])? (int)$_POST['codleitor'] : null;

if ($codleitor > 0) {
    $sql ="select * from leitores where CodLeitor=$codleitor";
    $resultado = mysqli_query($conn,$sql) or die ("Não foi possível realizar a consulta");

    $linha = mysqli_fetch_array($resultado);

    if (!$linha) {
        die("Registro não encontrado.");
    }
};
?>
        
        
        <form action="altera-leitor.php" method="post">
        <div>
        <label for="codleitor">Código:</label></br>
        <input type="text" id="codleitor" name="codleitor" readonly value="<?php 
                    echo isset($linha['CodLeitor']) ? htmlspecialchars($linha['CodLeitor']) : '' ?>" required />
      </div>
        <div>
        <label for="nome">Nome:</label></br>
        <input type="text" id="nome" name="nome" value="<?php 
                    echo isset($linha['Nome']) ? htmlspecialchars($linha['Nome']) : '' ?>" required />
      </div>
      <div>
        <label for="dtnasc">Data de Nascimento:</label></br>
        <input type="date" id="dtnasc" name="dtnasc" value="<?php echo isset($linha['DtNasc']) ? htmlspecialchars($linha['DtNasc']) : ''; ?>" required />
      </div>
      <div>
        <label for="celular">Celular:</label></br>
        <input type="tel" id="celular" name="celular" value="<?php echo isset($linha['Celular']) ? htmlspecialchars($linha['Celular']) : ''; ?>" required />
      </div>
      <div>
        <label for="email">E-mail:</label></br>
        <input type="email" id="email" name="email" value="<?php echo isset($linha['Email']) ? htmlspecialchars($linha['Email']) : ''; ?>" required />
      </div>
      <div>
        <label for="ra">RA:</label></br>
        <input type="ra" id="ra" name="ra" value="<?php echo isset($linha['RA']) ? htmlspecialchars($linha['RA']) : ''; ?>" required />
      </div>
      <div>
        <label for="endereco">Endereço:</label></br>
        <input type="text" id="endereco" name="endereco" value="<?php echo isset($linha['Endereco']) ? htmlspecialchars($linha['Endereco']) : ''; ?>" required />
      </div>
      <div>
        <label for="num_end">Número:</label></br>
        <input type="number" id="num_end" name="num_end" value="<?php echo isset($linha['NumEnd']) ? htmlspecialchars($linha['NumEnd']) : ''; ?>" required />
      </div>
      <div>
        <label for="bairro">Bairro:</label></br>
        <input type="text" id="bairro" name="bairro" value="<?php echo isset($linha['Bairro']) ? htmlspecialchars($linha['Bairro']) : ''; ?>" required />
      </div>
      <div>
        <label for="cidade">Cidade:</label></br>
        <input type="text" id="cidade" name="cidade" value="<?php echo isset($linha['CidadeUF']) ? htmlspecialchars($linha['CidadeUF']) : ''; ?>" required />
      </div>
      <div>
        <button type="submit">Atualizar</button>
        <button type="button" onclick="excluirLeitor()">Excluir</button>
      </div>
    </form>
    
  </div>

<a href="listar-leitores.php"><button title="Voltar ao início">Voltar</button></a>

  <script>
    function excluirLeitor() {
      if (confirm('Tem certeza que deseja excluir este cadastro?')) {
        // Aqui você pode adicionar a lógica para excluir o leitor, talvez redirecionando para uma página PHP
        window.location.href = 'exclui-leitor.php?codleitor=' + document.getElementById('codleitor').value;
      }
    }
  </script>
</body>
</html>