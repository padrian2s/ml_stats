#!/usr/bin/env python3
"""Generate pages-data.js with Romanian titles for all 1098 pages."""

# Chapter definitions: (chapter_num, start_page, end_page, title_ro, sections)
# sections: list of (page, title_ro, keywords_ro)
chapters = [
    (0, 1, 26, "Materie Preliminara", [
        (1, "Coperta", "machine learning probabilistic perspective"),
        (2, "Pagina goala", ""),
        (3, "Pagina de titlu", "machine learning probabilistic perspective"),
        (4, "Titlu complet", "machine learning kevin murphy MIT press"),
        (5, "Copyright", "copyright MIT press 2012"),
        (6, "Dedicatie", "dedicatie Alessandro Michael Stefano Gerard Joseph Murphy"),
        (7, "Pagina goala", ""),
        (8, "Pagina goala", ""),
        (9, "Cuprins (Partea 1)", "cuprins introducere probabilitati"),
        (10, "Cuprins (Partea 2)", "cuprins distributii continue covarianta"),
        (11, "Cuprins (Partea 3)", "cuprins modele generative beta-binomial Bayes naiv"),
        (12, "Cuprins (Partea 4)", "cuprins modele Gaussiene analiza discriminanta"),
        (13, "Cuprins (Partea 5)", "cuprins statistica Bayesiana frequentista regresie"),
        (14, "Cuprins (Partea 6)", "cuprins regresie logistica GLM familia exponentiala"),
        (15, "Cuprins (Partea 7)", "cuprins modele grafice directionate amestec EM"),
        (16, "Cuprins (Partea 8)", "cuprins modele liniare latente sparse kerneluri"),
        (17, "Cuprins (Partea 9)", "cuprins procese Gaussiene functii baza adaptive boosting"),
        (18, "Cuprins (Partea 10)", "cuprins Markov HMM spatiu stare modele grafice nedirectionate"),
        (19, "Cuprins (Partea 11)", "cuprins inferenta exacta variationala Monte Carlo MCMC"),
        (20, "Cuprins (Partea 12)", "cuprins clustering structura grafuri variabile latente invatare profunda"),
        (21, "Prefata (Partea 1)", "prefata manual probabilistic perspectiva"),
        (22, "Prefata (Partea 2)", "prefata continuare recunoastere"),
        (23, "Simboluri si notatii", "simboluri notatii matematice"),
        (24, "Simboluri si notatii (continuare)", "notatii continuare"),
        (25, "Pagina goala", ""),
        (26, "Pagina goala", ""),
    ]),
    (1, 27, 52, "Introducere", [
        (27, "1.1 Invatarea automata: ce si de ce?", "invatare automata machine learning ce de ce motivatie"),
        (28, "1.1.1 Tipuri de invatare automata", "tipuri invatare supervizata nesupervizata reinforcement"),
        (29, "1.2 Invatarea supervizata", "invatare supervizata clasificare"),
        (30, "1.2.1 Clasificare", "clasificare etichete clase predictor"),
        (31, "Clasificare (continuare)", "clasificare continuare exemple"),
        (32, "Clasificare: exemple", "clasificare spam documente imagini"),
        (33, "Clasificare: iris, MNIST", "iris MNIST clasificare imagini flori"),
        (34, "1.2.2 Regresie", "regresie variabile continue predictie"),
        (35, "1.3 Invatarea nesupervizata", "invatare nesupervizata fara etichete"),
        (36, "1.3.1 Descoperirea clusterelor", "clustering grupare descoperire clustere k-means"),
        (37, "1.3.2 Descoperirea factorilor latenti", "factori latenti reducere dimensionalitate PCA"),
        (38, "Factori latenti (continuare)", "factori latenti continuare"),
        (39, "1.3.3 Descoperirea structurii grafurilor", "structura grafuri retele relatii"),
        (40, "1.3.4 Completarea matricilor", "completarea matricilor valori lipsa imputare"),
        (41, "Completarea matricilor (continuare)", "matrici continuare Netflix recomandari"),
        (42, "1.4 Concepte de baza in ML", "concepte baza modele parametrice neparametrice"),
        (43, "1.4.2 KNN: clasificator neparametric", "KNN k vecini apropiati clasificator neparametric"),
        (44, "1.4.3 Blestemul dimensionalitatii", "blestemul dimensionalitatii spatii mari"),
        (45, "1.4.5 Regresie liniara", "regresie liniara cele mai mici patrate MLE"),
        (46, "Regresie liniara (continuare)", "regresie liniara continuare functii de baza"),
        (47, "1.4.6 Regresie logistica", "regresie logistica clasificare probabilistica"),
        (48, "1.4.7 Supraajustare", "supraajustare overfitting complexitate model"),
        (49, "1.4.8 Selectia modelului", "selectia modelului validare incrucisata"),
        (50, "Selectia modelului (continuare)", "selectia modelului BIC AIC"),
        (51, "1.4.9 Teorema: nu exista masa gratis", "no free lunch teorema fara masa gratis"),
        (52, "Exercitii Capitolul 1", "exercitii probleme capitolul 1"),
    ]),
    (2, 53, 90, "Probabilitati", [
        (53, "2.1 Introducere in probabilitati", "introducere probabilitati incertitudine"),
        (54, "2.2 Teoria probabilitatilor", "teoria probabilitatilor variabile aleatoare discrete"),
        (55, "2.2.3 Regula lui Bayes", "regula Bayes teorema posterior prior verosimilitate"),
        (56, "2.2.4 Independenta conditionata", "independenta conditionata variabile aleatoare"),
        (57, "Independenta (continuare)", "independenta continuare exemple"),
        (58, "2.2.5 Variabile aleatoare continue", "variabile continue CDF PDF densitate"),
        (59, "2.2.6-7 Cuantile, media si varianta", "cuantile media varianta momente"),
        (60, "2.3 Distributii discrete comune", "distributii discrete binomiala Bernoulli"),
        (61, "2.3.2 Distributia multinomiala", "multinomiala multinoulli distributie discreta"),
        (62, "Distributia multinomiala (continuare)", "multinomiala continuare"),
        (63, "2.3.3-4 Poisson si distributia empirica", "Poisson distributie empirica"),
        (64, "2.4 Distributii continue: Gaussiana", "Gaussiana normala distributie continua medie varianta"),
        (65, "2.4.2 PDF degenerata", "PDF degenerata distributie concentrata punct"),
        (66, "Distributii continue (continuare)", "distributii continue continuare"),
        (67, "2.4.3-4 Laplace si Gamma", "Laplace distributie gamma forma rata"),
        (68, "2.4.5 Distributia Beta", "beta distributie conjugata priori"),
        (69, "2.4.6 Distributia Pareto", "Pareto distributie legea puterii coada grea"),
        (70, "2.5 Distributii de probabilitate comune", "distributii comune covarianta corelatie"),
        (71, "Covarianta si corelatie (continuare)", "covarianta corelatie continuare"),
        (72, "2.5.2-3 Gaussiana multivariata si Student", "Gaussiana multivariata Student t distributie"),
        (73, "2.5.4 Distributia Dirichlet", "Dirichlet distributie multivariata simplex"),
        (74, "Dirichlet (continuare)", "Dirichlet continuare proprietati"),
        (75, "2.6 Transformari ale variabilelor aleatoare", "transformari variabile aleatoare liniare"),
        (76, "Transformari (continuare)", "transformari continuare generale"),
        (77, "Transformari generale", "transformari generale jacobian"),
        (78, "2.7 Aproximarea Monte Carlo", "Monte Carlo aproximare esantionare"),
        (79, "Monte Carlo (continuare)", "Monte Carlo continuare estimare pi"),
        (80, "Acuratetea aproximarii Monte Carlo", "acuratete Monte Carlo eroare"),
        (81, "Monte Carlo (continuare)", "Monte Carlo continuare convergenta"),
        (82, "2.8 Teoria informatiei: Entropie", "entropie teoria informatiei Shannon"),
        (83, "2.8.2 Divergenta KL", "divergenta KL Kullback-Leibler distanta distributii"),
        (84, "Divergenta KL (continuare)", "KL continuare proprietati"),
        (85, "2.8.3 Informatia mutuala", "informatia mutuala dependenta variabile"),
        (86, "Informatia mutuala (continuare)", "informatia mutuala continuare"),
        (87, "Exercitii Capitolul 2 (1)", "exercitii probabilitati"),
        (88, "Exercitii Capitolul 2 (2)", "exercitii probabilitati continuare"),
        (89, "Exercitii Capitolul 2 (3)", "exercitii probabilitati continuare"),
        (90, "Exercitii Capitolul 2 (4)", "exercitii probabilitati continuare"),
    ]),
]

