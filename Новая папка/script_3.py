
import zipfile
from io import BytesIO

# Создам полный ZIP архив со всеми файлами
zip_buffer = BytesIO()

with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    # Добавляю index.html
    zip_file.writestr('index.html', index_html)
    
    # Добавляю CSS
    zip_file.writestr('assets/css/styles.css', css_content)
    
    # Добавляю JS
    zip_file.writestr('assets/js/app.js', js_content)
    
    # Создам остальные HTML страницы
    
    # top.html
    top_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Топ игроков - TG-CASE 2026</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo"><h1 class="logo-text">TG-CASE</h1></div>
        <ul class="nav-menu">
            <li><a href="index.html">Главная</a></li>
            <li><a href="top.html" class="active">Топ</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="upgrader.html">Upgrader</a></li>
            <li><a href="profile.html">Профиль</a></li>
        </ul>
        <button class="btn-login" id="loginBtn">Войти</button>
    </nav>

    <section class="section">
        <h1 class="section-title">Топ пользователей</h1>
        <div class="leaderboard">
            <div class="leader-item top-1">
                <span class="rank">🥇 Топ-1</span>
                <span class="name">Санитар</span>
                <span class="stats">Выиграл 335369 ⭐ | Кейсов: 117</span>
            </div>
            <div class="leader-item top-2">
                <span class="rank">🥈 Топ-2</span>
                <span class="name">Игрок</span>
                <span class="stats">Выиграл 86482 ⭐ | Кейсов: 116</span>
            </div>
            <div class="leader-item top-3">
                <span class="rank">🥉 Топ-3</span>
                <span class="name">Виталий 1</span>
                <span class="stats">Выиграл 81546 ⭐ | Кейсов: 116</span>
            </div>
            <div class="leader-item">
                <span class="rank">4</span>
                <span class="name">Счастье-Которое Ты-Упустил</span>
                <span class="stats">Выиграл 79487 ⭐ | Кейсов: 113</span>
            </div>
            <div class="leader-item">
                <span class="rank">5</span>
                <span class="name">Мила</span>
                <span class="stats">Выиграл 77696 ⭐ | Кейсов: 112</span>
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>© 2025 tg-case.ru</p>
        <div class="footer-links">
            <a href="#">Пользовательское соглашение</a>
            <a href="#">Privacy Policy</a>
            <a href="faq.html">FAQ</a>
        </div>
    </footer>

    <script src="assets/js/app.js"></script>
