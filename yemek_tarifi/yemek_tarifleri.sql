-- MySQL dump 10.13  Distrib 9.3.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: yemek_tarifleri
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `kitaplar`
--

DROP TABLE IF EXISTS `kitaplar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kitaplar` (
  `kitap_id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(100) NOT NULL,
  `yazar` varchar(100) NOT NULL,
  `durum` enum('müsait','ödünç') DEFAULT 'müsait',
  PRIMARY KEY (`kitap_id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kitaplar`
--

LOCK TABLES `kitaplar` WRITE;
/*!40000 ALTER TABLE `kitaplar` DISABLE KEYS */;
INSERT INTO `kitaplar` VALUES (1,'Fikralar','also','müsait'),(2,'Fikralar','also','müsait'),(3,'deneme','deneme','ödünç'),(4,'Sefiller','Victor Hugo','müsait'),(5,'Suç ve Ceza','Fyodor Dostoyevski','ödünç'),(6,'Yüzyıllık Yalnızlık','Gabriel Garcia Marquez','müsait'),(7,'1984','George Orwell','ödünç'),(8,'Hayvan Çiftliği','George Orwell','müsait'),(9,'Küçük Prens','Antoine de Saint-Exupéry','müsait'),(10,'Simyacı','Paulo Coelho','ödünç'),(11,'Beyaz Diş','Jack London','müsait'),(12,'Martin Eden','Jack London','ödünç'),(13,'Anna Karenina','Lev Tolstoy','müsait'),(14,'Savaş ve Barış','Lev Tolstoy','ödünç'),(15,'Fahrenheit 451','Ray Bradbury','müsait'),(16,'Cesur Yeni Dünya','Aldous Huxley','ödünç'),(17,'Dava','Franz Kafka','müsait'),(18,'Dönüşüm','Franz Kafka','ödünç'),(19,'Bilinmeyen Bir Kadının Mektubu','Stefan Zweig','müsait'),(20,'Satranç','Stefan Zweig','ödünç'),(21,'Kürk Mantolu Madonna','Sabahattin Ali','müsait'),(22,'İçimizdeki Şeytan','Sabahattin Ali','ödünç'),(23,'Çalıkuşu','Reşat Nuri Güntekin','müsait'),(24,'Yaprak Dökümü','Reşat Nuri Güntekin','ödünç'),(25,'Aşk-ı Memnu','Halit Ziya Uşaklıgil','müsait'),(26,'Mai ve Siyah','Halit Ziya Uşaklıgil','ödünç'),(27,'Dokuzuncu Hariciye Koğuşu','Peyami Safa','müsait'),(28,'Yalnızız','Peyami Safa','ödünç'),(29,'Otomatik Portakal','Anthony Burgess','müsait'),(30,'Uçurtma Avcısı','Khaled Hosseini','ödünç'),(31,'Bin Muhteşem Güneş','Khaled Hosseini','müsait'),(32,'Alacakaranlık','Stephenie Meyer','ödünç'),(33,'Açlık Oyunları','Suzanne Collins','müsait'),(34,'Divergent','Veronica Roth','ödünç'),(35,'Harry Potter ve Felsefe Taşı','J.K. Rowling','müsait'),(36,'Yüzüklerin Efendisi: Yüzük Kardeşliği','J.R.R. Tolkien','ödünç'),(37,'Hobbit','J.R.R. Tolkien','müsait'),(38,'Dune','Frank Herbert','ödünç'),(39,'Zaman Makinesi','H.G. Wells','müsait'),(40,'Görünmez Adam','H.G. Wells','ödünç'),(41,'Frankenstein','Mary Shelley','müsait'),(42,'Dracula','Bram Stoker','ödünç'),(43,'Gurur ve Önyargı','Jane Austen','müsait'),(44,'Aşk ve Gurur','Jane Austen','ödünç'),(45,'Jane Eyre','Charlotte Brontë','müsait'),(46,'Uğultulu Tepeler','Emily Brontë','ödünç'),(47,'Moby Dick','Herman Melville','müsait'),(48,'Bülbülü Öldürmek','Harper Lee','ödünç'),(49,'Gazap Üzümleri','John Steinbeck','müsait'),(50,'Fareler ve İnsanlar','John Steinbeck','ödünç'),(51,'Şeker Portakalı','José Mauro de Vasconcelos','müsait'),(52,'Karamazov Kardeşler','Fyodor Dostoyevski','ödünç'),(53,'Budala','Fyodor Dostoyevski','müsait'),(54,'Yüzüklerin Efendisi: Yüzük Kardeşliği','J.R.R. Tolkien','müsait'),(55,'Yüzüklerin Efendisi: İki Kule','J.R.R. Tolkien','ödünç'),(56,'Yüzüklerin Efendisi: Kralın Dönüşü','J.R.R. Tolkien','müsait'),(57,'Harry Potter ve Felsefe Taşı','J.K. Rowling','ödünç'),(58,'Harry Potter ve Sırlar Odası','J.K. Rowling','müsait'),(59,'Harry Potter ve Azkaban Tutsağı','J.K. Rowling','müsait'),(60,'Harry Potter ve Ateş Kadehi','J.K. Rowling','ödünç'),(61,'Harry Potter ve Zümrüdüanka Yoldaşlığı','J.K. Rowling','müsait'),(62,'Harry Potter ve Melez Prens','J.K. Rowling','ödünç'),(63,'Harry Potter ve Ölüm Yadigarları','J.K. Rowling','müsait'),(64,'Otostopçunun Galaksi Rehberi','Douglas Adams','müsait'),(65,'Solgun Mavi Nokta','Carl Sagan','ödünç'),(66,'Sineklerin Tanrısı','William Golding','müsait'),(67,'1984','George Orwell','ödünç'),(68,'Hayvan Çiftliği','George Orwell','müsait'),(69,'Cesur Yeni Dünya','Aldous Huxley','müsait'),(70,'Dönüşüm','Franz Kafka','ödünç'),(71,'Suç ve Ceza','Fyodor Dostoyevski','müsait'),(72,'Gurur ve Önyargı','Jane Austen','müsait'),(73,'Küçük Prens','Antoine de Saint-Exupéry','ödünç'),(74,'Zehranın Kitabı','Zehra','müsait');
/*!40000 ALTER TABLE `kitaplar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ratings`
--

DROP TABLE IF EXISTS `ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ratings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recipe_id` int DEFAULT NULL,
  `rating` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_id` (`recipe_id`),
  CONSTRAINT `ratings_ibfk_1` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratings`
--

LOCK TABLES `ratings` WRITE;
/*!40000 ALTER TABLE `ratings` DISABLE KEYS */;
INSERT INTO `ratings` VALUES (1,63,5),(2,63,5),(3,63,4);
/*!40000 ALTER TABLE `ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `ingredients` text NOT NULL,
  `content` text NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `recipes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (50,'Karnıyarık','Patlıcan, kıyma, soğan, biber, domates, yağ','Patlıcanları kızartın. Kıymalı harcı hazırlayıp içine doldurun. Fırında pişirin.',1),(51,'Mercimek Çorbası','Kırmızı mercimek, soğan, havuç, patates, yağ, tuz','Sebzeleri kavurup mercimekleri ekleyin. Haşlayın ve blendırdan geçirin.',1),(52,'Menemen','Yumurta, domates, biber, yağ, tuz','Domates ve biberi kavurun, yumurtaları kırıp karıştırın.',1),(53,'İmam Bayıldı','Patlıcan, soğan, sarımsak, domates, zeytinyağı','Patlıcanları kızartıp iç harcını doldurun. Fırında pişirin.',1),(54,'Tavuk Sote','Tavuk göğsü, biber, domates, soğan, yağ','Tüm malzemeleri doğrayıp soteyin.',1),(55,'Kuru Fasulye','Kuru fasulye, soğan, salça, tuz','Fasulyeleri haşlayın, salçalı soğanla birlikte pişirin.',1),(56,'Pilav','Pirinç, tereyağı, su, tuz','Pirinçleri kavurup su ekleyerek pişirin.',1),(57,'Makarna Napolitan','Makarna, domates sos, sarımsak, yağ','Makarnayı haşlayın. Sosu hazırlayıp üzerine dökün.',1),(58,'Sebzeli Kuskus','Kuskus, kabak, havuç, biber, yağ','Sebzeleri soteleyip haşlanmış kuskus ile karıştırın.',1),(59,'Yoğurtlu Kabak','Kabak, yoğurt, sarımsak, dereotu','Kabakları rendeleyip pişirin. Yoğurtla karıştırın.',1),(60,'Lahmacun','Kıyma, soğan, domates, maydanoz, un','Hamuru açıp kıymalı içi sürün. Fırında pişirin.',1),(61,'Mantı','Hamur, kıyma, yoğurt, sarımsak, tereyağı','Hamura iç harcı koyup kapatın. Haşlayın, soslayın.',1),(62,'Zeytinyağlı Yaprak Sarma','Asma yaprağı, pirinç, soğan, nane, zeytinyağı','İç harcı sarıp tencerede pişirin.',1),(63,'Bulgur Pilavı','Bulgur, biber, domates salçası, soğan','Soğanla salçayı kavurup bulguru ekleyin. Suyunu çekene kadar pişirin.',1),(64,'Taze Fasulye','Taze fasulye, domates, soğan, zeytinyağı','Malzemeleri tencerede pişirin.',1),(65,'Güveç','Et, patates, havuç, biber, soğan','Malzemeleri güveç kabına yerleştirip fırında pişirin.',1),(66,'Fırında Tavuk','Tavuk but, patates, biber, salça, yağ','Tüm malzemeleri tepsiye dizip fırında pişirin.',1),(67,'Çılbır','Yumurta, yoğurt, sarımsak, tereyağı, pul biber','Yumurtaları haşlayıp sarımsaklı yoğurtla servis edin.',1),(68,'Peynirli Börek','Yufka, beyaz peynir, maydanoz, yumurta','Yufkaları sarıp fırında pişirin.',1),(69,'Mücver','Kabak, yumurta, un, peynir, dereotu','Malzemeleri karıştırıp kızartın.',1),(70,'deneme','deneme','deneme',1),(71,'Spaghetti Carbonara','Spaghetti, yumurta, parmesan peyniri, pancetta, karabiber, tuz','Spaghettiyi haşlayın. Yumurtaları peynirle çırpın. Pancetta’yı kavurun, ardından spaghettiyi ekleyin. Yumurtalı karışımı ekleyip karıştırın.',1),(72,'Tacos al Pastor','Domuz eti, ananas, mısır tortilla, soğan, kişniş','Eti marine edin, şişe dizin ve pişirin. Küçük parçalara ayırın, tortilla ile servis edin.',1),(73,'Pad Thai','Pirinç eriştesi, karides, yumurta, tofu, tamarind sosu, yer fıstığı, lime','Erişteleri haşlayın. Karides ve tofu soteleyin. Yumurtayı kırın, sos ve erişteyi ekleyin. Yer fıstığı ve lime ile servis edin.',1),(74,'Sushi','Suşi pirinci, nori, çiğ balık, salatalık, avokado, wasabi','Pirinci haşlayın ve sirke ile karıştırın. Nori üzerine pirinci yayın, malzemeleri ekleyin ve sarın. Dilimleyin.',1),(75,'Beef Stroganoff','Dana eti, mantar, soğan, krema, hardal, makarna','Eti ve mantarı soteleyin. Soğan ekleyin. Krema ve hardalı ekleyip makarna ile servis edin.',1),(76,'Coq au Vin','Tavuk, kırmızı şarap, mantar, havuç, soğan, sarımsak','Tavuğu şarapta marine edin. Sebzelerle birlikte pişirin.',1),(77,'Chili con Carne','Kıyma, kırmızı fasulye, domates, biber, soğan, sarımsak, baharatlar','Tüm malzemeleri birlikte pişirin. Baharatlarla tatlandırın.',1),(78,'Bibimbap','Pirinç, çeşitli sebzeler, yumurta, gochujang, et','Sebzeleri soteleyin, pirinç üzerine dizin. Üstüne yumurta ve sos ekleyin.',1),(79,'Ceviche','Beyaz balık, lime suyu, soğan, kişniş, biber','Balığı lime suyunda marine edin. Sebzeleri ekleyip karıştırın.',1),(80,'Biryani','Pirinç, tavuk, yoğurt, safran, baharatlar','Tavuğu marine edin. Pirinci haşlayın. Kat kat dizip pişirin.',1),(81,'Pho','Et suyu, pirinç eriştesi, dana eti, anason, tarçın, zencefil, soğan','Et suyunu baharatlarla kaynatın. Erişte ve etle servis edin.',1),(82,'Moussaka','Patlıcan, kıyma, beşamel sos, soğan, domates, kaşar','Kat kat dizin, üzerine beşamel dökün, fırında pişirin.',1),(83,'Paella','Pirinç, tavuk, deniz ürünleri, safran, bezelye, biber','Tüm malzemeleri tek tavada pişirin.',1),(84,'Falafel','Nohut, soğan, sarımsak, maydanoz, baharatlar','Karışımı hazırlayın, köfte yapıp kızartın.',1),(85,'Shakshuka','Yumurta, domates, biber, soğan, sarımsak','Sebzeleri pişirin, yumurtaları kırıp pişirin.',1),(86,'Tiramisu','Mascarpone, kedi dili bisküvi, kahve, kakao, yumurta, şeker','Katmanları dizin, buzdolabında bekletin.',1),(87,'Gyoza','Hamur, kıyma, lahana, soğan, sarımsak, soya sosu','İç harcı doldurup kızartın ve buharda pişirin.',1),(88,'Tom Yum','Karides, mantar, limon otu, lime yaprağı, acı biber, hindistancevizi sütü','Malzemeleri kaynatıp servis edin.',1),(89,'Ratatouille','Kabak, patlıcan, domates, biber, zeytinyağı','Sebzeleri doğrayıp kat kat dizin, fırında pişirin.',1),(90,'Baklava','Yufka, ceviz, şerbet, tereyağı','Kat kat dizin, fırında pişirin, şerbet dökün.',1),(91,'Peking Duck','Ördek, baharatlar, ince lavaş, salatalık, hoisin sos','Ördeği marine edip pişirin, dilimleyip lavaşta servis edin.',1),(92,'Rendang','Sığır eti, hindistancevizi sütü, baharatlar','Eti sosla uzun süre pişirin.',1),(93,'Jollof Rice','Pirinç, domates, biber, soğan, tavuk','Malzemeleri birlikte pişirin.',1),(94,'Kimchi','Lahana, kırmızı biber, sarımsak, zencefil, tuz','Malzemeleri karıştırın, fermente edin.',1),(95,'Goulash','Dana eti, soğan, kırmızı biber, domates, patates','Tüm malzemeleri güveçte pişirin.',1),(96,'Pierogi','Un, patates, peynir, soğan, tuz','Hamura iç harç koyup haşlayın.',1),(97,'Arepa','Mısır unu, su, tuz, peynir, et','Hamuru yoğurup tavada pişirin, içini doldurun.',1),(98,'Shawarma','Tavuk, yoğurt, sarımsak, lavaş, baharatlar','Eti marine edin, pişirin, lavaşta servis edin.',1),(99,'Pav Bhaji','Patates, bezelye, biber, domates, soğan, tereyağı','Sebzeleri ezip baharatlarla pişirin, ekmekle servis edin.',1),(100,'Okonomiyaki','Lahana, yumurta, un, domuz eti, okonomiyaki sosu','Malzemeleri karıştırın, tavada pişirin, sosla servis edin.',1);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'zehra','1234');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-17 19:12:20