# For chapters 3-28 and back matter, generate programmatic entries
chapter_defs = [
    # (ch, start, end, title_ro, topics_ro_for_search)
    (3, 91, 122, "Modele generative pentru date discrete", "modele generative date discrete Bayes concept learning beta-binomial Dirichlet multinomial Bayes naiv clasificator"),
    (4, 123, 174, "Modele Gaussiene", "modele Gaussiene analiza discriminanta QDA LDA sisteme liniare Wishart inferenta MVN"),
    (5, 175, 216, "Statistica Bayesiana", "statistica Bayesiana MAP estimare intervale credibile selectia modelului Occam priori Bayes ierarhic empiric decizie"),
    (6, 217, 242, "Statistica frequentista", "statistica frequentista estimatori bootstrap MLE risc minimax bias varianta validare incrucisata"),
    (7, 243, 270, "Regresie liniara", "regresie liniara MLE cele mai mici patrate geometrie convexitate robusta ridge regularizare Bayesiana"),
    (8, 271, 306, "Regresie logistica", "regresie logistica MLE gradient Newton IRLS regularizare multi-clasa Bayesiana Laplace online SGD generativa discriminativa"),
    (9, 307, 332, "GLM-uri si familia exponentiala", "GLM familia exponentiala definitie partitie MLE Bayes regresie probit multi-task modele liniare mixte rang"),
    (10, 333, 362, "Modele grafice directionate", "retele Bayesiene modele grafice directionate Bayes naiv HMM diagnostic inferenta invatare d-separare Markov blanket influenta"),
    (11, 363, 400, "Modele de amestec si algoritmul EM", "modele amestec EM algoritmul variabile latente Gaussiene multinoulli experti estimare parametri identificabilitate MAP non-convex"),
    (12, 401, 442, "Modele liniare latente", "modele liniare latente analiza factoriala PCA componente principale SVD probabilistica ICA independent"),
    (13, 443, 504, "Modele liniare sparse", "modele liniare sparse selectie variabile spike slab L0 L1 LASSO regularizare coordinate descent LARS elastic net ARD codificare rara"),
    (14, 505, 540, "Kerneluri", "kerneluri RBF Mercer string piramid masini vectori suport SVM clasificare regresie trucul kernel"),
    (15, 541, 568, "Procese Gaussiene", "procese Gaussiene GP regresie clasificare kernel parametri semi-parametric GLM conexiune metode"),
    (16, 569, 614, "Modele cu functii de baza adaptive", "arbori decizie CART random forests boosting AdaBoost retele neurale MLP convolutie backpropagation ensemble"),
    (17, 615, 656, "Modele Markov si HMM-uri", "Markov HMM model ascuns tranzitie limbaj PageRank forward backward Viterbi Baum-Welch semi-Markov ierarhic"),
    (18, 657, 688, "Modele de spatiu de stare", "spatiu stare SSM tracking SLAM Kalman filtru smoothing EKF UKF discret continuu"),
    (19, 689, 732, "Modele grafice nedirectionate", "modele grafice nedirectionate MRF Markov random field Ising Hopfield Potts Gaussien CRF conditional SSVM structural"),
    (20, 733, 754, "Inferenta exacta pentru modele grafice", "inferenta exacta propagare credinte belief propagation eliminare variabile junction tree mesaje"),
    (21, 755, 796, "Inferenta variationala", "inferenta variationala VB camp mediu mean field EP expectation propagation bound ELBO"),
    (22, 797, 842, "Inferenta variationala avansata", "inferenta variationala avansata VB-EM VAE autoencoder variational modele profunde"),
    (23, 843, 864, "Inferenta Monte Carlo", "inferenta Monte Carlo esantionare importanta SIR particule filtre"),
    (24, 865, 902, "MCMC", "MCMC Markov chain Monte Carlo Metropolis-Hastings Gibbs Hamilton HMC diagnostice convergenta"),
    (25, 903, 940, "Clustering", "clustering K-means modele amestec spectral ierarhic aglomerativ evaluare"),
    (26, 941, 972, "Invatarea structurii grafurilor", "invatarea structurii grafuri retele Bayesiene score cautare MRF"),
    (27, 973, 1010, "Modele cu variabile latente pentru date discrete", "variabile latente date discrete LDA topic model pLSI text"),
    (28, 1011, 1058, "Invatare profunda", "invatare profunda deep learning CNN RNN autoencoder GAN retele neurale convolutie recurenta"),
]

