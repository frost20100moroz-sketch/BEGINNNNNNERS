
# Создам CSS файл
css_content = """/* TG-CASE 2026 - Styles */

/* Imports */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* Reset & Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary: #8B5CF6;
    --primary-light: #A855F7;
    --secondary: #06B6D4;
    --secondary-light: #22D3EE;
    --accent: #EC4899;
    --accent-light: #F472B6;
    --bg-dark: #0F0F1E;
    --bg-darker: #0A0A14;
    --text-white: #FFFFFF;
    --text-gray: #A0A0B0;
    --gradient-primary: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    --gradient-secondary: linear-gradient(135deg, var(--secondary) 0%, var(--secondary-light) 100%);
    --gradient-accent: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
    --gradient-holographic: linear-gradient(135deg, #FF006E 0%, #8338EC 25%, #3A86FF 50%, #06FFA5 75%, #FFD60A 100%);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg-dark);
    color: var(--text-white);
    line-height: 1.6;
    overflow-x: hidden;
    position: relative;
}

body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at 20% 50%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

/* Navigation */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 5%;
    background: rgba(15, 15, 30, 0.7);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    background: var(--gradient-holographic);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 30px rgba(139, 92, 246, 0.5);
    animation: glow-pulse 3s ease-in-out infinite;
}

@keyframes glow-pulse {
    0%, 100% { filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.6)); }
    50% { filter: drop-shadow(0 0 40px rgba(139, 92, 246, 0.9)); }
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    color: var(--text-white);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s ease;
    position: relative;
}

.nav-menu a::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gradient-primary);
    transition: width 0.3s ease;
}

.nav-menu a:hover::after,
.nav-menu a.active::after {
    width: 100%;
}

.btn-login {
    padding: 0.75rem 2rem;
    background: var(--gradient-primary);
    border: none;
    border-radius: 50px;
    color: var(--text-white);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(139, 92, 246, 0.4);
}

.btn-login:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.6);
}

/* Hero Section */
.hero {
    min-height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    padding: 4rem 5%;
}

#webglCanvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.hero-content {
    text-align: center;
    z-index: 1;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(3rem, 10vw, 8rem);
    font-weight: 700;
    background: var(--gradient-holographic);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
    position: relative;
    animation: title-entrance 1s ease-out;
}

@keyframes title-entrance {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-subtitle {
    font-size: 1.5rem;
    color: var(--text-gray);
    margin-bottom: 3rem;
    animation: subtitle-entrance 1s ease-out 0.3s backwards;
}

@keyframes subtitle-entrance {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-stats {
    display: flex;
    gap: 3rem;
    justify-content: center;
    flex-wrap: wrap;
}

.stat-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    color: var(--text-gray);
    font-size: 1rem;
}

/* Section */
.section {
    padding: 5rem 5%;
    position: relative;
    z-index: 1;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 700;
    text-align: center;
    margin-bottom: 3rem;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 30px rgba(139, 92, 246, 0.5);
}

/* Cases Grid */
.cases-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 2rem;
}

.cases-grid.free {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.cases-grid.nft {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* Case Card */
.case-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}

.case-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.2) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.5s ease;
}

.case-card:hover::before {
    opacity: 1;
}

.case-card:hover {
    transform: translateY(-10px);
    border-color: var(--primary);
    box-shadow: 0 20px 60px rgba(139, 92, 246, 0.4);
}

.case-badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: var(--gradient-accent);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.875rem;
}

.popular-badge {
    background: var(--gradient-holographic) !important;
    animation: badge-pulse 2s ease-in-out infinite;
}

@keyframes badge-pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

.case-3d {
    width: 150px;
    height: 150px;
    margin: 1rem auto;
    perspective: 1000px;
}

.case-box {
    width: 100%;
    height: 100%;
    background: var(--gradient-primary);
    border-radius: 15px;
    transform-style: preserve-3d;
    transition: transform 0.6s ease;
    box-shadow: 0 10px 40px rgba(139, 92, 246, 0.5);
}

.case-card:hover .case-box {
    transform: rotateY(20deg) rotateX(20deg);
}

.case-card h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    margin: 1rem 0;
}

.case-price {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 1rem 0;
    color: var(--secondary-light);
}

.old-price {
    text-decoration: line-through;
    color: var(--text-gray);
    font-size: 1rem;
    margin-right: 0.5rem;
}

.btn-open {
    width: 100%;
    padding: 1rem;
    background: var(--gradient-primary);
    border: none;
    border-radius: 50px;
    color: var(--text-white);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 1rem;
}

.btn-open:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.6);
}

/* NFT Card */
.nft-card {
    position: relative;
}

.holographic-border {
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: var(--gradient-holographic);
    border-radius: 20px;
    z-index: -1;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.nft-card:hover .holographic-border {
    opacity: 1;
    animation: rotate-border 3s linear infinite;
}

@keyframes rotate-border {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* Free Case Countdown */
.countdown {
    font-family: 'Space Grotesk', monospace;
    font-size: 1.5rem;
    color: var(--accent-light);
    margin: 1rem 0;
    font-weight: 700;
}

.case-condition {
    color: var(--text-gray);
    font-size: 0.875rem;
    margin: 0.5rem 0;
}

.case-icon {
    font-size: 4rem;
    margin: 1rem 0;
}

/* AI Chatbot */
.ai-chatbot {
    position: fixed;
    bottom: 100px;
    right: 30px;
    width: 350px;
    background: rgba(15, 15, 30, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    display: none;
    flex-direction: column;
    z-index: 9999;
}

.ai-chatbot.active {
    display: flex;
}

.chatbot-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background: var(--gradient-primary);
    border-radius: 20px 20px 0 0;
    font-weight: 600;
}

.chatbot-close {
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
}

.chatbot-body {
    padding: 1.5rem;
    min-height: 200px;
}

.chatbot-trigger {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--gradient-primary);
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.5);
    z-index: 9998;
    transition: all 0.3s ease;
}

.chatbot-trigger:hover {
    transform: scale(1.1);
}

/* Footer */
.footer {
    text-align: center;
    padding: 3rem 5%;
    background: rgba(10, 10, 20, 0.8);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    margin-top: 5rem;
}

.footer-links {
    display: flex;
    gap: 2rem;
    justify-content: center;
    margin-top: 1rem;
    flex-wrap: wrap;
}

.footer-links a {
    color: var(--text-gray);
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-links a:hover {
    color: var(--primary-light);
}

/* Modal */
.modal {
    display: none;
    position: fixed;
    z-index: 10000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
}

.modal.active {
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-content {
    background: rgba(15, 15, 30, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 3rem;
    max-width: 400px;
    width: 90%;
    position: relative;
}

.modal-close {
    position: absolute;
    top: 1rem;
    right: 1.5rem;
    font-size: 2rem;
    cursor: pointer;
    color: var(--text-gray);
    transition: color 0.3s ease;
}

.modal-close:hover {
    color: var(--text-white);
}

.login-buttons {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 2rem;
}

.btn-social {
    padding: 1rem;
    border: none;
    border-radius: 50px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-social.google {
    background: #DB4437;
    color: white;
}

.btn-social.vk {
    background: #0077FF;
    color: white;
}

.btn-social.telegram {
    background: #0088CC;
    color: white;
}

.btn-social:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

/* Responsive */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-menu {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }
    
    .hero-stats {
        gap: 1.5rem;
    }
    
    .cases-grid {
        grid-template-columns: 1fr;
    }
    
    .ai-chatbot {
        width: calc(100% - 40px);
        right: 20px;
    }
}

/* Animations */
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

/* Cursor Effect */
body {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><circle cx="16" cy="16" r="8" fill="%238B5CF6" opacity="0.6"/></svg>'), auto;
}
"""

print("CSS файл создан")
print("Размер CSS:", len(css_content), "байт")
