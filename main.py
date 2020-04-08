import translator
import polib
import json


path_to_pot_files = [
    '/Users/.../nbjs.pot',
    '/Users/.../nbui.pot',
    '/Users/.../notebook.pot'
]
path_to_json = '/Users/.../nbjs.json'
api_key_azure = ''
language = 'nl'

def add_translation_to_pot_file(path_to_file, AzureKey, language='nl'):
    po = polib.pofile(path_to_file)
    for entry in po.untranslated_entries():

        print(entry.msgid)
        text = entry.msgid
        translation = translator.translate(text, AzureKey, language)
        translated_text = translation[0]['translations'][0]['text']
        print(translated_text)

        if len(entry.msgid_plural) == 0:
            entry.msgstr = translated_text
        
        else:
            entry.msgstr_plural[0] = translated_text

            print(entry.msgid_plural)
            text_plural = entry.msgid_plural
            translation_plural = translator.translate(text_plural, AzureKey, language)
            translated_text_plural = translation_plural[0]['translations'][0]['text']
            print(translated_text_plural)

            entry.msgstr_plural[1] = translated_text_plural

    po.save(path_to_file)

def add_to_translations_json(path_to_pot_file, path_to_json):
    with open(path_to_json, 'r') as file_read:
        json_obj = json.load(file_read)
    file_read.close()

    po = polib.pofile(path_to_pot_file)
    for entry in po.translated_entries():

        if len(entry.msgid_plural) == 0:
            json_obj['locale_data']['nbjs'][entry.msgid] = [entry.msgstr]
        else:
            json_obj['locale_data']['nbjs'][entry.msgid] = [msgstr for msgstr in entry.msgstr_plural.values()]
    
    with open(path_to_json, 'w') as file_write:
        json.dump(json_obj, file_write, indent=4,
                 ensure_ascii=False, separators=(',', ': '))
    file_write.close()

for path in path_to_pot_files:
    add_translation_to_pot_file(path, api_key_azure, language)

    add_to_translations_json(path, path_to_json)
