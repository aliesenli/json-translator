# json-translator
translate json files without considering {{ expressions }}

### example:
translates (EN): <br>
```
Your name is {{ user.firstname }}
```
to (DE): <br>
```
Ihr Name ist {{ user.firstname }}
```

everything inside expressions <ins>won't</ins> get translated.

### usage:
```bash
python main.py -s 'source_en.json' -d 'destination_de.json' -l 'german'
```
```-s``` Path to the source file<br>
```-d``` Path to the destination file<br>
```-l``` Target Language to be translated into<br>

use ```--help``` to see list of supported languages.
