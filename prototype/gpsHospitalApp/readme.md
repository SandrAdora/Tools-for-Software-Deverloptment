## Indoor GPS für Krankhäuser
## Medic Care Mobile Applikation

Dies ist eine Indoor-GPS-Anwendung (Global Position System) für Krankenhäuser. Sie wurde speziell für Mitarbeiter in der Intensivstation entwickelt. Sie soll ihnen helfen, Patienten in der Intensivpflege leichter und zeiteffizient zu ihren bevorstehenden Untersuchungen zu bewegen.

Die Anwendung ruft Informationen über einen *Patienten, der auf eine Untersuchung wartet* aus der Datenbank ab und listet alle für den Tag erforderlichen Untersuchungen auf.

# Spezifikationen 
Die Applikation verwendet für die Standortermittlung das WLan des Krankenhaus. Später wird die Standortermittlung detalierter, und Mobilfunkmasten werden stattdessen verwendet. 

# Technologie-Stack:
- *Flutter* – für die mobile Benutzeroberfläche.
- *Python* – für Backend-Logik und Datenverarbeitung.
- *C++* – für Algorithmen zur Positionsbestimmung.
- *MySQL* (phpMyAdmin) 
    – zur Speicherung der Positionsdaten
    _ Speicherung der Patienten Daten 


# Tree
- Frontend
    - Lib
        main
- Backend