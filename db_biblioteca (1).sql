-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 10-Out-2024 às 19:41
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `db_biblioteca`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `emprestimos`
--

CREATE TABLE `emprestimos` (
  `CodEmprestimo` int(11) NOT NULL,
  `Data_Emprestimo` date DEFAULT NULL,
  `Data_Devolucao` date DEFAULT NULL,
  `CodLivro` int(11) DEFAULT NULL,
  `CodLeitor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `emprestimos`
--

INSERT INTO `emprestimos` (`CodEmprestimo`, `Data_Emprestimo`, `Data_Devolucao`, `CodLivro`, `CodLeitor`) VALUES
(1, '2024-03-10', '2024-03-20', 5, 1),
(2, '2024-03-03', '2024-03-23', 2, 4),
(3, '0000-00-00', '2024-03-10', 1, 2),
(4, '2024-04-05', '2024-04-15', 2, 3),
(5, '2024-04-10', '2024-03-25', 3, 1),
(6, '2024-04-21', '2024-05-01', 4, 2),
(7, '2024-05-09', '2024-05-19', 1, 2),
(8, '2024-05-02', '2024-05-12', 2, 3),
(9, '2024-06-23', '2024-07-03', 5, 4),
(10, '2024-07-08', '2024-07-18', 4, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `leitores`
--

CREATE TABLE `leitores` (
  `CodLeitor` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `DtNasc` date DEFAULT NULL,
  `Celular` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `RA` int(11) DEFAULT NULL,
  `Endereco` varchar(255) DEFAULT NULL,
  `NumEnd` varchar(255) DEFAULT NULL,
  `Bairro` varchar(255) DEFAULT NULL,
  `CidadeUF` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `leitores`
--

INSERT INTO `leitores` (`CodLeitor`, `Nome`, `DtNasc`, `Celular`, `Email`, `RA`, `Endereco`, `NumEnd`, `Bairro`, `CidadeUF`) VALUES
(1, 'João Silva Sauro', '2001-04-01', '(11)98788-2311', 'Joao@hotnail.com', 631113101, 'Rua Boa Esperança', '201', 'Janga', 'Paulista/PE'),
(2, 'Maria Silva Nascimento', '2011-07-21', '(11)98788-2311', 'maria@hotmail.com', 631113102, 'Rua de Vovó', '101', 'Maranguape I', 'Paulista/PE'),
(3, 'Gabriel', '2002-03-05', '81994638409', 'gabrielmendosan01@gmail.com', 1235, 'Rua Brigadeiro', '293', 'Ribeirinho', 'AL'),
(4, 'Flavia', '1999-07-30', '81963749304', 'Flavinha0310@gmail.com', 7808, 'Rua Castelo Branco', '98', 'Cabo Verde', 'PE'),
(5, 'Cauã Vital', '1999-10-10', '(81) 9928736492', 'cauavital08@gmail.com', 9273, 'Rua Cristalino', '029', 'lagoa preta', 'PE'),
(6, 'Vital', '1999-02-02', '(81) 0000-0000', 'vitalzin@gmai.com', 1235, 'Rua Vitalzin', '01', 'Paratibe', 'Paulista/PE'),
(7, 'Dudu', '1999-02-01', '(81) 0000-0000', 'vn@gmai.com', 17655, 'Rua NV Vitalzin', '01', 'Paratibe', 'Paulista/PE');

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros`
--

CREATE TABLE `livros` (
  `CodLivro` int(11) NOT NULL,
  `Titulo` varchar(255) DEFAULT NULL,
  `Autor` varchar(255) DEFAULT NULL,
  `Editora` varchar(255) DEFAULT NULL,
  `Sinopse` varchar(225) DEFAULT NULL,
  `AnoPublicacao` int(11) DEFAULT NULL,
  `Genero` varchar(225) DEFAULT NULL,
  `Paginas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `livros`
--

INSERT INTO `livros` (`CodLivro`, `Titulo`, `Autor`, `Editora`, `Sinopse`, `AnoPublicacao`, `Genero`, `Paginas`) VALUES
(1, 'O pequeno príncipe preto', 'Rodrigo França', 'Nova Fronteira', '', 2020, 'Literatura Infantil', 96),
(2, 'O Menino do Pijama Listrado', 'John Boyne', 'Seguinte', '', 2006, 'Guerra e Drama', 192),
(3, 'É assim que acaba', 'Colleen Hoover', 'Galera', '', 2016, 'Romance', 368),
(5, 'É assim que começa', 'Colleen Hoover', 'Galera', '', 2024, 'romance', 336),
(6, 'Os dois morrem no final', 'Adam Silvera', 'Intrínseca Ltda', '', 2021, 'ficcao', 335);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `emprestimos`
--
ALTER TABLE `emprestimos`
  ADD PRIMARY KEY (`CodEmprestimo`),
  ADD KEY `CodLivro` (`CodLivro`),
  ADD KEY `CodLeitor` (`CodLeitor`);

--
-- Índices para tabela `leitores`
--
ALTER TABLE `leitores`
  ADD PRIMARY KEY (`CodLeitor`);

--
-- Índices para tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`CodLivro`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `emprestimos`
--
ALTER TABLE `emprestimos`
  MODIFY `CodEmprestimo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `leitores`
--
ALTER TABLE `leitores`
  MODIFY `CodLeitor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `CodLivro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `emprestimos`
--
ALTER TABLE `emprestimos`
  ADD CONSTRAINT `emprestimos_ibfk_1` FOREIGN KEY (`CodLeitor`) REFERENCES `leitores` (`CodLeitor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
