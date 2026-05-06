# Prompt — Volume 5 of 5

Paste this entire message into a fresh claude.ai conversation. This is
**Volume 5 of a 5-volume reference document on LLM engineering**. Each
volume is rendered in its own conversation and produced as a separate,
standalone print-ready HTML artifact. Volumes share visual style so the
five PDFs look like one consistent series.

**This volume contains**: a brief volume opener and **Parts 13-15** —
Trends to watch, Curated resources, Glossary.

---

I want you to produce a **single, polished, print-ready HTML artifact**
titled **"LLM Engineering — A Practitioner's Reference · Volume 5"**.
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
  - MathJax 3 (only used if any math appears; safe to include either way)
- All CSS inline in a `<style>` block.
- **Target length when printed: 14-18 A4 pages** for this volume.
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
  **12 pt**, line-height 1.55.
- **Headings**:
  - H1 (Part title): **32 pt**, weight 700, color `#0F2A4A`,
    line-height 1.15, `text-wrap: balance`.
  - H2 (Section): **20 pt**, weight 600, color `#0F2A4A`,
    24 pt top, 8 pt bottom, thin `1px solid #E5E9EF` bottom border.
  - H3 (Subsection): **14 pt**, weight 600, color `#1F6FEB`.
- **Code**: `"JetBrains Mono", "Fira Code", Consolas, monospace`, **11 pt**.
- **Figure captions** and other **muted text**: **10.5 pt**, color
  `#4A5568`.
- **Table captions**: **10.5 pt**, color `#4A5568`, placed *above* the
  table.
- **Footnotes**: small superscript markers; footnote text **9.5 pt** at
  the bottom of the page.
- **Running header / footer**: **9 pt**, color `#4A5568`.
- **Color palette**: Primary `#0F2A4A`, Accent `#1F6FEB`, Soft callout
  `#F4F6FA`, Success `#1F8B4C`, Warning `#B45309`, Muted `#4A5568`.
- **Page header (running)**: small, muted, current Part name on the left,
  document title with " · Volume 5" on the right.
- **Page footer**: page number `counter(page) / counter(pages)` centered;
  small "Volume 5 of 5" on the left.
- **Volume opener page (page 1, no header/footer)**:
  - Top third whitespace, accent rule above title.
  - Title: **LLM Engineering — A Practitioner's Reference**, **44 pt**,
    weight 700, navy.
  - Subtitle: *Volume 5 · Trends · Resources · Glossary*, **16 pt**,
    weight 400, muted.
  - Tasteful decorative SVG element in the lower portion.
  - Date line near the bottom: "2026 Edition", 11 pt, muted.
- **Volume contents (page 2)**: list of the three Parts in this volume,
  with leader dots and page numbers. Add a small "Companion volumes"
  note listing — by name only — what
  - Volume 1 (Parts 1-3: Foundations, Modern Model Landscape, Adapting
    Models)
  - Volume 2 (Parts 4-6: Retrieval-Augmented Generation, Agentic
    Systems, Inference Optimization & Serving)
  - Volume 3 (Parts 7-9: Production Engineering, Evaluation, Safety &
    Security)
  - Volume 4 (Parts 10-12: MLOps & LLMOps, Multimodal, System Design
    Playbook)

  contain.

- **Section openers**: full-width tinted banner (`#F4F6FA` background,
  `#0F2A4A` text, **3 px solid `#1F6FEB` left border**, 16 px vertical
  padding). Three lines: `PART N` accent-blue tracked → Part title H1 →
  italic deck (12.5 pt muted).
- **Tables**: full-width; zebra striping; no vertical rules; header row
  navy / white. Caption above.
- **Callouts**: **Key idea**, **Pitfall**, **Senior tip**.
- **Figures**: numbered `Figure {part}.{n}`, caption below.
- **Glossary table**: a special two-column layout — see Part 15 below.

## 2.5 "How to save as PDF" callout (visible on screen, hidden in print)

At the very top of the rendered HTML — directly after the volume opener
— add a `<div class="no-print">` callout that the user sees on screen
but is hidden in print output. Style it the same as a "Key idea"
callout.

The callout text:

> **How to save this volume as a PDF.** Open this file in **Chrome** or
> Edge. Wait until the timeline figure has finished rendering on
> screen. Press **Ctrl+P / ⌘P**. Set destination to **"Save as PDF"**.
> Under "More settings": **Margins → Default**, **Paper size → A4**,
> **Scale → Default (100 %)**, and **enable "Background graphics"** so
> banners and callout fills render. Then click **Save**.

## 3. Visualization & equation rendering — strict

- The single visual in this volume is **Figure 20** (a hand-written
  inline SVG timeline). No Mermaid diagrams are required, but if you do
  add any, they must follow the rules below.
