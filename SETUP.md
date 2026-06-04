# Шаг 0. Настройка окружения

Прогоните это **первым делом** в Codex или Claude на своём ноутбуке — до кейсов. Агент сам проверит, чего не хватает, поставит недостающее для практики и подготовит Git/SSH к первому push личной KB. Цель — чтобы участникам не пришлось разбираться с Git руками.

Что должно оказаться установлено: **Python 3 + pip**, **ripgrep**, **Node** (обычно уже есть), **Git** для первого commit/push, и Python-пакеты **openpyxl** и **pandas**. GitHub CLI не обязателен: основной auth-путь — SSH key.

Важно для личного `lastname-kb`: основной сценарий встречи — `Use this template -> Private repo -> Code -> Download ZIP -> unzip -> open folder in Codex -> Codex показывает SSH public key -> участник добавляет key в GitHub -> Codex делает первый commit/push`.

Скопируйте промпт под свою ОС целиком и вставьте в агента.

## Windows

```text
Ты — мой помощник по настройке рабочего окружения на этом компьютере (Windows). Цель: подготовить машину к AI-хакатону, чтобы без проблем прошли практические кейсы из репозитория https://github.com/MakenYutvi/hackathon-samples (чтение кода, анализ CSV и выгрузка в Excel, разбор транскриптов, кликабельный HTML-прототип) и работа с личной KB-папкой в Codex.

Правила: действуй по шагам; перед каждой установкой коротко объясни, что и зачем ставишь, и покажи команду до запуска. Ничего не ломай из уже установленного (Codex/Claude, Node, существующий Python) — ставь только то, чего нет. Где можно — без админ-прав. Если после установки команда не видна (PATH ещё не обновился), скажи мне переоткрыть терминал/агента и повтори проверку. Если команда `python` не работает или открывает Microsoft Store, используй вместо неё `py` (например `py -m pip ...`, `py -c ...`) — это штатный лаунчер Python на Windows.

1. Подтверди, что ОС — Windows, и проверь, что уже стоит (выведи версии или "нет"): git, python (или py), rg (ripgrep), node, а также winget --version.
2. Установи недостающее через winget (только отсутствующее):
   - Python 3:   winget install --id Python.Python.3.12 -e
   - ripgrep:    winget install --id BurntSushi.ripgrep.MSVC -e
   - Git:        winget install --id Git.Git -e
   - Node.js (только если node отсутствует): winget install --id OpenJS.NodeJS.LTS -e
3. Объясни правило для личного repo: после `Use this template` выбрать `Private`, затем `Code -> Download ZIP`, распаковать папку и открыть её в Codex. Дальше Codex должен показать SSH public key, попросить добавить его в GitHub и запросить SSH URL/name/email для первого commit/push.
4. Поставь Python-пакеты для кейсов: python -m pip install --user --upgrade pip openpyxl pandas
   (openpyxl — выгрузка отчёта в Excel; pandas — анализ данных).
5. Финальная проверка — выведи единый чек-лист со статусом и версиями (если `python` не работает, используй `py`):
   git --version; python --version (или py --version); rg --version; node --version;
   python -c "import openpyxl, pandas; print('py-deps ok')" (или py -c "...");
   Отметь, что готово, и явно перечисли, что не удалось и что мне сделать (например, переоткрыть терминал).
6. Если Git установлен, проверь наличие SSH public key для GitHub; если ключа нет, создай ed25519 SSH key без passphrase и покажи public key одной строкой. Не проси GitHub CLI, если SSH key подходит.

Опционально (только если я попрошу — чтобы реально запускать приложение из кейса A): python -m pip install --user flask pytest.
```

## macOS

```text
Ты — мой помощник по настройке рабочего окружения на этом компьютере (macOS). Цель: подготовить машину к AI-хакатону, чтобы без проблем прошли практические кейсы из https://github.com/MakenYutvi/hackathon-samples (чтение кода, анализ CSV и выгрузка в Excel, разбор транскриптов, кликабельный HTML-прототип) и работа с личной KB-папкой в Codex.

Правила: действуй по шагам; перед каждой установкой коротко объясни, что и зачем, и покажи команду до запуска. Ничего не ломай из уже установленного (Codex/Claude, Node, системный Python) — ставь только то, чего нет. Используй Homebrew как пакетный менеджер. Если понадобится пароль администратора или установка Xcode Command Line Tools — предупреди меня.

1. Подтверди, что ОС — macOS, и проверь, что уже стоит (версии или "нет"): git, python3 (и pip3), rg (ripgrep), node, brew.
2. Если Homebrew не установлен — установи: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   После установки добавь brew в PATH (на Apple Silicon: eval "$(/opt/homebrew/bin/brew shellenv)" и пропиши это в ~/.zprofile). При запросе согласись на установку Command Line Tools.
3. Установи недостающее через brew (только отсутствующее): brew install git python ripgrep
   и brew install node (только если node отсутствует).
4. Объясни правило для личного repo: после `Use this template` выбрать `Private`, затем `Code -> Download ZIP`, распаковать папку и открыть её в Codex. Дальше Codex должен показать SSH public key, попросить добавить его в GitHub и запросить SSH URL/name/email для первого commit/push.
5. Поставь Python-пакеты: python3 -m pip install --user --upgrade openpyxl pandas
   Если pip заблокирован политикой "externally managed environment" (PEP 668) — выбери безопасный способ (pipx или отдельный venv; --break-system-packages только крайним вариантом) и скажи мне, что именно сделал.
6. Финальная проверка — единый чек-лист с версиями:
   git --version; python3 --version; rg --version; node --version;
   python3 -c "import openpyxl, pandas; print('py-deps ok')";
   Отметь готовое и перечисли, что не удалось и что мне сделать.
7. Если Git установлен, проверь наличие SSH public key для GitHub; если ключа нет, создай ed25519 SSH key без passphrase и покажи public key одной строкой. Не проси GitHub CLI, если SSH key подходит.

Опционально (если попрошу — запускать app кейса A): python3 -m pip install --user flask pytest.
```

## Если что-то не встало

- Команда не находится сразу после установки — **переоткройте терминал/агента** (обновляется PATH) и повторите проверку.
- Нет `winget` (старая Windows) — поставьте «App Installer» из Microsoft Store или установите Python/ripgrep вручную.
- Нет `brew` и установка не идёт — Homebrew: https://brew.sh
- Не получилось — не страшно: на встрече есть технический буфер, разберём вместе или поработаете в паре.
