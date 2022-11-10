# Rasa-Chatbot

To run this project, you need to download:
- Rasa version 3.1.0 (https://rasa.com/docs/rasa/installation/installing-rasa-open-source)
- Python 3.9.7

(be aware that it is important to follow the steps to activate your conda environment)

When the project is already in your computer, don't forget to do the following change:
- in "config.yml" file, you need to indicate where you saved your word2vec model (line 20, variable cache_dir)

To run this project, you need to open 2 terminals.
In the first terminal, you will run the actions. Write the following command:
- rasa run actions

In the other terminal, run the following command:
- rasa run -m models --enable-api --cors "*"

After, open your project in the right directory. My directory is the following:
- file:///C:/Users/debor/OneDrive/Documentos/faculdade/5%C2%BA%20ano/tese/c%C3%B3digo/RASA/bot2/index.html"

but make sure you indicate the right directory where you saved the index.html file in your computer.

Hope you enjoy :)