- **No ASCII art, no box-drawing diagrams, no text-based figures.**
- SVGs are hand-written, with `viewBox` and labelled `<text>` elements;
  any text inside an SVG is at least 12 px.

### Mermaid configuration (only if any Mermaid is used)

If any Mermaid diagram is included, initialize once near the top:

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

Same legibility rules as the other volumes: `flowchart TB` default; ≤ 5
nodes per row; at most 4 subgraphs; never unroll repetition.

### Math rendering — non-negotiable (if any math is used)

If any math appears, include MathJax 3 in `<head>` with the delimiter
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

Render-completion guard at the end of `<body>`:

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

Use `\(...\)` for inline math and `$$...$$` for display math. Never
put math inside `<code>` or `<pre>`.

**Figures required in this volume:**

| #  | Figure                                | Type                | Part |
|----|---------------------------------------|---------------------|------|
| 20 | Technology timeline: 2023 → 2026      | Inline SVG timeline | 13   |

**Specific layout requirements for Figure 20**

- Inline SVG timeline running left-to-right across the page (the page is
  portrait but the figure can be the full content width of ~174 mm).
- A horizontal axis labeled with years 2023, 2024, 2025, 2026 at evenly
  spaced positions.
- Above the axis: cluster of 6-8 milestone events (e.g., release of
  Llama 2, FlashAttention-2, vLLM, Mixtral, Llama 3, GPT-4o, o1
  reasoning models, MCP, Llama 3.x, DeepSeek-R1, agentic AI mainstream
  adoption, etc.) with short labels and short connectors to the year
  on the axis. Use neutral wording; do not invent dates you are unsure
  of — if a date is uncertain, position the milestone roughly within the
  correct year.
- Below the axis: 2-3 themed bands ("Models", "Inference", "Agents")
  showing rough trend curves or labeled spans.
- Total SVG height ≤ 130 mm. Use the document palette
  (`#0F2A4A` axis, `#1F6FEB` accent for events, `#4A5568` muted text).
- Caption: "Approximate technology timeline, 2023-2026. Dates are
  illustrative; for an exact chronology consult primary sources."

## 4. Content — what each Part must contain

### Part 13 — Trends to watch (2025-2026) *(~4-5 pages)*
- Agentic AI graduating from demos to production.
- Computer-use / browser-control agents moving from research demos into
  shipped products.
- MCP and emerging open tool-protocol standards.
- Long context (1M+ tokens) and the retrieval-vs-context trade-off.
- Test-time compute / reasoning depth as a deployment knob.
- On-device and edge LLMs.
- Synthetic-data flywheels and self-improvement loops.
- Hardware shifts: NVIDIA Blackwell (B200 / B300), AMD MI300X, AWS
  Trainium2, dedicated inference accelerators (Groq, Cerebras), and
  what they imply for cost-per-token over the next two years.
- AI compilers and inference compilers (TVM-MLIR, OpenAI Triton, Mojo)
  as the layer everyone forgets exists until they need it.
- World models and multimodal generalists.
- Include **Figure 20**.

### Part 14 — Curated resources *(~3-4 pages)*
- Foundational papers (with one-line summary each): *Attention Is All You
  Need*, *Retrieval-Augmented Generation for Knowledge-Intensive NLP
  Tasks*, *LoRA*, *QLoRA*, *DPO*, *Self-RAG*, *vLLM / PagedAttention*,
  *FlashAttention*, *MoE / Switch Transformer*, *Mamba*. Use neutral
  descriptive language; do not invent links.
- Books worth reading: *Designing Machine Learning Systems* (Chip Huyen),
  *Machine Learning Engineering* (Andriy Burkov), *Hands-On Large Language
  Models* (Alammar & Grootendorst).
- Practitioner blogs: Lilian Weng, Sebastian Raschka, Eugene Yan.
- Open-source repositories worth reading code for.

### Part 15 — Glossary *(~5-7 pages)*
A clean two-column glossary of approximately 60-70 terms used across the
five-volume series. One-line plain-English definition per term. Sorted
alphabetically. Include core terms from Volumes 1-4 even though those
volumes are rendered separately, so this glossary serves the whole
series.

Use a CSS grid layout so terms wrap naturally:
```css
.glossary { display: grid; grid-template-columns: 1fr 1fr; gap: 12px 24px; }
.glossary dt { font-weight: 600; color: #0F2A4A; }
.glossary dd { margin: 0 0 8pt 0; color: #1A1A1A; }
@media print {
  .glossary { grid-template-columns: 1fr 1fr; }
  .glossary > * { break-inside: avoid !important; }
}
```

