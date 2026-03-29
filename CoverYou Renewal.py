import streamlit as st

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CoverYou Thank You</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --coral: #f15e4a;
    --coral-light: #f47a6b;
    --coral-dim: rgba(241,94,74,0.12);
    --dark: #0d0e10;
    --dark2: #14161a;
    --dark3: #1c1f24;
    --dark4: #252930;
    --border: rgba(255,255,255,0.07);
    --text: #f0eee8;
    --muted: #9a9590;
    --serif: 'Playfair Display', Georgia, serif;
    --sans: 'DM Sans', system-ui, sans-serif;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--dark);
    color: var(--text);
    font-family: var(--sans);
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
  }

  /* Grain overlay */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
  }


  /* Glow blob */
  .glow {
    position: fixed;
    top: -200px;
    right: -200px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(241,94,74,0.15) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }

  /* ---- HEADER ---- */
  header {
    position: relative;
    z-index: 1;
    padding: 28px 40px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid var(--border);
  }

  .logo {
    display: flex;
    align-items: center;
    text-decoration: none;
  }

  /* ---- HERO ---- */
  .hero {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin: 0 auto;
    padding: 80px 32px 60px;
    text-align: center;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--coral-dim);
    border: 1px solid rgba(241,94,74,0.25);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 12px;
    font-weight: 500;
    color: var(--coral-light);
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 32px;
    animation: fadeUp 0.6s ease both;
  }

  .badge-dot {
    width: 6px;
    height: 6px;
    background: var(--coral);
    border-radius: 50%;
    animation: pulse 2s ease infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.85); }
  }

  .hero h1 {
    font-family: var(--serif);
    font-size: clamp(36px, 6vw, 58px);
    font-weight: 700;
    line-height: 1.15;
    letter-spacing: -1px;
    margin-bottom: 20px;
    color: #ffffff;
    animation: fadeUp 0.7s 0.1s ease both;
  }

  .hero h1 em {
    font-style: normal;
    color: var(--coral);
  }

  .hero p {
    font-size: 17px;
    font-weight: 300;
    color: var(--muted);
    line-height: 1.75;
    max-width: 520px;
    margin: 0 auto 44px;
    animation: fadeUp 0.7s 0.2s ease both;
  }

  /* ---- DIVIDER ---- */
  .divider {
    position: relative;
    z-index: 1;
    max-width: 640px;
    margin: 0 auto;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
  }

  /* ---- STEPS ---- */
  .steps-section {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin: 0 auto;
    padding: 60px 32px 80px;
  }

  .steps-label {
    text-align: center;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 40px;
  }

  .steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
  }

  .step {
    background: var(--dark2);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 24px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.2s;
    animation: fadeUp 0.6s ease both;
  }

  .step:nth-child(1) { animation-delay: 0.4s; }
  .step:nth-child(2) { animation-delay: 0.5s; }
  .step:nth-child(3) { animation-delay: 0.6s; }

  .step:hover {
    border-color: rgba(241,94,74,0.3);
    transform: translateY(-3px);
  }

  .step::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--coral);
    opacity: 0;
    transition: opacity 0.2s;
  }

  .step:hover::before { opacity: 1; }

  .step-num {
    font-family: var(--serif);
    font-size: 38px;
    font-weight: 700;
    color: var(--dark3);
    line-height: 1;
    margin-bottom: 16px;
    -webkit-text-stroke: 1px rgba(241,94,74,0.25);
  }

  .step h3 {
    font-family: var(--sans);
    font-size: 15px;
    font-weight: 500;
    color: var(--text);
    margin-bottom: 8px;
  }

  .step p {
    font-size: 13px;
    font-weight: 300;
    color: var(--muted);
    line-height: 1.6;
  }

  /* ---- TRUST BAR ---- */
  .trust {
    position: relative;
    z-index: 1;
    background: var(--dark2);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    padding: 28px 40px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 32px;
    animation: fadeUp 0.6s 0.7s ease both;
  }

  .trust-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: var(--muted);
  }

  .trust-item svg { flex-shrink: 0; }

  /* ---- FOOTER ---- */
  footer {
    position: relative;
    z-index: 1;
    padding: 32px 40px;
    text-align: center;
    font-size: 12px;
    color: var(--muted);
    opacity: 0.7;
  }

  /* ---- ANIMATIONS ---- */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ---- RESPONSIVE ---- */
  @media (max-width: 520px) {
    header { padding: 20px 20px; }
    .hero { padding: 56px 20px 44px; }
    .steps-section { padding: 44px 20px 60px; }
    .trust { padding: 24px 20px; gap: 20px; }
    footer { padding: 24px 20px; }
  }
</style>
</head>
<body>

<div class="glow"></div>

<!-- Header -->
<header>
  <a href="#" class="logo">
    <img src=https://www.coveryou.in/images/svg/footer-logo.svg alt="CoverYou" style="height:60px;width:auto;object-fit:contain;" />
  </a>
</header>

<!-- Hero -->
<section class="hero">
  <div class="badge">
    <div class="badge-dot"></div>
    Always Here For You
  </div>

  <h1>Thank you for<br>reaching out to <em>CoverYou.</em></h1>

  <p>It means a lot that you chose CoverYou. Your dedicated Relationship Manager will personally reach out to you within 24 hours to guide you every step of the way.</p>

</section>

<div class="divider"></div>

<!-- Steps -->
<section class="steps-section">
  <div class="steps-label">What happens next</div>
  <div class="steps">
    <div class="step">
      <div class="step-num">01</div>
      <h3>We review your enquiry</h3>
      <p>We believe in complete transparency — every step of your renewal journey is shared openly with you, so you're always in the know.</p>
    </div>
    <div class="step">
      <div class="step-num">02</div>
      <h3>We review your renewal</h3>
      <p>We carefully assess your existing policy, identify any gaps, and ensure your renewal is smooth, timely, and always in your best interest.</p>
    </div>
    <div class="step">
      <div class="step-num">03</div>
      <h3>Your RM connects with you</h3>
      <p>Your dedicated Relationship Manager personally reaches out to guide you with the right plan.</p>
    </div>
  </div>
</section>

<!-- Trust Bar -->
<div class="trust">
  <div class="trust-item">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
      <path d="M8 1L9.5 5.5H14.5L10.5 8.5L12 13L8 10L4 13L5.5 8.5L1.5 5.5H6.5L8 1Z" fill="#f15e4a" fill-opacity="0.8"/>
    </svg>
    Specialists in doctor coverage
  </div>
  <div class="trust-item">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
      <circle cx="8" cy="8" r="6" stroke="#f15e4a" stroke-opacity="0.8" stroke-width="1.5"/>
      <path d="M5.5 8L7 9.5L10.5 6" stroke="#f15e4a" stroke-opacity="0.8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    Your RM connects within 24 hours
  </div>
  <div class="trust-item">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
      <rect x="3" y="5" width="10" height="8" rx="2" stroke="#f15e4a" stroke-opacity="0.8" stroke-width="1.5"/>
      <path d="M5.5 5V3.5C5.5 2.67 6.17 2 7 2H9C9.83 2 10.5 2.67 10.5 3.5V5" stroke="#f15e4a" stroke-opacity="0.8" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    100% confidential &amp; secure
  </div>
</div>

<!-- Footer -->
<footer>
  &copy; 2026 CoverYou. All rights reserved. &nbsp;|&nbsp; Doctor Insurance Solutions
</footer>

</body>
</html>
