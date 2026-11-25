"""Test per la validazione e la durata di una prenotazione."""

import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def setUp(self):
        self.giorno = date(2026, 11, 3)

    def test_rifiuta_orari_non_ammessi(self):
        casi = (
            ("passo non valido", "09:15", "10:00"),
            ("prima dell'apertura", "07:30", "09:00"),
            ("dopo la chiusura", "19:30", "20:30"),
            ("orari uguali", "10:00", "10:00"),
            ("fine prima dell'inizio", "11:00", "10:00"),
        )
        for motivo, inizio, fine in casi:
            with self.subTest(motivo=motivo, inizio=inizio, fine=fine):
                with self.assertRaises(ValueError):
                    Prenotazione("A2", self.giorno, inizio, fine, "Rossi", 8)

    def test_rifiuta_un_giorno_che_non_e_una_data(self):
        giorno = "2026-11-03"

        with self.assertRaises(TypeError):
            Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 8)

    def test_calcola_la_durata_in_minuti(self):
        prenotazione = Prenotazione("A2", self.giorno, "09:00", "10:30", "Rossi", 8)

        durata = prenotazione.durata_minuti()

        self.assertEqual(durata, 90)


if __name__ == "__main__":
    unittest.main()
