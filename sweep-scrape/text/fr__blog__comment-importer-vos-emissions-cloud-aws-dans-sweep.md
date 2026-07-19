# Comment importer vos émissions cloud AWS dans Sweep - Sweep


**Description:** Importez automatiquement vos émissions cloud AWS dans Sweep et consolidez vos données Scope 1, 2 et 3 sous une méthodologie unique, prête pour l'audit.


## Content


Home
Insights
Blog
Comment importer vos émissions cloud AWS dans Sweep
Catégorie
Blog
Dernière mise à jour
22 juin 2026
L’infrastructure cloud est l’un des postes d’émissions de Scope 3 qui croît le plus vite pour les entreprises, et l’un des plus difficiles à mesurer avec précision. Pour la plupart des organisations, obtenir des données d’émissions cloud propres et auditables impliquait jusqu’ici des exports manuels, des manipulations de tableurs et de nombreux allers-retours avec les équipes IT, avant même que les chiffres n’arrivent dans une plateforme développement durable.
Tout ça, c’est fini.
Sweep a développé une solution complète de mesure des émissions cloud, basée sur
AWS Sustainability
, le service de reporting des émissions lancé en standalone par Amazon Web Services. En tant que
partenaire AWS ISV-Accelerate entièrement déployé sur AWS
, Sweep est idéalement positionné pour se connecter directement aux données d’émissions AWS. L’intégration permet aux clients entreprises de consolider automatiquement leurs données d’émissions cloud AWS dans Sweep, aux côtés des données Scope 1, 2 et 3 couvrant l’ensemble de leurs opérations, sous une méthodologie unique, traçable jusqu’à la source et prête pour un audit externe.
Ce connecteur s’intègre naturellement à notre écosystème de données et offre une qualité de données qui dépasse nos attentes. Sweep nous permet de centraliser non seulement l’impact de notre infrastructure cloud, mais aussi toutes les données opérationnelles qui sous-tendent notre reporting extra-financier.
Federica Del Fiume
ESG Manager, Quonto
Pourquoi agir maintenant sur vos émissions cloud ?
L’infrastructure cloud reste un défi de taille dans le reporting carbone, notamment pour les entreprises avec une forte empreinte AWS. Sweep et Capgemini ont constaté que 61 % des responsables développement durable passent plus de quatre heures par semaine à consolider des données d’émissions.
Cette charge ne fait qu’augmenter, avec l’élargissement des obligations de reporting Scope 3 imposées par la CSRD, l’UK SRS, l’ISSB et la loi californienne SB 253.
AWS Sustainability offre aux entreprises un accès programmatique aux données d’émissions de Scopes 1, 2 et 3, ventilées par service, région et compte. Le connecteur Sweep intègre automatiquement ces données dans le bilan carbone de l’entreprise, sans exports manuels ni tableurs.
Ce que vous obtenez : des données d’émissions ventilées par service, région et compte
La console AWS Sustainability fournit des données d’émissions carbone couvrant :
Scope 1 :
émissions directes liées aux opérations AWS
Scope 2 (location-based et market-based) :
émissions indirectes liées à la consommation d’énergie, avec ou sans certificats d’énergie renouvelable (RECs) ou contrats d’achat d’énergie (PPAs)
Scope 3 :
émissions de la chaîne de valeur en amont et en aval
Toutes ces données arrivent dans Sweep avec une granularité par service AWS (ex. EC2, S3), région et compte, vous donnant la précision nécessaire pour identifier vos points chauds d’émissions cloud et suivre vos progrès dans le temps.
Comment fonctionne l’intégration
Sweep importe automatiquement les données d’émissions depuis AWS Sustainability via Amazon S3, avec une prise en charge native du versionnement des facteurs d’émission AWS et un traitement quasi en temps réel. L’intégration est compatible avec l’infrastructure AWS existante, notamment Redshift et Athena, ainsi qu’avec des plateformes comme Snowflake et Microsoft SQL Server.
Vue d’ensemble de la configuration
Pour configurer l’intégration, vous aurez besoin de :
Un accès à votre compte de gestion AWS
Les droits pour créer des buckets S3, des utilisateurs IAM et des exports BCM Data
Terraform installé (recommandé pour une configuration en infrastructure-as-code)
Le processus de configuration est le suivant  :
Créer un bucket S3 pour stocker les exports d’émissions carbone AWS
Configurer un export BCM Data pour envoyer les données d’émissions vers ce bucket
Créer un utilisateur IAM en lecture seule pour Sweep
Connecter l’export à Sweep via le connecteur AWS
Appliquer une règle de transformation pour mapper les données d’émissions AWS dans le modèle de données Sweep
L’intégration prend en charge les données d’émissions Scopes 1, 2 et 3 par service, région et compte. Sweep recommande par défaut d’utiliser les valeurs d’émissions location-based (LBM), bien que les valeurs market-based (MBM) soient également supportées.
Points importants à noter
Les données d’émissions AWS sont généralement publiées après la fin du mois de reporting
Les exports AWS incluent les identifiants de compte, pas les noms de compte
Le filtrage des imports par compte n’est pas encore disponible au niveau du connecteur
Le connecteur AWS Sustainability Console remplace l’ancien connecteur AWS Cloud Carbon Footprint (CCF)
Prêt(e) à démarrer ?
Le connecteur AWS est disponible dès aujourd’hui pour tous les clients Sweep. Si vous êtes déjà client, connectez-vous et suivez le lien vers notre centre d’aide :
help.sweep.net
.
Si vous n’êtes pas encore client Sweep et souhaitez découvrir comment la plateforme peut vous aider à consolider et reporter votre empreinte carbone complète,
réservez une démo ici
.
Contenus
Pourquoi agir maintenant sur vos émissions cloud ?
Comment fonctionne l’intégration
Prêt(e) à démarrer ?
Plus d'articles
Études
Verdantix : L’IA de Sweep révolutionne la gestion des données carbone
Études
Green Quadrant Verdantix 2026 : Sweep parmi les leaders du marché
ESG
Études
IDC place Sweep parmi les meilleurs logiciels de durabilité au monde
ESG


