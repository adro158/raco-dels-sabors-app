# El Racó dels Sabors - Sistema de Gestió i Predicció

Aquesta aplicació web és un sistema de gestió (CRUD) desenvolupat per al restaurant "El Racó dels Sabors". L'objectiu principal és gestionar la carta de plats i simular una predicció de la demanda diària per optimitzar recursos i reduir el malbaratament alimentari.

## Eines utilitzades i/o provades

* **Llenguatge principal:** Python 3
* **Framework Web:** Django
* **Base de Dades:** SQLite (integrada per defecte amb Django)
* **Control de versions:** Git
* **Entorn virtual:** venv (Python)
* **Front-end:** HTML5 i CSS3 (disseny inspirat en la interfície de Google Cloud Platform)
* **Lògica de negoci:** Algorismes de simulació en Python per replicar el funcionament d'eines d'IA (Vertex AI) aplicades a la predicció de vendes.

## Procés de creació del codi

1. **Configuració de l'entorn:** Creació de l'entorn virtual (`venv`) i instal·lació de Django.
2. **Creació del projecte i l'aplicació:** Inicialització del projecte `nucleo` i l'aplicació `previsiones`.
3. **Modelatge de Dades (Models):** Definició de dues entitats relacionades: `Plato` i `PrevisionDiaria` (relació One-to-Many).
4. **Interfície d'Administració:** Registre dels models al panell d'administrador de Django per a les proves inicials.
5. **Desenvolupament del CRUD (Vistes i URLs):** Programació de les funcions per LLegir, Crear, Editar i Esborrar plats i previsions (`views.py` i `urls.py`).
6. **Simulació d'IA:** Implementació d'una lògica a la vista de creació de previsions que calcula automàticament la demanda suggerida basant-se en el dia de la setmana i festius simulats.
7. **Disseny (Templates):** Creació de les plantilles HTML amb CSS integrat per donar-li un aspecte tecnològic i corporatiu.
8. **Automatització:** Creació d'un script executable (`arrancar.bat`) per facilitar l'inici del servidor.

## Instruccions d'instal·lació

Per executar aquest projecte en un entorn local, segueix aquests passos:

1. Clona aquest repositori al teu ordinador:
```bash
git clone <ENLLAÇ_DEL_TEU_REPOSITORI_AQUÍ>