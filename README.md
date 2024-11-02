# Solution d'Assistance Financière avec IA Générative - Datathon 2024: FinSight AI ou Geppetto

## 1. Conception Générale

Développement d'un assistant financier basé sur l'IA, conçu pour :
   - Résumés automatiques de rapports financiers
   - Analyse de sentiment sur sections spécifiques (ex : lettre aux actionnaires)
   - Surveillance des indicateurs financiers pour détecter des anomalies
   - Analyses prédictives pour les projections financières
   - Visualisation des KPI extraits et autres analyses
   - Comparaison multi-rapports (ex: entre années ou entreprises)

## 2. Détails de la Solution

### Module 1 : Collecte et Intégration de Données
   - **Sources de données** : Intégration de YahooFinance, MorningStar, FRED et des rapports annuels fournis.
   - **Pipeline de Traitement de Données** : Utilisation d’AWS Lambda et Glue pour ETL et Amazon Athena pour interroger les données.

### Module 2 : NLP et Résumés avec IA Générative
   - **Résumé** : Utilisation d’Amazon Bedrock pour générer des résumés concis.
   - **Analyse de Sentiment** : Amazon Comprehend pour déterminer le ton (optimiste, neutre, pessimiste) des sections.
   - **Personnalisation** : Ajustement des modèles via AWS Sagemaker pour un langage financier précis.

### Module 3 : Surveillance des Tendances et Extraction des KPI
   - **Détection de Tendances** : Analyse des tendances avec Amazon Forecast et détection d'anomalies via Sagemaker.
   - **Extraction de KPI** : Extraction via Amazon Textract et Comprehend pour des indicateurs financiers précis.

### Module 4 : Analyse Prédictive
   - **Séries Temporelles** : Utilisation de Amazon Forecast et Sagemaker pour prédire les revenus, coûts, etc.
   - **Scénarios Prédictifs** : Modèles personnalisés en Sagemaker pour différentes hypothèses de marché.

### Module 5 : Visualisation et Rapports
   - **Dashboard** : Création de tableaux de bord interactifs avec Amazon QuickSight.
   - **Comparaisons Multi-Périodes** : Comparaison visuelle automatisée de données financières.

## 3. Expérience Utilisateur (UX/UI)

   - **Tableau de Bord Intuitif** : Conception d'une interface centrale intuitive et facile d'accès.
   - **Navigation Simple** : Accès rapide aux fonctionnalités principales.
   - **Personnalisation** : Permet de configurer les vues selon les indicateurs préférés.

## 4. Optimisation de l'Environnement AWS

   - **Intégration AWS** : Cloud9 pour le développement, Lambda et Glue pour ETL, Sagemaker pour les modèles ML, Bedrock pour l’IA générative.
   - **Ressources Efficaces** : Programmation des tâches de traitement pour les périodes creuses.
   - **Scalabilité** : Configuration de l’auto-scaling pour gérer les charges de données.

## 5. Livrables et Échéances

   - **Code** : Répertoire GitHub à soumettre avant le 4 novembre.
   - **Démo Vidéo** : Vidéo de 3 minutes à soumettre avant le 5 novembre.
   - **Documentation Technique** : Diagramme et explication de l'architecture.
   - **Présentation (Finalistes)** : Préparation pour le 8 novembre.

