# Reverse-Engineered Cartelle Framer Architecture Specification
**Source Target:** `https://gregarious-pages-565888.framer.app/shop/collections/fall-collection` & `https://gregarious-pages-565888.framer.app/`
**Target Destination:** Replicating Cartelle aesthetic for UNTLD raw denim streetwear in `/Users/speedyzyzz/UNTLD/index.html`

---

## 1. Design Tokens & Palette System
Extracted directly from Framer CSS root variables (`:root` / `body`):

| Framer Token Variable | Hex / RGB Value | Role / Semantic Application |
|---|---|---|
| `--token-3231f815-59bd-4709-9984-27f462c2029e` | `#FFFFFF` | Background primary (Canvas / Sticky Nav background) |
| `--token-797ab030-f8f9-4fa5-9ca9-47203acd1eba` | `#FAFAFA` | Surface subtle off-white |
| `--token-fc5dffcb-9568-4484-a336-e739e6ee854b` | `#F5F5F5` | Surface muted / subtle card backing |
| `--token-8c2e2ee7-9d9a-4777-a6fb-8b243b942efd` | `#F4F4F4` | Card fill / Image placeholder tint |
| `--token-005e4f05-a1f6-41c5-9c55-4993c151e243` | `#EEEEEE` | Hairline border light |
| `--token-e95ee726-ab1d-4458-99db-780c0ed005f8` | `#E6E6E6` | Subtle dividers & link hover tint |
| `--token-937fdf82-e294-494c-afee-5e0ca84063e1` | `#DADADA` | Input border inactive |
| `--token-5c96456e-d648-4cb2-89d0-1861ea6d5669` | `#CCCCCC` | Inactive icon / indicator border |
| `--token-0089942e-b46b-4b30-a9fc-f9c710b6e92c` | `#BDBDBD` | Form border focused |
| `--token-4f95a47b-73b4-4844-84d0-91caa1d28764` | `#AEAEAE` | Strikethrough price text / muted label |
| `--token-3bb484c2-9f8e-4924-8278-1f0ba9028dad` | `#999999` | Strikethrough line bar (`#1md8h5s`) |
| `--token-25ff31ab-0d05-46b8-8f6f-323a44bc9868` | `#6D6D6D` | Product card price / secondary text / micro-tags |
| `--token-8872ea54-88a6-4157-8848-293bf9f2b125` | `#212121` | High contrast dark neutral |
| `--token-f317a2a6-2981-404a-911a-23ac76824a7d` | `#000000` | Pure Black (Headlines, titles, underlines, wordmark) |

---

## 2. Typography System & Presets
Cartelle pairs **Switzer** (from Fontshare CDN) with **Inter** (Google Fonts).

