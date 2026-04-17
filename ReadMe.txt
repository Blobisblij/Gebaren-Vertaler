Handleiding voor het starten van handgebaar herkenning

1. Ultraleap Tracking service installeren
    https://www.ultraleap.com/downloads/leap-controller/

2. Python libraries installeren.
    pandas - https://pandas.pydata.org/docs/getting_started/install.html -- pip install pandas
    pytorch - https://pytorch.org/get-started/locally/ (CPU versie) -- pip install torch torchvision
    pywin32 - https://pypi.org/project/pywin32/ -- pip install pywin32

3. Download de ZIP van dit project en un-zip het, dit zou "Gebaren-Vertaler-main" moeten heten

4. Open de map "Gebaren-Vertaler-main" als project in CLion (dit is de IDE die wij gebruikt hebben en waarop deze stappen zijn gebaseerd)

5. open "main.c" in MakeJSON, boven in het scherm komt een melding "This file does not belong to any project target".
    klik op "Fix" > Configure CMake Project > Select CMakeList.txt
    Selecteer nu CMakeList.txt in de MakeJSON folder

    Er is nu een "cmake-build-debug" folder gemaakt

6. Verplaats het "LeapC.dll" bestand naar de "cmake-build-debug" folder

7. Zorg dat de IR Camera aan is gesloten en de Ultraleap Hand Tracking Service aan staat (om dit zeker te weten kun je de ultraleap control panel openen)

8. Start nu het C programma (open main.c en RUN)

9. Om te beginnen zullen nieuwe gebaren gecollect en getraint moeten worden.
    Open NGT_TRANSLATOR.py en RUN.
    Hieruit zal een error komen, in deze error staat de pyton directory.
    In VS Code, copieer het geel gekleurde pad, dit zou ongeveer zo moeten uitzien:
        C:\Users\Gebruiker\AppData\Local\Python\pythoncore-3.14-64\python.exe
    
    Om data te collecten, voer het volgende command uit in de terminal
        [zojuist verkregen pyton directory] NGT_TRANSLATOR.py collect [naam van het gebaar dat je wil collecten]

    Als je al eens gebaren gecollect hebt en opnieuw wil beginnen maak je het gesture-dataset.csv bestand leeg, behalve regel 1 en 2
        f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,label
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    
    Bij het collecten is het belangrijk dat je het gebaar vast houd boven de camera en wat rond beweegt.
    Doe dit voor elk gebaar dat je wil hebben.

    Zodra je de handgebaren hebt gecollect die je wil moet het model getraint worden.
    Voer het command volgende command uit in de terminal
        [pyton directory] NGT_TRANSLATOR.py train
    
    Het model is nu getraint op jou gebaren.

10. Om de herkenning te starten, voer het volgende command uit.
        [python directory] NGT_TRANSLATOR.py run
    



    



