# Krushil Desai - Premium Awwwards-Style Portfolio

A cinematic, highly interactive portfolio website built with a Flask (Python) backend and styled using Awwwards-level frontend mechanics. It tells a visual story through smooth animations, horizontal scrolling panels, custom cursor dynamics, and a physics-based tech constellation canvas.

Designed to stand out to engineering leaders and recruiters at Google, Microsoft, Amazon, OpenAI, NVIDIA, and high-growth AI startups.

---

## 🎨 Design Philosophy

- **Vibrant & Asymmetric Layouts**: Swaps template card designs for spacious magazine layouts and high-contrast typography columns.
- **Color Theme**: Ultra-minimal dark theme (deep charcoal black `#070708`) paired with a single vibrant accent: **Neon Acid Lime** (`#ccff00`).
- **Typography Scale**: Generous whitespace with massive editorial header scales (using `Space Grotesk` for numbers and metadata tags and `Inter` for general copy).

---

## ⚡ Animation & Interactive Features

- **Lenis Smooth Scroll**: MOMENTUM scrolling tracker synced directly to GSAP's requestAnimationFrame ticking clock for ultra-smooth 60fps scrolling.
- **Double-Tracking Custom Cursor**: Custom tracking cursor containing a direct dot and a trailing elastic ring (`.cursor-ring`) with lag smoothing. Rings expand, invert, and magnetize to buttons, forms, and navigation nodes (`data-cursor-magnetic`).
- **Cinematic Preloader**: Initial typographic loading screen showing an automated monospaced percentage counter that slides out of view on completion.
- **SplitType Word Reveals**: Extracts sentences and headers into words, revealing characters sequentially on scroll via GSAP ScrollTrigger.
- **Horizontal Scroll Showcase**: Vertically locks the page when entering the `#work` panel and slides slides horizontally through the projects.
- **Interactive Skills Constellation**: Physics-calculated HTML5 `<canvas>` simulation where technical nodes float and connect dynamically, reacting to mouse cursor proximity and gravity.

---

## 🛠️ Project Showcases

1. **Vachnamrut RAG Chatbot**: A LangChain RAG pipeline trained on Swaminarayan scripture, using Chroma DB and Mistral AI's mistral-small model. Served via a premium chat layout.
2. **Gita Semantic Search**: TF-IDF & Cosine Similarity verses retriever featuring custom saffron-and-gold styling parameters, Dharma Wheel loader, and confidence percentage meters.
3. **ClickUp Automation Workflow**: Multi-modal Telegram assistant using Activepieces triggers to convert inputs (voice STT, text, media) into structured ClickUp tasks.
4. **AI Desktop Assistant**: OpenAI-integrated voice assistant built to execute systems queries and commands.
5. **Train Price Predictor**: Analytics pipeline forecasting ticketing prices using Random Forest estimators.

---

## 🚀 Quick Start (Local Development)

### 1. Set Up Virtual Environment

Create and activate a virtual environment using `venv` or `uv`:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate (Mac/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Development Server

```bash
python app.py
```

The application runs locally at `http://localhost:5001`.

---

## ☁️ Vercel Serverless Deployment

This project is preconfigured for serverless execution on Vercel:

1. Install the Vercel CLI: `npm install -g vercel`
2. Run `vercel` in the project root directory and follow the setup wizard.
3. Vercel automatically matches `vercel.json` configurations to build the python runtime and serve your Flask routes.
