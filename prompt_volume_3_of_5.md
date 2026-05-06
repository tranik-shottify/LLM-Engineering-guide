# Prompt — Volume 3 of 5

Paste this entire message into a fresh claude.ai conversation. This is
**Volume 3 of a 5-volume reference document on LLM engineering**. Each
volume is rendered in its own conversation and produced as a separate,
standalone print-ready HTML artifact. Volumes share visual style so the
five PDFs look like one consistent series.

**This volume contains**: a brief volume opener and **Parts 7-9** —
Production engineering for LLM apps, Evaluation, Safety / security /
responsible AI.

---

I want you to produce a **single, polished, print-ready HTML artifact**
titled **"LLM Engineering — A Practitioner's Reference · Volume 3"**.
I will save it as a PDF from my browser, so the document must be styled
for print. Treat this as a serious technical reference document — comparable
to a textbook chapter or a curated engineering handbook — for a working
machine-learning practitioner who already ships LLM-powered software and
wants a comprehensive reference covering modern, advanced, and
2025-2026-era LLM engineering.

This is **not** a tutorial for beginners and **not** a marketing document.
It is a dense, accurate, well-organized engineering reference.

---

## 1. Output format

- One **HTML artifact**, fully self-contained except for these CDN scripts:
  - Mermaid (`https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js`)
  - Prism.js core + autoloader for syntax highlighting
  - MathJax 3 for equations
- All CSS inline in a `<style>` block. No external CSS files.
- **Target length when printed: 18-22 A4 pages** for this volume.
- Renders correctly when opened in Chrome and printed via "Print → Save
  as PDF".

## 2. Page, typography, color (identical across all five volumes)

```css
@page { size: A4; margin: 20mm 18mm 22mm 18mm; }
html { hyphens: auto; -webkit-hyphens: auto; }
*, *::before, *::after { box-sizing: border-box; }
body { text-align: left; }
p { margin: 0 0 8pt 0; }

@media print {
  .part { break-before: page !important; page-break-before: always !important; }

  figure {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
    max-height: 200mm;
    margin: 12pt 0 16pt 0;
  }
  figure .mermaid,
  figure .mermaid > svg,
  figure svg,
  figure img {
    max-width: 100% !important;
    max-height: 180mm !important;
    width: auto !important;
    height: auto !important;
    display: block;
    margin: 0 auto;
  }
  figcaption {
    break-before: avoid !important;
    page-break-before: avoid !important;
    margin-top: 6pt;
  }

  pre {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
    max-height: 180mm;
    overflow: hidden;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .callout, .math-display {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  table { break-inside: auto; }
  thead { display: table-header-group; }
  tfoot { display: table-footer-group; }
  tr, td, th {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  h1, h2, h3, h4 {
    break-after: avoid !important;
    page-break-after: avoid !important;
    text-wrap: balance;
  }

  .section-banner, .part-banner {
    break-after: avoid !important;
    page-break-after: avoid !important;
  }

  p, li, dd { widows: 2; orphans: 2; }

  .no-print { display: none !important; }
}
```

The `<html>` root element must carry the attribute `lang="en"`.

> **Why these rules matter.** `break-inside: avoid` is only a hint; if
> an element is taller than the printable page area the browser must
> break it. The `!important` weight, the absolute-unit caps in mm, and
> the `figure svg { max-height: 180mm }` rule together prevent
> Mermaid's inline SVG sizing from overriding the cap.

- **Body**: `Inter, "Segoe UI", system-ui, -apple-system, sans-serif`,
  **12 pt**, line-height 1.55, color `#1A1A1A` on `#FFFFFF`,
  `text-align: left`, `hyphens: auto`. Paragraph spacing: 0 top, 8 pt
  bottom.
- **Headings**:
  - H1 (Part title): **32 pt**, weight 700, color `#0F2A4A`,
    line-height 1.15, `text-wrap: balance`.
  - H2 (Section): **20 pt**, weight 600, color `#0F2A4A`,
    24 pt top margin, 8 pt bottom margin, with a thin
    `1px solid #E5E9EF` bottom border and 6 pt of bottom padding.
  - H3 (Subsection): **14 pt**, weight 600, color `#1F6FEB`,
    18 pt top margin, 4 pt bottom margin.
- **Code**: `"JetBrains Mono", "Fira Code", Consolas, monospace`, **11 pt**,
  background `#F4F6FA`, padding 12 px, border-radius 6 px. Language
  label in the top-right corner of each block, set in uppercase, 9 pt,
  tracked, color `#4A5568`.
