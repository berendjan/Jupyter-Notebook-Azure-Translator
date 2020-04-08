# Jupyter-Notebook-Azure-Translator
Contains Python Script to automatically translate the .pot and .json files necessary for adding other languages.

## NOTES:
The code to generate the `.json` file should de commented out, you need to generate it with the command below in step 13.

### Requirements

- *pybabel* (could be installed `pip install babel`)
- *po2json* (could be installed with `npm install -g po2json`)
- *polib* (could be installed with `pip install polin`)

### Steps

1. Clone this repo to your pc
2. Obtain an API key from [Azure](portal.azure.com) for basic translations. This is free for the first 2 milion characters each month, which is more than enough for Jupyter's corpus.
3. Fill in the Azure key in the main file and change the language to your language.
4. Run main and wait.
5. Change files from `.pot` to `.po`.
6. Open a terminal window and in the notebook folder and do the following 

    `cd notebook/i18n/`
    
7. Find out how the browser accepts your language as a header.
    1. Open a notebook in Google Chrome
    2. inspect page
    3. Go to network
    4. Reload the page
    5. Click on tree in list
    6. Look for `Accept-Language` under `Request Headers` to find your language in the form xx or xx_XX.
8. Add your language in the file `nbjs.json` under *supported languages*.
8. In terminal do: `mkdir xx` or `mkdir xx_XX`.
9. `cd xx` or `cd xx_XX.`
10. `mkdir LC_MESSAGES`
11. `cd LC_MESSAGES`
12. Copy the `.po` files to this folder.
13. Do the following commands in the terminal where ${LANG} is your xx or xx_XX:
```
pybabel compile -D notebook -f -l ${LANG} -i ${LANG}/LC_MESSAGES/notebook.po -o ${LANG}/LC_MESSAGES/notebook.mo
pybabel compile -D nbui -f -l ${LANG} -i ${LANG}/LC_MESSAGES/nbui.po -o ${LANG}/LC_MESSAGES/nbui.mo
po2json -p -F -f jed1.x -d nbjs ${LANG}/LC_MESSAGES/nbjs.po ${LANG}/LC_MESSAGES/nbjs.json
```
14. Done

### Testing

1. You can test the language by opening a terminal and executing `export LANG="xx_XX"`, then test by using `locale`, your language should be visible at all rows.
2. Open Jupyter Notebook as usual with the command `jupyter notebook`.
