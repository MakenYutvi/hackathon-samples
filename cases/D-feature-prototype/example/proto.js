// Лёгкий клиентский JS для lo-fi прототипа. Без библиотек и сборки.

// 1) Кликабельные элементы с data-href (строки таблицы, карточки)
document.querySelectorAll('[data-href]').forEach(function (el) {
  el.style.cursor = 'pointer';
  el.addEventListener('click', function () {
    window.location.href = el.getAttribute('data-href');
  });
});

// 2) Живая фильтрация списка по селектам
function val(id) {
  var e = document.getElementById(id);
  return e ? e.value : 'Все';
}

function applyFilters() {
  var ch = val('f-channel'), ow = val('f-owner'), st = val('f-status');
  var shown = 0;
  document.querySelectorAll('tbody tr[data-channel]').forEach(function (tr) {
    var ok = (ch === 'Все' || tr.dataset.channel === ch) &&
             (ow === 'Все' || tr.dataset.owner === ow) &&
             (st === 'Все' || tr.dataset.status === st);
    tr.style.display = ok ? '' : 'none';
    if (ok) shown++;
  });
  var c = document.getElementById('result-count');
  if (c) c.textContent = shown;
}

['f-channel', 'f-owner', 'f-status'].forEach(function (id) {
  var e = document.getElementById(id);
  if (e) e.addEventListener('change', applyFilters);
});