</body>
</html>"""
    
    zip_file.writestr('top.html', top_html)
    
    # faq.html
    faq_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ - TG-CASE 2026</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo"><h1 class="logo-text">TG-CASE</h1></div>
        <ul class="nav-menu">
            <li><a href="index.html">Главная</a></li>
            <li><a href="top.html">Топ</a></li>
            <li><a href="faq.html" class="active">FAQ</a></li>
            <li><a href="upgrader.html">Upgrader</a></li>
            <li><a href="profile.html">Профиль</a></li>
        </ul>
        <button class="btn-login" id="loginBtn">Войти</button>
    </nav>

    <section class="section">
        <h1 class="section-title">Часто задаваемые вопросы</h1>
        <div class="faq-container">
            <div class="faq-item">
                <h3>Как вывести подарок?</h3>
                <p>Чтобы вывести подарок, вам нужно зайти в профиль, выбрать подарок, нажать на нём кнопку «Получить» и ввести свой @Username или ссылку на свой Telegram-аккаунт.</p>
            </div>
            <div class="faq-item">
                <h3>Как пополнить баланс на сайте?</h3>
                <p>Для начала авторизуйтесь через Google, ВКонтакте или Telegram в верхнем правом углу, затем нажмите на «+» или «Пополнить баланс». Укажите сумму пополнения. Далее вы будете перенаправлены на сайт, где необходимо выбрать удобный способ оплаты.</p>
            </div>
            <div class="faq-item">
                <h3>Почему нельзя выводить подарок дешевле 15 звезд?</h3>
                <p>Это сделано специально для того, чтобы мы могли быстрее отправлять выигрыши игрокам сайта.</p>
            </div>
            <div class="faq-item">
                <h3>Как открыть бесплатные кейсы?</h3>
                <p>«Каждые 3 дня» можно открыть, если вы пригласили 10 рефералов; «Каждые 7 дней» можно открыть, если вы пополнили баланс не менее чем на 1000 рублей; «Каждые 24 часа» можно открыть, если вы вступили в наш Telegram-канал.</p>
            </div>
            <div class="faq-item">
                <h3>Что за партнёрская программа на вашем сайте?</h3>
                <p>Всё очень просто: Вы отправляете другу свою реферальную ссылку. Он авторизуется на сайте по вашей ссылке и становится вашим рефералом. 🎁 Вы оба получаете по одному подарку.</p>
            </div>
            <div class="faq-item">
                <h3>В течение какого времени ко мне придёт подарок?</h3>
                <p>Обычно наша команда выводит подарок в Telegram в течение 24 часов.</p>
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>© 2025 tg-case.ru</p>
        <div class="footer-links">
            <a href="#">Пользовательское соглашение</a>
            <a href="#">Privacy Policy</a>
            <a href="faq.html">FAQ</a>
        </div>
    </footer>

    <script src="assets/js/app.js"></script>
</body>
</html>"""
    
    zip_file.writestr('faq.html', faq_html)
    
    # upgrader.html
    upgrader_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upgrader - TG-CASE 2026</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo"><h1 class="logo-text">TG-CASE</h1></div>
        <ul class="nav-menu">
            <li><a href="index.html">Главная</a></li>
            <li><a href="top.html">Топ</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="upgrader.html" class="active">Upgrader</a></li>
            <li><a href="profile.html">Профиль</a></li>
        </ul>
        <button class="btn-login" id="loginBtn">Войти</button>
    </nav>

    <section class="section">
        <h1 class="section-title">Апгрейд предметов</h1>
        <div class="upgrader-container">
            <div class="upgrade-box">
                <h3>ВАШ ПРЕДМЕТ</h3>
                <div class="item-slot" id="sourceItem">
                    <p>Выберите предмет с вашего инвентаря</p>
                </div>
            </div>
            <div class="upgrade-arrow">➜</div>
            <div class="upgrade-box">
                <h3>ПРЕДМЕТ ДЛЯ АПГРЕЙДА</h3>
                <div class="item-slot" id="targetItem">
                    <p>Выберите предмет для апгрейда</p>
                </div>
            </div>
        </div>
        <div class="upgrade-stats">
            <div class="stat">
                <span>ШАНС</span>
                <span id="chance">0%</span>
            </div>
            <div class="stat">
                <span>КОЭФФИЦИЕНТ</span>
                <span id="coefficient">0x</span>
            </div>
        </div>
        <button class="btn-upgrade">АПГРЕЙД</button>
    </section>

    <footer class="footer">
        <p>© 2025 tg-case.ru</p>
        <div class="footer-links">
            <a href="#">Пользовательское соглашение</a>
            <a href="#">Privacy Policy</a>
            <a href="faq.html">FAQ</a>
        </div>
    </footer>

    <script src="assets/js/app.js"></script>