- **Inline code**: same monospace stack, 11 pt, `#F4F6FA` background.
- **Figure captions** and other **muted text**: **10.5 pt**, color
  `#4A5568`; figure captions optionally italic.
- **Table captions**: **10.5 pt**, color `#4A5568`, placed *above* the
  table, prefixed `Table {part}.{n} · `.
- **Footnotes**: small superscript markers; footnote text **9.5 pt** at
  the bottom of the page.
- **Running header / footer**: **9 pt**, color `#4A5568`.
- **Color palette**: Primary `#0F2A4A`, Accent `#1F6FEB`, Soft callout
  `#F4F6FA`, Success `#1F8B4C`, Warning `#B45309`, Muted `#4A5568`.
- **Page header (running)**: small, muted, current Part name on the left,
  document title with " · Volume 3" on the right.
- **Page footer**: page number `counter(page) / counter(pages)` centered;
  small "Volume 3 of 5" on the left.
- **Volume opener page (page 1, no header/footer)**:
  - Top third whitespace.
  - Short horizontal accent rule, ~40 % width, 2 px solid `#0F2A4A`.
  - Title: **LLM Engineering — A Practitioner's Reference**, **44 pt**,
    weight 700, navy.
  - Subtitle: *Volume 3 · Production · Evaluation · Safety*, **16 pt**,
    weight 400, muted color `#4A5568`.
  - Tasteful decorative SVG element in the lower portion.
  - Date line near the bottom: "2026 Edition", 11 pt, muted.
- **Volume contents (page 2)**: list of the three Parts in this volume,
  with leader dots and page numbers. Add a small "Companion volumes"
  note listing — by name only — what
  - Volume 1 (Parts 1-3: Foundations, Modern Model Landscape, Adapting
    Models)
  - Volume 2 (Parts 4-6: Retrieval-Augmented Generation, Agentic
    Systems, Inference Optimization & Serving)
  - Volume 4 (Parts 10-12: MLOps & LLMOps, Multimodal, System Design
    Playbook)
  - Volume 5 (Parts 13-15: Trends, Curated Resources, Glossary)

  contain.

- **Section openers**: full-width tinted banner (`#F4F6FA` background,
  `#0F2A4A` text, **3 px solid `#1F6FEB` left border**, 16 px vertical
  padding). Three lines: `PART N` tracked accent-blue (11 pt) → Part
  title H1 (32 pt navy) → italic deck (12.5 pt muted).
- **Tables**: full-width; zebra striping; no vertical rules; header row
  navy / white; cell padding 8 px / 12 px. Caption above.
- **Callouts**: **Key idea**, **Pitfall**, **Senior tip** with distinct
  left border colors. Inline SVG icon, not emoji.
- **Figures**: numbered `Figure {part}.{n}`, caption below.

## 2.5 "How to save as PDF" callout (visible on screen, hidden in print)

At the very top of the rendered HTML — directly after the volume opener
— add a `<div class="no-print">` callout that the user sees on screen
but is hidden in print output. Style it the same as a "Key idea"
callout.

The callout text:

> **How to save this volume as a PDF.** Open this file in **Chrome** or
> Edge. Wait until every diagram and equation has finished rendering on
> screen. Press **Ctrl+P / ⌘P**. Set destination to **"Save as PDF"**.
> Under "More settings": **Margins → Default**, **Paper size → A4**,
> **Scale → Default (100 %)**, and **enable "Background graphics"** so
> banners and callout fills render. Then click **Save**.

## 3. Visualization & equation rendering — strict

- Every figure is a real visual: a **Mermaid** diagram or **inline SVG**.
- **No ASCII art, no box-drawing diagrams, no text-based figures.**
- SVGs are hand-written, with `viewBox` and labelled `<text>` elements;
  any text inside an SVG is at least 12 px.

### Mermaid configuration & legibility — non-negotiable

The printed page content area is ~174 mm wide. A flowchart with more
than five nodes laid out left-to-right becomes unreadable when scaled
to that width.

- **Initialize Mermaid once** near the top of the document:

  ```js
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' },
    themeVariables: {
      fontFamily: 'Inter, "Segoe UI", system-ui, sans-serif',
      fontSize: '15px',
      primaryColor: '#F4F6FA',
      primaryBorderColor: '#0F2A4A',
      primaryTextColor: '#0F2A4A',
      lineColor: '#4A5568',
      secondaryColor: '#FFFFFF',
      tertiaryColor: '#E5E9EF'
    }
  });
  ```

- **Default to `flowchart TB`**. Use `flowchart LR` only when a diagram
  has at most five nodes total.
