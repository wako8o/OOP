#!/bin/bash
# =============================================================================
#  terminal_setup.sh  —  GNOME Terminal Персонализация
# =============================================================================
#
#  Какво прави:
#    1. Инсталира шрифта JetBrains Mono (ако не е наличен)
#    2. Задава цветова схема Catppuccin Mocha в GNOME Terminal
#         Фон      : #1E1E2E  (тъмно синьо-лилаво)
#         Текст    : #CDD6F4  (светло синьо)
#         Курсор   : #F5E0DC  (розово)
#    3. Добавя красив bash prompt в ~/.bashrc:
#         [14:32:05] потребител@хост ~/проект (main)
#         $
#
#  Употреба:
#    chmod +x terminal_setup.sh
#    ./terminal_setup.sh
#
#  Изисквания:
#    - Linux с GNOME Terminal
#    - dconf (apt install dconf-cli)
# =============================================================================

# ── Цветове за изхода на самия скрипт ─────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'
RESET='\033[0m'

ok()      { echo -e "${GREEN}  ✔  $*${RESET}"; }
info()    { echo -e "${CYAN}  ➜  $*${RESET}"; }
warn()    { echo -e "${YELLOW}  ⚠  $*${RESET}"; }
err()     { echo -e "${RED}  ✖  $*${RESET}" >&2; }
section() { echo -e "\n${BOLD}${MAGENTA}▶  $*${RESET}"; }

# ── Банер ─────────────────────────────────────────────────────────────────────
echo -e "${BOLD}${CYAN}"
cat << 'BANNER'
  ╔══════════════════════════════════════════════════════╗
  ║   🖥️   GNOME Terminal Персонализация                  ║
  ║   Тема  : Catppuccin Mocha (тъмна)                   ║
  ║   Шрифт : JetBrains Mono 12                          ║
  ║   Prompt: [час] потребител@хост директория (git)     ║
  ╚══════════════════════════════════════════════════════╝
BANNER
echo -e "${RESET}"

# ── 1. Проверка на изисквания ──────────────────────────────────────────────────
section "1. Проверка на изисквания"

if ! command -v gnome-terminal &>/dev/null; then
    err "GNOME Terminal не е намерен. Инсталирайте го и опитайте отново."
    exit 1
fi
ok "GNOME Terminal е намерен"

if ! command -v dconf &>/dev/null; then
    warn "dconf не е намерен — опитвам инсталация..."
    if command -v apt-get &>/dev/null; then
        sudo apt-get install -y dconf-cli || { err "Неуспешно: sudo apt install dconf-cli"; exit 1; }
    else
        err "Моля, инсталирайте dconf ръчно и пуснете скрипта отново."
        exit 1
    fi
fi
ok "dconf е наличен"

# ── 2. Шрифт: JetBrains Mono ──────────────────────────────────────────────────
section "2. Шрифт: JetBrains Mono"

FONT_NAME="Monospace 12"
if fc-list 2>/dev/null | grep -qi "JetBrains Mono"; then
    ok "JetBrains Mono вече е инсталиран"
    FONT_NAME="JetBrains Mono 12"
else
    info "Инсталиране на fonts-jetbrains-mono..."
    INSTALLED=false
    if command -v apt-get &>/dev/null; then
        sudo apt-get install -y fonts-jetbrains-mono 2>/dev/null && INSTALLED=true
    elif command -v dnf &>/dev/null; then
        sudo dnf install -y jetbrains-mono-fonts 2>/dev/null && INSTALLED=true
    elif command -v pacman &>/dev/null; then
        sudo pacman -S --noconfirm ttf-jetbrains-mono 2>/dev/null && INSTALLED=true
    fi

    if [ "$INSTALLED" = true ]; then
        fc-cache -fv &>/dev/null
        ok "JetBrains Mono е инсталиран"
        FONT_NAME="JetBrains Mono 12"
    else
        warn "Не може да се инсталира автоматично — ще се използва 'Monospace 12'"
        info "Ръчна инсталация: https://www.jetbrains.com/lp/mono/"
    fi
fi

# ── 3. GNOME Terminal: Цветова схема Catppuccin Mocha ─────────────────────────
section "3. GNOME Terminal — Catppuccin Mocha цветова схема"

PROFILE=""
if command -v gsettings &>/dev/null; then
    PROFILE=$(gsettings get org.gnome.Terminal.ProfilesList default 2>/dev/null | tr -d "' ")
fi
if [ -z "$PROFILE" ]; then
    PROFILE=$(dconf read /org/gnome/terminal/legacy/profiles:/default 2>/dev/null | tr -d "' ")
fi
if [ -z "$PROFILE" ]; then
    PROFILE=$(dconf list /org/gnome/terminal/legacy/profiles:/ 2>/dev/null | grep '^:' | head -1 | tr -d ':/')
fi

if [ -z "$PROFILE" ]; then
    warn "Не може да се намери GNOME Terminal профил."
    warn "Цветовете и шрифтът ще трябва да се зададат ръчно от Edit → Preferences."
