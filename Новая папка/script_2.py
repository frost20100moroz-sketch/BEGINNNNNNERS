
# Создам JavaScript файл
js_content = """// TG-CASE 2026 - Main JavaScript

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initModals();
    initChatbot();
    initCaseCards();
    initWebGL();
    initCountdowns();
    initSoundEffects();
    initScrollAnimations();
});

// Navigation
function initNavigation() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-menu a').forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
}

// Modals
function initModals() {
    const loginBtn = document.getElementById('loginBtn');
    const loginModal = document.getElementById('loginModal');
    const closeBtn = loginModal?.querySelector('.modal-close');

    loginBtn?.addEventListener('click', () => {
        loginModal.classList.add('active');
    });

    closeBtn?.addEventListener('click', () => {
        loginModal.classList.remove('active');
    });

    loginModal?.addEventListener('click', (e) => {
        if (e.target === loginModal) {
            loginModal.classList.remove('active');
        }
    });
}

// Chatbot
function initChatbot() {
    const chatbotTrigger = document.getElementById('chatbotTrigger');
    const chatbot = document.getElementById('aiChatbot');
    const chatbotClose = chatbot?.querySelector('.chatbot-close');

    chatbotTrigger?.addEventListener('click', () => {
        chatbot.classList.toggle('active');
    });

    chatbotClose?.addEventListener('click', () => {
        chatbot.classList.remove('active');
    });
}

// Case Cards Interaction
function initCaseCards() {
    const caseCards = document.querySelectorAll('.case-card');
    
    caseCards.forEach(card => {
        // 3D Tilt Effect
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            const caseBox = card.querySelector('.case-box');
            if (caseBox) {
                caseBox.style.transform = \`rotateX(\${rotateX}deg) rotateY(\${rotateY}deg)\`;
            }
        });
        
        card.addEventListener('mouseleave', () => {
            const caseBox = card.querySelector('.case-box');
            if (caseBox) {
                caseBox.style.transform = 'rotateX(0) rotateY(0)';
            }
        });
        
        // Click to open case
        const openBtn = card.querySelector('.btn-open');
        openBtn?.addEventListener('click', (e) => {
            e.stopPropagation();
            openCase(card);
        });
    });
}

// Open Case Animation
function openCase(card) {
    const caseName = card.querySelector('h3')?.textContent || 'Кейс';
    
    // Play sound
    playSound('open');
    
    // Show animation
    card.style.animation = 'case-open 1s ease-out';
    
    setTimeout(() => {
        alert(\`Открытие кейса "\${caseName}"!\\n\\nЭто демо-версия. В реальной версии здесь будет анимация рулетки.\`);
        card.style.animation = '';
    }, 1000);
}

// WebGL Background Effect
function initWebGL() {
    const canvas = document.getElementById('webglCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const particleCount = 100;
    
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.size = Math.random() * 3 + 1;
            this.color = \`hsla(\${Math.random() * 60 + 260}, 80%, 70%, 0.3)\`;
        }
        
        update() {
            this.x += this.vx;
            this.y += this.vy;
            
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
        }
    }
    
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });
        
        // Draw connections
        particles.forEach((p1, i) => {
            particles.slice(i + 1).forEach(p2 => {
                const dx = p1.x - p2.x;
                const dy = p1.y - p2.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                
                if (dist < 150) {
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = \`rgba(139, 92, 246, \${0.2 * (1 - dist / 150)})\`;
                    ctx.stroke();
                }
            });
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
    
    // Resize handler
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// Countdown Timers
function initCountdowns() {
    const countdowns = document.querySelectorAll('.countdown');
    
    countdowns.forEach(countdown => {
        const timer = countdown.dataset.timer;
        let seconds;
        
        switch(timer) {
            case '3d': seconds = 3 * 24 * 60 * 60; break;
            case '24h': seconds = 24 * 60 * 60; break;
            case '7d': seconds = 7 * 24 * 60 * 60; break;
            default: seconds = 0;
        }
        
        function updateCountdown() {
            const hours = Math.floor(seconds / 3600);
            const minutes = Math.floor((seconds % 3600) / 60);
            const secs = seconds % 60;
            
            countdown.textContent = \`\${String(hours).padStart(2, '0')}:\${String(minutes).padStart(2, '0')}:\${String(secs).padStart(2, '0')}\`;
            
            if (seconds > 0) {
                seconds--;
            } else {
                seconds = timer === '3d' ? 259200 : timer === '24h' ? 86400 : 604800;
            }
        }
        
        updateCountdown();
        setInterval(updateCountdown, 1000);
    });
}

// Sound Effects
const sounds = {
    hover: new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBTGH0fPTgjMGHm7A7+OZSA0PVKzn77BdGAg+m9zzxXIn'),
    open: new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBTGH0fPTgjMGHm7A7+OZSA0PVKzn77BdGAg+m9zzxXIn')
};

function initSoundEffects() {
    document.querySelectorAll('[data-sound]').forEach(element => {
        element.addEventListener('mouseenter', () => {
            playSound('hover');
        });
    });
}

function playSound(name) {
    const sound = sounds[name];
    if (sound) {
        sound.currentTime = 0;
        sound.volume = 0.1;
        sound.play().catch(() => {});
    }
}

// Scroll Animations
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fade-in-up 0.6s ease-out forwards';
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.section').forEach(section => {
        observer.observe(section);
    });
}

// Magnetic Cursor Effect
document.addEventListener('mousemove', (e) => {
    const cursor = document.createElement('div');
    cursor.className = 'cursor-particle';
    cursor.style.left = e.pageX + 'px';
    cursor.style.top = e.pageY + 'px';
    document.body.appendChild(cursor);
    
    setTimeout(() => cursor.remove(), 500);
});

// CSS Animation
const style = document.createElement('style');
style.textContent = \`
    @keyframes fade-in-up {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes case-open {
        0% { transform: scale(1) rotateY(0); }
        50% { transform: scale(1.2) rotateY(180deg); }
        100% { transform: scale(1) rotateY(360deg); }
    }
    
    .cursor-particle {
        position: absolute;
        width: 5px;
        height: 5px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.8), transparent);
        border-radius: 50%;
        pointer-events: none;
        animation: particle-fade 0.5s ease-out forwards;
    }
    
    @keyframes particle-fade {
        to {
            opacity: 0;
            transform: scale(2);
        }
    }
\`;
document.head.appendChild(style);

console.log('🎮 TG-CASE 2026 initialized successfully!');
"""

print("JavaScript файл создан")
print("Размер JS:", len(js_content), "байт")
