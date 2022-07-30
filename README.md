# json-translator
translate json files without considering {{ expressions }}

<img src="https://github.com/aliesenli/json-translator/blob/master/json-translator/img/example-usage-terminal.png">
<img src="img/example-usage-terminal.png">

### example:
translates (EN): <br>
```json
{
   "profile_user_name": "Your name is {{ user.firstname }}"
}
```
to (DE): <br>
```json
{
   "profile_user_name": "Ihr Name ist {{ user.firstname }}"
}
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
