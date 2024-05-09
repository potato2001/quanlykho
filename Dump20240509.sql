-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (arm64)
--
-- Host: localhost    Database: quanlykho
-- ------------------------------------------------------
-- Server version	8.3.0

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
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(45) DEFAULT NULL,
  `HasBeenDeleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (6,'Ha Noi','string');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `CustomerName` varchar(45) DEFAULT NULL,
  `CustomerAddress` varchar(45) DEFAULT NULL,
  `CustomerPhone` varchar(45) DEFAULT NULL,
  `CustomerEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'string','string','string','string');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inventory`
--

DROP TABLE IF EXISTS `Inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Inventory` (
  `InventoryID` int NOT NULL AUTO_INCREMENT,
  `QuantityAvailable` varchar(45) DEFAULT NULL,
  `Product_ProductID` int NOT NULL,
  `Invoice_InvoiceID` int NOT NULL,
  PRIMARY KEY (`InventoryID`,`Product_ProductID`,`Invoice_InvoiceID`),
  UNIQUE KEY `userName` (`QuantityAvailable`),
  KEY `ix_User_userId` (`InventoryID`),
  KEY `fk_Inventory_Product1_idx` (`Product_ProductID`),
  KEY `fk_Inventory_Invoice1_idx` (`Invoice_InvoiceID`),
  CONSTRAINT `fk_Inventory_Invoice1` FOREIGN KEY (`Invoice_InvoiceID`) REFERENCES `Invoice` (`InvoiceID`),
  CONSTRAINT `fk_Inventory_Product1` FOREIGN KEY (`Product_ProductID`) REFERENCES `Product` (`ProductID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventory`
--

LOCK TABLES `Inventory` WRITE;
/*!40000 ALTER TABLE `Inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `Inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InventoryHistory`
--

DROP TABLE IF EXISTS `InventoryHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `InventoryHistory` (
  `HistoryID` int NOT NULL,
  `QuantityChange` int DEFAULT NULL,
  `ChangeDate` varchar(45) DEFAULT NULL,
  `Inventory_InventoryID` int NOT NULL,
  PRIMARY KEY (`HistoryID`,`Inventory_InventoryID`),
  KEY `fk_InventoryHistory_Inventory1_idx` (`Inventory_InventoryID`),
  CONSTRAINT `fk_InventoryHistory_Inventory1` FOREIGN KEY (`Inventory_InventoryID`) REFERENCES `Inventory` (`InventoryID`)
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
  `InvoiceID` int NOT NULL AUTO_INCREMENT,
  `UserID` varchar(45) DEFAULT NULL,
  `ToalCost` int DEFAULT NULL,
  `OrderDetail_OrderDetailID` int NOT NULL,
  PRIMARY KEY (`InvoiceID`,`OrderDetail_OrderDetailID`),
  KEY `fk_Invoice_OrderDetail1_idx` (`OrderDetail_OrderDetailID`),
  CONSTRAINT `fk_Invoice_OrderDetail1` FOREIGN KEY (`OrderDetail_OrderDetailID`) REFERENCES `OrderDetail` (`OrderDetailID`)
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
-- Table structure for table `OrderDetail`
--

DROP TABLE IF EXISTS `OrderDetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OrderDetail` (
  `OrderDetailID` int NOT NULL AUTO_INCREMENT,
  `OrderDetailCode` varchar(45) DEFAULT NULL,
  `CustomerID` int NOT NULL,
  `ProductID` int NOT NULL,
  `OrderQuantity` int DEFAULT NULL,
  `OrderDate` varchar(45) DEFAULT NULL,
  `ReceivedDate` varchar(45) DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`OrderDetailID`,`CustomerID`,`ProductID`),
  KEY `fk_OrderDetail_Product1_idx` (`ProductID`),
  KEY `fk_OrderDetail_Customer1_idx` (`CustomerID`),
  CONSTRAINT `fk_OrderDetail_Customer1` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`CustomerID`),
  CONSTRAINT `fk_OrderDetail_Product1` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderDetail`
--

