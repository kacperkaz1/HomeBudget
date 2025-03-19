const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Konfiguracja połączenia z bazą MySQL
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'twoje_haslo',  // Zmień na swoje hasło
  database: 'budget_db'
});

db.connect(err => {
  if (err) {
    console.error('Błąd połączenia z bazą danych:', err);
  } else {
    console.log('Połączono z bazą danych MySQL.');
  }
});

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint do pobierania wszystkich transakcji
app.get('/api/transactions', (req, res) => {
  const query = 'SELECT * FROM transactions ORDER BY date DESC';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Błąd podczas pobierania transakcji:', err);
      return res.status(500).json({ message: 'Błąd serwera.' });
    }
    res.json({ transactions: results });
  });
});

// Endpoint do dodawania nowej transakcji
app.post('/api/transaction', (req, res) => {
  const { type, category, amount, description, date } = req.body;
  if (!type || !category || !amount || !date) {
    return res.status(400).json({ message: 'Wszystkie pola oprócz opisu są wymagane.' });
  }
  const query = 'INSERT INTO transactions (type, category, amount, description, date) VALUES (?, ?, ?, ?, ?)';
  db.query(query, [type, category, amount, description, date], (err, results) => {
    if (err) {
      console.error('Błąd podczas dodawania transakcji:', err);
      return res.status(500).json({ message: 'Błąd serwera.' });
    }
    res.json({ message: 'Transakcja została dodana.' });
  });
});

app.listen(port, () => {
  console.log(`Serwer działa na porcie ${port}`);
});