</body>
</html>"""
    
    zip_file.writestr('upgrader.html', upgrader_html)
    
    # profile.html
    profile_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Профиль - TG-CASE 2026</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo"><h1 class="logo-text">TG-CASE</h1></div>
        <ul class="nav-menu">
            <li><a href="index.html">Главная</a></li>
            <li><a href="top.html">Топ</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="upgrader.html">Upgrader</a></li>
            <li><a href="profile.html" class="active">Профиль</a></li>
        </ul>
        <button class="btn-login" id="loginBtn">Войти</button>
    </nav>

    <section class="section">
        <h1 class="section-title">Мой профиль</h1>
        <div class="profile-info">
            <div class="balance">
                <h3>Баланс</h3>
                <p class="balance-amount">2100 ⭐</p>
                <button class="btn-deposit">+ Пополнить</button>
            </div>
        </div>
        <h2 class="section-title">Инвентарь</h2>
        <div class="inventory-grid">
            <div class="inventory-item">
                <h4>Input Key</h4>
                <p class="item-price">2100 ⭐</p>
                <button class="btn-claim">Получить</button>
            </div>
            <div class="inventory-item">
                <h4>Gem Signet</h4>
                <p class="item-price">27700 ⭐</p>
                <button class="btn-claim">Получить</button>
            </div>
            <div class="inventory-item">
                <h4>Stellar Rocket</h4>
                <p class="item-price">11500 ⭐</p>
                <button class="btn-claim">Получить</button>
            </div>
            <div class="inventory-item">
                <h4>Voodoo Doll</h4>
                <p class="item-price">5400 ⭐</p>
                <button class="btn-claim">Получить</button>
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>© 2025 tg-case.ru</p>
        <div class="footer-links">
            <a href="#">Пользовательское соглашение</a>
            <a href="#">Privacy Policy</a>
            <a href="faq.html">FAQ</a>
        </div>
    </footer>

    <script src="assets/js/app.js"></script>
</body>
</html>"""
    
    zip_file.writestr('profile.html', profile_html)
    
    # Добавляю дополнительные CSS стили для страниц
    additional_css = """
/* Additional Styles for Pages */

.leaderboard {
    max-width: 800px;
    margin: 0 auto;
}

.leader-item {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
}

.leader-item:hover {
    transform: translateX(10px);
    border-color: var(--primary);
}

.leader-item.top-1 {
    background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 215, 0, 0.05));
    border-color: #FFD700;
}

.leader-item.top-2 {
    background: linear-gradient(135deg, rgba(192, 192, 192, 0.1), rgba(192, 192, 192, 0.05));
    border-color: #C0C0C0;
}

.leader-item.top-3 {
    background: linear-gradient(135deg, rgba(205, 127, 50, 0.1), rgba(205, 127, 50, 0.05));
    border-color: #CD7F32;
}

.faq-container {
    max-width: 800px;
    margin: 0 auto;
}

.faq-item {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    transition: all 0.3s ease;
}

.faq-item:hover {
    border-color: var(--primary);
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.3);
}

.faq-item h3 {
    color: var(--primary-light);
    margin-bottom: 1rem;
}

.upgrader-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    margin: 3rem 0;
    flex-wrap: wrap;
}

.upgrade-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    min-width: 250px;
}

.item-slot {
    min-height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.3);
    border-radius: 15px;
    margin-top: 1rem;
    border: 2px dashed rgba(255, 255, 255, 0.2);
}

.upgrade-arrow {
    font-size: 3rem;
    color: var(--primary);
}

.upgrade-stats {
    display: flex;
    justify-content: center;
    gap: 4rem;
    margin: 2rem 0;
}

.upgrade-stats .stat {
    text-align: center;
}

.upgrade-stats .stat span:first-child {
    display: block;
    color: var(--text-gray);
    margin-bottom: 0.5rem;
}

.upgrade-stats .stat span:last-child {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-light);
}

.btn-upgrade {
    display: block;
    margin: 2rem auto;
    padding: 1.5rem 4rem;
    background: var(--gradient-primary);
    border: none;
    border-radius: 50px;
    color: white;
    font-size: 1.2rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-upgrade:hover {
    transform: scale(1.05);
    box-shadow: 0 15px 40px rgba(139, 92, 246, 0.6);
}

.profile-info {
    max-width: 400px;
    margin: 2rem auto;
}

.balance {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
}

.balance-amount {
    font-size: 3rem;
    font-weight: 700;
    color: var(--secondary-light);
    margin: 1rem 0;
}

.btn-deposit {
    padding: 1rem 3rem;
    background: var(--gradient-secondary);
    border: none;
    border-radius: 50px;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-deposit:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(6, 182, 212, 0.5);
}

.inventory-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.inventory-item {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
}

.inventory-item:hover {
    transform: translateY(-5px);
    border-color: var(--primary);
}

.item-price {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent-light);
    margin: 1rem 0;
}

.btn-claim {
    width: 100%;
    padding: 1rem;
    background: var(--gradient-accent);
    border: none;
    border-radius: 50px;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-claim:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(236, 72, 153, 0.5);
}
"""
    
    zip_file.writestr('assets/css/additional.css', additional_css)
    
    # README файл
    readme = """# TG-CASE 2026 - Современный сайт для открытия кейсов

## Описание
Футуристический сайт для открытия кейсов с подарками, выполненный в стиле 2026 года с применением самых современных трендов веб-дизайна.

## Структура проекта

```
tg-case-2026/
├── index.html          # Главная страница
├── top.html            # Топ игроков
├── faq.html            # Часто задаваемые вопросы
├── upgrader.html       # Апгрейд предметов
├── profile.html        # Профиль пользователя
├── assets/
│   ├── css/
│   │   ├── styles.css       # Основные стили
│   │   └── additional.css   # Дополнительные стили
│   └── js/
│       └── app.js           # Основной JavaScript
└── README.md           # Этот файл
```

## Особенности дизайна 2026

✨ **Визуальные эффекты:**
- 3D WebGL анимации и частицы на фоне
- Holographic градиенты на NFT кейсах
- Neon glow эффекты на заголовках и кнопках
- Glassmorphism на карточках
- Neo-brutalism элементы

🎮 **Интерактивность:**
- Magnetic cursor trails
- Микро-анимации на всех элементах
- Scroll-triggered animations
- 3D hover эффекты на кейсах
- Tactile feedback на кнопках

🎨 **Цветовая схема:**
- Electric Purple (#8B5CF6)
- Neon Cyan (#06B6D4)
- Hot Pink (#EC4899)
- Deep Dark Background (#0F0F1E)

🔊 **Звуковой дизайн:**
- Audio cues при hover
- Звуки открытия кейсов
- Ambient фоновый звук (опционально)

## Установка и запуск

1. Распакуйте архив в любую папку
2. Откройте index.html в современном браузере (Chrome, Firefox, Edge)
3. Для локального сервера (опционально):
   ```bash
   python -m http.server 8000
   ```
   Затем откройте http://localhost:8000

## Требования

- Современный браузер с поддержкой:
  - CSS Grid & Flexbox
  - CSS Backdrop Filter
  - CSS Custom Properties (Variables)
  - Canvas API
  - ES6+ JavaScript

## Технологии

- HTML5
- CSS3 (Variable Fonts, Gradients, Animations)
- Vanilla JavaScript (ES6+)
- Canvas API для WebGL эффектов
- Google Fonts (Space Grotesk, Inter)

## Адаптивность

Сайт полностью адаптирован для:
- Desktop (1920px+)
- Laptop (1366px+)
- Tablet (768px+)
- Mobile (320px+)

## Браузерная совместимость

✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+

## Лицензия

© 2025 TG-CASE.ru
Все права защищены.

## Контакты

Website: https://tg-case.ru
Telegram: @tgcase_support

---

**Создано с использованием передовых технологий веб-дизайна 2026 года** 🚀
"""
    
    zip_file.writestr('README.md', readme)

# Сохраняю ZIP файл
zip_buffer.seek(0)
with open('tg-case-2026-full.zip', 'wb') as f:
    f.write(zip_buffer.read())

print("✅ Полный пакет сайта создан!")
print("\n📦 Содержимое архива:")
print("   - index.html (главная страница)")
print("   - top.html (топ игроков)")
print("   - faq.html (FAQ)")
print("   - upgrader.html (апгрейдер)")
print("   - profile.html (профиль)")
print("   - assets/css/styles.css (основные стили)")
print("   - assets/css/additional.css (дополнительные стили)")
print("   - assets/js/app.js (JavaScript)")
print("   - README.md (инструкция)")
print("\n📁 Размер архива:", len(zip_buffer.getvalue()), "байт")
print("\n🚀 Готово к развертыванию!")