back_matter = (0, 1059, 1098, "Materie Suplimentara", "bibliografie index referinte notatie algebra liniara")

import json

entries = []

# Process detailed chapters (0, 1, 2)
for ch_num, ch_start, ch_end, ch_title, sections in chapters:
    section_dict = {s[0]: (s[1], s[2]) for s in sections}
    for p in range(ch_start, ch_end + 1):
        if p in section_dict:
            title, search = section_dict[p]
        else:
            title = f"{ch_title} (continuare)"
            search = ch_title.lower()
        entries.append({
            "page": p,
            "title": title,
            "chapter": ch_num,
            "searchText": search
        })

# Process chapters 3-28 with generated entries
for ch_num, ch_start, ch_end, ch_title, topics in chapter_defs:
    total = ch_end - ch_start + 1
    for i, p in enumerate(range(ch_start, ch_end + 1)):
        if i == 0:
            title = f"Capitolul {ch_num}: {ch_title}"
        elif i == total - 1:
            title = f"Exercitii Capitolul {ch_num}"
        elif i == 1:
            title = f"{ch_title} — Introducere"
        else:
            # Distribute section titles
            title = f"{ch_title} (p.{p})"
        entries.append({
            "page": p,
            "title": title,
            "chapter": ch_num,
            "searchText": topics
        })

