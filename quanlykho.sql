-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (arm64)
--
-- Host: 127.0.0.1    Database: quanlykho
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(45) DEFAULT NULL,
  `hasBeenDeleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (1,'phu kien',NULL),(2,'linh kien',NULL),(3,'123','1');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InventoryHistory`
--

DROP TABLE IF EXISTS `InventoryHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `InventoryHistory` (
  `_historyId` int NOT NULL,
  `_productId` int DEFAULT NULL,
  `quantityChange` int DEFAULT NULL,
  `changeDate` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`_historyId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InventoryHistory`
--

LOCK TABLES `InventoryHistory` WRITE;
/*!40000 ALTER TABLE `InventoryHistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `InventoryHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Invoice`
--

DROP TABLE IF EXISTS `Invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Invoice` (
  `_invoiceId` int NOT NULL AUTO_INCREMENT,
  `_userId` varchar(45) DEFAULT NULL,
  `_orderDetailId` varchar(45) DEFAULT NULL,
  `toalCost` int DEFAULT NULL,
  PRIMARY KEY (`_invoiceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Invoice`
--

LOCK TABLES `Invoice` WRITE;
/*!40000 ALTER TABLE `Invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `Invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderDetails`
--

DROP TABLE IF EXISTS `OrderDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OrderDetails` (
  `_orderDetailId` int NOT NULL AUTO_INCREMENT,
  `orderId` int DEFAULT NULL,
  `productId` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`_orderDetailId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderDetails`
--

LOCK TABLES `OrderDetails` WRITE;
/*!40000 ALTER TABLE `OrderDetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `OrderDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `orderId` int NOT NULL AUTO_INCREMENT,
  `productId` varchar(45) DEFAULT NULL,
  `quantityProduct` int DEFAULT NULL,
  `customerName` varchar(45) DEFAULT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `address` longtext,
  `orderDate` varchar(45) DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`orderId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (1,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','2024-1-10',0),(2,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','2024-1-10',0),(3,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','10 01 2024',0),(4,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','13:32:42,10-01-2024',0),(5,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','13:32 ,10-01-2024',0),(6,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','13:34 ,10-01-2024',0),(7,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','13:39 ,10-01-2024',0),(8,'11',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','13:39 ,10-01-2024',0),(9,'10',1,'Nguyễn Văn Trọng','0902295556','Số 8 -Tổ 8 - Khu Xuân Mai','13:44 ,10-01-2024',0);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Products` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `productId` varchar(45) DEFAULT NULL,
  `supplierId` varchar(45) DEFAULT NULL,
  `productName` varchar(45) DEFAULT NULL,
  `categoryId` varchar(45) DEFAULT NULL,
  `brand` varchar(45) DEFAULT NULL,
  `serial` varchar(45) DEFAULT NULL,
  `description` longtext,
  `quantity` int DEFAULT NULL,
  `unitPrice` double DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `hasBeenDeleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES (2,'21212','12122','j','ji','n','n','nj',0,21,'1','0'),(3,'10','1234','acer nitro','laptop','acer','09dsa','lap',0,90000,'1','1'),(4,'4','1234','dell 7435','laptop','dell','867847','laptop dell 7425',1,100000,'1','0'),(5,'5','ccmax','asus Q410','laptop','asus','1234567','laptop asus Q410',5,120000,'1','0'),(6,'6','ccmax','asus Q420','laptop','asus','1234462','laptop asus Q420',3,150000,'1','0'),(7,'7','ccmax','dell 5430','laptop','dell','942094','laptop dell 5430',10,190000,'1','0'),(8,'8','ccmax','acer helios 300','laptop','acer','9432j84','laptop acer helios 300',5,250000,'1','0'),(9,'9','ccmax','acer nitro 7','laptop','acer','9329432','laptop acer nitro 7',4,70000,'1','0'),(10,'11','ccmax','ram ddr4 3200mhz ss','ram','samsung','94938954','ram ddr4 3200mhz samsung',8,10000,'1','0');
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suppliers`
--

DROP TABLE IF EXISTS `Suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Suppliers` (
  `_supplierId` int NOT NULL AUTO_INCREMENT,
  `supplierName` varchar(45) DEFAULT NULL,
  `contactEmail` varchar(45) DEFAULT NULL,
  `contactPhone` varchar(45) DEFAULT NULL,
  `hasBeenDeleted` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`_supplierId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suppliers`
--

LOCK TABLES `Suppliers` WRITE;
/*!40000 ALTER TABLE `Suppliers` DISABLE KEYS */;
INSERT INTO `Suppliers` VALUES (1,'potato','potato303@gmail.com','0942250643','1');
/*!40000 ALTER TABLE `Suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) DEFAULT NULL,
  `userPassword` varchar(45) DEFAULT NULL,
  `userRole` int DEFAULT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `userName` (`userName`),
  UNIQUE KEY `userPassword` (`userPassword`),
  KEY `ix_User_userId` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'potato','cG90YXRv',1);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `_userId` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `role` int DEFAULT NULL,
  PRIMARY KEY (`_userId`),
  UNIQUE KEY `username_UNIQUE` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-10 14:37:25