LOCK TABLES `OrderDetail` WRITE;
/*!40000 ALTER TABLE `OrderDetail` DISABLE KEYS */;
INSERT INTO `OrderDetail` VALUES (1,NULL,1,2,0,'string','string','0'),(2,NULL,1,2,0,'string','string','0'),(3,NULL,1,3,0,'string','string','0'),(4,NULL,1,2,0,'string','string','0'),(5,NULL,1,3,0,'string','string','0'),(6,NULL,1,2,1,'string','string','0'),(7,NULL,1,2,1,'string','string','0'),(8,NULL,1,3,5,'string','string','0'),(9,NULL,1,2,1,'string','string','0'),(10,NULL,1,3,6,'string','string','0'),(11,'Ma 1',1,2,1,'string','string','0'),(12,'Ma 1',1,3,2,'string','string','0'),(13,'Ma 2',1,2,1,'2024-05-09 13:41:34.012180','2024-05-09 13:50','1'),(14,'Ma 2',1,2,1,'2024-05-09 13:43','2024-05-09 13:50','1'),(15,'e1904db2-0988-443f-912e-b20e6a9e1695',1,2,1,'2024-05-09 13:44','2024-05-09 13:50','1'),(16,'ad4d0b45-5fb9-4dc3-9b78-244fbe785e45',1,2,4,'2024-05-09 14:18',NULL,'0'),(17,'7361f324-5653-4e13-8819-3151289acb38',1,3,5,'2024-05-09 14:18',NULL,'0'),(18,'91584dc8-5572-4bd1-b196-7a63674893fd',1,2,4,'2024-05-09 14:21',NULL,'0'),(19,'91584dc8-5572-4bd1-b196-7a63674893fd',1,3,5,'2024-05-09 14:21',NULL,'0'),(20,'8fd5908a-ed5a-421f-97b6-3fcb174eece4',1,2,4,'2024-05-09 14:21',NULL,'0'),(21,'8fd5908a-ed5a-421f-97b6-3fcb174eece4',1,3,5,'2024-05-09 14:21',NULL,'0');
/*!40000 ALTER TABLE `OrderDetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `ProductID` int NOT NULL AUTO_INCREMENT,
  `ProductCode` varchar(45) DEFAULT NULL,
  `ProductName` varchar(100) DEFAULT NULL,
  `ProductBrand` varchar(100) DEFAULT NULL,
  `ProductSerial` varchar(45) DEFAULT NULL,
  `ProductDescription` longtext NOT NULL,
  `UnitPrice` double DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  `HasBeenDeleted` varchar(10) DEFAULT NULL,
  `Category_CategoryID` int NOT NULL,
  `Provider_ProviderID` int NOT NULL,
  PRIMARY KEY (`ProductID`,`Category_CategoryID`,`Provider_ProviderID`),
  KEY `fk_Product_Category1_idx` (`Category_CategoryID`),
  KEY `fk_Product_Provider1_idx` (`Provider_ProviderID`),
  CONSTRAINT `fk_Product_Category1` FOREIGN KEY (`Category_CategoryID`) REFERENCES `Category` (`CategoryID`),
  CONSTRAINT `fk_Product_Provider1` FOREIGN KEY (`Provider_ProviderID`) REFERENCES `Provider` (`ProviderID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (2,NULL,'string','string','string','string',0,'string','0',6,2),(3,'string','string','string','string','string',0,'string','0',6,2);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Provider`
--

DROP TABLE IF EXISTS `Provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Provider` (
  `ProviderID` int NOT NULL AUTO_INCREMENT,
  `ProviderName` varchar(100) DEFAULT NULL,
  `ProviderAddress` varchar(200) DEFAULT NULL,
  `ProviderPhone` varchar(45) DEFAULT NULL,
  `ProviderEmail` varchar(45) DEFAULT NULL,
  `HasBeenDeleted` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ProviderID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Provider`
--

LOCK TABLES `Provider` WRITE;
/*!40000 ALTER TABLE `Provider` DISABLE KEYS */;
INSERT INTO `Provider` VALUES (2,'Trong','string','string','string','0');
/*!40000 ALTER TABLE `Provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `UserName` varchar(45) DEFAULT NULL,
  `UserPassword` varchar(45) DEFAULT NULL,
  `Role` int DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `username_UNIQUE` (`UserName`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-09 20:32:16
