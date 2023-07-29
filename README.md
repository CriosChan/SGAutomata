## Architecture du dossier jeu
```
STEINS;GATE
    -> extracted
        -> debug            // Stock la version debug des fichiers texts
        -> en_backup        // Stock la version anglaise des fichiers texts
        -> release          // Stock la version release des fichiers texts
        -> script           // Contient les .SCX du jeu
    -> py_scripts
        -> tools
            -> magespack    // Logiciel servant à packer les SCX en un mpk
            -> sc3tools     // Unpack et repack les .SCX
            -> sg-unpack    // Unpack les mpk
        | enter_debug_mode.py
        | enter_release_mode.py
        | extact_scx_files.py
        | modify_translation.py
        | pack_scx_files.py
        | translator.py
    -> USRDIR
    ...Game files
```

## Tools
- [magespack](https://github.com/DanOl98/MagesPack)
- [sc3tools](https://github.com/CommitteeOfZero/sc3tools)
- [sg-unpack](https://github.com/rdavisau/sg-unpack)

## enter_debug_mode.py
Script permettant de convertir les fichiers .txt se trouvant dans le dossier release en mode "debug", le mode debug permet d'avoir ingame un identifiant de dialogue permettant de changer le dialogue grâce à ```modify_translation.py```

Pour le faire fonctionne il faut absolument que le dossier extracted > debug et extracted > release soient tout les deux créés
Ensuite ouvrez un terminal dans py_scripts et tapez `python enter_debug_mode.py`

## enter_release_mode.py
Comme pour `enter_debug_mode.py`, convertit les .txt en mode debug vers une version release

Pour le faire fonctionne il faut absolument que le dossier extracted > debug et extracted > release soient tout les deux créés
Ensuite ouvrez un terminal dans py_scripts et tapez `python enter_release_mode.py`

## extract_scx_files.py
Ce script utilise sc3tools pour convertir les SCX en .txt. Une fois démarré le script créera les txts dans le dossier extracted/script.

Pour le faire fonctionner il faut au préalable avoir extrait script.mpk en utilisant magespack ou sg-unpack.
Ouvrez un terminal dans py_scripts et tapez `python enter_release_mode.py`

## modify_tranlation.py
FONCTIONNE UNIQUEMENT SI VOUS ÊTES EN MODE DEBUG, QUE `extracted/debug/` EST REMPLIE DE FICHIER, ET QUE `extracted/en_backup` EST REMPLIE DE FICHIER ANGLAIS ORIGINAUX.

Comme son nom l'indique ce script vous permettra de voir la version anglaise d'un dialogue et de modifier sa version française. Pensez évidemment à utilise `pack_scx_files.py` pour voir les changements s'opérer.

Ouvrez un terminal dans py_scripts et tapez `python modify_translation.py`

## pack_scx_files.py
Comme son nom l'indique ce script vous permettra de remettre les .txt en .SCX.
Le script a une argument facultatif étant `--debug`
Si mentionner, le script ira chercher les fichiers disponible dans le dossier `extracted/debug/`

Ouvrez un terminal dans py_scripts et tapez `python pack_scx_files.py` ou `python pack_scx_files.py --debug`

## translator.py
Dans le cas où un dossier `To Translate` existe dans le dossier `extracted`, le script ira chercher chaque dialogue disponible dans les .txt se trouvant dans le dossier pour essayer de les traduire

Pour le faire fonctionner il vous faut : [SELENIUM](https://selenium-python.readthedocs.io/) et un VPN si possible pour ne pas être ban de DeepL.

Ouvrez un terminal dans py_scripts et tapez `python translator.py` ou `python translator.py -d VOTRE_DOSSIER`
`-d` est un argument permettant de choisir le dossier où aller chercher les .txt, plutôt que `To Translate`