Sample terms to cover (non-exhaustive — extend to about 60-70 total):
ALiBi, ANN index, Attention, BPE, Bi-encoder, Causal LM, Chinchilla
scaling, Chunking, Constitutional AI, Contextual retrieval, Continuous
batching, Cross-encoder, DPO, DAPT, DDP, Distillation, Drift, Embedding,
EAGLE, FAISS, FlashAttention, FSDP, GGUF, GPTQ / AWQ, GraphRAG, GQA,
Guardrails, Hallucination, HNSW, HyDE, IFEval, Instruction tuning,
KV cache, LoRA / QLoRA, LLM-as-judge, MCP, MMLU, MoE, MQA, Multi-vector
retrieval, NTK scaling, Paged attention, PEFT, Perplexity, Prompt
injection, Prompt caching, Quantization, RAG, RAGAs, Reranker, RLHF,
RoPE, Self-RAG, SFT, SimPO, Speculative decoding, SwiGLU, Test-time
compute, TGI, vLLM, YaRN, ZeRO. Add: Disaggregated prefill/decode,
ColPali, Late interaction, Reward hacking, Catastrophic forgetting,
Lost-in-the-middle, FinOps (LLM), Eval harness, Prompt registry, MTEB,
Mamba/SSM.

## 5. Code-snippet rules

This volume contains no required code snippets — Parts 13-15 are
predominantly conceptual, comparative, and reference material. If a
brief inline snippet (≤10 lines) genuinely clarifies a point in
Part 13's hardware discussion, you may include one; otherwise prefer
prose, math, and tables. **No math inside any code block.**

## 6. Hard constraints

1. **One self-contained HTML artifact** for this volume.
2. **No ASCII art, no box-drawing diagrams, no text-based figures.**
3. **Technical accuracy first.** Never fabricate citations, URLs, or
   arXiv IDs.
4. **Consistent American English** throughout.
5. **No mention of interviews, hiring, jobs, candidates, CVs, recruitment,
   or any role-related framing.**
6. **No personal names, no logos, no company branding** beyond well-known
   public product names referenced for technical accuracy. Author names
   may appear only in Part 14's curated resources list (book authors,
   blog authors), not anywhere else.
7. **Page-break discipline**: every Part starts on a new page; figures,
   code blocks, tables, and callouts must never be split across pages.
   Apply the print-CSS block in Section 2 exactly as written, including
   all `!important` weights and absolute-unit caps. The two-column
   glossary uses `break-inside: avoid` on each term row so a term and
   its definition stay together.
8. **Density discipline**: dense, information-rich prose. No filler.
9. **HTML root must carry `lang="en"`**.
10. **Every Part must open with a one-sentence italic deck line**.
11. **This is Volume 5 of 5**. Render only Parts 13-15 in this artifact.
    Do not generate content for Parts 1-12.

## 7. Self-review pass before delivery

Before returning the artifact:

1. Re-read the document end-to-end.
2. If any Mermaid is used, validate every diagram: matching brackets;
   correct directives; no row longer than 5 nodes; at most 4 subgraphs
   per figure. Confirm `mermaid.initialize` is present with
   `fontSize: '15px'`.
3. Confirm Figure 20 is present and correctly numbered (the only
   figure in Part 13 is `Figure 13.1`).
4. Confirm the glossary contains roughly 60-70 terms, alphabetically
   sorted, each with a single-line definition. Confirm the two-column
   grid layout works under print CSS.
5. Sweep for grammar, spelling, agreement, consistent tense.
6. Sweep for any factual claim you are not confident about — soften or
   remove. The hardware roadmap section is especially prone to
   hallucinated dates and product specs; if unsure, describe
   qualitatively.
7. Sweep for any ASCII figure that may have slipped in.
8. **Print-CSS verification**: confirm the `@media print` block contains
   `!important` on every break/size rule, the figure
   `max-height: 200mm`, the `figure svg { max-height: 180mm !important }`
   rule, the `pre { max-height: 180mm; white-space: pre-wrap }`, the
   `thead { display: table-header-group }` rule, and the
   `tr { break-inside: avoid !important }` rule.
9. Confirm no mention of interviews, hiring, recruitment, or personal
   names beyond Part 14's resources list.
10. Confirm every Part has its mandatory italic deck line.
11. Confirm `<html lang="en">` is set.
12. If any math is used, confirm MathJax 3 is loaded in `<head>` with
    the inline-math delimiter config block placed BEFORE the loader
    script. Visually verify each equation renders as typeset math,
    never as raw `\(...\)` or `$$...$$` source. No math inside
    `<code>` or `<pre>`.
13. Confirm the screen-only "How to save as PDF" callout is present
    near the top, wrapped in `<div class="no-print">`.

Only then deliver.

---

**Begin now.** Output the complete Volume 5 HTML artifact.
