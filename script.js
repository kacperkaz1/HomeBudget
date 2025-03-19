document.addEventListener('DOMContentLoaded', () => {
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