# Back matter
bm_ch, bm_start, bm_end, bm_title, bm_topics = back_matter
for p in range(bm_start, bm_end + 1):
    if p <= 1065:
        title = "Notatie si algebra liniara"
    elif p <= 1090:
        title = "Bibliografie"
    else:
        title = "Index"
    entries.append({
        "page": p,
        "title": title,
        "chapter": 0,
        "searchText": bm_topics
    })

# Sort by page
entries.sort(key=lambda x: x["page"])

# Verify completeness
pages_seen = set(e["page"] for e in entries)
missing = [p for p in range(1, 1099) if p not in pages_seen]
if missing:
    print(f"WARNING: Missing pages: {missing[:20]}...")

# Write JS file
with open("/Users/adrian/personal/ml_stats/js/pages-data.js", "w") as f:
    f.write("window.pagesData = [\n")
    for i, entry in enumerate(entries):
        comma = "," if i < len(entries) - 1 else ""
        title_escaped = entry["title"].replace('"', '\\"')
        search_escaped = entry["searchText"].replace('"', '\\"')
        f.write(f'  {{ page: {entry["page"]}, title: "{title_escaped}", chapter: {entry["chapter"]}, searchText: "{search_escaped}" }}{comma}\n')
    f.write("];\n")

print(f"Generated {len(entries)} entries for pages-data.js")
print(f"Pages covered: 1 to {max(e['page'] for e in entries)}")
