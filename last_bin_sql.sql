-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 10, 2022 at 04:45 PM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `f6V3kVwxvH`
--

-- --------------------------------------------------------

--
-- Table structure for table `last_bin_sql`
--

CREATE TABLE `last_bin_sql` (
  `id` int(11) NOT NULL,
  `bot_name` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `last_bin` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `last_ssen` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `last_bin_sql`
--

INSERT INTO `last_bin_sql` (`id`, `bot_name`, `last_bin`, `last_ssen`) VALUES
(1, 'bot_one', '40001799', '09-02-2022'),
(2, 'bot_tow', '50005989', '24-11-2021');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `last_bin_sql`
--
ALTER TABLE `last_bin_sql`
  ADD KEY `id` (`id`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `last_bin_sql`
--
ALTER TABLE `last_bin_sql`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
