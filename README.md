# TyzenControl

## Über
Tyzen Control ist ein in Python geschriebenes Projekt zur Remotesteuerung verschiedener Samsung Fernseher mit TyzenOS als Betriebsystem. Ziel der Anwendung ist es verschiedene Aspekte des jeweiligen Gerätes über's Netzwerk zu steuern. Das Projekt bietet somit eine Grundlage für verschiedene Automatisierungsmöglichkeiten (z.B. von Zeitschaltungen etc.).

## Umsetzung
Das Projekt bedient sich der Samsung eigenen Web API, um Aktionen auszuführen. Dafür muss zunächst einmalig ein Token zur Validierung gespeichert werden. Anschließend kann mit dem Gerät dann über Websockets kommuniziert werden.

---

## Funktionen
Nachahmen einer Fernbedienung mit dessen Funktionstasten:
> Remote.sendkey(key: Str, times: int)

Einschalten des Fernsehers über WakeOnLan:
> Remote.turn_on()

## "tyzen_cli.py" als CLI-Anwendung
Senden einer Taste einer Fernbedienung:
> python3 tyzen_cli.py remote KEY TIMES

| Parameter | Beschreibung                                              |
|-----------|-----------------------------------------------------------|
| KEY       | Die zusendene Taste (z.B. "KEY_VOLUP")                    |
| TIMES     | Angabe wie oft die Taste gesendet werden soll (DEAFULT=1) |

Einschalten des Fernsehers:
> python3 tyzen_cli.py turnon

---

## Dependencies

Python modules:
wakeonlan, requests, websocket-client

