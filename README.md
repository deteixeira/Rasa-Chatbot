# Rasa-Chatbot

To run this project, you need to download:
- Rasa version 3.1.0 (https://rasa.com/docs/rasa/installation/installing-rasa-open-source)
- Python 3.9.7

(be aware that it is important to follow the steps to activate your conda environment. You can follow this tutorial if you need any help: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

When the project is already in your computer, don't forget to do the following change:
- in "config.yml" file, you need to indicate where you saved your word2vec model (line 20, variable cache_dir)

If you don't have your own word2vec model, you can use mine that is present in the "w2c" folder. If you want to use a model with more training data, you can also download the wor2vec model from Google: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g . This model is explained in https://code.google.com/archive/p/word2vec/

To run this project, you need to open 2 terminals.
In the first terminal, you will run the actions that are present in file "actions.py". Write the following command to run the actions:
- rasa run actions

In the other terminal, you need to start the rasa server. To do that, run the following command:
- rasa run -m models --enable-api --cors "\*"
This command not only starts the rasa server, but also starts the web server API (using --enable-api) and allows an URL to make requests to the server (using --cors "\*")

After, open your project in the right directory. My directory is the following:
- file:///C:/Users/debor/OneDrive/Documentos/faculdade/5%C2%BA%20ano/tese/c%C3%B3digo/RASA/bot2/index.html"

but make sure you indicate the right directory where you saved the index.html file in your computer.

Hope you enjoy :)
