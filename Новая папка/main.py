#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TG-CASE 2026 - Main Application File
Основной файл приложения для локального запуска и тестирования
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path
import json
import datetime

# Конфигурация
CONFIG = {
    'host': 'localhost',
    'port': 8000,
    'auto_open': True,
    'debug': True,
    'site_name': 'TG-CASE 2026',
    'version': '1.0.0'
}

class TGCaseHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Кастомный HTTP handler для сайта TG-CASE"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

    def end_headers(self):
        # Добавляем CORS заголовки для разработки
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

        # Кеширование для статических файлов
        if self.path.endswith(('.css', '.js', '.png', '.jpg', '.ico')):
            self.send_header('Cache-Control', 'public, max-age=31536000')
        else:
            self.send_header('Cache-Control', 'no-cache')

        super().end_headers()

    def do_GET(self):
        # Логирование запросов
        if CONFIG['debug']:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] GET {self.path}")

        # Обработка корневого пути
        if self.path == '/':
            self.path = '/index.html'

        super().do_GET()

    def log_message(self, format, *args):
        # Кастомное логирование
        if CONFIG['debug']:
            print(f"[SERVER] {format % args}")

def check_files():
    """Проверка наличия необходимых файлов"""
    required_files = [
        'index.html',
        'assets/css/styles.css',
        'assets/js/app.js'
    ]

    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)

    if missing_files:
        print("❌ Отсутствуют необходимые файлы:")
        for file in missing_files:
            print(f"   - {file}")
        print("\n💡 Убедитесь, что распаковали архив с сайтом в текущую папку")
        return False

    return True

def show_server_info():
    """Показать информацию о сервере"""
    print("=" * 60)
    print(f"🚀 {CONFIG['site_name']} v{CONFIG['version']}")
    print("=" * 60)
    print(f"📍 Адрес сервера: http://{CONFIG['host']}:{CONFIG['port']}")
    print(f"📁 Корневая папка: {os.getcwd()}")
    print(f"🌐 Автооткрытие браузера: {'Да' if CONFIG['auto_open'] else 'Нет'}")
    print(f"🐛 Режим отладки: {'Включен' if CONFIG['debug'] else 'Выключен'}")
    print("=" * 60)
    print("\n📋 Доступные страницы:")
    pages = [
        ("Главная", "/"),
        ("Топ игроков", "/top.html"),
        ("FAQ", "/faq.html"),
        ("Upgrader", "/upgrader.html"),
        ("Профиль", "/profile.html")
    ]

    for name, path in pages:
        print(f"   • {name}: http://{CONFIG['host']}:{CONFIG['port']}{path}")

    print("\n⌨️  Команды управления:")
    print("   • Ctrl+C - остановить сервер")
    print("   • r + Enter - перезапустить")
    print("   • o + Enter - открыть в браузере")
    print("   • q + Enter - выйти")
    print("=" * 60)

def start_server():
    """Запуск веб-сервера"""
    try:
        with socketserver.TCPServer((CONFIG['host'], CONFIG['port']), TGCaseHTTPRequestHandler) as httpd:
            show_server_info()

            # Автооткрытие браузера
            if CONFIG['auto_open']:
                url = f"http://{CONFIG['host']}:{CONFIG['port']}"
                try:
                    webbrowser.open(url)
                    print(f"🌐 Браузер открыт: {url}")
                except Exception as e:
                    print(f"⚠️  Не удалось открыть браузер: {e}")

            print(f"\n✅ Сервер запущен успешно!")
            print("   Нажмите Ctrl+C для остановки\n")

            # Запуск сервера
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n\n🛑 Сервер остановлен пользователем")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Порт {CONFIG['port']} уже используется!")
            print("💡 Попробуйте другой порт или закройте другой сервер")
        else:
            print(f"❌ Ошибка сервера: {e}")
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")

def setup_environment():
    """Настройка окружения"""
    # Создание папок если их нет
    os.makedirs('assets/css', exist_ok=True)
    os.makedirs('assets/js', exist_ok=True)
    os.makedirs('assets/images', exist_ok=True)

    # Создание .gitignore если его нет
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Temporary files
*.tmp
*.temp
"""

    if not Path('.gitignore').exists():
        with open('.gitignore', 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        print("📝 Создан файл .gitignore")

def interactive_mode():
    """Интерактивный режим управления"""
    while True:
        try:
            command = input("\n> ").strip().lower()

            if command == 'q':
                print("👋 До свидания!")
                break
            elif command == 'r':
                print("🔄 Перезапуск сервера...")
                start_server()
            elif command == 'o':
                url = f"http://{CONFIG['host']}:{CONFIG['port']}"
                webbrowser.open(url)
                print(f"🌐 Открыто в браузере: {url}")
            elif command == 'help' or command == 'h':
                print("\n📋 Доступные команды:")
                print("   • r - перезапустить сервер")
                print("   • o - открыть в браузере")
                print("   • q - выйти")
                print("   • help - показать помощь")
            else:
                print("❓ Неизвестная команда. Введите 'help' для справки")

        except KeyboardInterrupt:
            print("\n👋 До свидания!")
            break
        except EOFError:
            print("\n👋 До свидания!")
            break

def main():
    """Главная функция"""
    print("🎮 Запуск TG-CASE 2026 Development Server...")

    # Проверка Python версии
    if sys.version_info < (3, 6):
        print("❌ Требуется Python 3.6 или выше")
        print(f"   Текущая версия: {sys.version}")
        sys.exit(1)

    # Настройка окружения
    setup_environment()

    # Проверка файлов
    if not check_files():
        sys.exit(1)

    print("✅ Все файлы найдены")

    # Обработка аргументов командной строки
    if len(sys.argv) > 1:
        if '--port' in sys.argv:
            port_index = sys.argv.index('--port') + 1
            if port_index < len(sys.argv):
                try:
                    CONFIG['port'] = int(sys.argv[port_index])
                except ValueError:
                    print("❌ Неверный формат порта")
                    sys.exit(1)

        if '--no-browser' in sys.argv:
            CONFIG['auto_open'] = False

        if '--debug' in sys.argv:
            CONFIG['debug'] = True

    # Запуск сервера
    start_server()

    # Интерактивный режим после остановки сервера
    interactive_mode()

if __name__ == '__main__':
    main()
