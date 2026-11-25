"""Test di regressione per i difetti segnalati dalla segreteria."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def test_prenota_fasce_contigue_nella_stessa_sala(self):
        oggi = date(2026, 11, 2)
        martedi = date(2026, 11, 3)
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        prima = Prenotazione("A2", martedi, "09:00", "10:00", "Rossi", 8)
        seconda = Prenotazione("A2", martedi, "10:00", "11:00", "Bianchi", 8)
        agenda.prenota(prima, oggi=oggi)

        identificativo = agenda.prenota(seconda, oggi=oggi)

        self.assertIs(agenda.prenotazione(identificativo), seconda)


if __name__ == "__main__":
    unittest.main()
