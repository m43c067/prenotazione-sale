"""Test di regressione per i difetti segnalati dalla segreteria."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def setUp(self):
        self.oggi = date(2026, 11, 2)
        self.martedi = date(2026, 11, 3)
        self.agenda = Agenda()

    def test_prenota_fasce_contigue_nella_stessa_sala(self):
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        prima = Prenotazione("A2", self.martedi, "09:00", "10:00", "Rossi", 8)
        seconda = Prenotazione("A2", self.martedi, "10:00", "11:00", "Bianchi", 8)
        self.agenda.prenota(prima, oggi=self.oggi)

        identificativo = self.agenda.prenota(seconda, oggi=self.oggi)

        self.assertIs(self.agenda.prenotazione(identificativo), seconda)

    def test_prenota_con_partecipanti_pari_alla_capienza(self):
        self.agenda.aggiungi_sala(Sala("R1", "Sala riunioni", 10))
        richiesta = Prenotazione("R1", self.martedi, "09:00", "10:00", "Rossi", 10)

        identificativo = self.agenda.prenota(richiesta, oggi=self.oggi)

        self.assertIs(self.agenda.prenotazione(identificativo), richiesta)


if __name__ == "__main__":
    unittest.main()
