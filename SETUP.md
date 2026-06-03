# Шаг 0. Настройка окружения

Прогоните это **первым делом** в Codex или Claude на своём ноутбуке — до кейсов. Агент сам проверит, чего не хватает, поставит недостающее, настроит Git и доступ к GitHub и в конце покажет чек-лист. Цель — чтобы у всех было одинаковое окружение и все 4 кейса прошли без сюрпризов.

Что должно оказаться установлено: **Git**, **Python 3 + pip**, **ripgrep**, **Node** (обычно уже есть), **GitHub CLI (gh)**, и Python-пакеты **openpyxl** и **pandas**.

Скопируйте промпт под свою ОС целиком и вставьте в агента.

## Windows

```text
Ты — мой помощник по настройке рабочего окружения на этом компьютере (Windows). Цель: подготовить машину к AI-хакатону, чтобы без проблем прошли практические кейсы из репозитория https://github.com/MakenYutvi/hackathon-samples (чтение кода, анализ CSV и выгрузка в Excel, разбор транскриптов, кликабельный HTML-прототип) и работа с личным репозиторием через Git/GitHub.

Правила: действуй по шагам; перед каждой установкой коротко объясни, что и зачем ставишь, и покажи команду до запуска. Ничего не ломай из уже установленного (Codex/Claude, Node, существующий Python) — ставь только то, чего нет. Где можно — без админ-прав. Если после установки команда не видна (PATH ещё не обновился), скажи мне переоткрыть терминал/агента и повтори проверку.

1. Подтверди, что ОС — Windows, и проверь, что уже стоит (выведи версии или "нет"): git, python (или py), rg (ripgrep), node, gh (GitHub CLI), а также winget --version.
2. Установи недостающее через winget (только отсутствующее):
   - Git:        winget install --id Git.Git -e
   - Python 3:   winget install --id Python.Python.3.12 -e
   - ripgrep:    winget install --id BurntSushi.ripgrep.MSVC -e
   - GitHub CLI: winget install --id GitHub.cli -e
   - Node.js (только если node отсутствует): winget install --id OpenJS.NodeJS.LTS -e
3. Настрой Git identity (спроси у меня имя и email, если они ещё не заданы):
   git config --global user.name "Имя Фамилия"
   git config --global user.email "you@example.com"
   git config --global init.defaultBranch main
4. Настрой доступ к GitHub: запусти gh auth login (выбор: GitHub.com → HTTPS → вход через браузер), затем gh auth setup-git, чтобы git использовал gh для аутентификации. Вход в браузере я пройду сам.
5. Поставь Python-пакеты для кейсов: python -m pip install --user --upgrade pip openpyxl pandas
   (openpyxl — выгрузка отчёта в Excel; pandas — анализ данных).
6. Финальная проверка — выведи единый чек-лист со статусом и версиями:
   git --version; python --version; rg --version; node --version; gh --version; gh auth status;
   python -c "import openpyxl, pandas; print('py-deps ok')";
   git config --global user.name; git config --global user.email.
   Отметь, что готово, и явно перечисли, что не удалось и что мне сделать (например, переоткрыть терминал).

Опционально (только если я попрошу — чтобы реально запускать приложение из кейса A): python -m pip install --user flask pytest.
```

## macOS

```text
Ты — мой помощник по настройке рабочего окружения на этом компьютере (macOS). Цель: подготовить машину к AI-хакатону, чтобы без проблем прошли практические кейсы из https://github.com/MakenYutvi/hackathon-samples (чтение кода, анализ CSV и выгрузка в Excel, разбор транскриптов, кликабельный HTML-прототип) и работа с Git/GitHub.

Правила: действуй по шагам; перед каждой установкой коротко объясни, что и зачем, и покажи команду до запуска. Ничего не ломай из уже установленного (Codex/Claude, Node, системный Python) — ставь только то, чего нет. Используй Homebrew как пакетный менеджер. Если понадобится пароль администратора или установка Xcode Command Line Tools — предупреди меня.

1. Подтверди, что ОС — macOS, и проверь, что уже стоит (версии или "нет"): git, python3 (и pip3), rg (ripgrep), node, gh (GitHub CLI), brew.
2. Если Homebrew не установлен — установи: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   После установки добавь brew в PATH (на Apple Silicon: eval "$(/opt/homebrew/bin/brew shellenv)" и пропиши это в ~/.zprofile). При запросе согласись на установку Command Line Tools.
3. Установи недостающее через brew (только отсутствующее): brew install git python ripgrep gh
   и brew install node (только если node отсутствует).
4. Настрой Git identity (спроси имя и email, если ещё не заданы):
   git config --global user.name "Имя Фамилия"
   git config --global user.email "you@example.com"
   git config --global init.defaultBranch main
5. Настрой доступ к GitHub: gh auth login (GitHub.com → HTTPS → вход через браузер), затем gh auth setup-git. Вход в браузере я пройду сам.
6. Поставь Python-пакеты: python3 -m pip install --user --upgrade openpyxl pandas
   Если pip заблокирован политикой "externally managed environment" (PEP 668) — выбери безопасный способ (pipx или отдельный venv; --break-system-packages только крайним вариантом) и скажи мне, что именно сделал.
7. Финальная проверка — единый чек-лист с версиями:
   git --version; python3 --version; rg --version; node --version; gh --version; gh auth status;
   python3 -c "import openpyxl, pandas; print('py-deps ok')";
   git config --global user.name; git config --global user.email.
   Отметь готовое и перечисли, что не удалось и что мне сделать.

Опционально (если попрошу — запускать app кейса A): python3 -m pip install --user flask pytest.
```

## Если что-то не встало

- Команда не находится сразу после установки — **переоткройте терминал/агента** (обновляется PATH) и повторите проверку.
- Нет `winget` (старая Windows) — поставьте «App Installer» из Microsoft Store или Git вручную: https://git-scm.com/download/win
- Нет `brew` и установка не идёт — Homebrew: https://brew.sh
- Не получилось — не страшно: на встрече есть технический буфер, разберём вместе или поработаете в паре.
