"""Test per il registro delle sale e le regole sulle date."""

import unittest
from datetime import date

from prenotazioni import (
    Agenda,
    DataNonAmmessa,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        self.oggi = date(2026, 11, 2)

    def _richiesta(self, giorno):
        return Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 8)

    def test_rifiuta_una_sala_con_codice_duplicato(self):
        duplicata = Sala("A2", "Altra aula", 30)

        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(duplicata)

    def test_segnala_una_sala_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("Z9")

    def test_rifiuta_le_date_non_ammesse(self):
        casi = (
            ("data passata", date(2026, 10, 31)),
            ("domenica", date(2026, 11, 8)),
            ("oltre l'orizzonte", date(2027, 1, 2)),
        )
        for motivo, giorno in casi:
            with self.subTest(motivo=motivo, giorno=giorno):
                richiesta = self._richiesta(giorno)

                with self.assertRaises(DataNonAmmessa):
                    self.agenda.prenota(richiesta, oggi=self.oggi)

    def test_accetta_una_prenotazione_per_oggi(self):
        richiesta = self._richiesta(self.oggi)

        identificativo = self.agenda.prenota(richiesta, oggi=self.oggi)

        self.assertIs(self.agenda.prenotazione(identificativo), richiesta)

    def test_prenotazione_segnala_un_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(99)

    def test_cancella_segnala_un_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(99)


if __name__ == "__main__":
    unittest.main()