- **Never chain more than 5 nodes in a single row.**
- **Do not unroll repeating structures** — use one `subgraph` with
  `× N` annotation.
- **Use `subgraph` to group logically.** Limit to four subgraphs per
  figure; if a flow needs more, split into N.a / N.b.
- **Node labels stay short — at most about 3 words.**
- For **sequence diagrams**: at most ~5 participants and ~12 messages.
- For **mind-maps and graphs**: prefer `flowchart TB` with subgraphs.
- After drafting each diagram, mentally render it at ~174 mm wide and
  ask *"would labels stay readable in print, and would the diagram fit
  inside 180 mm of vertical space?"* If not, redesign.
- Always validate Mermaid syntax.

### Math rendering — non-negotiable

Every equation must render as proper math typography, never as raw
`$...$` source on the page.

- **Include MathJax 3 in the document `<head>`**, with the delimiter
  config defined BEFORE the loader script:

  ```html
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true
      },
      svg: { fontCache: 'global' },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }
    };
  </script>
  <script id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
  ```

- **Render-completion guard** — add at the end of `<body>`:

  ```html
  <script>
    window.addEventListener('load', function() {
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise().catch(function(err) {
          console.error('MathJax typesetting failed:', err);
        });
      }
    });
  </script>
  ```

- **Use `\(...\)` for inline math and `$$...$$` for display math.**
- **Display math goes in its own block** wrapped in
  `<div class="math-display">$$ ... $$</div>`.
- **Heading + equation grouping**: wrap heading + paragraph + equation
  in a single `<div style="break-inside: avoid;
  page-break-inside: avoid;">`.
- **Never put math inside `<code>` or `<pre>`**, and never inside a
  markdown fenced code block.
- After drafting, scan every formula visually.

**Figures required in this volume:**

| #  | Figure                                                                  | Type                | Part |
|----|-------------------------------------------------------------------------|---------------------|------|
| 13 | Streaming + caching request lifecycle                                   | Mermaid sequence    | 7    |
| 14 | Evaluation taxonomy (offline / online / human / LLM-judge)              | Mermaid mindmap     | 8    |
| 15 | RAG evaluation metrics map (RAGAs)                                      | Mermaid graph       | 8    |
| 16 | LLM threat-model overview                                               | Mermaid flow        | 9    |

**Specific layout requirements for individual figures**

- **Figure 14** (evaluation taxonomy) — render as `flowchart TB` mindmap-
  style with at most four top-level branches (offline benchmarks, online
  eval, human eval, LLM-as-judge), each holding 2-3 leaves. Avoid the
  raw `mindmap` directive if it overflows; use `flowchart TB` with
  subgraphs instead.
- **Figure 16** (LLM threat-model overview) — `flowchart TB`. Group by
  attack class (input-side / tool-side / output-side) using subgraphs.
  At most three subgraphs; at most three leaves per subgraph.

## 4. Content — what each Part must contain

### Part 7 — Production engineering for LLM apps *(~6-7 pages)*
- Streaming over SSE / WebSockets, backpressure, cancellation tokens.
- Caching: exact-match, semantic cache, provider-side prompt caching
  (Anthropic / OpenAI prompt-cache features).
- Multi-provider routing: LiteLLM, OpenRouter, Portkey. Failover and
  cost-aware routing.
- Structured outputs: JSON-mode, tool-call constraints, libraries like
  Outlines, Instructor, Guidance.
- Reliability: retries with exponential back-off and jitter, idempotency,
  circuit breakers, rate-limit handling.
- Token budgeting: conversation windowing, summarization compression,
  sliding windows.
- Include **Figure 13**.
- Include a **15-line code snippet**: streamed FastAPI endpoint that
  proxies to an LLM provider with retry-with-jitter.

### Part 8 — Evaluation *(~6-7 pages)*
- Standard benchmarks and what they actually measure: MMLU, MMLU-Pro,
  BBH, GPQA, HumanEval, MBPP, MATH, IFEval. Caveats and contamination;
  contamination-resistant benchmarks (LiveBench, fresh QA sets).
- Human preference at scale: LMSYS Chatbot Arena and the limits of
  Elo-style preference rankings.
- Designing task-specific evals: golden sets, regression suites, sliced
  metrics, statistical significance and power.
- Synthetic eval generation: using an LLM to produce eval inputs and
  oracle answers, with the obvious circularity caveats.
- LLM-as-judge: pairwise, single-grade, G-Eval, MT-Bench. Bias and
  calibration. Position bias, length bias, self-preference bias.
- RAG evaluation: faithfulness, answer relevance, context precision /
  recall. RAGAs, TruLens, Phoenix.
