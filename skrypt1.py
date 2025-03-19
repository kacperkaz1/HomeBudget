import os

def update_file(path, content):
    """Nadpisuje plik 'path' zawartością 'content'."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Zaktualizowano: {path}")

def main():
    # Ścieżka do folderu projektu
    base_dir = 'budget-tracker'
    public_dir = os.path.join(base_dir, 'public')
    os.makedirs(public_dir, exist_ok=True)

    # --- Osadzone obrazy jako SVG w data URI ---
    # Logo – 200x200
    LOGO_BASE64 = (
        "data:image/svg+xml;base64," +
        "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIj4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iI2ZmN2U1ZiIvPgogIDx0ZXh0IHg9IjEwMCIgeT0iMTEwIiBmb250LXNpemU9IjQwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJ3aGl0ZSIgZm9udC1mYW1pbHk9IlBhcGljY29sbyI+TG9nbzwvdGV4dD4KPC9zdmc+"
    )
    # Baner lewy 1 – 150x300, kolor pastelowy, tekst "Baner 1"
    LEFT_1_BASE64 = (
        "data:image/svg+xml;base64," +
        "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTAiIGhlaWdodD0iMzAwIj4KICA8cmVjdCB3aWR0aD0iMTUwIiBoZWlnaHQ9IjMwMCIgZmlsbD0iI2ZlYjQ3YiIvPgogIDx0ZXh0IHg9Ijc1IiB5PSIxNjAiIGZvbnQtc2l6ZT0iMzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IndoaXRlIiBmb250LWZhbWlseT0iUm9ib3RvIj5CYW5lciAxPC90ZXh0Pgo8L3N2Zz4="
    )
    # Baner lewy 2 – 150x300, inny kolor, tekst "Baner 2"
    LEFT_2_BASE64 = (
        "data:image/svg+xml;base64," +
        "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTAiIGhlaWdodD0iMzAwIj4KICA8cmVjdCB3aWR0aD0iMTUwIiBoZWlnaHQ9IjMwMCIgZmlsbD0iI2ZmN2U1ZiIvPgogIDx0ZXh0IHg9Ijc1IiB5PSIxNjAiIGZvbnQtc2l6ZT0iMzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IndoaXRlIiBmb250LWZhbWlseT0iUm9ib3RvIj5CYW5lciAyPC90ZXh0Pgo8L3N2Zz4="
    )
    # Baner prawy 1 – 150x300, niebieski, tekst "Baner 3"
    RIGHT_1_BASE64 = (
        "data:image/svg+xml;base64," +
        "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTAiIGhlaWdodD0iMzAwIj4KICA8cmVjdCB3aWR0aD0iMTUwIiBoZWlnaHQ9IjMwMCIgZmlsbD0iIzAwN0JGRiIvPgogIDx0ZXh0IHg9Ijc1IiB5PSIxNjAiIGZvbnQtc2l6ZT0iMzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IndoaXRlIiBmb250LWZhbWlseT0iUm9ib3RvIj5CYW5lciAzPC90ZXh0Pgo8L3N2Zz4="
    )
    # Baner prawy 2 – 150x300, zielony, tekst "Baner 4"
    RIGHT_2_BASE64 = (
        "data:image/svg+xml;base64," +
        "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTAiIGhlaWdodD0iMzAwIj4KICA8cmVjdCB3aWR0aD0iMTUwIiBoZWlnaHQ9IjMwMCIgZmlsbD0iIzI4YTc0NSIvPgogIDx0ZXh0IHg9Ijc1IiB5PSIxNjAiIGZvbnQtc2l6ZT0iMzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IndoaXRlIiBmb250LWZhbWlseT0iUm9ib3RvIj5CYW5lciA0PC90ZXh0Pgo8L3N2Zz4="
    )

    # --- Zaktualizowana zawartość index.html ---
    index_html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Śledzenie Budżetu Domowego - Osadzone Obrazy</title>
  <!-- Czcionki Google -->
  <link href="https://fonts.googleapis.com/css?family=Pacifico|Roboto:400,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Nagłówek z logo (osadzone w data URI) po lewej oraz nawigacją -->
  <header>
    <div class="top-bar">
      <div class="logo-container">
        <img src="{LOGO_BASE64}" alt="Logo strony" class="logo-ai">
      </div>
      <nav class="main-nav">
        <ul>
          <li><a href="#" data-tab="dashboard" class="active">Dashboard</a></li>
          <li><a href="#" data-tab="add-transaction">Dodaj Transakcję</a></li>
          <li><a href="#" data-tab="reports">Raporty</a></li>
          <li><a href="#" data-tab="settings">Ustawienia</a></li>
          <li><a href="#" data-tab="analytics">Analizy</a></li>
          <li><a href="#" data-tab="categories">Kategorie</a></li>
        </ul>
      </nav>
    </div>
  </header>
  
  <!-- Główny layout z panelami bocznymi -->
  <div class="container">
    <aside class="sidebar left">
      <div class="ad-panel">
        <img src="{LEFT_1_BASE64}" alt="Obraz 1">
      </div>
      <div class="ad-panel">
        <img src="{LEFT_2_BASE64}" alt="Obraz 2">
      </div>
    </aside>
    <main>
      <!-- Sekcja Hero -->
      <section class="hero">
        <div class="hero-overlay"></div>
        <div class="hero-content">
          <h2>Nowoczesne Narzędzie do Zarządzania Finansami</h2>
          <p>Kontroluj swoje wydatki, zarządzaj przychodami i planuj budżet z pasją!</p>
          <button onclick="document.getElementById('dashboard').scrollIntoView({{ behavior: 'smooth' }});">Rozpocznij</button>
        </div>
      </section>
      <!-- Zakładki -->
      <section id="dashboard" class="tab-content">
        <h2>Dashboard</h2>
        <div id="transactions-list">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Typ</th>
                <th>Kategoria</th>
                <th>Kwota</th>
                <th>Opis</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody id="transactions-table-body">
              <!-- Rekordy transakcji – ładowane dynamicznie lub przykładowe -->
            </tbody>
          </table>
        </div>
      </section>
      <section id="add-transaction" class="tab-content" style="display: none;">
        <h2>Dodaj Transakcję</h2>
        <form id="transactionForm">
          <div class="form-group">
            <label for="type">Typ:</label>
            <select id="type" name="type" required>
              <option value="income">Przychód</option>
              <option value="expense">Wydatek</option>
            </select>
          </div>
          <div class="form-group">
            <label for="category">Kategoria:</label>
            <input type="text" id="category" name="category" required>
          </div>
          <div class="form-group">
            <label for="amount">Kwota:</label>
            <input type="number" step="0.01" id="amount" name="amount" required>
          </div>
          <div class="form-group">
            <label for="description">Opis:</label>
            <textarea id="description" name="description"></textarea>
          </div>
          <div class="form-group">
            <label for="date">Data transakcji:</label>
            <input type="date" id="date" name="date" required>
          </div>
          <button type="submit">Dodaj</button>
        </form>
        <div id="formResult"></div>
      </section>
      <section id="reports" class="tab-content" style="display: none;">
        <h2>Raporty</h2>
        <p>
          Tutaj znajdziesz szczegółowe zestawienia finansowe, wykresy przychodów i wydatków oraz narzędzia do generowania raportów okresowych.
        </p>
      </section>
      <section id="settings" class="tab-content" style="display: none;">
        <h2>Ustawienia</h2>
        <p>
          Skonfiguruj aplikację według własnych potrzeb: zmień walutę, format daty, dodaj zabezpieczenia hasłem lub ustaw alerty o przekroczeniu budżetu.
        </p>
      </section>
      <section id="analytics" class="tab-content" style="display: none;">
        <h2>Analizy</h2>
        <p>
          Zaawansowane narzędzia analityczne pomogą Ci śledzić trendy w wydatkach, porównywać przychody i planować przyszłe inwestycje.
        </p>
      </section>
      <section id="categories" class="tab-content" style="display: none;">
        <h2>Kategorie</h2>
        <p>
          Dodawaj, edytuj i usuwaj kategorie transakcji. Organizuj swoje finanse, aby łatwiej je było śledzić i analizować.
        </p>
      </section>
    </main>
    <aside class="sidebar right">
      <div class="ad-panel">
        <img src="{RIGHT_1_BASE64}" alt="Obraz 3">
      </div>
      <div class="ad-panel">
        <img src="{RIGHT_2_BASE64}" alt="Obraz 4">
      </div>
    </aside>
  </div>
  
  <!-- Stopka -->
  <footer>
    <p>&copy; 2025 Śledzenie Budżetu Domowego. Wszelkie prawa zastrzeżone.</p>
    <p>
      Kontakt: <a href="mailto:kontakt@budzet-domowy.pl">kontakt@budzet-domowy.pl</a> | Regulamin | Polityka Prywatności
    </p>
  </footer>
  
  <script src="script.js"></script>
</body>
</html>
"""

    # --- Zawartość style.css ---
    style_css = """/* Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: #e0e0e0;
  color: #333;
}

/* Nagłówek */
.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(135deg, #ff7e5f, #feb47b);
  padding: 10px 20px;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo-ai {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 15px;
}

.main-nav ul {
  list-style: none;
  display: flex;
  gap: 15px;
}

.main-nav ul li a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
  padding: 8px 12px;
  border-radius: 4px;
  transition: background 0.3s;
}

.main-nav ul li a:hover,
.main-nav ul li a.active {
  background: rgba(255, 255, 255, 0.3);
}

/* Layout główny */
.container {
  display: flex;
  max-width: 1200px;
  margin: 20px auto;
  gap: 20px;
}

/* Sidebar */
.sidebar {
  width: 200px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.ad-panel img {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.ad-panel img:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 12px rgba(0,0,0,0.2);
}

/* Główna zawartość */
main {
  flex: 1;
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Sekcja Hero */
.hero {
  position: relative;
  height: 350px;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 30px;
  background: url('https://source.unsplash.com/featured/?finance,city') no-repeat center center/cover;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  animation: pulse 6s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 0.7; }
}

.hero-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #fff;
  text-align: center;
}

.hero-content h2 {
  font-size: 2.2rem;
  margin-bottom: 10px;
}

.hero-content p {
  font-size: 1.1rem;
  margin-bottom: 20px;
}

.hero-content button {
  padding: 10px 25px;
  font-size: 1rem;
  border: none;
  border-radius: 30px;
  background: #ff7e5f;
  color: white;
  cursor: pointer;
  transition: background 0.3s;
}

.hero-content button:hover {
  background: #feb47b;
}

/* Zakładki */
.tab-content {
  margin-top: 20px;
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.tab-content h2 {
  font-size: 1.8rem;
  margin-bottom: 15px;
  border-bottom: 3px solid #ff7e5f;
  padding-bottom: 5px;
}

/* Tabela */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
}

th, td {
  padding: 10px;
  text-align: left;
  border: 1px solid #ddd;
}

th {
  background: #f2f2f2;
}

/* Formularz */
form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  align-self: flex-start;
  padding: 10px 20px;
  background: #ff7e5f;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

form button:hover {
  background: #feb47b;
}

/* Stopka */
footer {
  text-align: center;
  padding: 20px;
  background: #fff;
  border-top: 1px solid #ddd;
  margin-top: 30px;
  font-size: 0.9rem;
  color: #777;
}

footer p {
  margin: 5px 0;
}

footer a {
  color: #ff7e5f;
  text-decoration: none;
  font-weight: bold;
}

footer a:hover {
  text-decoration: underline;
}

/* Responsywność */
@media (max-width: 768px) {
  .top-bar {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .main-nav ul {
    flex-wrap: wrap;
  }

  .container {
    flex-direction: column;
  }

  .sidebar {
    flex-direction: row;
    width: 100%;
    justify-content: space-around;
  }

  main {
    margin-top: 20px;
  }
}
"""

    # --- Zawartość script.js ---
    script_js = """document.addEventListener('DOMContentLoaded', () => {
  // Przełączanie zakładek
  const tabs = document.querySelectorAll('nav ul li a');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabs.forEach(tab => {
    tab.addEventListener('click', (e) => {
      e.preventDefault();
      tabs.forEach(t => t.classList.remove('active'));
      tabContents.forEach(content => content.style.display = 'none');
      
      tab.classList.add('active');
      const tabId = tab.getAttribute('data-tab');
      document.getElementById(tabId).style.display = 'block';
    });
  });
  
  // Wyświetlenie domyślnej zakładki Dashboard
  if (document.querySelector('nav ul li a[data-tab="dashboard"]')) {
    document.querySelector('nav ul li a[data-tab="dashboard"]').classList.add('active');
    document.getElementById('dashboard').style.display = 'block';
  }
  
  // Ładowanie transakcji lub przykładowych rekordów
  loadTransactions();
  
  // Obsługa formularza dodawania transakcji
  const transactionForm = document.getElementById('transactionForm');
  if (transactionForm) {
    transactionForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = {
        type: document.getElementById('type').value,
        category: document.getElementById('category').value,
        amount: parseFloat(document.getElementById('amount').value),
        description: document.getElementById('description').value,
        date: document.getElementById('date').value
      };
  
      fetch('/api/transaction', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(result => {
        const formResult = document.getElementById('formResult');
        formResult.innerHTML = `<p>${result.message}</p>`;
        transactionForm.reset();
        loadTransactions();
      })
      .catch(error => {
        console.error('Błąd:', error);
        document.getElementById('formResult').innerHTML = `<p>Wystąpił błąd podczas dodawania transakcji.</p>`;
      });
    });
  }
});

function loadTransactions() {
  fetch('/api/transactions')
    .then(response => response.json())
    .then(data => {
      const tbody = document.getElementById('transactions-table-body');
      if (!tbody) return;
      tbody.innerHTML = '';
      if (data.transactions && data.transactions.length > 0) {
        data.transactions.forEach(tx => {
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td>${tx.id}</td>
            <td>${tx.type}</td>
            <td>${tx.category}</td>
            <td>${parseFloat(tx.amount).toFixed(2)}</td>
            <td>${tx.description || ''}</td>
            <td>${tx.date}</td>
          `;
          tbody.appendChild(tr);
        });
      } else {
        displaySampleRecords();
      }
    })
    .catch(error => {
      console.error('Błąd podczas ładowania transakcji:', error);
      displaySampleRecords();
    });
}

function displaySampleRecords() {
  const sampleTransactions = [
    { id: 1, type: 'income', category: 'Salary', amount: 5000.00, description: 'Miesięczne wynagrodzenie', date: '2024-01-01' },
    { id: 2, type: 'expense', category: 'Rent', amount: 1500.00, description: 'Czynsz za styczeń', date: '2024-01-03' },
    { id: 3, type: 'expense', category: 'Groceries', amount: 320.75, description: 'Zakupy spożywcze', date: '2024-01-05' },
    { id: 4, type: 'expense', category: 'Utilities', amount: 210.40, description: 'Opłata za media', date: '2024-01-06' },
    { id: 5, type: 'expense', category: 'Transport', amount: 50.00, description: 'Bilety komunikacji miejskiej', date: '2024-01-07' }
  ];
  const tbody = document.getElementById('transactions-table-body');
  if (!tbody) return;
  tbody.innerHTML = '';
  sampleTransactions.forEach(tx => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${tx.id}</td>
      <td>${tx.type}</td>
      <td>${tx.category}</td>
      <td>${parseFloat(tx.amount).toFixed(2)}</td>
      <td>${tx.description || ''}</td>
      <td>${tx.date}</td>
    `;
    tbody.appendChild(tr);
  });
}
"""

    # Nadpisanie plików w folderze public
    update_file(os.path.join(public_dir, 'index.html'), index_html)
    update_file(os.path.join(public_dir, 'style.css'), style_css)
    update_file(os.path.join(public_dir, 'script.js'), script_js)
    
    print("\nAktualizacja zakończona! Otwórz plik index.html w przeglądarce (najlepiej przez lokalny serwer), aby zobaczyć zmiany.")

if __name__ == '__main__':
    main()