### Fonts CDN Import
```html
<!-- Switzer (Fontshare CDN) -->
<link href="https://api.fontshare.com/v2/css?f[]=switzer@400,500,600,700&display=swap" rel="stylesheet">
<!-- Inter (Google Fonts) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Exact Font Features & CSS Rules
```css
:root {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
* {
  --framer-font-open-type-features: 'blwf' on, 'cv09' on, 'cv03' on, 'cv04' on, 'cv11' on;
}
```

### Typography Hierarchy & Presets:
1. **Collection Headline (`.framer-styles-preset-dt6k0o`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `500` (Medium)
   - Desktop (>= 1200px): `font-size: 48px; line-height: 1.2em; letter-spacing: -0.03em;`
   - Tablet (810px - 1199px): `font-size: 36px; line-height: 1.2em; letter-spacing: -0.05em;`
   - Mobile (< 810px): `font-size: 28px; line-height: 1.2em; letter-spacing: -0.05em;`
   - Color: `#000000`
   - Text wrap: `text-wrap: balance; max-width: 600px;`

2. **Collection Subtitle / Lead Paragraph (`.framer-styles-preset-14qtfp`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `500` (Medium)
   - Desktop: `font-size: 22px; line-height: 1.4em; letter-spacing: -0.02em;`
   - Tablet: `font-size: 20px; line-height: 1.4em; letter-spacing: -0.02em;`
   - Mobile: `font-size: 18px; line-height: 1.4em; letter-spacing: -0.02em;`
   - Color: `#000000`
   - Text wrap: `text-wrap: balance; max-width: 600px;`

3. **Brand Wordmark (`.framer-5s6c4w h4`)**:
   - Font: `'Inter', sans-serif`
   - Weight: `500` (Medium)
   - `font-size: 24px; line-height: 1.4em; letter-spacing: -0.04em;`
   - Color: `#000000`

4. **Product Card Title (`.framer-styles-preset-13n02sm`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `400` (Regular)
   - `font-size: 18px; line-height: 1.4em; letter-spacing: -0.03em;`
   - Color: `#000000`

5. **Product Card Active Price (`.framer-styles-preset-1a6wygs`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `400` (Regular)
   - `font-size: 16px; line-height: 1.4em; letter-spacing: -0.02em;`
   - Color: `#6D6D6D`

6. **Product Card Original Price (`.framer-styles-preset-saf75d`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `400` (Regular)
   - `font-size: 16px; line-height: 1.4em; letter-spacing: -0.02em;`
   - Color: `#AEAEAE`
   - Strikethrough bar: `height: 1px; background: #999999; top: calc(47.8% - 0.5px);`

7. **Sticky Nav Links (`.framer-styles-preset-1cy06lx`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `400` (Regular)
   - `font-size: 16px; line-height: 1.2em; letter-spacing: -0.02em;`
   - Color: `#000000`

8. **Micro-Labels & Technical Badges (`.framer-styles-preset-1w6xih8`)**:
   - Font: `'Switzer', sans-serif`
   - Weight: `400`
   - `font-size: 13px; line-height: 1.2em; letter-spacing: 0em; text-transform: uppercase;`
   - Color: `#6D6D6D`

---

## 3. Motion Physics, Easing Curves & Transitions
Framer Motion definitions extracted directly from the compiled runtime modules:

### 1. Signature Cartelle Easing Curve
```css
/* Cubic-Bezier: [0.44, 0, 0.56, 1] */
cubic-bezier(0.44, 0, 0.56, 1)
```

### 2. Sticky Nav Entrance / Appear
- Initial: `opacity: 0.001; transform: none;`
- Animate: `opacity: 1; transform: none;`
- Spring Physics:
  ```js
  transition: { type: "spring", stiffness: 400, damping: 30, mass: 1, delay: 0 }
  ```

### 3. Page Element Entrance Tweens
- Hero / Main elements:
  ```js
  transition: { type: "tween", duration: 1.0, delay: 0, ease: [0.44, 0, 0.56, 1] }
  ```
- Sub-elements:
  ```js
  transition: { type: "tween", duration: 0.6, delay: 0, ease: [0.44, 0, 0.56, 1] }
  ```
- Delayed secondary elements:
  ```js
  transition: { type: "tween", duration: 0.6, delay: 2.0, ease: [0.44, 0, 0.56, 1] }
  ```

### 4. Nav Link Hover Underline Animation
```css
.nav-link {
  position: relative;
  text-decoration: none;
  cursor: pointer;
}
.nav-link .nav-line {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 1px;
  width: 0%;
  background-color: #000000;
  transition: width 0.4s cubic-bezier(0.44, 0, 0.56, 1);
  pointer-events: none;
}
.nav-link:hover .nav-line {
  width: 100%;
}
```

### 5. Product Card Dual-Image Hover Crossfade
- Component: `Product Listing` (`Q.displayName = "Product Listing"`, defaultProps: `width: 433, height: 501`)
- Structure:
  - `.main-image`: `position: relative; z-index: 2; width: 100%; aspect-ratio: 1 / 1; opacity: 1;`
  - `.secondary-image`: `position: absolute; top: 0; left: 0; right: 0; z-index: 1; width: 100%; aspect-ratio: 1 / 1;`
- Spring Physics from Framer module:
  ```js
  H = { type: "spring", bounce: 0.2, duration: 0.8, delay: 0 }
  ```
- CSS Implementation:
  ```css
  .product-image-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 1 / 1;
    overflow: hidden;
    background-color: #f4f4f4;
  }
  .product-image-wrap .main-img {
    position: relative;
    z-index: 2;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 1;
    transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  }
  .product-image-wrap .sec-img {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .product-card:hover .main-img {
    opacity: 0;
  }
  ```

---

## 4. Layout Architecture & Responsive Breakpoints

### Breakpoint Matrix
- **Desktop**: `min-width: 1200px` (Max content container: `1600px`)
- **Tablet**: `(min-width: 810px) and (max-width: 1199.98px)`
- **Mobile**: `max-width: 809.98px`

### Page Container (`.framer-prsms7`)
- Desktop: `max-width: 1600px; padding: 0 40px 100px; gap: 80px; margin: 0 auto;`
- Tablet: `padding: 0 40px 80px; gap: 32px;`
- Mobile: `padding: 0 20px 64px; gap: 24px;`

### Collection Header Section (`.framer-1noehon` & `.framer-QlYXd`)
- Desktop: `padding-top: 120px;` (to clear fixed nav)
- Content stack:
  - Top padding inside Left: `padding-top: 80px;` (Desktop), `40px` (Tablet), `20px` (Mobile)
  - Gap between H1 and Subtitle: `12px`
  - Max width: `600px` with `text-wrap: balance`

### Product Grid (`.framer-18vb0fi`) — The Signature Cartelle Grid!
**Notice the unique gap ratio:**
```css
/* Desktop: 3 columns, tight 8px column gap, 40px row gap! */
@media (min-width: 1200px) {
  .product-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(50px, 1fr));
    gap: 40px 8px; /* 40px row gap, 8px column gap */
    width: 100%;
  }
}

/* Tablet: 2 columns */
@media (min-width: 810px) and (max-width: 1199.98px) {
  .product-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(50px, 1fr));
    gap: 40px 8px;
    width: 100%;
  }
}

/* Mobile: Single column stacked */
@media (max-width: 809.98px) {
  .product-grid {
    display: flex;
    flex-direction: column;
    gap: 32px;
    width: 100%;
  }
}
```

---

## 5. Sticky Navigation Architecture
```css
.sticky-header-container {
  position: fixed;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  z-index: 1000;
  background-color: #FFFFFF;
}

.sticky-nav-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1600px;
  margin: 0 auto;
  padding: 24px 40px; /* Tablet/Mobile: 20px */
}

.nav-links-wrap {
  display: flex;
  align-items: center;
  gap: 20px;
}
```

---

## 6. Footer Layout Architecture
- Outer container: `max-width: 1600px; margin: 0 auto; padding: 40px 48px;` (Mobile: `40px 20px;`)
- Upper block:
  - Left column: Wordmark (`Cartelle` / `UNTLD`) + Contact dispatch info (`cartelle@design.com`, `+1 206-123-1234`)
  - Right columns: Nav directory lists (3 columns: Pages, Collections, Legal) with animated underline links
- Lower block:
  - Newsletter dispatch form: Pill/Clean input + submit button
  - Bottom bar: Copyright & Designed by badge

---

## 7. Mapping UNTLD Assets into the Cartelle Replicant
Author must map UNTLD's raw denim archive into this exact 3-column / 1:1 image square structure:

| UNTLD Product | Price | Sale / Original Price | Primary Image | Hover Secondary Image |
|---|---|---|---|---|
| **Vintage Bootcut Denim** | ₹8,990 | ₹11,990 | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/BAGGYFITDENIM_SUMMERFADE_-7.jpg?v=1788254512` | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/SKR05069.jpg?v=1793878719` |
| **Baggy Fit Raw Denim** | ₹9,490 | — | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/SKR03027.jpg?v=1790693173` | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/BAGGYFITDENIM_SUMMERFADE_-7.jpg?v=1788254512` |
| **Layered Waistband Jeans** | ₹11,200 | ₹13,500 | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/M.EAPRIL20252.0_CROPPED_-29.jpg?v=1747992758` | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/UNTLDAUGUST2025-5.jpg?v=1757252508` |
| **Straight Fit Selvedge** | ₹8,490 | — | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/UNTLDJUNE2025-274.jpg?v=1754129067` | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/SKR03027.jpg?v=1790693173` |
| **Flared Selvedge Denim** | ₹9,990 | ₹12,490 | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/UNTLDAUGUST2025-5.jpg?v=1757252508` | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/M.EAPRIL20252.0_CROPPED_-29.jpg?v=1747992758` |
| **Panel Construction Denim**| ₹12,500 | — | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/SKR05069.jpg?v=1793878719` | `https://cdn.shopify.com/s/files/1/0661/1478/1415/files/UNTLDJUNE2025-274.jpg?v=1754129067` |

Also integrate:
- Store locator module or link featuring `untld_store_mumbai.jpg` (Bandra West flagship atelier).
- Interactive Bag / Cart slide-over drawer and toast feedback.
- Clean self-contained HTML/CSS/JS without external CSS frameworks (Tailwind/Bootstrap).