- Agent evaluation: trajectory eval, tool-call accuracy, end-to-end
  success.
- Online evaluation: shadow traffic, A/B tests, win-rate, regret,
  user-feedback loops.
- Include **Figures 14 and 15**.
- Include a **15-line code snippet**: computing two RAGAs metrics on a
  sample dataset.

### Part 9 — Safety, security, responsible AI *(~5-6 pages)*
- Threat model: direct and indirect prompt injection, jailbreaks, data
  exfiltration, tool abuse, model supply-chain attacks.
- Defenses: input and output guardrails, NeMo Guardrails, Guardrails AI,
  Llama Guard, Prompt Guard, Rebuff.
- PII detection and redaction; content policy; the OWASP LLM Top 10.
- Bias, toxicity, fairness; provenance and citation enforcement;
  basic watermarking ideas.
- Compliance touch-points: GDPR, HIPAA, SOC 2 — LLM-specific data-handling
  pitfalls (training data, logging of prompts and completions, retention).
- Governance artifacts: model cards, system cards, dataset cards;
  NIST AI Risk Management Framework; EU AI Act obligations for general-
  purpose AI and high-risk applications (engineer-level awareness, not
  legal advice).
- Include **Figure 16**.

## 5. Code-snippet rules

- Each snippet stays between **10 and 30 lines**.
- Must be valid, runnable as written, using up-to-date APIs.
- No boilerplate scaffolding — only the conceptually important code.
- One-line caption above each snippet.
- Use Prism.js classes (`<pre><code class="language-python">…`).
- **No math inside any code block.**

## 6. Hard constraints

1. **One self-contained HTML artifact** for this volume. Inline CSS. CDN
   scripts only for Mermaid, Prism.js, MathJax 3.
2. **No ASCII art, no box-drawing diagrams, no text-based figures.**
3. **Technical accuracy first.** Never fabricate citations, URLs, or
   arXiv IDs.
4. **Consistent American English** throughout.
5. **No mention of interviews, hiring, jobs, candidates, CVs, recruitment,
   or any role-related framing.**
6. **No personal names, no logos, no company branding** beyond well-known
   public product names referenced for technical accuracy.
7. **Page-break discipline**: every Part starts on a new page; figures,
   code blocks, tables, and callouts must never be split across pages.
   Apply the print-CSS block in Section 2 exactly as written, including
   all `!important` weights and absolute-unit caps.
8. **Density discipline**: dense, information-rich prose. No filler.
9. **HTML root must carry `lang="en"`**.
10. **Every Part must open with a one-sentence italic deck line**.
11. **This is Volume 3 of 5**. Render only Parts 7-9 in this artifact.
    Do not generate content for Parts 1-6 or 10-15.

## 7. Self-review pass before delivery

Before returning the artifact:

1. Re-read the document end-to-end.
2. Validate every Mermaid diagram: matching brackets; correct directives;
   no row longer than 5 nodes; at most 4 subgraphs per figure;
   repeating structures shown as a single `subgraph` with `× N`.
   Confirm `mermaid.initialize` is present with `fontSize: '15px'`.
3. Confirm Figures 13-16 are present and correctly numbered using
   `Figure {part}.{n}` (e.g., the first figure in Part 7 is
   `Figure 7.1`).
4. Confirm all required code snippets are present and within the line
   budget. Confirm no math inside any `<pre>`/`<code>`.
5. Sweep for grammar, spelling, agreement, consistent tense.
6. Sweep for any factual claim you are not confident about — soften or
   remove.
7. Sweep for any ASCII figure that may have slipped in.
8. **Print-CSS verification**: confirm the `@media print` block contains
   `!important` on every break/size rule, the figure
   `max-height: 200mm`, the `figure svg { max-height: 180mm !important }`
   rule, the `pre { max-height: 180mm; white-space: pre-wrap }`, the
   `thead { display: table-header-group }` rule, and the
   `tr { break-inside: avoid !important }` rule.
9. Confirm no mention of interviews, hiring, recruitment, or personal
   names.
10. Confirm every Part has its mandatory italic deck line.
11. Confirm `<html lang="en">` is set.
12. Confirm MathJax 3 is loaded in `<head>` with the inline-math
    delimiter config block placed BEFORE the loader script. Visually
    verify each equation renders as typeset math, never as raw
    `\(...\)` or `$$...$$` source. No math inside `<code>` or `<pre>`.
13. Confirm the screen-only "How to save as PDF" callout is present
    near the top, wrapped in `<div class="no-print">`.

Only then deliver.

---

**Begin now.** Output the complete Volume 3 HTML artifact.
