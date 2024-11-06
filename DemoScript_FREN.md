# Démo Datathon Polyfinance 2024 - Équipe #41 : Geppetto

Bonjour à tous! Je me présente, je m'appelle Omar et aujourd'hui j'ai le grand honneur et plaisir de vous présenter la solution que mon équipe et moi avons réalisé pour répondre au mandat de l'édition 2024 du Datathon organisé par Polyfinances, notre application révolutionnaire: **Geppetto**. 

Le mandat de cet évènement fut très simple: Créez un outil utilisant l’IA générative pour assister les analystes financiers à faire leur travail. La toute première question que nous nous sommes demandé était la plus importante: **Pourquoi Geppetto ?** Et par cela, je veux dire, Pourquoi un analyste financier quelquonque utiliserait notre outil et non pas un des grands LLMs connu et déjà établi comme ChatGPT, Perplexity, Claude, ... ect. Nous avons répondu à cette question avec une autre question: **Quelles sont les problèmes principaux qu'un analyste financier pourrait rencontrer en utilisant ces derniers ?** 

Après une rechercher approfondis, deux problèmes sont sortis du lot. D'abord, **Les LLMs peuvent accablant (overwheling) pour quelqu'un qui n'a pas l'habitude de les utilisés.** et puis **Ils sont conçus pour être utilisé pour tout et n'importe quoi et non pas pour répondre au besoinss un utilisateur spécifique.**

Ces questions nous ont mené à la réalisation de **Geppetto** qui utilise le **pouvoir de l’IA générative** et l’infrastructure d’**AWS** pour automatiser et simplifier l’analyse financière à partir d'un simple rapport annuel. Nous n'avons que 3 minutes, alors, attachez vos ceintures !

La page d'acceuil est simple et invite l'analyste à commencer une analyse d'une compagnie spécifique à une année spécifique, il suffit de télécharger le rapport financier et nous sommes rédirigé à notre **page des fonctionnalités** qui présente quelques infos récupéré sur la compagnie, l'option de changer de fichier, ou bien nos fonctionnalités principales, le résumé ou bien la génération de dashboard, tout deux automatiser grace à Geppetto!

Comencons par démo le Résumé automatique, pendant que Geppetto travaille, je prend ce moment pour vous expliquer ce qui se passe, le fichier selectionner est telecharger sur notre bucket S3 et puis ce dernier est synchroniser avec notre knowledge base et puis grace à l'API de AWS, on peut utilisé la génération de texte avancés d’AWS Bedrock plus précisément de Claude 3.5 qui a été finetuner et entrainer uniquement pour nos besoins pour au final analyser le rapport qui peut être composé de centaines de pages et livrer l'essentiel à notre serveur NodeJS qui communique avec notre client Angular à travers HTTP qui lui présente le tout de manière claire et concise. Geppetto présente le résumé du rapport avec des insights clés et conduit également en parrallèle une **analyse de sentiment** — parfait pour repérer les signaux d’optimisme… ou de prudence !

Mais attendez, ce n’est pas tout. Besoin de précisions ? Rencontrez notre **ChatBot** pour demander toutes question de suivis! Doté de **RAG**, il répond aux questions spécifiques sur le rapport et uniquement cela. Pas de blabla nons pertinents comme avec les autre outils!

Pour finir, direction la **page d'analyse des données**. Ici, on visualise les principaux **indicateurs financiers** et les **tendances du marché** via cinq **graphiques interactifs**. Vous pouvez exporter les graphiques en png, le rapport sous forme de **PDF**, ou bien uniquement les données en **CSV** pour les intégrer facilement à vos rapports.

Notre architecture est modulaire, évolutive, et conçue pour durer.

En somme, Geppetto est un game-changer pour les analystes financiers. On a de l’**IA générative**, du **monitoring en temps réel** et une interface conçue pour des analyses plus rapides et plus intelligentes. Merci à Polyfinance et à Banque Nationale pour cette opportunité de révolutionner l’analyse financière et j'éspère pouvoir vous présenter Geppetto en personne Vendredi !