else
    info "Профил: ${PROFILE}"
    DP="/org/gnome/terminal/legacy/profiles:/:${PROFILE}"

    # Catppuccin Mocha — 16-цветна палитра
    PALETTE="['#45475A', '#F38BA8', '#A6E3A1', '#F9E2AF', '#89B4FA', '#F5C2E7', '#94E2D5', '#BAC2DE', '#585B70', '#F38BA8', '#A6E3A1', '#F9E2AF', '#89B4FA', '#F5C2E7', '#94E2D5', '#A6ADC8']"

    dconf write "${DP}/background-color"          "'#1E1E2E'"
    dconf write "${DP}/foreground-color"          "'#CDD6F4'"
    dconf write "${DP}/bold-color"                "'#CDD6F4'"
    dconf write "${DP}/cursor-background-color"   "'#F5E0DC'"
    dconf write "${DP}/cursor-foreground-color"   "'#1E1E2E'"
    dconf write "${DP}/highlight-background-color" "'#585B70'"
    dconf write "${DP}/highlight-foreground-color" "'#CDD6F4'"
    dconf write "${DP}/palette"                   "${PALETTE}"
    dconf write "${DP}/use-theme-colors"          "false"
    dconf write "${DP}/bold-color-same-as-fg"     "true"
    dconf write "${DP}/bold-is-bright"            "true"
    dconf write "${DP}/cursor-colors-set"         "true"
    dconf write "${DP}/highlight-colors-set"      "true"
    dconf write "${DP}/use-system-font"           "false"
    dconf write "${DP}/font"                      "'${FONT_NAME}'"

    ok "Цветова схема: Catppuccin Mocha ✓"
    ok "Шрифт: ${FONT_NAME} ✓"
fi

# ── 4. Bash Prompt ─────────────────────────────────────────────────────────────
section "4. Bash Prompt (~/.bashrc)"

BASHRC="${HOME}/.bashrc"
MARKER="# >>> terminal_setup: custom prompt <<<"

if grep -q "${MARKER}" "${BASHRC}" 2>/dev/null; then
    warn "Prompt конфигурацията вече съществува в ~/.bashrc"
    info "За повторна инсталация изтрийте блока между маркерите и пуснете скрипта отново."
else
    # Резервно копие на .bashrc
    if [ -f "${BASHRC}" ]; then
        BACKUP="${BASHRC}.backup.$(date +%Y%m%d_%H%M%S)"
        if cp "${BASHRC}" "${BACKUP}"; then
            ok "Резервно копие: ${BACKUP}"
        else
            warn "Не може да се направи резервно копие на ~/.bashrc — продължаване без backup"
        fi
    fi

    # Добавяме конфигурацията на prompt-а
    cat >> "${BASHRC}" << 'PROMPT_BLOCK'

# >>> terminal_setup: custom prompt <<<
# Красив bash prompt: [час] потребител@хост директория (git-клон)
# Генериран от terminal_setup.sh  —  https://github.com/wako8o/OOP

# Показва активния git клон (с цвят, съвместимо с readline)
_git_branch_prompt() {
    local branch
    branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
    [ -n "$branch" ] && printf ' \001\033[0;33m\002(%s)\001\033[0m\002' "$branch"
}

# Prompt на два реда:
#   Ред 1: [14:32:05] потребител@хост ~/директория (main)
#   Ред 2: $
PS1='\[\033[0;36m\][\t]\[\033[0m\]'          # [час]  в синьо-зелено
PS1+=' \[\033[1;32m\]\u@\h\[\033[0m\]'       # потребител@хост  в зелено
PS1+=' \[\033[0;34m\]\w\[\033[0m\]'          # ~/директория  в синьо
PS1+='$(_git_branch_prompt)'                 # (git-клон)  в жълто
PS1+='\n\[\033[1;37m\]\$\[\033[0m\] '        # нов ред, после $

# <<< terminal_setup: custom prompt <<<
PROMPT_BLOCK

    ok "Bash prompt е добавен в ~/.bashrc"
fi

# ── 5. Активиране на prompt-а в текущата сесия ────────────────────────────────
# shellcheck source=/dev/null
if grep -q "${MARKER}" "${BASHRC}" 2>/dev/null; then
    # shellcheck disable=SC1090
    source "${BASHRC}" 2>/dev/null || true
fi

# ── 6. Готово ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}"
cat << 'DONE'
  ╔══════════════════════════════════════════════════════╗
  ║   ✅  Готово!                                         ║
  ╠══════════════════════════════════════════════════════╣
  ║  Следващи стъпки:                                    ║
  ║   1.  source ~/.bashrc        ← активира prompt-а   ║
  ║   2.  Затвори и отвори нов    ← активира цветовете  ║
  ║       прозорец на терминала     и шрифта             ║
  ╚══════════════════════════════════════════════════════╝
DONE
echo -e "${RESET}"

info "Как ще изглежда prompt-ът ти:"
echo -e "  ${CYAN}[$(date +%H:%M:%S)]${RESET} ${BOLD}${GREEN}$(whoami)@$(hostname)${RESET} ${BLUE}~/projects/OOP${RESET} ${YELLOW}(main)${RESET}"
echo -e "  ${BOLD}${WHITE:-\033[1;37m}\$${RESET} _"
echo ""
info "Цветова схема Catppuccin Mocha:"
echo -e "  Фон     : ${BOLD}#1E1E2E${RESET}   Текст  : ${BOLD}#CDD6F4${RESET}"
echo -e "  Червено : ${RED}#F38BA8${RESET}   Зелено : ${GREEN}#A6E3A1${RESET}"
echo -e "  Жълто   : ${YELLOW}#F9E2AF${RESET}   Синьо  : ${BLUE}#89B4FA${RESET}"
echo -e "  Лилаво  : ${MAGENTA}#F5C2E7${RESET}   Циан   : ${CYAN}#94E2D5${RESET}"
echo ""