## Links


  [Lire l'étude](https://www.sweep.net/fr/reports/sweep-leader-de-letude-idc-marketscape-2026-des-plateformes-carbone)
  [En savoir plus](https://www.linkedin.com/posts/republik-finance-cfo_les-laur%C3%A9ats-de-la-cat%C3%A9gorierse-impact-activity-7457128488077053953-zJY_/?rcm=ACoAAABlsAQB23Tol3TLqAzaGoUiAseioecBlt4)
  [Lire l'article](/fr/reports/green-quadrant-verdantix-2026-sweep-parmi-les-leaders-du-marche)
  [Comptabilité carbone](/fr/comptabilite-carbone)
  [Émissions supply chain](/fr/emissions-supply-chain)
  [Reporting ESG](/fr/reporting-esg)
  [Stratégie de décarbonation](/fr/strategie-de-decarbonation)
  [CSRD](/fr/csrd)
  [GRI](/fr/gri)
  [ISSB](/fr/issb)
  [SFDR](/fr/sfdr)
  [CDP](/fr/cdp)
  [Plateforme](/fr/platform)
  [Sweep AI](/fr/platform/ia-responsable)
  [Clients](/fr/customers)
  [Études](/fr/reports)
  [Événements](/fr/events)
  [Presse](/fr/newsroom)
  [Blog](/fr/blog)
  [Se préparer à la version finale de la CSRD – avec Julien Denormandie](/fr/blog/se-preparer-a-la-version-finale-de-la-csrd-avec-julien-denormandie)
  [Pourquoi calculer une empreinte carbone produit ? Interview avec Lucie Varéon](/fr/blog/pourquoi-calculer-une-empreinte-carbone-produit-interview-avec-lucie-vareon)
  [La COP30 reste un espace de dialogue nécessaire](/fr/blog/la-cop30-reste-un-espace-de-dialogue-necessaire)
  [Guides](/fr/guides)
  [CSRD : le guide du reporting pour les entreprises de la vague 2](/fr/guides/csrd-le-guide-du-reporting-pour-les-entreprises-de-la-vague-2)
  [La méthode complète pour améliorer votre score CDP](/fr/guides/la-methode-pour-ameliorer-votre-score-cdp)
  [Le guide d’achat des logiciels ESG](/fr/guides/le-guide-dachat-des-logiciels-esg)
  [Outils](/fr/tools)
  [Guide interactif CDP 2026](/fr/tools/guide-interactif-cdp-2026)
  [Construire sa matrice de double matérialité](/fr/tools/csrd-materiality-builder)
  [Construire sa roadmap CSRD](/fr/tools/csrd-roadmap-tool)
  [Qui sommes-nous ?](/fr/about)
  [Pourquoi choisir Sweep ?](/fr/pourquoi-nous)
  [Nos partenaires](/fr/partners)
  [Nous rejoindre](https://sweep.teamtailor.com/)
  [English](/blog/how-to-import-your-aws-cloud-emissions-into-sweep/)
  [French](/fr/blog/comment-importer-vos-emissions-cloud-aws-dans-sweep/)
  [S'identifier](https://app.sweep.net/auth/sign-in)
  [Demandez une démo](/fr/demo)
  [Home](/fr)
  [Blog](/fr/blog)
  [partenaire AWS ISV-Accelerate entièrement déployé sur AWS](https://www.sweep.net/blog/sweep-is-fully-deployed-on-aws-heres-why-it-matters-2)
  [help.sweep.net](https://help.sweep.net/en/aws-sustainability-console.html)
  [réservez une démo ici](https://www.sweep.net/demo)
  [Pourquoi agir maintenant sur vos émissions cloud ?](#pourquoi-agir-maintenant-sur-vos-emissions-cloud)
  [Comment fonctionne l’intégration](#comment-fonctionne-lintegration)
  [Prêt(e) à démarrer ?](#pret-e-a-demarrer)
  [ÉtudesVerdantix : L’IA de Sweep révolutionne la gestion des données carbone](/fr/reports/verdantix-lia-de-sweep-revolutionne-la-gestion-des-donnees-carbone/)
  [ÉtudesGreen Quadrant Verdantix 2026 : Sweep parmi les leaders du marchéESG](/fr/reports/green-quadrant-verdantix-2026-sweep-parmi-les-leaders-du-marche/)
  [ÉtudesIDC place Sweep parmi les meilleurs logiciels de durabilité au mondeESG](/fr/reports/sweep-parmi-les-leaders-du-rapport-idc-marketscape-2025/)
  [Comptabilité carbone](/fr/comptabilite-carbone)
  [Émissions supply chain](/fr/emissions-supply-chain)
  [Reporting ESG](/fr/reporting-esg)
  [Stratégie de décarbonation](/fr/strategie-de-decarbonation)
  [Grands groupes](/fr/enterprise)
  [ETI et PME](/fr/midmarket)
  [Institutions financières](/fr/financial-institutions)
  [Sweep Starter](https://www2.sweep.net/fr/starter-package)
  [Notre plateforme](/fr/platform)
  [AI](/fr/platform/ia-responsable)
  [Ressources](/fr/blog)
  [Événements](/fr/events)
  [Salle de presse](/fr/newsroom)
  [Plus rentable](/fr/plus-durable-plus-rentable)
  [Plus conforme](/fr/plus-durable-plus-conforme)
  [Plus compétitif](/fr/plus-durable-plus-competitif)
  [Plus efficace](/fr/plus-durable-plus-efficace)
  [Plus résilient](/fr/plus-durable-plus-resilient)
  [CSRD](/fr/csrd)
  [GRI](/fr/gri)
  [ISSB](/fr/issb)
  [SFDR](/fr/sfdr)
  [CDP](/fr/sfdr)
  [Bien de consommation](/fr/industry/consumer-goods)
  [Commerce de détail](/fr/industry/retail)
  [Médias et télécommunications](/fr/industry/media-telecoms)
  [Énergie, services publics, pétrole et gaz](/fr/industry/energy-oil-and-gas)
  [Épicerie](/fr/industry/grocery)
  [Production](/fr/industry/manufacturing)
  [Cabinet de conseil](/fr/industry/services)
  [Santé](/fr/industry/healthcare)
  [Qui sommes-nous ?](/fr/about)
  [Clients](/fr/customers)
  [Partenaires](/fr/partners)
  [Presse](https://sweepnet.notion.site/Sweep-media-kit-2025-170f1c3c643c802c8d98d8a5833dc107)
  [Contact](/fr/contact)
  [Juridique](/fr/company/terms)
  [Conditions d'utilisation](/fr/company/terms)
  [Linkedin](https://www.linkedin.com/company/sweeptheplanet/about/)
  [YouTube](https://www.youtube.com/@SweepThePlanet)
  [Instagram](https://www.instagram.com/sweeptheplanet/)
  [Système](https://status.sweep.net/)
  [Sécurité](https://trust.sweep.net/)
  [Greenly vs Sweep](/fr/greenly-vs-sweep)
  [Tennaxia vs Sweep](/fr/tennaxia-vs-sweep)


## Images


  ![Sweep AWS](/_astro/LP_header1_1n1Qj.webp)
  ![Federica Del Fume](/_astro/Screenshot20260529at13.19.14_Z1LmUv7.webp)
  ![Verdantix Report 2025](/_astro/homepage_spotlight1_25gFBi.webp)
  ![Verdantix Green Quadrant 2026](/_astro/sweep_verdantix_mar26header01_F61EB.webp)
  ![Cover IDC 2025](/_astro/LP_1_1BpLzX.webp)
  ![](/_astro/Group_1rOUQL.svg)
  ![](/_astro/Frame_ZrUz7Q.svg)
  ![](/_astro/csr_WHITE1_Z1Jryw.svg)
  ![](/_astro/LFT_2025white_ZXsvVq.webp)